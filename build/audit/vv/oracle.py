"""Independent oracle for the Map's lit-set rules (SPEC step D.1).

Pure Python, stdlib only. Built from data/graph.json and the editor's written
rules (see RULES.md); it never reads the implementation.
"""
import json
import math
import random

TOGGLE_TYPES = {"requires": "requires", "alternatives": "replaces", "conflicts": "conflicts"}
TOGGLES = ("requires", "alternatives", "conflicts")
LENSES = ("family", "aff", "time", "det", "mech", "destr", "mid",
          "d", "mod", "place", "f", "g", "status")   # 17 Sep: the reading-marks lens was removed (RULES.md adjudication 10)
NONE = "none"


class Machine:
    """One register machine as a lit-set term (RULES.md §Machine term): its real (non-gap) stations on every layer,
    primary and alternate; `alt` = stations it uses only as an alternate; `path` = its map path (the only line kept)."""
    __slots__ = ("id", "name", "family", "path", "nodes", "alt")

    def __init__(self, m, node_ids):
        self.id, self.name, self.family, self.path = m["id"], m["name"], m["family"], m["map_path"]
        prim, alt = set(), set()
        for cells in (m.get("layers") or {}).values():
            for c in cells:
                nid = c["node"]
                if c.get("gap") or nid.startswith("\u2205") or nid not in node_ids:
                    continue   # gap nodes (\u2205...) are not graph nodes and contribute nothing
                (alt if c.get("role") == "alternate" else prim).add(nid)
        self.nodes = frozenset(prim | alt)
        self.alt = frozenset(alt - prim)


class Model:
    def __init__(self, g, machines=None):
        self.g = g
        self.nodes = {n["id"]: n for n in g["nodes"]}
        self.station_ids = sorted(self.nodes)
        self.paths = {p["id"]: p for p in g["paths"]}
        self.path_ids = [p["id"] for p in g["paths"]]
        self.path_stations = {
            pid: frozenset(x for s in p["slots"].values() for x in s if x in self.nodes)
            for pid, p in self.paths.items()
        }
        self.station_paths = {sid: set() for sid in self.nodes}
        for pid, st in self.path_stations.items():
            for s in st:
                self.station_paths[s].add(pid)
        self.empty_status = set(g.get("empty_status", []))
        # relation edges only: toggleable types with both endpoints stations
        self.rel_edges = sorted({
            (e["src"], e["dst"], e["type"]) for e in g["edges"]
            if e["type"] in TOGGLE_TYPES.values()
            and e["src"] in self.nodes and e["dst"] in self.nodes
        })
        self.lens_attr = {lens: {sid: frozenset(_lens_values_of(self, lens, n))
                                 for sid, n in self.nodes.items()} for lens in LENSES}
        # machines register (C2): id -> Machine; empty when machines.json is not given
        self.machines = {m["id"]: Machine(m, self.nodes) for m in (machines or {}).get("machines", [])}
        self.machine_ids = [m["id"] for m in (machines or {}).get("machines", [])]


# ADJ-4 (DESIGN-GAP): the page bins time to the NEAREST of 7 bin centres -8.5..-2.5 (ties -> lower bin, clamped at
# both ends); the oracle value is bin index - 9 (so -9 = "<= 3 ns" ... -3 = ">= 3 ms"), matching the runner's page_key.
TBIN_CENTRES = (-8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5)


def _time_bucket(n):
    t = (n.get("b") or {}).get("t")
    if t is None:
        t = (n.get("c") or {}).get("t")
    if t is None:
        return NONE
    best = 0
    for i, c in enumerate(TBIN_CENTRES):
        if abs(c - t) < abs(TBIN_CENTRES[best] - t):
            best = i
    return best - 9


def _tri(v):
    return NONE if v is None else bool(v)


def _lens_values_of(model, lens, n):
    """Set of lens values a station carries (multi-valued lenses may return several)."""
    b = n.get("b") or {}
    c = n.get("c") or {}
    e = n.get("e") or {}
    if lens == "family":
        return set(n.get("families") or [])
    if lens == "aff":
        return {float(n["aff"])}
    if lens == "time":
        return {_time_bucket(n)}
    if lens == "det":
        return {b.get("det") or NONE}
    if lens == "mech":
        return {c.get("mech") or NONE}
    if lens == "destr":
        return {_tri(c.get("destr"))}
    if lens == "mid":
        return {_tri(c.get("mid"))}
    if lens == "d":
        return {n.get("d") or NONE}
    if lens == "mod":
        return {e.get("mod") or NONE}
    if lens == "place":   # list-valued since 17 Sep 2026 (first entry = primary stage); membership over the list, as f
        p = e.get("place")
        return (set(p) if isinstance(p, list) else {p}) - {None} or {NONE}
    if lens == "f":
        return set(n.get("f") or []) or {NONE}
    if lens == "g":
        return {n.get("g") or NONE}
    if lens == "status":
        return {n.get("status") or NONE}
    raise KeyError(lens)


def _sortkey(v):
    return (type(v).__name__, str(v) if not isinstance(v, (int, float)) or isinstance(v, bool) else "%020.6f" % (v + 1e6))


def load(graph_path, machines_path=None):
    """graph.json (+ machines.json, default: the sibling file next to graph.json when it exists)."""
    import os
    with open(graph_path, encoding="utf-8") as fh:
        g = json.load(fh)
    if machines_path is None:
        cand = os.path.join(os.path.dirname(os.path.abspath(graph_path)), "machines.json")
        machines_path = cand if os.path.exists(cand) else None
    machines = None
    if machines_path:
        with open(machines_path, encoding="utf-8") as fh:
            machines = json.load(fh)
    return Model(g, machines)


def lens_values(model, lens):
    vals = set()
    for sid in model.station_ids:
        vals |= model.lens_attr[lens][sid]
    return sorted(vals, key=_sortkey)


def default_state():
    return {"lens": "family", "values": set(), "toggles": {t: False for t in TOGGLES},
            "isolate": None, "focus": None, "machine": None}


def _on_types(state):
    tg = state.get("toggles") or {}
    return {TOGGLE_TYPES[t] for t in TOGGLES if tg.get(t)}


def _lens_active(state):
    return bool(state.get("lens")) and bool(state.get("values"))


def effective(model, state):
    """ADJ-12 (21 Sep 2026): the three selections narrow each other only while they can share a line. Applied in the driver's
    gesture order (isolate, then machine, then focus), a newer selection releases an older one it cannot share a line with:
    a machine on another path releases the isolate; a focused station releases an isolate whose path does not pass through it
    and a machine whose path does not pass through it. Returns (isolate, machine_id, focus) as the page ends up holding them."""
    iso, mid, foc = state.get("isolate"), state.get("machine"), state.get("focus")
    if mid and iso and model.machines[mid].path != iso:
        iso = None
    if foc:
        if iso and iso not in model.station_paths[foc]:
            iso = None
        if mid and model.machines[mid].path not in model.station_paths[foc]:
            mid = None
    return iso, mid, foc


def expected(model, state):
    all_st = set(model.station_ids)
    on = _on_types(state)
    lens, values = state.get("lens"), set(state.get("values") or ())
    iso, mid, foc = effective(model, state)
    mach = model.machines[mid] if mid else None

    # isolate term
    iso_set = set(model.path_stations[iso]) if iso else all_st
    # machine term (C2, RULES.md §Machine term): the machine's non-gap stations, primary and alternate, all layers
    mach_set = set(mach.nodes) if mach else all_st
    # focus term
    if foc:
        foc_set = {foc}
        for pid in model.station_paths[foc]:
            foc_set |= model.path_stations[pid]
        for (u, v, t) in model.rel_edges:
            if t in on:
                if u == foc:
                    foc_set.add(v)
                elif v == foc:
                    foc_set.add(u)
    else:
        foc_set = all_st
    # lens term
    if _lens_active(state):
        attr = model.lens_attr[lens]
        lens_set = {s for s in all_st if attr[s] & values}
    else:
        lens_set = all_st
    lit = iso_set & foc_set & lens_set & mach_set
    if foc:
        lit.add(foc)   # ADJ-3 (ORACLE-FIX): the clicked station is always lit (rule 2)

    # lines -- ADJ-1/ADJ-2 (DESIGN-GAP, page behaviour as de-facto rule):
    #   isolate/focus set -> the isolated line / the focused station's lines (intersection), narrowed by a family value;
    #                        a non-family lens value does not narrow them;
    #   else a family value -> that family's lines; any other lens value -> no line; no lens value -> every line.
    #   a machine (C2) keeps exactly its own path line, like an isolate (intersection with {map_path}).
    lines = set()
    for pid in model.path_ids:
        if iso and pid != iso:
            continue
        if mach and pid != mach.path:
            continue
        if foc and pid not in model.station_paths[foc]:
            continue
        if _lens_active(state):
            if lens == "family":
                if model.paths[pid]["family"] not in values:
                    continue
            elif not (iso or foc or mach):
                continue
        lines.add(pid)

    # edges
    selection = bool(iso or foc or mach or _lens_active(state))
    edges = set()
    for (u, v, t) in model.rel_edges:
        if t not in on:
            continue
        if selection and not (u in lit and v in lit):
            continue
        edges.add((u, v, t))
    # the strip (ADJ-13, 23 Sep 2026): a line is bright iff its station is lit; the focus is the thick line; the chosen machine's
    # alternate-only stations are dashed while lit; the lens's axis is marked and the pressed values are the lens values
    pc_alt = (set(mach.alt) & lit) if mach else set()
    return {"stations": lit, "lines": lines, "edges": edges,
            "pc_bright": set(lit), "pc_hi": foc, "pc_alt": pc_alt,
            "pc_axis": LENS_AXIS.get(lens), "pc_pressed": {(lens, v) for v in values} if _lens_active(state) else set()}


# strip axes (design attributes) that stand for a lens; family and status have no axis
LENS_AXIS = {"aff": "aff", "time": "b", "det": "b", "mech": "c", "destr": "c", "mid": "c", "d": "d", "mod": "e", "place": "e", "f": "f", "g": "g"}
AXIS_LENS = {"aff": "aff", "b": "time", "c": "mech", "d": "d", "e": "mod", "f": "f", "g": "g"}


def all_single_states(model):
    for lens in LENSES:
        for val in lens_values(model, lens):
            s = default_state()
            s["lens"], s["values"] = lens, {val}
            yield s
    for t in TOGGLES:
        s = default_state()
        s["toggles"][t] = True
        yield s
    for pid in model.path_ids:
        s = default_state()
        s["isolate"] = pid
        yield s
    for sid in model.station_ids:
        s = default_state()
        s["focus"] = sid
        yield s
    for mid in model.machine_ids:   # C2: every machine alone
        s = default_state()
        s["machine"] = mid
        yield s


def random_state(model, rng):
    s = default_state()
    lens = rng.choice(LENSES)
    s["lens"] = lens
    vals = lens_values(model, lens)
    k = rng.choice([0, 0, 1, 1, 2, 3])
    s["values"] = set(rng.sample(vals, min(k, len(vals))))
    s["toggles"] = {t: rng.random() < 0.5 for t in TOGGLES}
    s["isolate"] = rng.choice(model.path_ids) if rng.random() < 0.35 else None
    s["focus"] = rng.choice(model.station_ids) if rng.random() < 0.35 else None
    s["machine"] = rng.choice(model.machine_ids) if model.machine_ids and rng.random() < 0.3 else None
    return s


def _copy(s):
    return {"lens": s["lens"], "values": set(s["values"]), "toggles": dict(s["toggles"]),
            "isolate": s["isolate"], "focus": s["focus"], "machine": s.get("machine")}


def _fmt(s):
    return "lens=%s values=%s toggles=%s isolate=%s focus=%s machine=%s" % (
        s["lens"], sorted(s["values"], key=_sortkey),
        "".join(t[0] for t in TOGGLES if s["toggles"].get(t)) or "-", s["isolate"], s["focus"], s.get("machine"))


def metamorphic_checks(model, rng, n):
    viol = []
    for i in range(n):
        s = random_state(model, rng)
        base = expected(model, s)
        lens = s["lens"]
        attr = model.lens_attr[lens]
        # M1: adding a value never lights fewer stations of that lens
        rest = [v for v in lens_values(model, lens) if v not in s["values"]]
        if rest and s["values"]:
            s2 = _copy(s)
            s2["values"].add(rng.choice(rest))
            after = expected(model, s2)
            if not base["stations"] <= after["stations"]:
                viol.append("M1 add-value shrank lit set: %s -> +%s" % (_fmt(s), sorted(s2["values"] - s["values"], key=_sortkey)))
        # M2: isolate then clear returns previous
        if s["isolate"] is None:
            s2 = _copy(s)
            s2["isolate"] = rng.choice(model.path_ids)
            expected(model, s2)
            s2["isolate"] = None
            if expected(model, s2) != base:
                viol.append("M2 isolate/clear not identity: %s" % _fmt(s))
        # M3: toggling twice is identity
        t = rng.choice(TOGGLES)
        s2 = _copy(s)
        s2["toggles"][t] = not s2["toggles"][t]
        mid = expected(model, s2)
        s2["toggles"][t] = not s2["toggles"][t]
        if expected(model, s2) != base:
            viol.append("M3 double toggle %s not identity: %s" % (t, _fmt(s)))
        # M3b: a toggle never changes lit stations/lines unless a focus is set
        if not s["focus"] and (mid["stations"] != base["stations"] or mid["lines"] != base["lines"]):
            viol.append("M3b toggle %s changed stations/lines without focus: %s" % (t, _fmt(s)))
        # M4: union over family-lens values equals the unfiltered set
        s0 = _copy(s)
        s0["lens"], s0["values"] = "family", set()
        unf = expected(model, s0)
        u_st, u_ln = set(), set()
        for v in lens_values(model, "family"):
            sv = _copy(s0)
            sv["values"] = {v}
            r = expected(model, sv)
            u_st |= r["stations"]
            u_ln |= r["lines"]
        pathless = {x for x in unf["stations"] if not model.lens_attr["family"][x] and x != s0["focus"]}
        if u_st != unf["stations"] - pathless or u_ln != unf["lines"]:
            viol.append("M4 family union != unfiltered: %s" % _fmt(s0))
        # M5: all-values selection equals unfiltered (lens with total coverage)
        sa = _copy(s)
        sa["values"] = set(lens_values(model, lens))
        if expected(model, sa)["stations"] != expected(model, s0)["stations"] - {x for x in model.station_ids if not attr[x] and x != s["focus"]}:
            viol.append("M5 all-values != unfiltered (minus stations without a %s value): %s" % (lens, _fmt(sa)))
        # invariants: edges only among lit stations under a selection; stations of drawn edges typed on
        on = _on_types(s)
        for (u, v, ty) in base["edges"]:
            if ty not in on:
                viol.append("I1 edge of untoggled type drawn: %s" % _fmt(s))
                break
    return sorted(set(viol))

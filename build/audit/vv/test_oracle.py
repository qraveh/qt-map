"""Sanity tests for the oracle on data/graph.json. Run: python3 build/audit/vv/test_oracle.py"""
import os
import random
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oracle  # noqa: E402

GRAPH = os.path.join(HERE, "..", "..", "..", "data", "graph.json")


class OracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = oracle.load(GRAPH)

    def test_default_state(self):
        r = oracle.expected(self.m, oracle.default_state())
        self.assertEqual(len(r["stations"]), 96)
        self.assertEqual(len(r["lines"]), 14)
        self.assertEqual(r["edges"], set())

    def test_isolations(self):
        for pid in self.m.path_ids:
            s = oracle.default_state()
            s["isolate"] = pid
            r = oracle.expected(self.m, s)
            want = {x for sl in self.m.paths[pid]["slots"].values() for x in sl}
            self.assertEqual(r["stations"], want, pid)
            self.assertEqual(r["lines"], {pid})
            self.assertEqual(r["edges"], set())

    def test_focus_hub(self):
        hubs = [n["id"] for n in self.m.g["nodes"] if n["hub"]]
        self.assertTrue(hubs)
        for h in hubs:
            s = oracle.default_state()
            s["focus"] = h
            r = oracle.expected(self.m, s)
            want = {x for p in self.m.g["paths"] if p["id"] in self.m.nodes[h]["paths"]
                    for sl in p["slots"].values() for x in sl}
            self.assertTrue(want <= r["stations"], h)
            self.assertEqual(r["stations"], want | {h})  # no toggle -> no neighbours
            self.assertEqual(r["lines"], set(self.m.nodes[h]["paths"]))
            s["toggles"] = {t: True for t in oracle.TOGGLES}
            r2 = oracle.expected(self.m, s)
            self.assertTrue(r["stations"] <= r2["stations"])
            for (u, v, t) in r2["edges"]:
                self.assertIn(u, r2["stations"])
                self.assertIn(v, r2["stations"])

    def test_toggle_alone_draws_all_of_type(self):
        for t, ty in oracle.TOGGLE_TYPES.items():
            s = oracle.default_state()
            s["toggles"][t] = True
            r = oracle.expected(self.m, s)
            self.assertEqual(r["edges"], {e for e in self.m.rel_edges if e[2] == ty})
            self.assertEqual(len(r["stations"]), 96)

    def test_all_single_states_and_lens_values(self):
        states = list(oracle.all_single_states(self.m))
        nvals = sum(len(oracle.lens_values(self.m, l)) for l in oracle.LENSES)
        self.assertEqual(len(states), nvals + 3 + 14 + 96)
        for s in states:
            oracle.expected(self.m, s)

    def test_deterministic(self):
        a = [oracle.random_state(self.m, random.Random(7)) for _ in range(3)]
        b = [oracle.random_state(self.m, random.Random(7)) for _ in range(3)]
        self.assertEqual(a, b)

    def test_metamorphic_200(self):
        v = oracle.metamorphic_checks(self.m, random.Random(20260916), 200)
        self.assertEqual(v, [], "\n".join(v[:20]))


if __name__ == "__main__":
    unittest.main(verbosity=2)

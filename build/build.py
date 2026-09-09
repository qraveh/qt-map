#!/usr/bin/env python3
"""One-shot build: graph → data/graph.json + §7 of the reports → dist/Quantum-Technology-Map-<edition>.html + CHANGELOG.md"""
import os, sys, runpy
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build')); sys.path.insert(0, os.path.join(ROOT, 'data'))
runpy.run_path(os.path.join(ROOT, 'build', 'make_sections.py'), run_name='__main__')
import build_html; build_html.build(build_html.PUBLIC)
from editions import changelog_md
open(os.path.join(ROOT, 'CHANGELOG.md'), 'w', encoding='utf-8', newline='\n').write(changelog_md())
print('CHANGELOG.md written')

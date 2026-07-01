#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "src" / "epub" / "OPS"

FILES = ["p1chap1", "p2chap1", "p3chap1", "p4chap1", "p5chap1", "p6chap1", "p7chap1", "p8chap1"]

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

heading_map = {}  # numeric prefix -> full text (e.g. "1.1" -> "1.1   Ölçek ve Uzmanlaşma")
no_prefix = []

for fname in FILES:
    path = f"{BASE}/{fname}.xhtml"
    content = open(path, encoding="utf-8").read()
    for m in re.finditer(r"<h[234][^>]*>(.*?)</h[234]>", content, re.DOTALL):
        raw = m.group(1)
        text = strip_tags(raw)
        if not text:
            continue
        pm = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", text)
        if pm:
            num, title = pm.group(1), pm.group(2)
            heading_map[num] = f"{num}   {title}"
        else:
            no_prefix.append((fname, text))

for num in sorted(heading_map, key=lambda x: [int(p) for p in x.split(".")]):
    print(heading_map[num])

print("\n--- no numeric prefix (chapter-level h2 etc, skip) ---")
for f, t in no_prefix:
    print(f, "|", t)

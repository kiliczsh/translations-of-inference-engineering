#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "src" / "epub" / "OPS"
CHAPTER_FILES = ["p1chap1", "p2chap1", "p3chap1", "p4chap1", "p5chap1", "p6chap1", "p7chap1", "p8chap1"]
TOC_FILES = ["nav.xhtml", "sommaire.xhtml", "toc.ncx"]

def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

# 1. extract ground-truth titles keyed by numeric prefix, from actual chapter body h3/h4
heading_map = {}
for fname in CHAPTER_FILES:
    content = open(f"{BASE}/{fname}.xhtml", encoding="utf-8").read()
    for m in re.finditer(r"<h[234][^>]*>(.*?)</h[234]>", content, re.DOTALL):
        text = strip_tags(m.group(1))
        pm = re.match(r"^(\d+(?:\.\d+)*)\s+(.*)$", text)
        if pm:
            heading_map[pm.group(1)] = pm.group(2)

print(f"ground-truth headings extracted: {len(heading_map)}")

def fix_entry(m):
    full = m.group(1)
    pm = re.match(r"^(\d+(?:\.\d+)*)([\s\xa0]+)(.*)$", full, re.DOTALL)
    if not pm:
        return m.group(0)
    num, sep, old_title = pm.group(1), pm.group(2), pm.group(3)
    if num not in heading_map:
        return m.group(0)
    new_title = heading_map[num]
    if strip_tags(old_title) == new_title:
        return m.group(0)
    fix_entry.count += 1
    return ">" + num + sep + new_title + "<"
fix_entry.count = 0

for fname in TOC_FILES:
    path = f"{BASE}/{fname}"
    content = open(path, encoding="utf-8").read()
    before = fix_entry.count
    content = re.sub(r">(\d+(?:\.\d+)*[\s\xa0]+[^<]*)<", fix_entry, content)
    open(path, "w", encoding="utf-8").write(content)
    print(f"{fname}: {fix_entry.count - before} entries synced")

print("total synced:", fix_entry.count)

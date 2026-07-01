# Inference Engineering — Turkish Translation

This repository contains the Turkish translation sources for Philip Kiely's
*Inference Engineering*.

## Project structure

```text
.
├── docs/       Translation guidelines and terminology
├── input/      Original source EPUB
├── src/epub/   Extracted and translated EPUB source tree
├── scripts/    Translation and table-of-contents utilities
└── dist/       Built Turkish EPUB
```

The filenames inside `src/epub/OPS` are retained from the original EPUB.
Changing them requires updating the EPUB manifest, spine, navigation files,
and internal links together.

## Key files

- `docs/glossary.md`: canonical Turkish terminology and style guide
- `input/inference-engineering.epub`: original English publication
- `dist/inference-engineering-tr.epub`: generated Turkish publication
- `scripts/extract_headings.py`: extracts numbered headings from chapters
- `scripts/sync_toc.py`: synchronizes navigation titles with chapter headings
- `scripts/translate_toc.py`: applies the original navigation translation map
- `scripts/translate_toc_flexible.py`: whitespace-tolerant navigation translator

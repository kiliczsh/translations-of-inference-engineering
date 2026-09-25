# Inference Engineering Translations

This repository contains translations of
[*Inference Engineering*](https://www.baseten.co/inference-engineering/) by
[Philip Kiely](https://philipkiely.com/). The book explains how to build fast,
reliable, and cost-efficient systems for running AI models in production.

Each translation is isolated under its ISO 639-1 language code so additional
editions can be added without mixing language-specific sources or tooling. See
the [official book page](https://www.baseten.co/inference-engineering/) for
information about the original publication.

## Download

- [Download the Original](https://simple-download.vercel.app/)

## Project structure

```text
.
├── dist/
│   └── inference-engineering-tr.epub
├── source/
│   └── inference-engineering.epub
└── translations/
    └── tr/
        ├── docs/
        │   └── glossary.md
        ├── src/epub/
        └── scripts/
```

New languages should follow the same layout under `translations/<language>/`.
Use an ISO 639-1 language code such as `de`, `es`, or `fr` for the directory
name. Completed EPUB files belong in the shared `dist/` directory and use the
language code as their filename suffix, for example
`inference-engineering-de.epub`.

The filenames inside each `src/epub/OPS` directory are retained from the
original EPUB. Changing them requires updating the EPUB manifest, spine,
navigation files, and internal links together.

## Key files

- `source/inference-engineering.epub`: original English publication
- `dist/inference-engineering-tr.epub`: generated Turkish publication
- `translations/tr/docs/glossary.md`: canonical Turkish terminology and style guide
- `translations/tr/scripts/extract_headings.py`: extracts numbered headings
- `translations/tr/scripts/sync_toc.py`: synchronizes navigation titles
- `translations/tr/scripts/translate_toc.py`: applies the navigation translation map
- `translations/tr/scripts/translate_toc_flexible.py`: whitespace-tolerant translator

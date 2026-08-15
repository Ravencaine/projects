---
title: "GitHub"
source: "https://search.app/rMEKH"
author: "search.app"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> A fast, helpful, and open-source document parser. Contribute to run-llama/liteparse development by creating an account on GitHub.

GitHub - run-llama/liteparse: A fast, helpful, and open-source document parser · GitHub Skip to content You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} Uh oh! There was an error while loading. Please reload this page . run-llama / liteparse Public Notifications You must be signed in to change notification settings Fork 826 Star 12.1k main Branches Tags Go to file Code Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit History 940 Commits 940 Commits .github .github crates crates dataset_eval_utils dataset_eval_utils demo/ docs demo/ docs docs/ src/ content/ docs/ liteparse docs/ src/ content/ docs/ liteparse integration_tests_data integration_tests_data ocr ocr packages packages scripts scripts wasm-demo-site wasm-demo-site .gitignore .gitignore .prettierignore .prettierignore .prettierrc .prettierrc AGENTS.md AGENTS.md CHANGELOG.md CHANGELOG.md CLAUDE.md CLAUDE.md CONTRIBUTING.md CONTRIBUTING.md Cargo.lock Cargo.lock Cargo.toml Cargo.toml Dockerfile Dockerfile LICENSE LICENSE Makefile Makefile OCR_API_SPEC.md OCR_API_SPEC.md README.md README.md README.zh-CN.md README.zh-CN.md SECURITY.md SECURITY.md docs.config.mjs docs.config.mjs eslint.config.js eslint.config.js full.Dockerfile full.Dockerfile musl_build_cargozig.md musl_build_cargozig.md View all files Repository files navigation LiteParse | | | | | | Docs English | 简体中文 Looking for LiteParse V1? Follow this link to the old code LiteParse is a standalone OSS PDF parsing tool focused exclusively on fast and light parsing. It provides high-quality spatial text parsing with bounding boxes, without proprietary LLM features or cloud dependencies. Everything runs locally on your machine. Hitting the limits of local parsing? For complex documents (dense tables, multi-column layouts, charts, handwritten text, or scanned PDFs), you'll get significantly better results with LlamaParse , our cloud-based document parser built for production document pipelines. LlamaParse handles the hard stuff so your models see clean, structured data and markdown. Sign up for LlamaParse free Overview Fast Text Parsing : Spatial text parsing using PDFium Flexible OCR System : Built-in : Tesseract (zero setup, bundled with the library) HTTP Servers : Plug in any OCR server (EasyOCR, PaddleOCR, custom) Standard API : Simple, well-defined OCR API specification Complexity Detection : Cheaply check whether a document needs OCR or heavier parsing — route, reject, or estimate cost before a full parse Screenshot Generation : Generate high-quality page screenshots for LLM agents Multiple Output Formats : Markdown, JSON, and Text Markdown Output : Structured Markdown with headings, tables, lists, images, and links — great for feeding LLMs and RAG pipelines Bounding Boxes : Precise text positioning information Multi-language : Use from Rust, Node.js/TypeScript, Python, or the browser (WASM) Multi-platform : Linux, macOS (Intel/ARM), Windows  Loading Installation Install via your preferred package manager. All versions (except WASM) ship with the same  CLI. Language Install Library Docs Node.js / TypeScript  Node.js README Python  Python README Rust  (CLI) /  (lib) Rust README (crates.io) Browser (WASM)  WASM README Agent Skill You can use  as an agent skill, downloading it with the  CLI tool:  Or copy-pasting the  file to your own skills setup. See the Agent Skill guide for requirements and usage patterns. CLI Usage The CLI is the same across all installations (  ,  ,  ). Parse Files  Markdown Output LiteParse can render documents directly to Markdown. This means reconstructing headings, tables, lists, images, and links from the spatial layout. This is ideal for feeding documents to LLMs and RAG pipelines. This mode is purely heuristics and rule-based, so complex documents may not render perfectly, but it will be fast.  Image handling is controlled by  : Mode Behavior  (default) Emits  references in reading order  Strips images entirely  Emits the same image references as   is the only option that enables embedded-image extraction.  requires it and writes the extracted bytes to disk. JSON output contains each image's  ,  , page bbox, intrinsic pixel dimensions, rotation, format, and duplicate relationship; pixel bytes are never embedded in JSON. Identical image resources reuse the same output file. Library callers can opt in with  (Rust),  (Node/WASM), or  (Python). It defaults to false. Markdown image mode controls presentation only; placeholder refs are still discovered without bytes. Markdown reconstruction quality varies with document complexity. For the hardest documents (dense tables, multi-column layouts, scans), LlamaParse remains the most accurate option. Vector Graphics Vector path output is opt-in because path-heavy PDFs can produce large payloads. Enable it with  , Rust/Python  , or JavaScript/WASM  . Each page then includes  (  in JavaScript) with:  : path bounding box, stroke/fill paint state and ARGB colors, and whether the path contains a Bezier curve.  : compatible horizontal/vertical segments merged using stroke width and paint colors, with top-left 72-DPI viewport coordinates. The representation follows LlamaParse PDFium path extraction; LiteParse calls the shape rectangle  rather than PDFium's  , and uses  /  rather than  /  . The field is absent (or  /  ) by default. Diagonal and curved segments are represented by their parent shape but are not emitted as lines. Tagged PDF structure tree Enable  (Rust/Python  , JavaScript/WASM  ) to add a page-scoped  . It preserves every root and recursively exposes element type, ID, actual/alternate text, title, typed scalar attributes, marked-content IDs, children, and referenced link annotations. The field is absent by default; enabled untagged pages contain  . D

## Code / Examples

```
flowchart LR subgraph Input["Input Formats"] direction TB PDF["PDF"] DOCX["DOCX"] XLSX["XLSX"] PPTX["PPTX"] IMG["Images"] end subgraph Core["Rust Core"] direction TB CONV["Format Conversion\nLibreOffice / Rust image + resvg + usvg crates"] EXTRACT["Text Extraction\nPDFium C library"] OCR["Selective OCR\nTesseract / HTTP / Custom"] MERGE["OCR Merge\nNative text + OCR results"] PROJ["Grid Projection\nSpatial layout reconstruction"] CONV --> EXTRACT EXTRACT --> OCR --> MERGE --> PROJ EXTRACT --> MERGE end subgraph Output[" Output "] direction TB JSON["Structured JSON\ntext + bounding boxes"] TEXT["Plain Text\nlayout-preserved"] SCREEN["Screenshots\nPNG rendering"] end subgraph Bindings["Language Bindings"] direction TB NAPI["Node.js / TypeScript\nnapi-rs"] PYO3["Python\nPyO3"] WASM["Browser / WASM\nwasm-bindgen"] CLI["CLI\ncargo / npm / pip"] NAPI ~~~ PYO3 ~~~ WASM ~~~ CLI end PDF --> EXTRACT DOCX & XLSX & PPTX & IMG --> CONV PROJ --> JSON & TEXT & SCREEN JSON & TEXT & SCREEN --> Bindings style Input fill:#F5F5F5,color:#000000,stroke:#37D7FA,stroke-width:2px style Core fill:#F5F5F5,color:#000000,stroke:#3E18F9,stroke-width:2px style Output fill:#F5F5F5,color:#000000,stroke:#FF8705,stroke-width:2px style Bindings fill:#F5F5F5,color:#000000,stroke:#FF8DF2,stroke-width:2px style PDF fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px style DOCX fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px style XLSX fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px sty
```
```
lit
```
```
npm i -g @llamaindex/liteparse
```
```
pip install liteparse
```
```
cargo install liteparse
```
```
cargo add liteparse
```
```
npm i @llamaindex/liteparse-wasm
```
```
liteparse
```


---
*Source: [search.app](https://search.app/rMEKH)*

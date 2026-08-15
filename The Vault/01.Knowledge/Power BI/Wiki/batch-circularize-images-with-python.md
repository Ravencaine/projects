---
created: 2026-08-13
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: workflow
tags: [python, pillow, batch-image, circular-image, chatgpt-script]
---

# Batch Circularize Images with Python

Use a short Pillow (PIL) script to convert every image in a folder to a circular PNG — useful when there are dozens or hundreds of files and PowerPoint's manual crop won't scale.

## When to Use

- You have many local image files (10s, 100s, 1000s).
- You don't want to click through each one in PowerPoint.
- You have (or can install) Python + Pillow on your machine.

## Prerequisites

- Python 3 with `Pillow` installed:
  ```bash
  pip install Pillow
  ```
- A folder containing the source images
- The original prompt below is enough to generate the script with any LLM

## Steps

### 1 — Generate the Script with an LLM

You don't need to know Python to write this. Prompt ChatGPT or Claude with:

> *"Write a Python script that makes all images in a folder circular by applying a circular mask. Save the results as PNGs with a transparent background."*

The expected output is roughly:

```python
import os
from PIL import Image, ImageDraw

INPUT_DIR  = r"C:\path\to\input_images"
OUTPUT_DIR = r"C:\path\to\circular_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue
    img = Image.open(os.path.join(INPUT_DIR, filename)).convert("RGBA")

    # Build a circular mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

    # Apply the mask — pixels outside the circle become transparent
    result = Image.new("RGBA", img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)

    out_name = os.path.splitext(filename)[0] + ".png"
    result.save(os.path.join(OUTPUT_DIR, out_name))

print(f"Done — wrote {len(os.listdir(OUTPUT_DIR))} files")
```

### 2 — Run the Script

Open Command Prompt → navigate to the script folder → `python circularize.py`.

### 3 — Optional: Generate a URL List Programmatically

If you also need the shareable URLs (e.g. to upload to a CDN or OneDrive), add a second small script that walks the output folder and emits a CSV/JSON of filenames → URLs.

### 4 — Wire Up in Power BI

Same as [[pre-circularize-images-in-powerpoint]] — host the PNGs where Power BI can reach them, set the URL column's data category to **Image URL**, drop into a Card visual with **Image type = Image URL**.

## Variations

- **Square with rounded corners** — replace `draw.ellipse(...)` with `draw.rounded_rectangle((0, 0, w, h), radius=20, fill=255)`.
- **Resize on the way through** — add `img = img.resize((256, 256))` before the mask step for consistent output sizes.
- **Different size per file** — pass through `--size` or read from filename.
- **Compress output** — `result.save(..., optimize=True)` reduces file size for the web.

## Pros

- Scales to thousands of files in seconds.
- Reproducible — same script re-runs cleanly when images change.
- Output is a normal raster file — works in any visual.

## Cons

- Requires Python install + Pillow dependency.
- Loses dynamic switching back to the square version.
- One-shot batch — won't react to new images arriving in the source folder.

## Related

- [[pre-circularize-images-in-powerpoint]] — for small sets
- [[circular-overlay-mask-powerpoint-power-bi]] — alternative that keeps the original image
- [[circular-image-approaches-decision-guide]] — when to use which approach

---
name: bg-remover-selector
description: Intelligent background removal tool selector and executor. Analyzes an image to determine its category (portrait, VFX, cartoon, e-commerce, complex, animals) and recommends the optimal Replicate background removal model, then runs it. Use when the user wants to (1) remove a background from an image, (2) choose the best bg removal tool for an image, (3) compare background removal results, (4) process images with transparent backgrounds, or (5) mentions "remove background", "bg removal", "cut out", "transparent background", "chroma key", or "green screen removal". Requires REPLICATE_API_TOKEN environment variable.
---

# Background Remover Selector

Analyze an image, select the best background removal tool based on empirical test data, and run it via the Replicate API.

## Prerequisites

- `REPLICATE_API_TOKEN` env var must be set. If missing, prompt the user to set it.
- `replicate` Python package: `pip install replicate`

## Workflow

### Step 1: Analyze the Image

Read the user's image using the Read tool. Classify it into one of these categories based on visual content:

| Category | Indicators |
|----------|-----------|
| `portrait` | Human faces, hair detail, skin texture, headshots, group photos |
| `vfx` | Glows, light rays, semi-transparent effects, particle systems, lens flares |
| `cartoon` | Illustrated/3D characters, vector art, game sprites, cel-shaded outlines |
| `ecommerce` | Product on studio/solid background, catalog shots, 3D product renders |
| `complex` | Multiple objects as foreground, UI elements, reflective surfaces, ambiguous depth |
| `low_contrast` | Subject color matches background, camouflage effect, minimal color difference |
| `green_screen` | Solid chroma key green/blue background |
| `animals` | Animal subjects with fur/feather texture |

Also note secondary characteristics:
- Has fine hair/flyaways?
- Has semi-transparent/glowing elements?
- Has green screen background?
- Subject color similar to background?

### Step 2: Select the Best Tool

Apply this decision logic (in priority order):

1. **Fine hair or flyaway strands** → `851-labs/background-remover` (avg 9.0/10 on portraits)
2. **Semi-transparent glows or VFX** → `bria/remove-background` (avg 8/10) or `lucataco/remove-bg` (avg 7.3/10 for gradient-style VFX)
3. **Cartoon/illustration/game asset** → `lucataco/remove-bg` (avg 7.0/10)
4. **Product photography/e-commerce** → `851-labs/background-remover` (avg 7.5/10)
5. **Complex multi-object/UI scenes** → `bria/remove-background` (avg 6.8/10)
6. **Low contrast (subject matches bg)** → `men1scus/birefnet` (avg 7.0/10)
7. **Green screen / chroma key** → `lucataco/remove-bg` (avg 7.5/10)
8. **Animals with fur** → `851-labs/background-remover` (avg 7.0/10)
9. **General / unsure** → `851-labs/background-remover` (most consistent overall at 7.4/10)

For detailed scoring data, see [references/tool-comparison.md](references/tool-comparison.md).

### Step 3: Present Recommendation

Before running, tell the user:
- Detected category
- Recommended tool and why
- Expected quality score

Example:
```
Detected: Portrait with backlit flyaway hair
Recommended: 851 Labs (851-labs/background-remover)
Expected quality: ~9/10 for edge accuracy and detail preservation
```

### Step 4: Run the Tool

Execute the removal script:

```bash
python3 scripts/remove_bg.py --model MODEL_ID --input IMAGE_PATH --output OUTPUT_PATH
```

Example:
```bash
python3 scripts/remove_bg.py \
  --model 851-labs/background-remover \
  --input /path/to/photo.png \
  --output /path/to/photo_nobg.png
```

If no `--output` is given, it defaults to `{input}_nobg.png`.

### Step 5: Deliver Result

Show the user the output path and offer to open or view the result.

## Available Models Quick Reference

| Model | Best For | Avg Score |
|-------|----------|-----------|
| `851-labs/background-remover` | Portraits, products, general | 7.4 |
| `lucataco/remove-bg` | Cartoons, green screen, VFX | 6.8 |
| `bria/remove-background` | Complex scenes, VFX transparency | 6.7 |
| `men1scus/birefnet` | Low contrast, geometric shapes | 5.4 |
| `cjwbw/rembg` | Basic/budget removal | 4.1 |

## User Override

If the user explicitly requests a specific tool, use that tool regardless of the analysis. The recommendation is advisory.

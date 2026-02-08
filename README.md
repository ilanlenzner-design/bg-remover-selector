# bg-remover-selector

A Claude Code skill that intelligently selects and runs the best background removal tool for your image.

Instead of guessing which AI model to use, this skill analyzes your image, classifies it into a category, and picks the optimal Replicate model based on empirical test data from **22 diverse test cases** across **8 image categories**.

## How It Works

```
You: "Remove the background from this photo"
                    |
        Skill analyzes the image
                    |
    Classifies: portrait, cartoon, VFX,
    e-commerce, complex, low-contrast,
    green screen, or animals
                    |
    Selects the highest-scoring model
    for that category
                    |
    Runs it via Replicate API
                    |
    Delivers the transparent PNG
```

## Best Tool by Category

| Image Type | Recommended Model | Avg Score |
|---|---|---|
| Portraits & Fine Hair | 851 Labs | 9.0/10 |
| VFX & Transparent Glows | BRIA AI | 8.0/10 |
| Cartoon & Illustration | Lucataco | 7.0/10 |
| E-commerce Products | 851 Labs | 7.5/10 |
| Complex Multi-Object | BRIA AI | 6.8/10 |
| Low Contrast | BiRefNet | 7.0/10 |
| Green Screen / Chroma Key | Lucataco | 7.5/10 |
| Animals & Fur | 851 Labs | 7.0/10 |

## Tested Models

| Model | Replicate ID | Best For |
|---|---|---|
| 851 Labs | `851-labs/background-remover` | Portraits, products, general use |
| Lucataco Tracer | `lucataco/remove-bg` | Cartoons, green screen, VFX edges |
| BRIA AI | `bria/remove-background` | Complex scenes, VFX transparency |
| BiRefNet | `men1scus/birefnet` | Low contrast, geometric shapes |
| CJWBW RemBG | `cjwbw/rembg` | Basic/budget removal |

## Installation

### As a Claude Code Skill

```bash
claude skill install /path/to/bg-remover-selector
```

Or copy the `bg-remover-selector/` folder into `~/.claude/skills/`.

### Prerequisites

1. **Replicate API Token** - Get one at [replicate.com](https://replicate.com)

```bash
export REPLICATE_API_TOKEN='r8_your_token_here'
```

2. **Python package**

```bash
pip install replicate
```

## Usage

Once installed, just ask Claude to remove a background:

- *"Remove the background from this image"*
- *"Which bg removal tool should I use for this cartoon?"*
- *"Cut out this product photo"*
- *"Remove the green screen from this sprite sheet"*

The skill will automatically:
1. Analyze your image
2. Recommend the best tool with expected quality score
3. Run it via Replicate
4. Save the result as a transparent PNG

## Standalone Script Usage

You can also use the script directly:

```bash
python3 scripts/remove_bg.py \
  --model 851-labs/background-remover \
  --input photo.png \
  --output photo_nobg.png
```

## Project Structure

```
bg-remover-selector/
├── SKILL.md                      # Skill definition & decision logic
├── README.md                     # This file
├── scripts/
│   └── remove_bg.py              # Replicate API runner
└── references/
    └── tool-comparison.md        # Full scoring data from 22 test cases
```

## Test Data

The recommendations are based on rigorous testing across these categories:

- **VFX**: Fiery stars, glowing suns, starburst explosions, transparent beams
- **Cartoon**: 3D characters, sprite sheets, illustrated scenes, game UI
- **Portrait**: Backlit photos, curly hair, group shots
- **E-commerce**: Monochromatic renders, product shots, glossy objects
- **Complex**: Multi-object scenes, reflective surfaces, low contrast

Each image was processed by all 5 tools and scored on:
- Edge Accuracy
- Detail Preservation
- Transparency Handling
- Overall Quality

## License

MIT

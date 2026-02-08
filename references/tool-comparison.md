# Background Removal Tool Comparison Data

## Tool Registry

| ID | Model ID | Display Name |
|----|----------|-------------|
| 851 | `851-labs/background-remover` | 851 Labs |
| lucataco | `lucataco/remove-bg` | Lucataco Tracer |
| bria | `bria/remove-background` | BRIA AI (Official) |
| birefnet | `men1scus/birefnet` | BiRefNet (High-Res) |
| cjwbw | `cjwbw/rembg` | CJWBW RemBG |

## Category Definitions

| Category | Description | Examples |
|----------|-------------|---------|
| portrait | Human subjects, hair detail, skin texture | Headshots, group photos, fitness portraits |
| vfx | Glows, transparency, light rays, semi-transparent effects | Fire effects, lens flares, particle systems |
| cartoon | Illustrated/3D rendered characters and assets | Game characters, vector art, sprite sheets |
| ecommerce | Product photography, studio shots | Product catalogs, 3D renders on solid backgrounds |
| complex | Multi-object scenes, UI elements, ambiguous foreground/background | Game UIs, scenes with reflections, low-contrast |
| animals | Animal subjects with fur/feather texture | Pet photos, wildlife, 3D animal renders |

## Performance Scores by Category (average overall score)

### Portrait & Fine Hair
| Tool | Score |
|------|-------|
| 851 Labs | **9.0** |
| BRIA AI | 8.0 |
| BiRefNet | 7.0 |
| Lucataco | 6.0 |
| CJWBW | 4.0 |

### VFX & Transparent Effects
| Tool | Score |
|------|-------|
| Lucataco | **7.3** |
| 851 Labs | 7.0 |
| BRIA AI | 6.5 |
| BiRefNet | 3.8 |
| CJWBW | 2.8 |

### Cartoon & Illustration
| Tool | Score |
|------|-------|
| Lucataco | **7.0** |
| 851 Labs | 6.9 |
| BRIA AI | 6.0 |
| CJWBW | 5.5 |
| BiRefNet | 5.5 |

### E-commerce Products
| Tool | Score |
|------|-------|
| 851 Labs | **7.5** |
| Lucataco | 7.0 |
| BRIA AI | 6.5 |
| BiRefNet | 5.5 |
| CJWBW | 4.0 |

### Complex Scenes
| Tool | Score |
|------|-------|
| BRIA AI | **6.8** |
| 851 Labs | 6.5 |
| Lucataco | 6.3 |
| BiRefNet | 5.5 |
| CJWBW | 4.0 |

### Low Contrast (subject similar color to background)
| Tool | Score |
|------|-------|
| BiRefNet | **7.0** |
| CJWBW | **7.0** |
| 851 Labs | 6.0 |
| Lucataco | 6.0 |
| BRIA AI | 4.0 |

### Green Screen / Chroma Key
| Tool | Score |
|------|-------|
| Lucataco | **7.5** |
| 851 Labs | 7.2 |
| BRIA AI | 6.5 |
| BiRefNet | 5.5 |
| CJWBW | 5.5 |

### Animals & Fur
| Tool | Score |
|------|-------|
| 851 Labs | **7.0** |
| Lucataco | **7.0** |
| BRIA AI | **7.0** |
| BiRefNet | **7.0** |
| CJWBW | 4.0 |

## Decision Matrix

```
Image has fine hair/flyaways?     → 851 Labs (851-labs/background-remover)
Image has glowing/transparent FX? → BRIA AI (bria/remove-background) or Lucataco (lucataco/remove-bg)
Image is cartoon/illustration?    → Lucataco (lucataco/remove-bg)
Image is product photography?     → 851 Labs (851-labs/background-remover)
Image has multiple UI elements?   → BRIA AI (bria/remove-background)
Subject matches background color? → BiRefNet (men1scus/birefnet)
Image is green screen?            → Lucataco (lucataco/remove-bg)
Image has animal fur?             → 851 Labs (851-labs/background-remover)
General / unsure?                 → 851 Labs (851-labs/background-remover)
```

## Detailed Test Cases

### Test: Fiery Star with Glow Effects (VFX)
Challenge: Semi-transparent glow, no hard edges, light rays fading into background
- BRIA AI: **8/10** (best alpha matting for complex glows)
- 851 Labs: 6/10
- BiRefNet: 5/10
- Lucataco: 2/10
- CJWBW: 1/10

### Test: Backlit Fitness Portrait (Portrait)
Challenge: Backlit hair with flyaways, halo effects on shoulders
- 851 Labs: **10/10** (exceptional hair strand preservation)
- BRIA AI: 8/10
- BiRefNet: 7/10
- Lucataco: 5/10
- CJWBW: 4/10

### Test: 3D Superhero Pig Green Screen (Cartoon)
Challenge: Green spill on glossy 3D surfaces, floor shadows
- Lucataco: **8/10** (best green spill removal)
- 851 Labs: 8/10
- BRIA AI: 6/10
- BiRefNet: 5/10
- CJWBW: 4/10

### Test: Monochromatic 3D Duck (E-commerce)
Challenge: No color info, grayscale subject, shadow blending
- 851 Labs: **8/10** (best luminance-based edge detection)
- Lucataco: 7/10
- BRIA AI: 6/10
- BiRefNet: 5/10
- CJWBW: 4/10

### Test: Mobile Game UI and Cards (Complex)
Challenge: Multiple spatially separated UI elements, glowing arrow
- BiRefNet: **7/10**
- Lucataco: **7/10**
- BRIA AI: 6/10
- 851 Labs: 3/10
- CJWBW: 1/10

### Test: 3D Boy Blue on Blue (Low Contrast)
Challenge: Blue shorts/shoes against blue background
- BiRefNet: **7/10** (best color-agnostic edge detection)
- CJWBW: **7/10**
- 851 Labs: 6/10
- Lucataco: 6/10
- BRIA AI: 4/10

### Test: Animated Block Characters Ice Skating (Complex/Reflections)
Challenge: Reflective icy surface, falling snow, color overlap
- BRIA AI: **7/10** (best reflection handling)
- 851 Labs: 7/10
- BiRefNet: 6/10
- Lucataco: 2/10 (fails on reflective surfaces)
- CJWBW: 1/10

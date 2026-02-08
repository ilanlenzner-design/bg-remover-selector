#!/usr/bin/env python3
"""
Background Removal Script using Replicate API.
Runs a specified background removal model on an input image.

Usage:
    python3 remove_bg.py --model MODEL_ID --input IMAGE_PATH [--output OUTPUT_PATH]

Models:
    851-labs/background-remover   - Best for portraits, e-commerce, general use
    lucataco/remove-bg            - Best for cartoons, green screen, VFX
    bria/remove-background        - Best for complex scenes, VFX transparency
    men1scus/birefnet             - Best for low-contrast scenarios
    cjwbw/rembg                   - Budget option, basic removal

Environment:
    REPLICATE_API_TOKEN must be set.
"""

import argparse
import os
import sys
import json
import urllib.request
import urllib.error


def check_token():
    token = os.environ.get("REPLICATE_API_TOKEN", "")
    if not token:
        print("ERROR: REPLICATE_API_TOKEN environment variable is not set.", file=sys.stderr)
        print("Set it with: export REPLICATE_API_TOKEN='r8_...'", file=sys.stderr)
        sys.exit(1)
    return token


def run_model(model_id, image_path, output_path, token):
    """Run a Replicate model and save the output."""
    import replicate

    os.environ["REPLICATE_API_TOKEN"] = token

    # Determine input format based on model
    print(f"Running {model_id} on {image_path}...")

    with open(image_path, "rb") as f:
        image_data = f

        # Different models accept different input schemas
        if model_id == "851-labs/background-remover":
            output = replicate.run(model_id, input={"image": f})
        elif model_id == "lucataco/remove-bg":
            output = replicate.run(model_id, input={"image": f})
        elif model_id == "bria/remove-background":
            output = replicate.run(model_id, input={"image": f})
        elif model_id == "men1scus/birefnet":
            output = replicate.run(model_id, input={"image": f})
        elif model_id == "cjwbw/rembg":
            output = replicate.run(model_id, input={"image": f})
        else:
            print(f"Unknown model: {model_id}", file=sys.stderr)
            sys.exit(1)

    # Handle output - could be a URL string or a FileOutput object
    result_url = None
    if isinstance(output, str):
        result_url = output
    elif hasattr(output, "url"):
        result_url = output.url
    elif isinstance(output, list) and len(output) > 0:
        item = output[0]
        result_url = item if isinstance(item, str) else getattr(item, "url", str(item))
    else:
        result_url = str(output)

    # Download the result
    print(f"Downloading result from: {result_url}")
    req = urllib.request.Request(result_url)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    with open(output_path, "wb") as f:
        f.write(data)

    print(f"Saved to: {output_path}")
    print(json.dumps({"status": "success", "output": output_path, "model": model_id, "url": result_url}))
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Remove background from an image using Replicate API")
    parser.add_argument("--model", required=True, help="Replicate model ID (e.g., 851-labs/background-remover)")
    parser.add_argument("--input", required=True, help="Path to the input image")
    parser.add_argument("--output", default=None, help="Path for the output image (default: input_nobg.png)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    token = check_token()

    if args.output is None:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_nobg.png"

    run_model(args.model, args.input, args.output, token)


if __name__ == "__main__":
    main()

"""CLI renderer."""
import argparse
from pathlib import Path
from manim import tempconfig
from .model import load_spec
from .scene import FlowScene

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("media"))
    parser.add_argument("--quality", choices=["preview", "full"], default="preview")
    args = parser.parse_args()
    spec = args.spec.resolve()
    load_spec(spec)
    width, height = (1920, 1080) if args.quality == "full" else (854, 480)
    with tempconfig({
        "media_dir": str(args.output_dir.resolve()),
        "pixel_width": width,
        "pixel_height": height,
        "frame_rate": 30,
        "output_file": spec.stem,
        "format": "mp4",
        "write_to_movie": True,
        "disable_caching": True,
    }):
        scene = FlowScene()
        scene.spec_path = spec
        scene.render()

if __name__ == "__main__":
    main()

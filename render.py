"""Build step (run once on the author's machine, not by the grader).

Screenshots page.html at 1024x1024 with headless Chrome and saves it as entry.png,
dropping to a 256-colour palette only if the full-colour PNG is over 1 MiB.
main.ts then just copies entry.png, so every run writes the same bytes.
"""
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
SHOT = ROOT / "build" / "shot.png"
ENTRY = ROOT / "entry.png"
MAX_BYTES = 1_048_576


def screenshot() -> None:
    SHOT.parent.mkdir(exist_ok=True)
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--force-device-scale-factor=1", "--window-size=1024,1024",
        f"--screenshot={SHOT}", (ROOT / "page.html").as_uri(),
    ]
    subprocess.run(cmd, check=True, timeout=90, capture_output=True)


def write_entry() -> None:
    img = Image.open(SHOT).convert("RGB")
    if img.size != (1024, 1024):
        sys.exit(f"unexpected screenshot size {img.size}")
    img.save(ENTRY, "PNG", optimize=True)
    if ENTRY.stat().st_size > MAX_BYTES:
        pal = img.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        pal.save(ENTRY, "PNG", optimize=True)
    size = ENTRY.stat().st_size
    print(f"entry.png 1024x1024, {size} bytes")
    if size > MAX_BYTES:
        sys.exit("entry.png is still over 1 MiB")


if __name__ == "__main__":
    screenshot()
    write_entry()

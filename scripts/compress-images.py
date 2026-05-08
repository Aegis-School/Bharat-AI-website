"""
compress-images.py — One-shot image-compression utility for bharataiinnovation.com.

Reads all images referenced from *.html / css/style.css, compresses oversized
ones in-place, backs up originals to images/originals/, and writes a WebP
sibling next to each compressed JPEG/PNG so a future <picture> upgrade is easy.

Usage:
    # Dry run (no changes; prints what would happen)
    python scripts/compress-images.py --dry-run

    # Real run
    python scripts/compress-images.py

Targets:
    - Gallery photos: max 1600px wide, JPEG q=78
    - Speaker portraits: max 800px wide, JPEG q=82
    - Floor plan / expo layout: max 1800px wide, JPEG q=80
    - Skips images already <300 KB
"""
import argparse, re, sys, shutil
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
ORIG_DIR = ROOT / "images" / "originals"

PROFILES = {
    # path-fragment match -> (max_width, jpeg_quality, webp_quality)
    "images/gallery/":  (1600, 78, 75),
    "speaker-":          (800, 82, 78),
    "expo-layout":      (1800, 80, 75),
    "default":          (1600, 80, 75),
}

def pick_profile(rel_path: str):
    rel = rel_path.replace("\\", "/")
    for key, val in PROFILES.items():
        if key != "default" and key in rel:
            return val
    return PROFILES["default"]

def referenced_images() -> set[str]:
    seen = set()
    pat = re.compile(r'''(?:src|href|content)=["']([^"']*(?:\.jpg|\.jpeg|\.png|\.avif|\.webp))["']''', re.IGNORECASE)
    for html in ROOT.glob("*.html"):
        for m in pat.finditer(html.read_text(encoding="utf-8")):
            ref = m.group(1)
            if not ref.startswith(("http://", "https://", "data:")):
                seen.add(ref.lstrip("./").replace("\\", "/"))
    css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
    for m in re.finditer(r'''url\(["']?([^"')]+)["']?\)''', css):
        ref = m.group(1)
        if not ref.startswith(("http", "data:")):
            seen.add(ref.lstrip("./").replace("\\", "/"))
    return seen

def compress_one(src: Path, max_w: int, jpeg_q: int, webp_q: int, dry_run: bool):
    orig_size = src.stat().st_size
    try:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)  # respect EXIF rotation
            w, h = im.size
            ratio = max_w / w if w > max_w else 1.0
            new_w, new_h = (max_w, int(h * ratio)) if ratio < 1.0 else (w, h)

            if dry_run:
                # Estimate: rough heuristic, JPEG at q=80 typically yields ~1bit/pixel = w*h/8 bytes
                est = (new_w * new_h) // 9
                return orig_size, est, (new_w, new_h)

            ORIG_DIR.mkdir(parents=True, exist_ok=True)
            backup = ORIG_DIR / src.name
            if not backup.exists():
                shutil.copy2(src, backup)

            if ratio < 1.0:
                im = im.resize((new_w, new_h), Image.LANCZOS)

            ext = src.suffix.lower()
            if ext in (".jpg", ".jpeg"):
                im_to_save = im.convert("RGB") if im.mode in ("RGBA", "P", "LA") else im
                im_to_save.save(src, "JPEG", quality=jpeg_q, optimize=True, progressive=True)
            elif ext == ".png":
                # If PNG of a photograph, recompress as JPEG and update the file extension is too risky;
                # keep PNG but optimize, then write a .webp sibling.
                im.save(src, "PNG", optimize=True)
            else:
                # leave avif/webp originals alone
                pass

            # WebP sibling
            webp_path = src.with_suffix(".webp")
            im_for_webp = im.convert("RGB") if im.mode in ("P", "LA") else im
            im_for_webp.save(webp_path, "WEBP", quality=webp_q, method=6)

            new_size = src.stat().st_size
            return orig_size, new_size, (new_w, new_h)
    except Exception as e:
        return orig_size, None, str(e)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--threshold", type=int, default=300_000, help="skip files smaller than this many bytes")
    args = ap.parse_args()

    refs = referenced_images()
    targets = []
    for rel in sorted(refs):
        p = ROOT / rel
        if p.exists() and p.stat().st_size > args.threshold:
            targets.append(p)

    if not targets:
        print("Nothing to compress.")
        return

    total_before = total_after = 0
    fails = 0

    print(f"{'Status':<10} {'Before':>10} {'After':>10} {'Saved':>8}  Path")
    print("-" * 90)
    for p in targets:
        rel = p.relative_to(ROOT).as_posix()
        max_w, jpeg_q, webp_q = pick_profile(rel)
        before, after, dim = compress_one(p, max_w, jpeg_q, webp_q, args.dry_run)
        if after is None:
            fails += 1
            print(f"{'FAIL':<10} {before//1024:>7d} KB                       {rel}  ({dim})")
            continue
        total_before += before
        total_after += after
        saved_pct = (1 - after / before) * 100 if before else 0
        tag = "DRY-RUN" if args.dry_run else "OK"
        print(f"{tag:<10} {before//1024:>7d} KB {after//1024:>7d} KB {saved_pct:>6.1f}%  {rel} -> {dim[0]}x{dim[1]}")

    print("-" * 90)
    print(f"{len(targets)} files, before: {total_before/1024/1024:.1f} MB, after: {total_after/1024/1024:.1f} MB, saved: {(total_before-total_after)/1024/1024:.1f} MB ({(1 - total_after/total_before)*100 if total_before else 0:.1f}%)")
    if fails:
        print(f"{fails} files failed.")
    if args.dry_run:
        print("\n(dry-run; no files modified. Re-run without --dry-run to apply.)")
    else:
        print(f"\nOriginals backed up to: {ORIG_DIR.relative_to(ROOT)}")
        print("WebP siblings written next to each JPEG/PNG.")

if __name__ == "__main__":
    main()

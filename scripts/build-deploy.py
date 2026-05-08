"""
build-deploy.py — Create a clean ./deploy/ folder for Cloudflare Pages drag-drop.

Copies the live website assets and excludes:
- .git/, .github/, .vscode/, .claude/, .tdad/  (hidden dev folders)
- images/originals/  (raw photo backups, if present)
- scripts/, .gitignore, CLAUDE.md, *.py  (dev/tooling files)
- backup HTML files (*-backup.html)
- admin.html  (not for public site)
- images/expo-layout.png  (unused dupe of .jpg)

Usage:
    python scripts/build-deploy.py

After running:
    1. Drag the new ./deploy/ folder into Cloudflare Pages
    2. Save and deploy
"""
import shutil
import pathlib
import os

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEPLOY = ROOT / "deploy"

EXCLUDE_DIRS = {
    ".git", ".github", ".vscode", ".claude", ".tdad",
    "scripts", "deploy",  # don't copy ourselves
    "originals",  # safety: any folder named originals at any level
}

EXCLUDE_FILES = {
    ".gitignore", "CLAUDE.md",
    "register-backup.html", "contact-backup.html",
    "admin.html",
    "images/expo-layout.png",  # unused dupe
}

EXCLUDE_EXTENSIONS = {".py", ".pyc"}

def should_exclude(rel_path: pathlib.Path) -> bool:
    parts = rel_path.parts
    # Hidden / excluded dirs anywhere in the path
    for p in parts:
        if p in EXCLUDE_DIRS:
            return True
    # Specific files
    if rel_path.as_posix() in EXCLUDE_FILES:
        return True
    if rel_path.name in EXCLUDE_FILES:
        return True
    # Extensions
    if rel_path.suffix.lower() in EXCLUDE_EXTENSIONS:
        return True
    return False

def main():
    if DEPLOY.exists():
        print(f"Removing old {DEPLOY}/")
        shutil.rmtree(DEPLOY)
    DEPLOY.mkdir()

    copied = 0
    skipped = 0
    total_size = 0

    for src in ROOT.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(ROOT)
        if should_exclude(rel):
            skipped += 1
            continue
        dst = DEPLOY / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        total_size += src.stat().st_size
        copied += 1

    print(f"\nCopied {copied} files, skipped {skipped}")
    print(f"Total size: {total_size/1024/1024:.1f} MB")
    print(f"\nDeploy folder ready: {DEPLOY}")
    print("Next: Cloudflare Pages -> Create deployment -> drag the 'deploy' folder")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Nexus Engine build command. Usage: python build.py [windows|linux|macos|html|android]"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():
    parser = argparse.ArgumentParser(description="Nexus Engine Build — Made in Nexus")
    parser.add_argument("platform", nargs="?", default="auto",
                        choices=["auto", "windows", "linux", "macos", "html", "android"])
    parser.add_argument("--entry", "-e", default="main.py")
    parser.add_argument("--name", "-n", default="NexusGame")
    parser.add_argument("--icon", default=None)
    parser.add_argument("--onedir", action="store_true")
    args = parser.parse_args()

    platform = args.platform
    if platform == "auto":
        if sys.platform.startswith("win"):
            platform = "windows"
        elif sys.platform == "darwin":
            platform = "macos"
        else:
            platform = "linux"
        print(f"[NexusBuild] Plataforma detectada: {platform}")

    from nexus_engine.build.builder import Builder
    print("\n  NEXUS ENGINE BUILD — Made in Nexus\n")
    Builder(entry_point=args.entry, app_name=args.name, icon=args.icon,
            one_file=not args.onedir).build(platform)
    print("[NexusBuild] Made in Nexus")


if __name__ == "__main__":
    main()

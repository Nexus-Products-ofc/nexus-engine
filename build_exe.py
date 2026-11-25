#!/usr/bin/env python3
"""Build NexusEngine.exe with PyInstaller (run on Windows)."""
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main() -> int:
    if sys.platform != "win32":
        print("Run this on Windows to produce NexusEngine.exe:")
        print("  python build_exe.py")
        print("  or double-click build_exe.bat")
        return 1
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "pygame", "numpy"])
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--windowed", "--onefile",
        "--name", "NexusEngine",
        "--collect-all", "pygame",
        str(ROOT / "main.py"),
    ]
    subprocess.check_call(cmd, cwd=str(ROOT))
    print("OK:", ROOT / "dist" / "NexusEngine.exe")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

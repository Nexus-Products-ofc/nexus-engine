"""
Nexus Engine — entry point.
  python main.py              → showcase
  python main.py --editor     → Unity-like Engine Mode
  python main.py --platformer → 2D platformer
  python main.py --fps        → 3D first person
  python main.py --tps        → 3D third person
  python main.py --3d         → hello 3D
"""

import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def check_deps(need_3d=False):
    missing = []
    try:
        import pygame  # noqa: F401
    except ImportError:
        missing.append("pygame")
    if need_3d:
        try:
            import ursina  # noqa: F401
        except ImportError:
            pass  # examples have pygame fallback
    return missing


def main():
    args = sys.argv[1:]
    editor = "--editor" in args or "-e" in args
    use_3d = "--3d" in args
    platformer = "--platformer" in args
    fps = "--fps" in args
    tps = "--tps" in args

    missing = check_deps(need_3d=use_3d or fps or tps)
    if missing:
        print("=" * 50)
        print("  MISSING DEPENDENCIES")
        print("=" * 50)
        print(f"  pip install {' '.join(missing)}")
        print("=" * 50)
        try:
            input("\nPress ENTER to exit...")
        except Exception:
            pass
        sys.exit(1)

    if editor:
        from nexus_engine.editor import EngineMode
        print("[Nexus] Opening Engine Mode...")
        EngineMode().run()
        return

    if platformer:
        from nexus_engine.examples.platformer_2d import main as run_plat
        run_plat()
        return

    if fps:
        from nexus_engine.examples.fps_3d import main as run_fps
        run_fps()
        return

    if tps:
        from nexus_engine.examples.third_person_3d import main as run_tps
        run_tps()
        return

    if use_3d:
        from nexus_engine.examples.hello_3d import main as run3d
        run3d()
        return

    from nexus_engine.examples.showcase import main as run_showcase
    run_showcase()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[NexusEngine] Closed by user.")
    except Exception:
        print("\n" + "=" * 50)
        print("  ERROR OPENING NEXUS ENGINE")
        print("=" * 50)
        traceback.print_exc()
        print("=" * 50)
        try:
            input("\nPress ENTER to exit...")
        except Exception:
            pass
        sys.exit(1)

"""
Nexus Engine — entry point.
  python main.py
  python main.py --editor
  python main.py --project file.nexusEng
  python main.py --platformer
  python main.py --fps
  python main.py --tps
  python main.py --3d
"""

import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def check_deps():
    missing = []
    try:
        import pygame  # noqa: F401
    except ImportError:
        missing.append("pygame")
    return missing


def main():
    args = sys.argv[1:]
    editor = "--editor" in args or "-e" in args
    use_3d = "--3d" in args
    platformer = "--platformer" in args
    fps = "--fps" in args
    tps = "--tps" in args
    project = None
    if "--project" in args:
        i = args.index("--project")
        if i + 1 < len(args):
            project = args[i + 1]

    missing = check_deps()
    if missing:
        print("pip install " + " ".join(missing))
        sys.exit(1)

    if project:
        from nexus_engine.editor import EngineMode
        from nexus_engine.project.project_file import load_project, scene_dict_to_world
        print(f"[Nexus] Opening project: {project}")
        ed = EngineMode()
        def _load_world():
            proj = load_project(project)
            ed.project = proj
            ed.project_path = project
            scene = proj.scenes.get(proj.main_scene) or {"entities": []}
            return scene_dict_to_world(scene, proj.main_scene)
        ed._create_demo_world = _load_world
        ed.run()
        return

    if editor:
        from nexus_engine.editor import EngineMode
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
        print("\n[NexusEngine] Closed.")
    except Exception:
        traceback.print_exc()
        sys.exit(1)

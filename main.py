"""
Nexus Engine — ponto de entrada.
Execute: python main.py
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
    try:
        import numpy  # noqa: F401
    except ImportError:
        pass
    return missing


def main():
    missing = check_deps()
    if missing:
        print("=" * 50)
        print("  DEPENDENCIAS FALTANDO")
        print("=" * 50)
        print("Rode no terminal:")
        print(f"  pip install {' '.join(missing)}")
        print()
        print("Ou:")
        print("  pip install -r requirements.txt")
        print("=" * 50)
        input("\nPressione ENTER para sair...")
        sys.exit(1)

    from nexus_engine.examples.showcase import main as run_showcase
    run_showcase()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[NexusEngine] Fechado pelo usuario.")
    except Exception:
        print("\n" + "=" * 50)
        print("  ERRO AO ABRIR A NEXUS ENGINE")
        print("=" * 50)
        traceback.print_exc()
        print("=" * 50)
        print("\nDicas:")
        print("  1. Abra o terminal NESTA pasta")
        print("  2. Rode:  pip install pygame numpy")
        print("  3. Rode:  python main.py")
        print("=" * 50)
        try:
            input("\nPressione ENTER para sair...")
        except Exception:
            pass
        sys.exit(1)

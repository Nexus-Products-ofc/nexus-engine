# Nexus Engine 1.0 TURBO

**Official open-source Python game engine** — Unity-inspired editor, ECS, 2D/3D backends, `.nexusEng` projects.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-yellow.svg)](https://www.python.org/)

> Official repo: https://github.com/heitorhanzelgontijo-svg/nexus-engine  
> Site: https://heitorhanzelgontijo-svg.github.io/nexus-engine/  
> Not affiliated with Unity Technologies.

---

## What is Nexus?

- **Engine Mode** — visual editor (Hierarchy, Scene, Inspector, Console, Project)
- **ECS** — entities, components, systems
- **2D & 3D** — Pygame, Ursina / Panda3D / Taichi
- **`.nexusEng` projects** — save/load scenes
- **Turbo profiles** — quality / balanced / turbo / ultra
- **Media & VFX** — music, SFX, images, particles, screen effects
- **MIT license** — free for commercial games

---

## Quick start

```bash
git clone https://github.com/heitorhanzelgontijo-svg/nexus-engine.git
cd nexus-engine
pip install pygame numpy
pip install ursina   # optional 3D
```

| Command | What it does |
|---------|----------------|
| `python main.py` | Showcase |
| `python main.py --editor` | **Unity-like editor** |
| `python main.py --project examples_projects/exemplo.nexusEng` | Open project |
| `python main.py --platformer` | 2D platformer |
| `python main.py --fps` | 3D first-person |
| `python main.py --tps` | 3D third-person |
| `python main.py --3d` | Hello 3D |
| `python build_exe.py --zip` | Windows EXE (on Windows) |

---

## Engine Mode (editor)

```
[ File | GameObject | Assets | Help ]
[ ▶ Play / ■ Stop ]
[ Hierarchy | Scene | Inspector ]
[ Project | Console ]
```

- **File** — New / Open / Save `.nexusEng`
- **GameObject** — Empty, Sprite, Block, Item
- **Assets** — Import Image
- **Space** Play · **N** Empty · **B** Block · **I** Item · **Del** Delete

Code: `nexus_engine/editor/editor_window.py`

---

## Project files (`.nexusEng`)

Example: `examples_projects/exemplo.nexusEng`

```bash
python main.py --project examples_projects/exemplo.nexusEng
```

Components v1: `Transform`, `SpriteRenderer`, `Camera`, `Rigidbody2D`, `BoxCollider2D`  
Docs: [docs/PROJECT_FORMAT.md](docs/PROJECT_FORMAT.md)

---

## Minimal API

```python
from nexus_engine import (
    Application, World, Transform, SpriteRenderer, Camera, Turbo, Debug
)

Turbo.set("turbo")
world = World("Game")
player = world.create_entity("Player")
player.add_component(Transform(100, 100))
player.add_component(SpriteRenderer(color=(100, 200, 255), width=32, height=32))
Application(title="My Game", backend="pygame", turbo="turbo").run(world)
```

### Packages

| Package | Role |
|---------|------|
| `core/` | Application, Engine, Turbo |
| `ecs/` | World, Entity, components |
| `editor/` | Engine Mode UI |
| `project/` | `.nexusEng` load/save |
| `physics/` `rendering/` `audio/` `vfx/` | Systems |
| `examples/` | Platformer, FPS, TPS |

---

## Build EXE (Windows)

```bat
python build_exe.py --zip
```

Output: `dist\NexusEngine.exe`  
SmartScreen may warn until code-signed.

---

## Trust

- Public MIT source
- Official URL only: `github.com/heitorhanzelgontijo-svg/nexus-engine`
- [SECURITY.md](SECURITY.md) · [TRUST.md](TRUST.md)

---

## Compare

| | Nexus | Unity | Godot |
|--|-------|-------|-------|
| Language | Python | C# | GDScript / C# |
| License | MIT | Proprietary* | MIT |
| Best for | Python indies, education | Mid/AAA | General indies |

---

## Support

- [Report bug](https://github.com/heitorhanzelgontijo-svg/nexus-engine/issues/new?labels=bug)
- [Suggest idea](https://github.com/heitorhanzelgontijo-svg/nexus-engine/issues/new?labels=enhancement)
- [Discussions](https://github.com/heitorhanzelgontijo-svg/nexus-engine/discussions)

## License

MIT — **Made in Nexus.**

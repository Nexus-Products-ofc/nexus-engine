<p align="center">
  <img src="docs/website/assets/logo.svg" width="120" alt="Nexus Engine" />
</p>

<h1 align="center">Nexus Engine</h1>

<p align="center">
  <b>Open-source Python game engine</b> — Unity-inspired architecture · Made in Nexus
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="docs/i18n/README.pt-BR.md">Português</a> ·
  <a href="docs/i18n/README.es.md">Español</a> ·
  <a href="docs/i18n/README.fr.md">Français</a> ·
  <a href="docs/i18n/README.de.md">Deutsch</a> ·
  <a href="docs/i18n/README.ja.md">日本語</a> ·
  <a href="docs/i18n/README.zh-CN.md">简体中文</a> ·
  <a href="docs/i18n/README.ru.md">Русский</a> ·
  <a href="docs/i18n/README.ar.md">العربية</a> ·
  <a href="docs/i18n/README.hi.md">हिन्दी</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/2D%20%7C%203D-purple" />
  <img src="https://img.shields.io/badge/version-0.5.0-orange" />
</p>

---

## Why Nexus can compete (for the right projects)

Nexus is not a pixel-perfect clone of Unity’s C++ core. It competes where Unity is heavy and Python is strong: 2D indies, education, jams, and rapid prototypes — with an **MIT** license.

## Nexus vs Unity vs Godot

| | **Nexus** | **Unity** | **Godot** |
|--|-----------|-----------|-----------|
| Main language | **Python** | C# | GDScript / C# |
| License | **MIT** | Proprietary* | MIT |
| Visual editor | Engine Mode | Full editor | Full editor |
| 2D | Strong (Pygame) | Excellent | Excellent |
| 3D | Ursina / Panda3D / Taichi | Excellent | Good |
| Best for | Python indies, jams, education | Mid/AAA, mobile polish | General indies |

**Advantages:** pure Python, MIT, Unity-like APIs, multi-backend, Engine Mode, Debug, SceneManager, Resources.

**Trade-offs:** younger editor, 3D via backends, Python performance limits, smaller asset store.

---

## Quick start

```bash
git clone https://github.com/heitorhanzelgontijo-svg/nexus-engine.git
cd nexus-engine
pip install pygame numpy

python main.py              # 2D showcase + Made in Nexus splash
python main.py --editor     # Unity-like Engine Mode
python main.py --3d         # 3D sample (pip install ursina)
python build.py             # export game
```

### Controls
Showcase: A/D move · Space jump · Shift dash · Click particles · F5/F9 save/load  
Engine Mode: Space Play/Pause · **N** new object · Del delete · F1 FPS · Esc close

---

## Architecture (Unity mapping)

| Unity | Nexus |
|-------|--------|
| GameObject | `Entity` |
| MonoBehaviour | `Component` |
| Scene | `World` + `SceneManager` |
| Debug.Log | `Debug.log` |
| Gizmos | `Gizmos.draw_line` |
| Resources.Load | `Resources.load` |
| Prefab | `Prefab` + `ObjectPool` |
| Coroutine | `wait_for_seconds` |

```python
from nexus_engine import Application, World, Transform, SpriteRenderer, Camera, Debug, SceneManager

world = SceneManager.create_scene("Level1")
player = world.create_entity("Player")
player.add_component(Transform(100, 100))
player.add_component(SpriteRenderer(color=(100, 200, 255), width=32, height=32))
Debug.log("Level1 ready")
Application(title="MyGame", backend="pygame").run(world)
```

### 3D

```bash
pip install ursina
python main.py --3d
```

---

## Feature set (v0.5)

ECS · Physics2D · Particles · Tilemap · UI · Audio · Prefabs · ObjectPool · Coroutines  
Scene JSON · Gizmos · Debug · **SceneManager** · **ProjectSettings** · **Resources**  
MeshRenderer / Camera3D · Engine Mode · Multi-platform build

---

## License

[MIT](LICENSE) — commercial games allowed.

**Made in Nexus**

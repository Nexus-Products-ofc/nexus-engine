# Nexus Engine

**Engine de jogos open-source em Python** — arquitetura inspirada na Unity · Made in Nexus

[English](../../README.md) · **Português** · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md)

## Por que a Nexus compete (nos projetos certos)

Não é um clone C++ da Unity. Compete onde Python é forte: protótipos rápidos, educação, indies 2D e ferramentas — com licença **MIT**.

## Nexus vs Unity vs Godot

| | Nexus | Unity | Godot |
|--|-------|-------|-------|
| Linguagem | Python | C# | GDScript / C# |
| Licença | MIT | Proprietária* | MIT |
| Editor | Engine Mode | Completo | Completo |
| 2D | Forte (Pygame) | Excelente | Excelente |
| 3D | Ursina / Panda3D | Excelente | Bom |

**Vantagens:** Python, MIT, conceitos Unity, multi-backend, Engine Mode.  
**Limitações:** editor jovem, 3D via backends, performance Python, menos assets prontos.

## Como começar

```bash
pip install pygame numpy
python main.py              # showcase 2D
python main.py --editor     # modo editor (estilo Unity)
python main.py --3d         # 3D (pip install ursina)
python build.py
```

**Showcase:** A/D andar · Espaço pular · Shift dash · Clique partículas · F5/F9 save  
**Editor:** Espaço Play · N novo objeto · Del apagar · F1 FPS

## Exemplo mínimo

```python
from nexus_engine import Application, World, Transform, SpriteRenderer, Camera, Debug
world = World("Jogo")
cam = world.create_entity("Cam")
cam.add_component(Transform(0, 0))
cam.add_component(Camera())
p = world.create_entity("Player")
p.add_component(Transform(100, 100))
p.add_component(SpriteRenderer(color=(100, 200, 255), width=32, height=32))
Debug.log("Pronto")
Application(title="Meu Jogo", backend="pygame").run(world)
```

## Recursos principais

ECS, Física2D, Partículas, Tilemap, UI, Áudio, Prefabs, Pool, Corrotinas, SceneManager, ProjectSettings, Resources, Debug/Gizmos, MeshRenderer/Camera3D, Engine Mode, Build multiplataforma.

## Licença

MIT — **Made in Nexus**

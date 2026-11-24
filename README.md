<p align="center">
  <strong>Nexus Engine</strong><br/>
  Open-source Python game engine — Unity-inspired · Made in Nexus
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
  <img alt="2D/3D" src="https://img.shields.io/badge/2D%20%7C%203D-purple" />
</p>

---

## Como começar

```bash
git clone https://github.com/heitorhanzelgontijo-svg/nexus-engine.git
cd nexus-engine
pip install pygame numpy

python main.py              # showcase 2D
python main.py --editor     # Engine Mode (estilo Unity)
python main.py --3d         # 3D (pip install ursina)
python build.py             # build do jogo
```

### Controles showcase
A/D andar · Espaço pular · Shift dash · Clique explosão · F5/F9 save/load · ESC sair

### Controles Engine Mode
Espaço Play/Pause · Clique Hierarchy seleciona · Delete remove · F1 FPS · ESC fecha

---

## Nexus vs Unity vs Godot

| | **Nexus** | **Unity** | **Godot** |
|--|-----------|-----------|----------|
| Linguagem | Python | C# | GDScript / C# |
| Licença | MIT | Proprietária* | MIT |
| Editor | Engine Mode (Hierarchy, Inspector, Scene, Console) | Completo | Completo |
| 2D | Forte (Pygame) | Excelente | Excelente |
| 3D | Ursina / Panda3D / Taichi | Excelente | Bom |
| Curva | Baixa (se sabe Python) | Média | Baixa–média |
| Ideal | Indies Python, protótipos, educação | Mid/AAA, mobile | Indies gerais |

### Vantagens Nexus
1. Python puro — protótipos rápidos
2. MIT — comercial sem runtime fee
3. Conceitos Unity (Transform, Rigidbody, Prefab, Coroutines)
4. Multi-backend (Pygame, Ursina, Panda3D, Taichi)
5. Engine Mode visual
6. Código aberto e legível

### Desvantagens Nexus
1. Editor ainda básico vs Unity/Godot
2. 3D em evolução (depende de backends)
3. Performance Python < C++/C# nativo em jogos pesados
4. Ecossistema de assets menor
5. Mobile/console experimental

**Escolha Nexus** para jams, educação e 2D indie em Python. **Unity/Godot** para 3D grande, mobile polido ou multiplayer complexo.

---

## 2D e 3D

**2D (padrão)** — `backend="pygame"`

```python
from nexus_engine import Application, World, Transform, SpriteRenderer, Camera
world = World("Game")
cam = world.create_entity("Cam")
cam.add_component(Transform(0, 0))
cam.add_component(Camera())
player = world.create_entity("Player")
player.add_component(Transform(100, 100))
player.add_component(SpriteRenderer(color=(100, 200, 255), width=32, height=32))
Application(title="Nexus 2D", backend="pygame").run(world)
```

**3D** — `MeshRenderer` + `Camera3D` + Ursina:

```bash
pip install ursina
python main.py --3d
```

```python
from nexus_engine import Application, World, Transform, MeshRenderer, Camera3D
world = World("Hello3D")
cam = world.create_entity("Main Camera")
cam.add_component(Transform(0, 2, -8))
cam.add_component(Camera3D(fov=60))
cube = world.create_entity("Cube")
cube.add_component(Transform(0, 1, 0))
cube.add_component(MeshRenderer(model="cube", color=(0.6, 0.4, 1, 1)))
Application(title="Nexus 3D", backend="ursina").run(world)
```

---

## Engine Mode

Janela estilo Unity Editor: Toolbar, Hierarchy, Scene, Inspector, Console.

```bash
python main.py --editor
python -m nexus_engine.editor
```

---

## Debug

```python
from nexus_engine import Debug, Gizmos, Vector2, Color
Debug.log("spawn")
Debug.log_warning("vida baixa")
Debug.log_error("falha")
Debug.show_fps = True
Gizmos.draw_line(Vector2(0, 0), Vector2(100, 100))
```

Overlay de FPS/entidades no jogo; logs no Console do Engine Mode.

---

## Build

```bash
python build.py
python build.py windows --name MeuJogo
```

---

## Licença

MIT — **Made in Nexus**

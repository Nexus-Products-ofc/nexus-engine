# Nexus Engine — API Reference (v0.5)

## Application & Engine

```python
from nexus_engine import Application, NexusEngine, ProjectSettings, SceneManager

app = Application(title="MyGame", width=1280, height=720, backend="pygame",
                  show_splash=True, watermark=True)
app.run(world)

engine = NexusEngine.instance()
engine.time.delta_time
engine.time.fps()
engine.quit()

s = ProjectSettings.instance()
s.product_name = "MyGame"

world = SceneManager.create_scene("Level1")
SceneManager.load_scene("Level1")
```

## ECS

```python
from nexus_engine import World, Component, Transform, SpriteRenderer, Camera

class Mover(Component):
    def update(self, dt):
        self.transform.x += 40 * dt

world = World("Main")
e = world.create_entity("Player")
e.add_component(Transform(100, 100))
e.add_component(SpriteRenderer(color=(100,200,255), width=32, height=32))
e.add_component(Mover())
world.find("Player")
world.destroy_entity(e)
```

## Physics / Input / Audio

```python
from nexus_engine import Rigidbody2D, BoxCollider2D, Physics2D, Vector2, Input, Audio

e.add_component(Rigidbody2D(mass=1.0))
e.add_component(BoxCollider2D(size=Vector2(32, 48)))
Physics2D.raycast(Vector2(0,0), Vector2(0,1), 100)

Input.get_key_down("space")
Input.get_axis("Horizontal")
Input.mouse_pressed(0)
Audio.play_sfx("jump.wav")
Audio.play_music("theme.ogg", loop=True)
```

## Particles / UI / Prefab / Coroutines / Save

```python
from nexus_engine import ParticleEmitter, Color, Prefab, ObjectPool
from nexus_engine import SceneSerializer, Resources, Debug, Gizmos
from nexus_engine import NexusEngine, wait_for_seconds

ParticleEmitter(max_particles=80, emission_rate=40, lifetime=0.7,
                start_color=Color(1,0.7,0.2,1), end_color=Color(1,0,0,0))

prefab = Prefab("Bullet")
prefab.add_component_factory(lambda: Transform())

def intro():
    yield wait_for_seconds(1.0)
NexusEngine.instance().start_coroutine(intro())

SceneSerializer.save(world, "saves/level.json")
Resources.load("config/game.json")
Debug.log("ok")
Gizmos.draw_line(Vector2(0,0), Vector2(100,100))
```

## 3D

```python
from nexus_engine import MeshRenderer, Camera3D
cam.add_component(Camera3D(fov=60))
cube.add_component(MeshRenderer(model="cube", color=(0.6,0.4,1,1)))
Application(backend="ursina").run(world)
```

## Engine Mode

```bash
python main.py --editor
python -m nexus_engine.editor
```

## Multi-platform build

```bash
python build.py
python build.py windows --name MyGame
python build.py linux --name MyGame
python build.py macos --name MyGame
python build.py html
python build.py android
```

| Target | Output |
|--------|--------|
| windows | dist/MyGame.exe |
| linux | dist/MyGame |
| macos | dist/ app or binary |
| html | dist/html/ |
| android | dist/android/ |

Full tutorial: `docs/website/tutorial.html`

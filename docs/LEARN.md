# Learn Nexus Engine 1.0 (English)

## Two paths

### 1) Unity-like editor
```bat
Nexus Engine.bat
# or
python main.py --editor
```
Hierarchy · Inspector · Scene · Console · Play

### 2) Code (optimized)
```python
from nexus_engine import Application, World, Transform, SpriteRenderer, Camera, Turbo, Debug
Turbo.set("turbo")
world = World("Game")
# ...
Application(title="My Game", backend="pygame", turbo="turbo").run(world)
```

## Windows Defender
SmartScreen blocks unsigned software. Use official GitHub downloads. Prefer `.bat` + Python over unknown `.exe`.
More info → Run anyway · or Properties → Unblock.

## Report
- Bugs: https://github.com/heitorhanzelgontijo-svg/nexus-engine/issues/new?labels=bug
- Ideas: https://github.com/heitorhanzelgontijo-svg/nexus-engine/issues/new?labels=enhancement
- Forum: https://github.com/heitorhanzelgontijo-svg/nexus-engine/discussions

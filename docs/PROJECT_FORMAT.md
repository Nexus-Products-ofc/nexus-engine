# `.nexusEng` project format

Nexus Engine project files are JSON with extension **`.nexusEng`**.

## In the editor

1. `python main.py --editor`
2. **File → Open .nexusEng…** / **Save** / **Save As…**

## CLI

```bash
python main.py --project examples_projects/exemplo.nexusEng
```

## Schema (v1)

- `format`: `nexusEng`
- `name`, `main_scene`, `settings`, `assets`
- `scenes.<name>.entities[]` with components:
  - Transform, SpriteRenderer, Camera, Rigidbody2D, BoxCollider2D

See `examples_projects/exemplo.nexusEng`.

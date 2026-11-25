"""Nexus Engine project files (*.nexusEng)."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

NEXUSENG_VERSION = 1
EXTENSION = ".nexusEng"


@dataclass
class ProjectFile:
    name: str = "Untitled"
    version: int = NEXUSENG_VERSION
    engine: str = "1.0.0"
    main_scene: str = "main"
    settings: Dict[str, Any] = field(default_factory=lambda: {
        "width": 960, "height": 540, "turbo": "turbo", "backend": "pygame",
    })
    scenes: Dict[str, Any] = field(default_factory=dict)
    assets: List[str] = field(default_factory=list)
    path: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "format": "nexusEng",
            "version": self.version,
            "engine": self.engine,
            "name": self.name,
            "main_scene": self.main_scene,
            "settings": self.settings,
            "scenes": self.scenes,
            "assets": self.assets,
        }

    @classmethod
    def from_dict(cls, data: dict, path: Optional[str] = None) -> "ProjectFile":
        return cls(
            name=data.get("name", "Untitled"),
            version=int(data.get("version", NEXUSENG_VERSION)),
            engine=str(data.get("engine", "1.0.0")),
            main_scene=data.get("main_scene", "main"),
            settings=dict(data.get("settings") or {}),
            scenes=dict(data.get("scenes") or {}),
            assets=list(data.get("assets") or []),
            path=path,
        )


def save_project(project: ProjectFile, path: str | Path) -> Path:
    path = Path(path)
    if path.suffix.lower() != EXTENSION.lower():
        path = path.with_suffix(EXTENSION)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(project.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    project.path = str(path)
    return path


def load_project(path: str | Path) -> ProjectFile:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    return ProjectFile.from_dict(data, path=str(path))


def world_to_scene_dict(world) -> dict:
    entities = []
    ents = getattr(world, "entities", None)
    if isinstance(ents, dict):
        iterable = ents.values()
    elif isinstance(ents, list):
        iterable = ents
    else:
        iterable = []

    for e in iterable:
        name = getattr(e, "name", "Entity")
        comps = []
        raw = []
        if hasattr(e, "components") and e.components is not None:
            raw = list(e.components) if not isinstance(e.components, dict) else list(e.components.values())
        elif hasattr(e, "_components"):
            raw = list(getattr(e, "_components").values())

        for c in raw:
            cn = c.__class__.__name__
            entry: Dict[str, Any] = {"type": cn}
            if cn == "Transform":
                if hasattr(c, "position"):
                    entry["x"] = float(getattr(c.position, "x", 0))
                    entry["y"] = float(getattr(c.position, "y", 0))
                else:
                    entry["x"] = float(getattr(c, "x", 0))
                    entry["y"] = float(getattr(c, "y", 0))
            elif cn == "SpriteRenderer":
                entry["width"] = int(getattr(c, "width", 32))
                entry["height"] = int(getattr(c, "height", 32))
                col = getattr(c, "color", (255, 255, 255, 255))
                entry["color"] = list(col) if col is not None else [255, 255, 255, 255]
            elif cn == "Camera":
                bg = getattr(c, "background_color", (30, 30, 40, 255))
                entry["background_color"] = list(bg) if bg is not None else [30, 30, 40, 255]
            elif cn == "Rigidbody2D":
                entry["mass"] = float(getattr(c, "mass", 1.0))
                entry["body_type"] = str(getattr(c, "body_type", "dynamic"))
            elif cn == "BoxCollider2D":
                size = getattr(c, "size", None)
                if size is not None:
                    entry["w"] = float(getattr(size, "x", 32))
                    entry["h"] = float(getattr(size, "y", 32))
                else:
                    entry["w"] = float(getattr(c, "width", 32))
                    entry["h"] = float(getattr(c, "height", 32))
            comps.append(entry)
        entities.append({"name": name, "components": comps})
    return {"entities": entities}


def scene_dict_to_world(scene: dict, scene_name: str = "Scene"):
    from nexus_engine.ecs.world import World
    from nexus_engine.ecs.components.transform import Transform
    from nexus_engine.ecs.components.sprite_renderer import SpriteRenderer
    from nexus_engine.ecs.components.camera import Camera
    from nexus_engine.ecs.components.rigidbody import Rigidbody2D
    from nexus_engine.ecs.components.collider import BoxCollider2D
    from nexus_engine.math.vector import Vector2

    world = World(scene_name)
    for edata in scene.get("entities") or []:
        name = edata.get("name", "Entity")
        e = world.create_entity(name)
        for c in edata.get("components") or []:
            t = c.get("type")
            if t == "Transform":
                e.add_component(Transform(float(c.get("x", 0)), float(c.get("y", 0))))
            elif t == "SpriteRenderer":
                col = c.get("color", [255, 255, 255, 255])
                if len(col) == 3:
                    col = list(col) + [255]
                e.add_component(SpriteRenderer(color=tuple(col), width=int(c.get("width", 32)), height=int(c.get("height", 32))))
            elif t == "Camera":
                bg = c.get("background_color", [30, 30, 40, 255])
                e.add_component(Camera(background_color=tuple(bg)))
            elif t == "Rigidbody2D":
                e.add_component(Rigidbody2D(mass=float(c.get("mass", 1.0)), body_type=str(c.get("body_type", "dynamic"))))
            elif t == "BoxCollider2D":
                e.add_component(BoxCollider2D(size=Vector2(float(c.get("w", 32)), float(c.get("h", 32)))))
    return world

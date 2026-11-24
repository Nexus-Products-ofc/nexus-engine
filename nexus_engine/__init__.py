"""
Nexus Engine — Game engine Python estilo Unity + Unreal.
"""

__version__ = "0.3.0"
__author__ = "Nexus Engine Team"

from .core.engine import NexusEngine
from .core.application import Application
from .ecs.world import World
from .ecs.entity import Entity
from .ecs.component import Component
from .ecs.system import System

from .math.vector import Vector2, Vector3
from .math.color import Color
from .math.rect import Rect
from .math.mathf import Mathf

from .ecs.components.transform import Transform
from .ecs.components.sprite_renderer import SpriteRenderer
from .ecs.components.camera import Camera
from .ecs.components.rigidbody import Rigidbody2D
from .ecs.components.collider import BoxCollider2D, CircleCollider2D

from .physics.physics2d import Physics2D
from .input.input_manager import Input
from .audio.audio_manager import Audio
from .prefab.prefab import Prefab
from .pooling.object_pool import ObjectPool
from .coroutines.coroutine_runner import wait_for_seconds, wait_for_end_of_frame
from .particles.particle_system import ParticleEmitter, ParticleSystem
from .tilemap.tilemap import Tilemap
from .debug.gizmos import Gizmos
from .serialization.scene_serializer import SceneSerializer

__all__ = [
    "NexusEngine", "Application", "World", "Entity", "Component", "System",
    "Vector2", "Vector3", "Color", "Rect", "Mathf",
    "Transform", "SpriteRenderer", "Camera",
    "Rigidbody2D", "BoxCollider2D", "CircleCollider2D",
    "Physics2D", "Input", "Audio", "Prefab", "ObjectPool",
    "wait_for_seconds", "wait_for_end_of_frame",
    "ParticleEmitter", "ParticleSystem", "Tilemap", "Gizmos", "SceneSerializer",
    "__version__",
]

"""System - logica sobre multiplas entidades (ECS)."""

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .world import World


class System:
    def __init__(self, name: str = "System"):
        self.name = name
        self.enabled = True
        self.world: Optional["World"] = None

    def on_added(self):
        pass

    def on_removed(self):
        pass

    def start(self):
        pass

    def update(self, dt: float):
        pass

    def fixed_update(self, dt: float):
        pass

    def late_update(self, dt: float):
        pass

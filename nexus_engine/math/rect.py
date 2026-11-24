"""Rect - retangulo 2D estilo Unity."""

from __future__ import annotations
from .vector import Vector2


class Rect:
    __slots__ = ("x", "y", "width", "height")

    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)

    @property
    def x_min(self) -> float:
        return self.x

    @property
    def y_min(self) -> float:
        return self.y

    @property
    def x_max(self) -> float:
        return self.x + self.width

    @property
    def y_max(self) -> float:
        return self.y + self.height

    @property
    def center(self) -> Vector2:
        return Vector2(self.x + self.width * 0.5, self.y + self.height * 0.5)

    @property
    def size(self) -> Vector2:
        return Vector2(self.width, self.height)

    def contains(self, point: Vector2) -> bool:
        return (
            self.x_min <= point.x <= self.x_max
            and self.y_min <= point.y <= self.y_max
        )

    def overlaps(self, other: "Rect") -> bool:
        return not (
            self.x_max < other.x_min
            or self.x_min > other.x_max
            or self.y_max < other.y_min
            or self.y_min > other.y_max
        )

    def __repr__(self) -> str:
        return f"Rect({self.x}, {self.y}, {self.width}, {self.height})"

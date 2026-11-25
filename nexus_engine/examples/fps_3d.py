"""
Nexus Example — 3D First Person
Controls: WASD move · mouse look · Space jump · Esc unlock mouse
Run:  python main.py --fps
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():
    try:
        from ursina import (
            Ursina, Entity, color, Vec3, mouse,
            FirstPersonController, Sky, Text,
        )
    except ImportError:
        print("Ursina not installed. pip install ursina")
        print("Falling back to pygame FPS mock...")
        _fps_mock()
        return

    app = Ursina()
    try:
        from ursina import window
        window.title = "Nexus — 3D First Person"
    except Exception:
        pass

    Sky()
    Entity(
        model="plane", scale=(40, 1, 40),
        color=color.rgb(60, 100, 60),
        texture="white_cube", texture_scale=(20, 20), collider="box",
    )
    for pos in [Vec3(5, 0.5, 5), Vec3(-4, 0.5, 3), Vec3(2, 0.5, -6), Vec3(-7, 1, -2)]:
        Entity(
            model="cube", color=color.rgb(120, 100, 160),
            position=pos, scale=Vec3(2, 2 if pos.y > 0.6 else 1, 2),
            collider="box", texture="white_cube",
        )

    FirstPersonController(position=Vec3(0, 2, 0), speed=8, mouse_sensitivity=Vec3(40, 40, 0))
    Text(text="Nexus FPS — WASD + mouse · Made in Nexus", position=(-0.85, 0.45), scale=1.2, color=color.azure)

    def input(key):
        if key == "escape":
            mouse.locked = not mouse.locked

    print("[Nexus] 3D First Person started (Ursina)")
    app.run()


def _fps_mock():
    import math
    import pygame

    pygame.init()
    W, H = 960, 540
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Nexus — FPS Mock (install ursina for real 3D)")
    clock = pygame.time.Clock()
    px, pz, ang = 5.0, 5.0, 0.0
    world = [
        [1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,0,1],
        [1,0,1,0,0,0,0,1],
        [1,0,0,0,1,0,0,1],
        [1,0,1,0,1,0,1,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1],
    ]
    FOV = math.pi / 3
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ang -= 1.8 * dt
        if keys[pygame.K_RIGHT]:
            ang += 1.8 * dt
        sp = 2.5 * dt
        nx, nz = px, pz
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            nx += math.cos(ang) * sp
            nz += math.sin(ang) * sp
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            nx -= math.cos(ang) * sp
            nz -= math.sin(ang) * sp
        if 0 <= int(nx) < 8 and 0 <= int(nz) < 8 and world[int(nz)][int(nx)] == 0:
            px, pz = nx, nz

        screen.fill((30, 40, 70))
        pygame.draw.rect(screen, (40, 50, 40), (0, H // 2, W, H // 2))
        for col in range(W):
            ray_a = ang - FOV / 2 + (col / W) * FOV
            dist = 0.0
            hit = False
            while dist < 12 and not hit:
                dist += 0.05
                rx = px + math.cos(ray_a) * dist
                rz = pz + math.sin(ray_a) * dist
                if rx < 0 or rz < 0 or rx >= 8 or rz >= 8 or world[int(rz)][int(rx)] == 1:
                    hit = True
            if hit:
                h = min(H, int(H / (dist + 0.1)))
                shade = max(40, 220 - int(dist * 30))
                pygame.draw.line(screen, (shade, shade // 2, shade), (col, H // 2 - h // 2), (col, H // 2 + h // 2))
        font = pygame.font.SysFont("segoeui", 16)
        screen.blit(font.render("FPS mock · Arrows/WASD · pip install ursina · Made in Nexus", True, (200, 200, 220)), (10, 10))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

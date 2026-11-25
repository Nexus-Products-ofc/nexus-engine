"""
Nexus Example — 3D Third Person
Controls: WASD move · mouse orbit · Space jump
Run:  python main.py --tps
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
            Ursina, Entity, color, Vec3, held_keys, time, mouse,
            Sky, Text, camera, clamp,
        )
    except ImportError:
        print("Ursina not installed. pip install ursina")
        print("Falling back to pygame third-person mock...")
        _tps_mock()
        return

    app = Ursina()
    try:
        from ursina import window
        window.title = "Nexus — 3D Third Person"
    except Exception:
        pass

    Sky()
    Entity(
        model="plane", scale=(50, 1, 50),
        color=color.rgb(55, 95, 55),
        texture="white_cube", texture_scale=(25, 25), collider="box",
    )
    for i, pos in enumerate([Vec3(4, 0.5, 4), Vec3(-5, 0.5, 2), Vec3(0, 0.5, -8), Vec3(8, 1, -3)]):
        Entity(
            model="cube", position=pos, scale=Vec3(2, 1 + (i % 2), 2),
            color=color.rgb(140, 110, 180), texture="white_cube", collider="box",
        )

    player = Entity(model="cube", color=color.azure, position=Vec3(0, 1, 0), scale=Vec3(1, 2, 1), collider="box")
    pivot = Entity(parent=player, y=1)
    camera.parent = pivot
    camera.position = Vec3(0, 2, -8)
    camera.rotation_x = 15
    mouse.locked = True

    speed = 6
    vel_y = 0.0
    Text(text="Nexus TPS — WASD move · mouse orbit · Made in Nexus", position=(-0.85, 0.45), scale=1.2)

    def update():
        nonlocal vel_y
        import math
        dir = Vec3(held_keys["d"] - held_keys["a"], 0, held_keys["w"] - held_keys["s"])
        if dir.length() > 0:
            dir = dir.normalized()
            yaw = pivot.rotation_y
            fx = math.sin(math.radians(yaw))
            fz = math.cos(math.radians(yaw))
            right = Vec3(fz, 0, -fx)
            forward = Vec3(fx, 0, fz)
            player.position += (forward * dir.z + right * dir.x) * speed * time.dt

        pivot.rotation_y += mouse.velocity[0] * 40
        pivot.rotation_x = clamp(pivot.rotation_x - mouse.velocity[1] * 40, -30, 60)

        vel_y -= 20 * time.dt
        player.y += vel_y * time.dt
        if player.y < 1:
            player.y = 1
            vel_y = 0
        if held_keys["space"] and player.y <= 1.05:
            vel_y = 8

    def input(key):
        if key == "escape":
            mouse.locked = not mouse.locked

    print("[Nexus] 3D Third Person started (Ursina)")
    app.run()


def _tps_mock():
    import pygame
    import math

    pygame.init()
    W, H = 960, 540
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Nexus — TPS Mock (install ursina for real 3D)")
    clock = pygame.time.Clock()
    px, pz, ang = 0.0, 0.0, 0.0
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
            ang -= 2 * dt
        if keys[pygame.K_RIGHT]:
            ang += 2 * dt
        sp = 3 * dt
        if keys[pygame.K_w]:
            px += math.cos(ang) * sp
            pz += math.sin(ang) * sp
        if keys[pygame.K_s]:
            px -= math.cos(ang) * sp
            pz -= math.sin(ang) * sp
        screen.fill((28, 35, 55))
        for i in range(-10, 11):
            pygame.draw.line(screen, (50, 60, 80), (0, H // 2 + i * 20), (W, H // 2 + i * 20))
        cx, cy = W // 2 + int(px * 20), H // 2 + int(pz * 20)
        pygame.draw.circle(screen, (100, 180, 255), (cx, cy), 12)
        pygame.draw.line(screen, (255, 255, 255), (cx, cy), (cx + int(math.cos(ang) * 24), cy + int(math.sin(ang) * 24)), 2)
        bx = cx - int(math.cos(ang) * 40)
        by = cy - int(math.sin(ang) * 40)
        pygame.draw.circle(screen, (200, 160, 255), (bx, by), 6)
        font = pygame.font.SysFont("segoeui", 16)
        screen.blit(font.render("TPS mock · WASD/Arrows · pip install ursina · Made in Nexus", True, (200, 200, 220)), (10, 10))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

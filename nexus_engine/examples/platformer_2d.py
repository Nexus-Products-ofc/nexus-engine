"""
Nexus Example — Simple 2D Platformer
Controls: A/D or Left/Right move · Space / W jump
Run:  python main.py --platformer
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main():
    import pygame
    from nexus_engine import Debug, Turbo
    from nexus_engine.ui.splash import show_splash

    Turbo.set("turbo")
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Nexus — 2D Platformer")
    try:
        show_splash(screen, pygame, 960, 540, duration=1.5, title="2D Platformer", subtitle="Made in Nexus")
    except Exception:
        pass

    Debug.log("2D Platformer — A/D move, Space jump")
    clock = pygame.time.Clock()
    running = True
    vel_y = 0.0
    on_ground = False
    px, py = 100.0, 450.0
    gravity = 1800.0
    jump_v = -520.0
    speed = 260.0

    platforms = [
        ("Ground", 480, 520, 960, 40, (60, 100, 60)),
        ("PlatA", 200, 400, 160, 20, (90, 90, 120)),
        ("PlatB", 500, 320, 160, 20, (90, 90, 120)),
        ("PlatC", 780, 250, 140, 20, (90, 90, 120)),
        ("WallL", 10, 270, 20, 540, (70, 70, 90)),
        ("WallR", 950, 270, 20, 540, (70, 70, 90)),
    ]
    solid = [(x, y, w, h) for _, x, y, w, h, _ in platforms]

    def aabb(ax, ay, aw, ah, bx, by, bw, bh):
        return abs(ax - bx) < (aw + bw) / 2 and abs(ay - by) < (ah + bh) / 2

    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        vx = 0.0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            vx = -speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            vx = speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and on_ground:
            vel_y = jump_v
            on_ground = False

        vel_y += gravity * dt
        px += vx * dt
        py += vel_y * dt
        on_ground = False

        pw, ph = 28, 40
        for sx, sy, sw, sh in solid:
            if aabb(px, py, pw, ph, sx, sy, sw, sh):
                if vel_y > 0 and py < sy:
                    py = sy - (sh / 2 + ph / 2)
                    vel_y = 0
                    on_ground = True
                elif vel_y < 0:
                    py = sy + (sh / 2 + ph / 2)
                    vel_y = 0
                if abs(px - sx) > abs(py - sy):
                    if px < sx:
                        px = sx - (sw / 2 + pw / 2)
                    else:
                        px = sx + (sw / 2 + pw / 2)

        px = max(30, min(930, px))
        if py > 600:
            px, py, vel_y = 100.0, 450.0, 0.0

        screen.fill((25, 30, 45))
        for _, x, y, w, h, col in platforms:
            pygame.draw.rect(screen, col, pygame.Rect(int(x - w / 2), int(y - h / 2), w, h))
        pygame.draw.rect(screen, (100, 180, 255), pygame.Rect(int(px - 14), int(py - 20), 28, 40))
        pygame.draw.circle(screen, (255, 210, 40), (780, 210), 9)
        font = pygame.font.SysFont("segoeui", 16)
        screen.blit(font.render("A/D move · Space jump · Esc quit · Made in Nexus", True, (180, 180, 200)), (12, 10))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

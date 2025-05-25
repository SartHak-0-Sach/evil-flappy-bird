import pygame
import random
import os
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Plane")

ASSET_DIR = "assets"
plane_img = pygame.image.load(os.path.join(ASSET_DIR, "plane.png"))
plane_img = pygame.transform.scale(plane_img, (60, 40))
plane_img = pygame.transform.flip(plane_img, True, False)

building_img = pygame.image.load(os.path.join(ASSET_DIR, "building.png"))
building_img = pygame.transform.scale(building_img, (80, 500))
building_img_flipped = pygame.transform.flip(building_img, False, True)

background = pygame.image.load(os.path.join(ASSET_DIR, "background.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

explosion_img = pygame.image.load(os.path.join(ASSET_DIR, "explosion.png"))
explosion_img = pygame.transform.scale(explosion_img, (80, 80))

crash_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "crash.wav"))
explosion_sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, "explosion.wav"))

font = pygame.font.Font(os.path.join(ASSET_DIR, "Ubuntu-Bold.ttf"), 40)

def game_loop():
    gravity = 0.5
    lift = -10
    plane_y = HEIGHT // 2
    plane_vel = 0
    buildings = []
    last_spawn_time = pygame.time.get_ticks()
    score = 0
    SPAWN_RATE = 1500
    BUILDING_WIDTH = 80
    GAP = 200
    game_started = False
    game_over = False
    clock = pygame.time.Clock()

    def draw_window():
        win.blit(background, (0, 0))
        if game_over:
            win.blit(explosion_img, (100, plane_y))
        else:
            win.blit(plane_img, (100, plane_y))

        for (top_bottom_1, top_bottom_2, x) in buildings:
            top1, bottom1 = top_bottom_1
            top2, bottom2 = top_bottom_2
            win.blit(building_img_flipped, (x, top1))
            win.blit(building_img_flipped, (x + BUILDING_WIDTH + 10, top2))
            win.blit(building_img, (x, bottom1))
            win.blit(building_img, (x + BUILDING_WIDTH + 10, bottom2))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        win.blit(score_text, (10, 10))
        pygame.display.update()

    def spawn_building():
        height = random.randint(100, 400)
        gap_between = 10
        x = WIDTH
        top1 = height - 500
        bottom1 = height + GAP
        top2 = height - 500
        bottom2 = height + GAP
        buildings.append([(top1, bottom1), (top2, bottom2), x])

    while not game_started:
        clock.tick(60)
        win.blit(background, (0, 0))
        win.blit(plane_img, (100, plane_y))
        msg = font.render("Press SPACE or CLICK to Start", True, (255, 255, 255))
        win.blit(msg, (40, HEIGHT // 2 - 30))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_started = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_started = True

    running = True
    while running:
        clock.tick(60)
        time_now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                plane_vel = lift

            plane_vel += gravity
            plane_y += plane_vel

            if time_now - last_spawn_time > SPAWN_RATE:
                spawn_building()
                last_spawn_time = time_now

            for b in buildings:
                b[2] -= 5

            buildings = [b for b in buildings if b[2] + 2 * BUILDING_WIDTH + 10 > 0]

            for b in buildings:
                if b[2] == 100:
                    score += 1

            for (top_bottom_1, top_bottom_2, x) in buildings:
                top1, bottom1 = top_bottom_1
                top2, bottom2 = top_bottom_2
                plane_rect = pygame.Rect(100, plane_y, 60, 40)
                top_rect1 = pygame.Rect(x, top1, BUILDING_WIDTH, HEIGHT // 2)
                bottom_rect1 = pygame.Rect(x, bottom1, BUILDING_WIDTH, HEIGHT)
                top_rect2 = pygame.Rect(x + BUILDING_WIDTH + 10, top2, BUILDING_WIDTH, HEIGHT // 2)
                bottom_rect2 = pygame.Rect(x + BUILDING_WIDTH + 10, bottom2, BUILDING_WIDTH, HEIGHT)

                if (plane_rect.colliderect(top_rect1) or
                    plane_rect.colliderect(bottom_rect1) or
                    plane_rect.colliderect(top_rect2) or
                    plane_rect.colliderect(bottom_rect2)):
                    crash_sound.play()
                    explosion_sound.play()
                    game_over = True
                    break

            if plane_y > HEIGHT or plane_y < 0:
                crash_sound.play()
                explosion_sound.play()
                game_over = True

        draw_window()

        if game_over:
            crash_len = max(crash_sound.get_length(), explosion_sound.get_length())
            pygame.time.delay(int(crash_len * 1000))
            return True

while True:
    if not game_loop():
        break
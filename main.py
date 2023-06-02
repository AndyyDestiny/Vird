import pygame
from flappy_bird import FlappyBird
from logo import Logo
from pipe import Pipe
from button import Button
from restart import Restart
import random

# set up pygame modules
pygame.init()
pygame.font.init()
def start_game():
    my_font1 = pygame.font.SysFont('Arial', 15)
    my_font2 = pygame.font.SysFont('Bauhaus 93', 100)
    bg = pygame.image.load("flappy-bird-background.png")
    ground_img = pygame.image.load("ground.png")
    size = ground_img.get_size()
    new_size = (size[0] * 0.935, size[1] * 0.3)
    ground_img = pygame.transform.scale(ground_img, new_size)
    size = bg.get_size()
    new_size2 = (size[0] / 0.9, size[1] / 0.905)
    bg = pygame.transform.scale(bg, new_size2)
    pygame.display.set_caption("Flappy Bird")

    # set up variables for the display
    SCREEN_HEIGHT = 601
    SCREEN_WIDTH = 804
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    restart = True
    run = True
    start_screen = True
    game_over = False
    pass_pipe1 = False
    pass_pipe2 = False
    pass_pipe3 = False
    pass_pipe4 = False
    pass_pipe5 = False
    pipe1 = False
    pipe2 = False
    pipe3 = False
    pipe4 = False
    pipe5 = False
    b = FlappyBird(370, 200)
    X_POSITION = 370
    Y_POSITION = 200
    l = Logo(280, 100)
    button = Button(350, 300)
    restart_button = Restart(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 100)
    ground_scroll = 0
    scroll_speed = 4
    frame = 0
    score = 0
    clock = pygame.time.Clock()
    pipe_height1 = random.randint(0, 150)
    pipe_height2 = random.randint(0, 150)
    pipe_height3 = random.randint(0, 150)
    pipe_height4 = random.randint(0, 150)
    pipe_height5 = random.randint(0, 150)

    btm_pipe1 = Pipe(1000, int(SCREEN_HEIGHT / 2.201) + pipe_height1, -1)
    top_pipe1 = Pipe(1000, -150 + pipe_height1, 1)
    btm_pipe2 = Pipe(1250, int(SCREEN_HEIGHT / 2.201) + pipe_height2, -1)
    top_pipe2 = Pipe(1250, -150 + pipe_height2, 1)
    btm_pipe3 = Pipe(1500, int(SCREEN_HEIGHT / 2.201) + pipe_height3, -1)
    top_pipe3 = Pipe(1500, -150 + pipe_height3, 1)
    btm_pipe4 = Pipe(1750, int(SCREEN_HEIGHT / 2.201) + pipe_height4, -1)
    top_pipe4 = Pipe(1750, -150 + pipe_height4, 1)
    btm_pipe5 = Pipe(2000, int(SCREEN_HEIGHT / 2.201) + pipe_height5, -1)
    top_pipe5 = Pipe(2000, -150 + pipe_height5, 1)
    # -------- Main Program Loop -----------
    while run:
        clock.tick(60)
        if game_over == False:
            if frame % 8 == 0:
                b.switch_image()
        if start_screen:
            image = screen.blit(bg, (0, 0))
            ground = screen.blit(ground_img, (ground_scroll, 553))
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 40:
                ground_scroll = 0
            screen.blit(b.image, b.rect)
            screen.blit(l.image, l.rect)
            screen.blit(button.image, button.rect)
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if button.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            start_screen = False
                else:
                    start_screen = True
        if not start_screen:
            screen.blit(top_pipe1.image, top_pipe1.rect)
            screen.blit(btm_pipe1.image, btm_pipe1.rect)
            screen.blit(top_pipe2.image, top_pipe2.rect)
            screen.blit(btm_pipe2.image, btm_pipe2.rect)
            screen.blit(top_pipe3.image, top_pipe3.rect)
            screen.blit(btm_pipe3.image, btm_pipe3.rect)
            screen.blit(top_pipe4.image, top_pipe4.rect)
            screen.blit(btm_pipe4.image, btm_pipe4.rect)
            screen.blit(top_pipe5.image, top_pipe5.rect)
            screen.blit(btm_pipe5.image, btm_pipe5.rect)
            display_score = my_font2.render(str(score), True, (255, 255, 255))
            image = screen.blit(bg, (0, 0))
            ground = screen.blit(ground_img, (ground_scroll, 553))
            if b.rect.bottom >= 553:
                game_over = True
            if game_over == True:
                screen.blit(top_pipe1.image, top_pipe1.rect)
                screen.blit(btm_pipe1.image, btm_pipe1.rect)
                screen.blit(top_pipe2.image, top_pipe2.rect)
                screen.blit(btm_pipe2.image, btm_pipe2.rect)
                screen.blit(top_pipe3.image, top_pipe3.rect)
                screen.blit(btm_pipe3.image, btm_pipe3.rect)
                screen.blit(top_pipe4.image, top_pipe4.rect)
                screen.blit(btm_pipe4.image, btm_pipe4.rect)
                screen.blit(top_pipe5.image, top_pipe5.rect)
                screen.blit(btm_pipe5.image, btm_pipe5.rect)
                b.bird_dead()
                b.update()
                screen.blit(restart_button.image, restart_button.rect)
                ground = screen.blit(ground_img, (ground_scroll, 553))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if button.rect.right > pos[0] > button.rect.left and 240 > pos[1] > 200:
                            if pygame.mouse.get_pressed()[0] == 1:
                                start_game()
            if game_over == False:
                screen.blit(top_pipe1.image, top_pipe1.rect)
                screen.blit(btm_pipe1.image, btm_pipe1.rect)
                screen.blit(top_pipe2.image, top_pipe2.rect)
                screen.blit(btm_pipe2.image, btm_pipe2.rect)
                screen.blit(top_pipe3.image, top_pipe3.rect)
                screen.blit(btm_pipe3.image, btm_pipe3.rect)
                screen.blit(top_pipe4.image, top_pipe4.rect)
                screen.blit(btm_pipe4.image, btm_pipe4.rect)
                screen.blit(top_pipe5.image, top_pipe5.rect)
                screen.blit(btm_pipe5.image, btm_pipe5.rect)
                top_pipe1.move_pipe()
                btm_pipe1.move_pipe()
                top_pipe2.move_pipe()
                btm_pipe2.move_pipe()
                top_pipe3.move_pipe()
                btm_pipe3.move_pipe()
                top_pipe4.move_pipe()
                btm_pipe4.move_pipe()
                top_pipe5.move_pipe()
                btm_pipe5.move_pipe()
                pipe_height = random.randint(0, 150)
                ground = screen.blit(ground_img, (ground_scroll, 553))
                if top_pipe1.rect.right < 0 and btm_pipe1.rect.right < 0:
                    pipe1 = False
                    btm_pipe1 = Pipe(btm_pipe5.rect.right + 200, int(SCREEN_HEIGHT / 2.201) + pipe_height, -1)
                    top_pipe1 = Pipe(top_pipe5.rect.right + 200, -150 + pipe_height, 1)
                    screen.blit(btm_pipe1.image, btm_pipe1.rect)
                    screen.blit(top_pipe1.image, top_pipe1.rect)
                    top_pipe1.move_pipe()
                    btm_pipe1.move_pipe()
                elif top_pipe2.rect.right < 0 and btm_pipe2.rect.right < 0:
                    pipe2 = False
                    btm_pipe2 = Pipe(btm_pipe1.rect.right + 200, int(SCREEN_HEIGHT / 2.201) + pipe_height, -1)
                    top_pipe2 = Pipe(top_pipe1.rect.right + 200, -150 + pipe_height, 1)
                    screen.blit(btm_pipe2.image, btm_pipe2.rect)
                    screen.blit(top_pipe2.image, top_pipe2.rect)
                    top_pipe2.move_pipe()
                    btm_pipe2.move_pipe()
                elif top_pipe3.rect.right < 0 and btm_pipe3.rect.right < 0:
                    pipe3 = False
                    btm_pipe3 = Pipe(btm_pipe2.rect.right + 200, int(SCREEN_HEIGHT / 2.201) + pipe_height, -1)
                    top_pipe3 = Pipe(top_pipe2.rect.right + 200, -150 + pipe_height, 1)
                    screen.blit(btm_pipe3.image, btm_pipe3.rect)
                    screen.blit(top_pipe3.image, top_pipe3.rect)
                    top_pipe3.move_pipe()
                    btm_pipe3.move_pipe()
                elif top_pipe4.rect.right < 0 and btm_pipe4.rect.right < 0:
                    pipe4 = False
                    btm_pipe4 = Pipe(btm_pipe3.rect.right + 200, int(SCREEN_HEIGHT / 2.201) + pipe_height, -1)
                    top_pipe4 = Pipe(top_pipe3.rect.right + 200, -150 + pipe_height, 1)
                    screen.blit(btm_pipe4.image, btm_pipe4.rect)
                    screen.blit(top_pipe4.image, top_pipe4.rect)
                    top_pipe4.move_pipe()
                    btm_pipe4.move_pipe()
                elif top_pipe5.rect.right < 0 and btm_pipe5.rect.right < 0:
                    pipe5 = False
                    btm_pipe5 = Pipe(btm_pipe4.rect.right + 200, int(SCREEN_HEIGHT / 2.201) + pipe_height, -1)
                    top_pipe5 = Pipe(top_pipe4.rect.right + 200, -150 + pipe_height, 1)
                    screen.blit(btm_pipe5.image, btm_pipe5.rect)
                    screen.blit(top_pipe5.image, top_pipe5.rect)
                    top_pipe5.move_pipe()
                    btm_pipe5.move_pipe()
                ground_scroll -= scroll_speed
                if b.rect.colliderect(top_pipe1.rect) or b.rect.colliderect(btm_pipe1.rect) or b.rect.top < 0:
                    game_over = True
                elif b.rect.colliderect(top_pipe2.rect) or b.rect.colliderect(btm_pipe2.rect) or b.rect.top < 0:
                    game_over = True
                elif b.rect.colliderect(top_pipe3.rect) or b.rect.colliderect(btm_pipe3.rect) or b.rect.top < 0:
                    game_over = True
                elif b.rect.colliderect(top_pipe4.rect) or b.rect.colliderect(btm_pipe4.rect) or b.rect.top < 0:
                    game_over = True
                elif b.rect.colliderect(top_pipe5.rect) or b.rect.colliderect(btm_pipe5.rect) or b.rect.top < 0:
                    game_over = True

                if b.rect.left > top_pipe1.rect.left and pipe1 == False:
                    pass_pipe1 = True
                elif b.rect.left > top_pipe2.rect.left and pipe2 == False:
                    pass_pipe2 = True
                elif b.rect.left > top_pipe3.rect.left and pipe3 == False:
                    pass_pipe3 = True
                elif b.rect.left > top_pipe4.rect.left and pipe4 == False:
                    pass_pipe4 = True
                elif b.rect.left > top_pipe5.rect.left and pipe5 == False:
                    pass_pipe5 = True
                if pass_pipe1:
                    score += 1
                    pass_pipe1 = False
                    pipe1 = True
                elif pass_pipe2:
                    score += 1
                    pass_pipe2 = False
                    pipe2 = True
                elif pass_pipe3:
                    score += 1
                    pass_pipe3 = False
                    pipe3 = True
                elif pass_pipe4:
                    score += 1
                    pass_pipe4 = False
                    pipe4 = True
                elif pass_pipe5:
                    score += 1
                    pass_pipe5 = False
                    pipe5 = True
                if abs(ground_scroll) > 40:
                    ground_scroll = 0
            screen.blit(display_score, (380, 30))
            screen.blit(b.image, b.rect)
            if game_over == False:
                b.update()
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    run = False
        pygame.display.update()
        frame += 1
    pygame.quit()
# Once we have exited the main program loop we can stop the game engine:
start_game()

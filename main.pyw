import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Grubhub Offical Game')
white = (255,255,255)
clock = pygame.time.Clock()

player = pygame.Rect(200, 200, 50, 50)
player_speed = pygame.Vector2()
speedyness = 2
speed = 2
speed_limit = 10
friction = 1

ground = pygame.Rect(0, 500, 800, 100)

objects = [ground]

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_speed.x > -speed_limit:
        player_speed.x -= 2

    if keys[pygame.K_RIGHT] and player_speed.x < speed_limit:
        player_speed.x += 2

    if keys[pygame.K_UP] and player.collidelist(objects) == 0:
        player_speed.y = -20

    player.move_ip(player_speed)

    player_speed.y += 1

    if player.collidelist(objects) == 0:
        player_speed.y = 0
        #player.move_ip(0, 0)

    if player_speed.x > 0 and player_speed.x != 0:
        player_speed.x -= friction
    elif player_speed.x < 0 and player_speed.x != 0:
        player_speed.x += friction

    screen.fill(white)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), ground)
    pygame.display.flip()

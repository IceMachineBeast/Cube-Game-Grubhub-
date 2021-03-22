import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Grubhub Offical Game')
white = (255,255,255)

player = pygame.Rect(200, 200, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.flip()

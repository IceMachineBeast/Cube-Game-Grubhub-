import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Grubhub Offical Game')
white = (255,255,255)

print("I am le tarde and I can't program - Konrád") # Not true
print("Umgak")
screen.fill((255,0,0))
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

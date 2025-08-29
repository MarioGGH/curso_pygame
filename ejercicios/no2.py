import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600 
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 2")

clock = pygame.time.Clock()

x, y = 100, 100
vel = 5
col = 0, 165, 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        x -= vel
    if teclas[pygame.K_RIGHT]:
        x += vel
    if teclas[pygame.K_UP]:
        y -= vel
    if teclas[pygame.K_DOWN]:
        y += vel
    
    ventana.fill((col))
    pygame.draw.rect(ventana, (0, 255, 0), (x, y, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)
import pygame
import sys

pygame.init()

ANCHO, ALTO = 1000, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Recibir teclas del usuario")

clock = pygame.time.Clock()

x, y = 100, 100
velocidad = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad 
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
        
    ventana.fill((0, 0, 0))
    pygame.draw.rect(ventana, (0, 155, 155), (x, y, 50, 50))
    
    pygame.display.flip()
    clock.tick(144)
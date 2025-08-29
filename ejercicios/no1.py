import pygame
import sys

pygame.init()

# Configurar la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0, 0, 255)) # Fondo azul
    pygame.draw.rect(ventana, (255, 0, 0), (100, 100, 50, 50))
    
    pygame.display.flip() # Actualizar la pantalla
    clock.tick(60) # Limitamos los fps a 60
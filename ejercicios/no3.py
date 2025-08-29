import pygame
import sys

pygame.init()

# Creamos la pantalla 
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 3")

# Controlamos los fps
clock = pygame.time.Clock()

x, y = 100, 100
vel = 5
ancho_c, altura_c = 50, 50 
col_fondo =  0, 165, 255
col_cuadrado = 0, 255, 0


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
    
    # Se mantiene al usuario dentro de la pantalla
    x = max(0, min(ANCHO - ancho_c, x))
    y = max(0, min(ALTO - altura_c, y))
    
    ventana.fill((col_fondo))
    pygame.draw.rect(ventana, (col_cuadrado) , (x, y, ancho_c, altura_c))
    
    pygame.display.flip()
    clock.tick(60)
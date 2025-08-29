import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 4")

clock = pygame.time.Clock()

# Colores
col_fondo = (0, 165, 255)
col_jugador = (0, 255, 0)
col_enemigo = (255, 0, 0)

# Jugador
x_jugador, y_jugador = 100, 100
vel_jugador = 5
ancho_jugador, altura_jugador = 50, 50

# Enemigo
x_enemigo, y_enemigo = 400, 300
vel_enemigo = 2
ancho_enemigo, altura_enemigo = 50, 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x_jugador -= vel_jugador
    if teclas[pygame.K_RIGHT]:
        x_jugador += vel_jugador
    if teclas[pygame.K_UP]:
        y_jugador -= vel_jugador
    if teclas[pygame.K_DOWN]:
        y_jugador += vel_jugador
        
    # Limites jugador
    x_jugador = max(0, min(ANCHO - ancho_jugador, x_jugador))
    y_jugador = max(0, min(ALTO - altura_jugador, y_jugador))
    
    # Comparacion para que el enemigo siga al jugador x
    if x_jugador > x_enemigo:
        x_enemigo += vel_enemigo
    if x_jugador < x_enemigo:
        x_enemigo -= vel_enemigo
        
    # Comparacion para que el enemigo siga al jugador y
    if y_jugador > y_enemigo:
        y_enemigo += vel_enemigo
    if y_jugador < y_enemigo:
        y_enemigo -= vel_enemigo
    
    # Dibujar el fondo
    ventana.fill(col_fondo)
    
    # Dibujamos al jugador y al enemigo
    jugador = pygame.draw.rect(ventana, col_jugador, (x_jugador, y_jugador, ancho_jugador, altura_jugador))
    enemigo = pygame.draw.rect(ventana,  col_enemigo, (x_enemigo, y_enemigo, ancho_enemigo, altura_enemigo))
    
    # Detectamos la colision
    if jugador.colliderect(enemigo):
        print("Colision detectada!!!")
        
    pygame.display.flip()
    clock.tick(60)
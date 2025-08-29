import pygame
import sys

# Inicializar pygame
pygame.init()

# Creamos la pantalla ANCHO, ALTO (600, 800)
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi primer juego en Pygame")

# Controlamos los fps
clock = pygame.time.Clock()

# Crearemos el bucle principal
while True:
    # Iniciamos el manejador de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Aqui pondremos la logica del juego
    
    # Dibujaremos la pantalla
    ventana.fill((30, 30, 30)) # Fondo Gris
    pygame.display.flip() # Actualizar la pantalla
    clock.tick(60) # Limitamos los fps a 60
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
    ventana.fill((50, 50, 100)) # Fondo Gris
    # Dibujamos un rectangulo
    pygame.draw.rect(ventana, (255, 0, 0), (100, 100, 50, 50))
    # Dibujamos un triangulo
    pygame.draw.circle(ventana, (0, 255, 0), (400, 300), 40)
    pygame.display.flip() # Actualizar la pantalla
    clock.tick(60) # Limitamos los fps a 60
# Importar las librerías necesarias
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("sprites")

# Configurar el reloj para controlar los FPS
clock = pygame.time.Clock()

# Cargar y escalar la imagen del jugador
jugador = pygame.image.load("caballero.png")
jugador = pygame.transform.scale(jugador, (100, 100))

# Cargar y escalar la imagen del enemigo
enemigo = pygame.image.load("caballero.png")
enemigo = pygame.transform.scale(enemigo, (100, 100))

# Posición inicial del jugador y velocidad de movimiento
x, y = 100, 100
velocidad = 2

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    x_prev, y_prev = x, y  # Guardar la posición anterior del jugador
    
    # Manejar el movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Mantener al jugador dentro de los límites de la ventana
    x = max(0, min(ANCHO - 100, x))
    y = max(0, min(ALTO - 100, y))
    # Dibujar todo
    ventana.fill((0, 0, 0))
    # Dibuja el enemigo
    ventana.blit(enemigo, (300, 300))
    # Dibuja el jugador
    ventana.blit(jugador, (x, y))
    # Detectar colisiones
    jug_rect = jugador.get_rect(topleft=(x, y))
    ene_rect = enemigo.get_rect(topleft=(300, 300))
    # Si hay colisión, cambiar el color de fondo y mostrar un mensaje
    if jug_rect.colliderect(ene_rect):
        x, y = x_prev, y_prev  # Revertir a la posición anterior
        jug_rect.topleft = (x, y)  # Actualizar el rectángulo del jugador
        ventana.fill((0, 155, 155))
        ventana.blit(enemigo, (300, 300))
        ventana.blit(jugador, (x, y))
    # Actualizar la pantalla y controlar los FPS
    pygame.display.flip()
    # Limitar los FPS a 60
    clock.tick(60)

    

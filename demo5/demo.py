import pygame
import sys

pygame.init()

# Configurar la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con Clases")

# Configurar el reloj para controlar los FPS
clock = pygame.time.Clock()

# ---------------------------- CLASE JUGADOR ----------------------------
class Jugador:
    # Constructor de la clase Jugador que inicializa la imagen, posición y velocidad
    def __init__(self):
        self.imagen = pygame.image.load("caballero.png")
        # Escalar la imagen a un tamaño adecuado
        self.imagen = pygame.transform.scale(self.imagen, (100, 100))
        # Posición inicial del jugador
        self.x = 100
        self.y = 100
        # Velocidad de movimiento del jugador
        self.vel = 5
        
    def mover(self, teclas):
        # Guardar la posición anterior
        x_prev, y_prev = self.x, self.y
        # Mover el jugador según las teclas presionadas
        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
        if teclas[pygame.K_UP]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN]:
            self.y += self.vel
        
        # Evitar que el jugador salga de los límites de la ventana
        self.x = max(0, min(ANCHO - self.imagen.get_width(), self.x))
        self.y = max(0, min(ALTO - self.imagen.get_height(), self.y))
        
        # Retornar la posición anterior para posibles colisiones
        return x_prev, y_prev
    
    # Obtener el rectángulo del jugador para detección de colisiones
    def rect(self):
        return self.imagen.get_rect(topleft=(self.x, self.y))
    
    # Dibujar el jugador en la ventana
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))
        
# ---------------------------- CLASE ENEMIGOS ----------------------------
class Enemigo:
    # Constructor de la clase Enemigo que inicializa la imagen, posición
    def __init__(self, x, y):
        self.imagen = pygame.image.load("caballero.png")
        self.x = x
        self.y = y
        
    # Obtener el rectángulo del enemigo para detección de colisiones
    def rect(self):
        return self.imagen.get_rect(topleft=(self.x, self.y))
    
    # Dibujar el enemigo en la ventana
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))
        
# ---------------------------- MAIN ----------------------------
# Crear instancias de Jugador y Enemigo
jugador = Jugador()
enemigo = Enemigo(400, 300)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    # Mover el jugador y obtener la posición anterior
    x_prev, y_prev = jugador.mover(teclas)

    # Detección de colisión
    if jugador.rect().colliderect(enemigo.rect()):
        print("Colisión detectada!")
        # Revertir al jugador a la posición anterior
        jugador.x, jugador.y = x_prev, y_prev
        
    # Dibujar todo
    ventana.fill((0, 155, 175))
    enemigo.dibujar(ventana)
    jugador.dibujar(ventana)
    
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS
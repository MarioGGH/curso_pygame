import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Ejercicio 7")

clock = pygame.time.Clock()

# ----- Clase Jugador --------
class Jugador:
    def __init__(self, x, y, ancho = 50, altura = 50, vel = 5, color = (0, 255, 0)):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.vel = vel
        self.color = color
        
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
        if teclas[pygame.K_UP]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN]:
            self.y += self.vel
        
        self.x = max(0, min(ANCHO - self.ancho, self.x))
        self.y = max(0, min(ALTO - self.altura, self.y))
        
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.altura))
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.altura)
    
    
# ----- Clase Enemigo  ----------
class Enemigo:
    def __init__(self, x, y, vel, color, ancho = 50, altura = 50):
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color
        self.ancho = ancho
        self.altura = altura
        
    def mover(self, jugador):
        # Hacemos que el enemigo se mueva en x hacia la direccion del jugador
        if jugador.x > self.x:
            self.x += self.vel
        if jugador.x < self.x:
            self.x -= self.vel

        # Hacemos que el enemigo se mueva en y hacia la direccion del jugador
        if jugador.y > self.y:
            self.y += self.vel
        if jugador.y < self.y:
            self.y -= self.vel
        
        # limitamos al enemigo(su espacio dentro de la pantalla)
        self.x = max(0, min(ANCHO - self.ancho, self.x))
        self.y = max(0, min(ALTO - self.altura, self.y))
        
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x , self.y, self.ancho, self.altura))
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.altura)
    
# --- Creamos al jugador ------
jugador = Jugador(100, 100)

# --- Creamos a los enemigos ----
enemigos = [
    Enemigo(400, 300, 2, (255, 0, 0)),
    Enemigo(200, 100, 3, (255, 128, 0)),
    Enemigo(600, 400, 1, (255, 255, 0))
]

# ---- iniciamos el bucle principal ----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    teclas = pygame.key.get_pressed()
    jugador.mover(teclas)
    
    ventana.fill((0, 165, 255))
    jugador.dibujar(ventana)
    
    # Mover y dibujar a los enemigos
    for enemigo in enemigos:
        enemigo.mover(jugador)
        enemigo.dibujar(ventana)
        
        # Detectamos si hubo una colision con el jugador
        if jugador.rect().colliderect(enemigo.rect()):
            print("Colisiion Detectada!!!")

    pygame.display.flip()
    clock.tick(60)    
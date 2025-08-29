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
    
# ----- Clase Proyectil  ---------- 
class Proyectil:
    def __init__(self, x, y, ancho = 5, altura= 20, vel = 10,  color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.vel = vel
        self.color = color
    
    def mover(self):
        self.y -= self.vel
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.altura))
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.altura)
    
    def fuera_pantalla(self):
        return self.y < -self.altura
    
    
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
jugador = Jugador(400, 600)

# --- Creamos a los enemigos ----
enemigos = [
    Enemigo(400, 300, 2, (255, 0, 0)),
    Enemigo(200, 100, 2, (255, 128, 0)),
    Enemigo(600, 400, 1, (255, 255, 0)),
    Enemigo(300, 300, 2, (255,255,0))
]

# -------- Creamos los proyectiles -----
proyectiles = []
proyectiles_a_eliminar = []
enemigos_a_eliminar = []

# ---- iniciamos el bucle principal ----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nuevo_proyectil = Proyectil(jugador.x + jugador.ancho//2 - 2, jugador.y)
                proyectiles.append(nuevo_proyectil)
    
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
            
    for proyectil in proyectiles[:]:
        proyectil.mover()
        proyectil.dibujar(ventana)
        # Eliminaremos el proyectil si se sale de la pantalla
        if proyectil.fuera_pantalla():
            proyectiles.remove(proyectil)
            
        # Colision de los proyectiles ante los enemigos
        for enemigo in enemigos[:]:
            if proyectil.rect().colliderect(enemigo.rect()):
                proyectiles.remove(proyectil)
                enemigos.remove(enemigo)
                break
    
    for proyectil in proyectiles_a_eliminar:
        if proyectil in proyectiles:
            proyectiles.remove(proyectil)
            
    for enemigo in enemigos_a_eliminar:
        if enemigo in enemigos:
            enemigos.remove(enemigo)

    pygame.display.flip()
    clock.tick(60)
    
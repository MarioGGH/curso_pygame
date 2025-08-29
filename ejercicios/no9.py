import pygame
import sys

pygame.init()

ANCHO, ALTO =  800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Demo RPG")

clock = pygame.time.Clock()

class Jugador:
    def __init__(self, x, y, vel=2, ancho=50, altura=50, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.vel = vel
        self.ancho = ancho
        self.altura = altura
        self.color = color
        
    def mover(self, teclas, obstaculos=[]):
        dx, dy = 0, 0
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            dx = -self.vel
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            dx = self.vel
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            dy = -self.vel
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            dy = self.vel

        # Movimiento por eje para evitar atravesar NPCs
        nueva_rect_x = self.rect().move(dx, 0)
        nueva_rect_y = self.rect().move(0, dy)

        # Eje X
        colision_x = any(nueva_rect_x.colliderect(obstaculo) for obstaculo in obstaculos)
        if not colision_x:
            self.x += dx

        # Eje Y
        colision_y = any(nueva_rect_y.colliderect(obstaculo) for obstaculo in obstaculos)
        if not colision_y:
            self.y += dy

        # Mantener dentro de la pantalla
        self.x = max(0, min(ANCHO - self.ancho, self.x))
        self.y = max(0, min(ALTO - self.altura, self.y))
            
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.altura))
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.altura)

class NPC:
    def __init__(self, x, y, color=(255, 0, 0), ancho=50, altura=50):
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.altura = altura
        
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.altura))
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.altura)

# --- Inicialización ---
Jugador1 = Jugador(350, 500)
NPC1 = NPC(350, 300)

fuente = pygame.font.Font(None, 32)
mostrando_dialogo = False
texto_dialogo = "Hola, aventurero! Bienvenido a nuestro pueblo."

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                # Solo mostrar diálogo si el jugador está cerca del NPC
                area_interaccion = NPC1.rect().inflate(20, 20)  # zona de interacción más grande
                if Jugador1.rect().colliderect(area_interaccion):
                    mostrando_dialogo = not mostrando_dialogo
                    
    teclas = pygame.key.get_pressed()
    Jugador1.mover(teclas, obstaculos=[NPC1.rect()])
    area_interaccion = NPC1.rect().inflate(20, 20)
    if not Jugador1.rect().colliderect(area_interaccion):
        mostrando_dialogo = False
        
    # Dibujar
    ventana.fill((100, 149, 237))
    Jugador1.dibujar(ventana)
    NPC1.dibujar(ventana)

    if mostrando_dialogo:
        rect_dialogo = pygame.Rect(50, ALTO - 100, ANCHO - 100, 80)
        pygame.draw.rect(ventana, (255, 255, 255), rect_dialogo)
        pygame.draw.rect(ventana, (0, 0, 0), rect_dialogo, 3)
        texto_surface = fuente.render(texto_dialogo, True, (0, 0, 0))
        ventana.blit(texto_surface, (rect_dialogo.x + 10, rect_dialogo.y + 10))

    pygame.display.flip()
    clock.tick(60)

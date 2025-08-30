import pygame
import pytmx
import sys

pygame.init()

ESCALA = 3

tmx_temp = pytmx.TiledMap("mapas/mapa.tmx")
ANCHO = tmx_temp.width * tmx_temp.tilewidth * ESCALA
ALTO = tmx_temp.height * tmx_temp.tileheight * ESCALA

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("RPG con Tiled Escalado")
clock = pygame.time.Clock()

tmx_data = pytmx.util_pygame.load_pygame("mapas/mapa.tmx")

def dibujar_mapa(ventana, tmx_data):
    for capa in tmx_data.visible_layers:
        if isinstance(capa, pytmx.TiledTileLayer):
            for x, y, gid in capa:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    tile = pygame.transform.scale(
                        tile,
                        (tmx_data.tilewidth * ESCALA, tmx_data.tileheight * ESCALA)
                    )
                    ventana.blit(tile, (x * tmx_data.tilewidth * ESCALA,
                                        y * tmx_data.tileheight * ESCALA))

class Jugador:
    def __init__(self, x, y):
        self.image = pygame.Surface((tmx_data.tilewidth * ESCALA, int(tmx_data.tileheight * 1.5 * ESCALA)))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad = 5  # velocidad fija, no multiplicada por ESCALA

    def mover(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.velocidad
        if keys[pygame.K_RIGHT]:
            dx = self.velocidad
        if keys[pygame.K_UP]:
            dy = -self.velocidad
        if keys[pygame.K_DOWN]:
            dy = self.velocidad

        # Mover en X
        self.rect.x += dx
        self.colisiones('x')
        # Mover en Y
        self.rect.y += dy
        self.colisiones('y')
        # Limitar dentro de la ventana
        self.rect.clamp_ip(ventana.get_rect())

    def colisiones(self, eje):
        for capa in tmx_data.visible_layers:
            if isinstance(capa, pytmx.TiledTileLayer):
                for x, y, gid in capa:
                    props = tmx_data.get_tile_properties_by_gid(gid)
                    if props and props.get('colision'):
                        tile_rect = pygame.Rect(
                            x * tmx_data.tilewidth * ESCALA,
                            y * tmx_data.tileheight * ESCALA,
                            tmx_data.tilewidth * ESCALA,
                            tmx_data.tileheight * ESCALA
                        )
                        if self.rect.colliderect(tile_rect):
                            if eje == 'x':
                                if self.rect.x < tile_rect.x:
                                    self.rect.right = tile_rect.left
                                else:
                                    self.rect.left = tile_rect.right
                            elif eje == 'y':
                                if self.rect.y < tile_rect.y:
                                    self.rect.bottom = tile_rect.top
                                else:
                                    self.rect.top = tile_rect.bottom

jugador = Jugador(100 * ESCALA, 100 * ESCALA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    jugador.mover(keys)

    ventana.fill((0, 0, 0))
    dibujar_mapa(ventana, tmx_data)
    ventana.blit(jugador.image, jugador.rect)

    pygame.display.flip()
    clock.tick(60)

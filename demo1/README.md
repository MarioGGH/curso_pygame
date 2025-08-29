# ⚙️ Demo 1 para aprender a usar PyGame.
---
## 1. Importacion de las librerias necesarias.

```python
import pygame
import sys
```
## 2. Incializaremos pygame

```python
pygame.init()
```

## 3. Crearemos una ventana con su ancho y alto (defenible).

```python
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi primer juego en Pygame")
```

## 4. Usaremos la siguiente linea para manejar el control de los fps del juego (fotogramas por segundo).

```python
clock = pygame.time.Clock()
```

## 5. Usaremos un bucle principal para el manejo de eventos.

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    ventana.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)
```

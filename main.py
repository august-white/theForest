import pygame
from utils import *   # Assuming this defines WIDTH, HEIGHT, TITLE, npcs, mobs, etc.
from tiles import *   # Assuming this defines Wall, Ground, NPC, Mob, and tiles


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.enemies = []
        self.bullets = []
        self.tiles = []

    def createMap(self):
        # Clear any previous tiles
        self.tiles = []

        # Loop properly over rows and columns
        for row_index, row in enumerate(tiles):
            for col_index, c in enumerate(row):
                if c == 'Wall':
                    self.tiles.append(Wall(col_index, row_index))
                elif c == 'Ground':
                    self.tiles.append(Ground(col_index, row_index))
                elif c in npcs:
                    self.tiles.append(NPC(col_index, row_index, c))
                elif c in mobs:
                    self.tiles.append(Mob(col_index, row_index, c))

    def loop(self):
        # Basic event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit signal

        # Update and draw tiles
        for tile in self.tiles:
            tile.loop()

        pygame.display.flip()
        self.clock.tick(60)
        return True


# Initialize and run game
game = Game()
game.createMap()

running = True
while running:
    running = game.loop()

pygame.quit()

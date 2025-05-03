import pygame
import colours as cl
import random


class HexCell():
    x = 0
    y = 0
    colour = 0
    def Draw(self, gl):
        pygame.draw.polygon(gl.dis, gl.hexagonal_colours[self.colour],
                            [[self.x, self.y], [self.x + 3**(1/2) / 2 * gl.hex_size, self.y - 0.5 * gl.hex_size],
                            [self.x + 3**(1/2) * gl.hex_size, self.y], [self.x + 3**(1/2) * gl.size, self.y + gl.hex_size],
                            [self.x + 3**(1/2) / 2 * gl.hex_size, self.y + 1.5 * gl.hex_size], [self.x, self.y + gl.hex_size]])


class Cell:
    x = 0
    y = 0
    colour = 0

    def Draw(self, gl):
        pygame.draw.rect(gl.dis, gl.square_colours[self.colour], [self.x * gl.size, self.y * gl.size, gl.size, gl.size])
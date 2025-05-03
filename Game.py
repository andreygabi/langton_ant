import pygame
import GlobalVariables as gv
import SquareGameLoop as sgl
import HexGameLoop as hgl
import cells as cs
pygame.init()

def DrawInterface(gl, ic):
    ic.hexagonal_b.Draw(gl.dis)
    ic.square_b.Draw(gl.dis)
    ic.steps_per_tick_b.Draw(gl.dis)

def Draw(gl, ic):
    for box in ic.input_boxes:
        box.update()
    for box in ic.input_boxes:
        box.draw(gl.dis)

class Game:
    def game_loop(self):
        game_over = False
        gl = gv.Global()
        ic = gv.Interface()
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ic.hexagonal_b.isOver(event.pos):
                        hgl.hexGameLoop(gl, ic)
                    if ic.square_b.isOver(event.pos):
                        sgl.squareGameLoop(gl, ic)
            pygame.display.update()
            DrawInterface(gl, ic)
            sgl.squareGameLoop(gl, ic)
        pygame.quit()
        quit()
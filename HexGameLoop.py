import pygame
import random
import colours as cl
import ants
import SquareGameLoop as sgl
import Game
import cells as cs

def hexGameLoop(gl, ic):
    gl.hexagonal_rule = ic.input_box_hexagonal_rule.text
    gl.hexagonal_rule_length = len(gl.hexagonal_rule)
    gl.steps_per_tick = int(ic.input_box_steps_per_tick.text)
    pygame.draw.rect(gl.dis, cl.black, [0, 0, gl.dis.get_width() - 400, gl.dis.get_height()])
    game_over = False
    N = int(gl.dis_height // (1.5))
    M = int(gl.dis_width // (3 ** (1/2)))
    field = []
    gl.hexagonal_colours = []
    for x in range(gl.hexagonal_rule_length):
        gl.hexagonal_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    for i in range(N):
        row = []
        for j in range(M):
            row.append(cs.HexCell())
            row[-1].x = (j * 3 ** (1/2)) * gl.hex_size
            row[-1].y = i * (1.5) * gl.hex_size
            if (i % 2 == 0):
                row[-1].x -= (3 ** (1/2) / 2) * gl.hex_size
        field += [row]
    ant = ants.HexAnt()
    ant.rule = gl.hexagonal_rule
    ant.i = N // 2
    ant.j = M // 2
    time_last = pygame.time.get_ticks()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ic.hexagonal_b.isOver(event.pos) or ic.steps_per_tick_b.isOver(event.pos):
                    hexGameLoop(gl, ic)
                if ic.square_b.isOver(event.pos):
                    sgl.squareGameLoop(gl, ic)
            for box in ic.input_boxes:
                box.handle_event(event)
        Game.Draw(gl, ic)
        pygame.display.update()
        if pygame.time.get_ticks() - time_last > 1:
            time_last = pygame.time.get_ticks()
            for i in range(gl.steps_per_tick):
                ant.MakeHexMove(field, gl)
                ant.FixCoords(N, M)
        pygame.display.update()
    pygame.quit()
    quit()
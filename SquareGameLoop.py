import pygame
import random
import colours as cl
import ants
import HexGameLoop as hgl
import cells as cs
import Game

def squareGameLoop(gl, ic):

    gl.steps_per_tick = int(ic.input_box_steps_per_tick.text)
    gl.square_rule = ic.input_box_square_rule.text
    gl.square_rule_length = len(gl.square_rule)
    pygame.draw.rect(gl.dis, cl.black, [0, 0, gl.dis.get_width() - 400, gl.dis.get_height()])
    game_over = False
    N = int(gl.dis_height)
    M = int(gl.dis_width)
    field = []
    gl.square_colours = []
    for x in range(gl.square_rule_length):
        gl.square_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    for i in range(N):
        row = []
        for j in range(M):
            row.append(cs.Cell())
            row[-1].x = i
            row[-1].y = j
        field += [row]
    ant = ants.SquareAnt()
    ant.rule = gl.square_rule
    ant.i, ant.j = int(gl.dis_height / (2 * gl.size)), int(gl.dis_width / (2 * gl.size))
    time_last = pygame.time.get_ticks()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ic.hexagonal_b.isOver(event.pos):
                    hgl.hexGameLoop(gl, ic)
                if ic.square_b.isOver(event.pos) or ic.steps_per_tick_b.isOver(event.pos):
                    squareGameLoop(gl, ic)
            for box in ic.input_boxes:
                box.handle_event(event)
        Game.Draw(gl, ic)
        if pygame.time.get_ticks() - time_last > 1:
            time_last = pygame.time.get_ticks()
            for i in range(gl.steps_per_tick):
                ant.MakeMove(field, gl)
                ant.FixCoords(N, M)
        pygame.display.update()
    pygame.quit()
    quit()
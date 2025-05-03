import pygame
import random
import colours as cl
import buttons as bt

class Global:
    clock = pygame.time.Clock()
    FONT = pygame.font.Font(None, 32)
    square_rule = "RL"
    hexagonal_rule = "54454"
    tick = 1
    steps_per_tick = 1
    square_rule_length = len(square_rule)
    hexagonal_rule_length = len(hexagonal_rule)
    square_colours = []
    hexagonal_colours = []
    for x in range(hexagonal_rule_length):
        hexagonal_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    for x in range(square_rule_length):
        square_colours.append(cl.standard_colours[random.randint(0, len(cl.standard_colours) - 1)])
    dis_width = 800
    dis_height = 800
    size = 1
    hex_size = 1
    N = int(dis_height)
    M = int(dis_width)
    dis = pygame.display.set_mode((dis_width + 400, dis_height))
    pygame.display.set_caption('AntGame')
    clock = pygame.time.Clock()

class Interface:
    gl = Global()
    hexagonal_b = bt.Button(cl.blue, gl.dis.get_width() - 350, 100, 200, 50, "Hexagonal")
    square_b = bt.Button(cl.red, gl.dis.get_width() - 350, 200, 150, 50, "Square")
    steps_per_tick_b = bt.Button(cl.green, gl.dis.get_width() - 350, 300, 300, 50, "Steps per tick")
    input_box_square_rule = bt.InputBox(square_b.x, square_b.y + 60, 200, 32, "RL")
    input_box_hexagonal_rule = bt.InputBox(hexagonal_b.x, hexagonal_b.y + 60, 200, 32, "55544")
    input_box_steps_per_tick = bt.InputBox(steps_per_tick_b.x, steps_per_tick_b.y + 60, 200, 32, "10000")
    input_boxes = [input_box_square_rule, input_box_hexagonal_rule, input_box_steps_per_tick]
#!/usr/bin/env python3
import pygame, time, random, copy

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


width, height = 100,100
tile = 5
padding = 1

s = pygame.display.set_mode((width*tile+padding*width, height*tile+padding*height))

def main():
    done = False
    tick = 0
    t = time.time()
    dt = time.time()
    field = generate_field()
    while not done:
            tick += 1
            dt = time.time()-t
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if event.type == pygame.KEYDOWN:
                        field = step(field)

            field = step(field)
            draw(field)
            pygame.display.flip()

def step(field):
    s.fill(white)
    updates = []
    for y, f in enumerate(field):
        for x, v in enumerate(f):
            n = neighbors(field,x,y)
            updates.append((y,x,rules(field[y][x], n)))
    for y,x,update in updates:
        field[y][x] = update
    return field

def rules(cell, n):
    if cell:
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n > 3: return False
    else:
        if n == 3: return True


def neighbors(field, x,y):
    n = 0
    X = width-1
    Y = height-1
    if y > 0:
        if x > 0 and field[y-1][x-1]: n+=1
        if x < X and field[y-1][x+1]: n+=1
        if field[y-1][x]: n+=1
    if x > 0:
        if y < Y and field[y+1][x-1]: n+=1
        if field[y][x-1]: n+=1
    if y < Y:
        if x < X and field[y+1][x+1]: n+=1
        if field[y+1][x]: n+=1
    if x < X and field[y][x+1]: n+=1
    return n


def draw(original):
    s.fill(white)
    field = original
    for y, f in enumerate(field):
        for x, v in enumerate(f):
            tile_y = y*tile+y*padding
            tile_x = x*tile+x*padding
            color = black if field[y][x] else white
            pygame.draw.rect(s, color, (tile_y, tile_x, tile, tile), 0)

def generate_field():
    field = []
    for a in range(width):
        l = []
        for b in range(height):
            l.append(random.random()>0.9)
        field.append(l)
    return field
main()

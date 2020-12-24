#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: huanglei

import pygame
import sys


class Map(object):
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('background.png')

    def update(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))


class Bird(object):

    def __init__(self, screen):
        self.screen = screen
        self.bird_rect = pygame.Rect(65, 50, 50, 50)
        self.bird_status = [
            pygame.image.load('bird1.png'),
            pygame.image.load('bird2.png'),
            pygame.image.load('bird_dead.png')
        ]
        self.position = (0, 0)
        self.jump = False
        self.speed = 10
        self.gravity = 5
        self.dead = False

    def update(self):
        if self.jump:
            self.gravity = 5
            self.position = (self.position[0], self.position[1]-self.speed)
            self.jump = False
        else:
            self.gravity += 0.2
            self.position = (self.position[0], self.position[1]+self.gravity)

        self.screen.blit(self.bird_status[0], self.position)


class Pipeline(object):

    def __init__(self):
        pass

    def update(self):
        pass


def main():
    pygame.init()
    pygame.display.set_caption('疯狂的小鸟')
    clock = pygame.time.Clock()
    size = 400, 650
    screen = pygame.display.set_mode(size)

    map = Map(screen)
    bird = Bird(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                bird.jump = True
                bird.gravity = 5
                bird.speed = 10
            elif event.type == pygame.QUIT:
                pygame.quit()

        map.update()
        bird.update()
        pygame.display.update()

    sys.exit()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Python(Day52).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XS_nEQ-GcuCRSX9NRciLmVJxbrDAMkwE
"""

pip install pygame

import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            active = False
    pygame.display.flip()

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
if keys[pygame.K_RIGHT]:
if keys[pygame.K_SPACE]:
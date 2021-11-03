import pygame
import sys
from pygame import draw
from pygame.constants import QUIT

pygame.init()
screen = pygame.display.set_mode((1080, 600))
pygame.display.set_caption('keyboard')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 設定琴鍵基礎參數


def draw_black_key():
    for x in range(21, 109, 1):
        if x == 22:
            pygame.draw.rect(screen, BLACK, [31.5, 0, 17, 45], 0)
        elif x % 12 == 1:
            pygame.draw.rect(screen, BLACK, [
                             ((x//12)-2)*140+60 + 11.5, 0, 17, 45], 0)
        elif x % 12 == 3:
            pygame.draw.rect(
                screen, BLACK, [((x//12)-2)*140+80 + 11.5, 0, 17, 45], 0)
        elif x % 12 == 6:
            pygame.draw.rect(
                screen, BLACK, [((x//12)-2)*140+120 + 11.5, 0, 17, 45], 0)
        elif x % 12 == 8:
            pygame.draw.rect(
                screen, BLACK, [((x//12)-2)*140+140 + 11.5, 0, 17, 45], 0)
        elif x % 12 == 10:
            pygame.draw.rect(
                screen, BLACK, [((x//12)-2)*140+160 + 11.5, 0, 17, 45], 0)


def draw_white_key():
    for x in range(1, 53, 1):
        pygame.draw.rect(screen, BLACK, [x*20, 0, 20, 70], 1)


head_font = pygame.font.SysFont(None, 60)
screen.blit(background, (0, 0))
draw_white_key()
draw_black_key()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

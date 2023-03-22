import numpy as np
import pygame
import Movement
import BoardData
import random
from time import sleep

from pygame.constants import K_h, QUIT

pygame.init()
Gamescreen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess Bot")


def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("down")
            x, y = event.pos
            x = x // 100
            y = y // 100
            BoardData.selected = y * 8 + x
            BoardData.highlighted = Movement.movePieces(BoardData.items_list[BoardData.selected], BoardData.selected)
        if event.type == pygame.MOUSEBUTTONUP:
            print("up")
            x, y = event.pos
            x = x // 100
            y = y // 100
            Movement.movefromto(BoardData.selected, y * 8 + x)
            BoardData.selected = None
            BoardData.highlighted.clear()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                BoardData.highlighted=[]
                x=random.randint(0,7)
                print(x)
                BoardData.highlighted.append(24+x)
                Movement.movefromto(8+x,24+x)
                BoardData.highlighted.clear()
        if event.type == pygame.QUIT:
            return True
    return False


def drawChessBoard():
    global Gamescreen
    width = 1
    Gamescreen.fill((0, 81, 0))
    for i in range(0, 8):
        for j in range(0, 8):
            index = j * 8 + i
            color = (83, 128, 0) if (i + j) % 2 == 0 else (222, 255, 198)
            piece = BoardData.items_list[index]
            if index == BoardData.selected:
                color = (0, 255, 255)
            if index in BoardData.highlighted:
                color = (200, 0, 255)
            rect = pygame.draw.rect(Gamescreen, color,
                                    (width + i * 100, width + j * 100, 100 - 2 * width, 100 - 2 * width))
            if BoardData.items_list[index] != BoardData.EMPTY:
                img = BoardData.chessPieces[piece]
                img2 = pygame.image.frombuffer(img.tobytes(), img.shape[:2][::-1], "RGBA")
                Gamescreen.blit(img2, rect)


def main():
    Gameexit = False
    BoardData.loadChessTextures()
    while not Gameexit:
        drawChessBoard()
        pygame.display.update()
        Gameexit = handleEvent()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

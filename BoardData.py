from PIL import Image
import numpy as np

EMPTY = 0
BKING=1
BQUEEEN=2
BROOK = 3
BKNIGHT=4
BBISHOP=5
BPAWN=6
WKING=7
WQUEEEN=8
WROOK=9
WKNIGHT=10
WBISHOP=11
WPAWN=12

chessPieces = ["","BPAWN", "BROOK", "BKNIGHT", "BBISHOP", "BQUEEEN", "BKING",
                "WPAWN", "WROOK", "WKNIGHT", "WBISHOP", "WQUEEEN", "WKING"]

items_list = [
    BROOK, BKNIGHT, BBISHOP, BQUEEEN, BKING, BBISHOP, BKNIGHT, BROOK,
    BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN, BPAWN,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN, WPAWN,
    WROOK, WKNIGHT, WBISHOP, WQUEEEN, WKING, WBISHOP, WKNIGHT, WROOK
]

selected = None
highlighted:list[int]=[]

def loadChessTextures():
    global chessPieces
    img = Image.open("textures/ChessPiecesArray.png")
    scale=1.5
    img = img.resize((round(img.size[0]*scale),round(img.size[1]*scale)),Image.ANTIALIAS)
    img = np.asarray(img)
    size = img.shape
    for i in range(0,2):


        for j in range(0,5+1):
            chessPieces[i*6+j+1]=img[(size[0]//2)*i:(size[0]//2)*(i+1),(size[1]//6)*j:(size[1]//6)*(j+1)]



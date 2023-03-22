import BoardData


def movefromto(a, b):
    if b not in BoardData.highlighted:
        return
    BoardData.items_list[b] = BoardData.items_list[a]
    BoardData.items_list[a] = BoardData.EMPTY


def movePieces(id: int, index: int) -> list[int]:
    pos: list[tuple[int, int]] = []
    y, x = divmod(index, 8)
    if id == BoardData.BPAWN or id == BoardData.WPAWN:
        pos = getMovementsOfPawn(x, y, True if id == BoardData.BPAWN else False)
    elif id == BoardData.BROOK or id == BoardData.WROOK:
        pos = getMovementsOfRook(x, y)
    elif id == BoardData.BKNIGHT or id == BoardData.WKNIGHT:
        pos = getMovementsOfKnight(x, y)
    elif id == BoardData.BBISHOP or id == BoardData.WBISHOP:
        pos = getMovementsOfBishop(x, y)
    elif id == BoardData.BQUEEEN or id == BoardData.WQUEEEN:
        pos = getMovementsOfQueen(x, y)
    elif id == BoardData.BKING or id == BoardData.WKING:
        pos = getMovementsOfQueen(x, y)

    res = [i * 8 + j for i, j in pos if 8 > i > -1 and 8 > j > -1]

    return res


def getMovementsOfPawn(x: int, y: int, down: bool):
    pos = [(y + (1 if down else -1), x)]
    if y == (1 if down else 6): pos.append((y + 2 * (1 if down else -1), x))
    return pos


def getMovementsOfRook(x: int, y: int):
    pos = [(y + i, x) for i in range(1, 8 - y)]
    pos.extend([(y, x + i) for i in range(1, 8 - x)])
    pos.extend([(y - i, x) for i in range(1, y + 1)])
    pos.extend([(y, x - i) for i in range(1, x + 1)])
    return pos


def getMovementsOfKnight(x: int, y: int):
    poss = [1, 2]
    pos = [(y + a * poss[i % 2], x + b * poss[(i % 2) - 1]) for i in range(8) for a, b in
           [(-1, 1), (1, -1), (-1, -1), (1, 1)]]
    return pos


def getMovementsOfBishop(x: int, y: int):
    pos = [(y + i, x + i) for i in range(1, 8)]
    pos.extend([(y - i, x - i) for i in range(1, 8)])
    pos.extend([(y - i, x + i) for i in range(1, 8)])
    pos.extend([(y + i, x - i) for i in range(1, 8)])
    return pos


def getMovementsOfQueen(x: int, y: int):
    return getMovementsOfBishop(x, y) + getMovementsOfRook(x, y)


def getMovementsOfKing(x: int, y: int):
    pos = [(y + i, x + j) for i in range(-1, 2) for j in range(-1, 2)]
    return pos

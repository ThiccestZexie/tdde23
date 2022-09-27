import math


def new_board():
    return {}
def is_free(gameBoard, y, x):
    if(y,x) in gameBoard:
        return False
    else:
        return True
def place_piece(gameBoard, y, x, piece):
    if is_free(gameBoard, y, x):
        gameBoard[(y,x)] = piece
        return True
    else:
        return False
def remove_piece(gameBoard, y, x):
    if not is_free(gameBoard, y, x):
        del gameBoard[(y,x)]
        return True
    else:
        return False
def move_piece(gameBoard, y, x, newY, newX):
    if is_free(gameBoard, newY, newX):
        name = gameBoard[(y,x)]
        remove_piece(gameBoard, y,x)
        place_piece(gameBoard, newY, newX, name)
        return True
    else:
        return False
def get_piece(gameBoard, y, x):
    if not is_free(gameBoard,y, x):
        return gameBoard.get((y,x))
    else:
        return False
def nearest_piece(gameBoard, y, x):
    newDis = 0
    lowDis = 0
    lowestCord = ()
    for key in gameBoard:
        newDis = math.dist((y,x), key)
        if lowDis > newDis:
            lowDis = newDis
            lowestCord = key
        else:
          lowDis = newDis
    return lowestCord
def count(gameBoard, type, cord, name):
    sum = 0
    if type == "row":
        for i in range(1000): # chanage range
            if get_piece(gameBoard,i ,cord) == name:
                sum += 1
    if type == "column":
        for i in range(1000):
            if get_piece(gameBoard,cord,i) == name:
                sum += 1
    return sum            

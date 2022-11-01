import math

def new_board():
    return {}


def is_free(gameBoard, x, y):
    if(x,y) in gameBoard:
        return False
    else:
        return True


def place_piece(gameBoard, x, y, piece):
    if is_free(gameBoard, x, y):
        gameBoard[(x,y)] = piece
        return True
    else:
        return False


def remove_piece(gameBoard, x, y):
    if not is_free(gameBoard, x, y):
        del gameBoard[(x,y)]
        return True
    else:
        return False


def move_piece(gameBoard, x, y, newx, newy):
    if is_free(gameBoard, newx, newy): # kollar inte x,y innan den bxter plats
        piece = gameBoard[(x,y)]
        remove_piece(gameBoard, x,y)
        place_piece(gameBoard, newx, newy, piece)
        return True
    else:
        return False


def get_piece(gameBoard, x, y):
    if not is_free(gameBoard,x, y):
        return gameBoard.get((x,y))
    else:
        return False


def nearest_piece(gameBoard, x, y):
    newDis = 0
    lowDis = 0
    lowestCord = ()
    
    for key in gameBoard:
        newDis = math.dist((x,y), key)
        if lowDis > newDis:
            lowDis = newDis
            lowestCord = key
        else:
          lowDis = newDis
    return lowestCord


def count(gameBoard, txpe, cord, piece):
    sum = 0
    if txpe == "row":
        for keys in gameBoard: 
            if gameBoard[keys] == piece:
                if keys[1] == cord:
                    sum += 1
    if txpe == "column":
       for keys in gameBoard: 
            if gameBoard[keys] == piece:
                if keys[0] == cord:
                    sum += 1
    return sum


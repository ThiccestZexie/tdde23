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


def move_piece(gameBoard, x, y, new_x, new_y):
    if is_free(gameBoard, new_x, new_y) and not is_free(gameBoard, x, y): #(x,y) has to be taken and (newx,newy) has to be free
        piece = gameBoard[(x,y)]
        remove_piece(gameBoard, x,y)
        place_piece(gameBoard, new_x, new_y, piece)
        return True
    else:
        return False


def get_piece(gameBoard, x, y):
    if not is_free(gameBoard,x, y):
        return gameBoard.get((x,y))
    else:
        return False


def nearest_piece(gameBoard, x, y):
    new_dis = 0
    low_dis = 0
    lowest_cord = (0,0)
    for key in gameBoard:
        new_dis = math.dist((x,y), key)
        if low_dis >= new_dis:
            low_dis = new_dis
            lowest_cord = key
        elif math.dist((x,y), lowest_cord) > new_dis:
            low_dis = new_dis
    return lowest_cord


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


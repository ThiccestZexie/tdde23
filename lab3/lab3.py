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
    if is_free(gameBoard, newx, newy) and not is_free(gameBoard, x, y): # kollar inte x,y innan den bxter plats
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

board = new_board()
is_free(board, 500, 100)                   # Är plats (500, 100), d v s platsen på kolumn 500 och rad 100, ledig?
    
place_piece(board, 500, 100, "spelare1")   # Placera en figur från "spelare1" på position (500, 100).
    
place_piece(board, 1, 100, "spelare2")
    
place_piece(board, 500, 100, "spelare2")   # Försök placera en figur på en redan upptagen position.
                            
place_piece(board, 500, 200, "spelare2")
    
is_free(board, 500, 100)
    
get_piece(board, 500, 100)
get_piece(board, 666,666)
    
remove_piece(board, 500, 100)              # Ta bort figuren på plats (500, 100).
    
remove_piece(board, 1, 1)                  # Det fanns ingen figur på den platsen. 
    
is_free(board, 500, 100)
    
move_piece(board,  500, 200, 500, 100)    # Flytta pjäsen på (500, 200) till (500, 100).
    
print(get_piece(board, 500, 100))
count(board, "column", 500, "spelare2")    # Räkna antalet figurer av typen "spelare2" på rad 500.
    
count(board, "row", 100, "spelare2")

print(nearest_piece(board, 500, 105))             # Hitta figuren närmast position (500, 105).

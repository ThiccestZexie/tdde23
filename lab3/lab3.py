from math import fabs
from operator import truediv

def new_board():
    gameBoard = {}
    for i in range(1000):
        gameBoard[(i,0)] = ({"is_free": True, "piece_name":'', "valid_place": True, "removable piece": True })
        for x in range(1000):
            gameBoard[(i,x)] = ({"is_free": True, "piece_name":'', "valid_place": True, "removable piece": True }) 
    return gameBoard

def is_free(gameBoard, xCor, yCor):
    return gameBoard[xCor,yCor].get("is_free")

def place_piece(gameBoard, xCor, yCor, name):
    if is_free(gameBoard, xCor, yCor) == True:
        gameBoard[xCor,yCor].update({"piece_name": name })
        gameBoard[xCor,yCor].update({"is_free": False })
        return True
    elif gameBoard[xCor,yCor].get("is_free") == False: # maybe just else statement
        return False

def remove_piece(gameBoard, xCor, yCor):
    if is_free(gameBoard, xCor, yCor) == False:
        gameBoard[xCor,yCor].update({"piece_name": '' })
        gameBoard[xCor,yCor].update({"is_free": True })
        return True
    elif is_free(gameBoard, xCor, yCor) == True: # maybe just else statement
        return False

def get_piece(gameBoard,xCor, yCor):
    if is_free(gameBoard, xCor, yCor) == False:
        return gameBoard[xCor,yCor].get("piece_name")
    else:
        return False

def move_piece(gameBoard, xCor, yCor, xCorMove, yCorMove):
    if is_free(gameBoard, xCor, yCor) == False:
        name = get_piece(gameBoard, xCor,yCor)
        remove_piece(gameBoard, xCor, yCor)
        place_piece(gameBoard, xCorMove, yCorMove, name)
        return True
    elif is_free(gameBoard, xCor, yCor) == True: # maybe just else statement
        return False

def count(gameBoard, type, yCor, ): # need som eextra work 
    playerSum = 0
    if type == "row":
        for i in range(len(gameBoard)):
            if is_free(gameBoard, i, yCor)== False:
                if get_piece(gameBoard, i, yCor) == "spelare2": # else its a spelare1
                    playerSum +=1
        
    
 
#def nearest_piece(gameBoard, xCor, yCor): # possibly nested loop that checks row +- colum +-row +- colum and so on and compares




board = new_board()
print(is_free(board, 500,100))
print(place_piece(board, 500, 100, "spelare1"))
print(place_piece(board, 1, 100, "spelare2"))
print(place_piece(board, 500, 100, "spelare2"))
print(place_piece(board, 500, 200, "spelare2"))
print(is_free(board,500,100))
print(get_piece(board,500,100))
print(get_piece(board, 666,666))
print(remove_piece(board, 500, 100))
print(remove_piece(board, 1,1))
print(is_free(board, 500, 100))
print(move_piece(board, 500,200,500,100)) # need to fix name
print(get_piece(board,500,100))



  


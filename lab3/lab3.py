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
    if gameBoard == {}:
        return False
    min_dist = float("inf")
    lowest_x, lowest_y = None, None

    for key in gameBoard:
        new_dis = math.dist((x,y),key)
        if new_dis < min_dist:
            min_dist = new_dis
            lowest_x,lowest_y = key
        elif math.dist((x,y), (lowest_x,lowest_y)) > new_dis:
            min_dist = new_dis
    return (lowest_x,lowest_y)


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


def test_1():
    board = new_board()
    place_piece(board, 500, 110, "spelare2")
    place_piece(board, 500, 103, "spelare2")
    place_piece(board, 400, 105, "spelare2")
    place_piece(board, 500, 102, "spelare2")

    # Hitta figuren närmast position (0, 0).
    assert nearest_piece(board, 500, 105) == (500, 103)


def test_2():
    board = new_board()

    place_piece(board, 500, 500, "spelare2")
    place_piece(board, 10, 10, "spelare2")
    assert nearest_piece(board, 0, 0) == (10,10)


def test_bas():
    board = new_board()
    assert (is_free(board, 500, 100)) == True 
    assert (place_piece(board, 500, 100, "spelare1"))  == True 
    assert (place_piece(board, 1, 100, "spelare2")) == True
    assert (place_piece(board, 500, 100, "spelare2")) == False 
    assert (place_piece(board, 500, 200, "spelare2")) == True
    assert (is_free(board, 500, 100)) == False
    assert (get_piece(board, 500, 100)) == 'spelare1'
    assert (get_piece(board, 666,666)) == False
    assert (remove_piece(board, 500, 100))        == True   
    assert (remove_piece(board, 1, 1) )            == False     
    assert (is_free(board, 500, 100)) == True
    assert (move_piece(board,  500, 200, 500, 100))  == True  
    assert (count(board, "column", 500, "spelare2") )  == 1 
    assert (count(board, "row", 100, "spelare2")) == 2
    assert (nearest_piece(board, 500, 105))  == (500,100)  

def test():
    test_1()
    test_2()
    test_bas()

    print("passed all tests")


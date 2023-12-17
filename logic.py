import random

def start_game():
    mat = [[0 for i in range(4)] for j in range(4)]
    return mat

def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
            elif mat[i][j] == 0:
                return 'GAME NOT OVER'
            elif i+1 < 4 and j+1 < 4:
                if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                    return 'GAME NOT OVER'
            elif i+1 >= 4 and j+1 < 4:
                if mat[i][j] == mat[i][j+1]:
                    return 'GAME NOT OVER'
            elif i+1 < 4 and j+1 >= 4:
                if mat[i][j] == mat[i+1][j]:
                    return 'GAME NOT OVER'
    return 'LOST'
            
def compress(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        p = 0
        for j in range(4):
            e = mat[i][j]
            new_mat[i][p] = e
            if e != 0:
                p += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            a = mat[i][j]
            b = mat[i][j+1]
            if a != 0 and a == b:
                mat[i][j] = 2*a
                mat[i][j+1] = 0
    return mat

def reverse(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[i][3-j]
    return new_mat

def transpose(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[j][i]
    return new_mat

def move_left(grid):
    ch = True
    a = compress(grid)
    a = merge(a)
    a = compress(a)
    if a == grid:
        ch = False
    return a,ch

def move_right(grid):
    a = reverse(grid)
    a,ch = move_left(a)
    a =  reverse(a)
    return a,ch

def move_up(grid):
    a = transpose(grid)
    a,ch = move_left(a)
    a = transpose(a)
    return a,ch

def move_down(grid):
    a = transpose(grid)
    a,ch = move_right(a)
    a = transpose(a)
    return a,ch


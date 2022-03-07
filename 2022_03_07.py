from copy import deepcopy
import sys

def startGame():
    gameBoard, A, B, d = initialize()
    print(run(gameBoard, A, B, d))

def initialize():
    # 게임 보드 사이즈를 입력받는다.
    M, N = setGameBoardSize(-1, -1)

    # User의 좌표 (A, B) 및 방향 d를 입력받는다.
    A, B, d = setUserPos()

    # M x N 크기의 게임보드를 생성한다.
    gameBoard = setGameBoard(M, N)

    return gameBoard, A, B, d

def setGameBoardSize(M, N):
    while (not(0<M<=50 and 3<=N )): # M, N의 범위에대한 예외처리
        M, N = map(int, sys.stdin.readline().split())
    
    return M, N

def setUserPos():
    return map(int, sys.stdin.readline().split())


def setGameBoard(M, N):
    gameBoard = []
    for row in range(M): gameBoard.append(list(map(int, sys.stdin.readline().split())))

    return gameBoard

def run(gameBoard, A, B, d):
    the_number_of_blocked_route = [] 
    game_flag = True
    cnt = 1
    
    supportGameBoard = deepcopy(gameBoard)

    # 0: 북, 1: 동, 2: 남, 3: 서
    direction = [0, 1, 2, 3]

    while(game_flag):
        # 1. 왼쪽 회전 
        d = direction[direction.index(d) - 1]
        
        # 2. 길 확인
        if d == 0 :
            if supportGameBoard[A][B-1] == 0:
                B, supportGameBoard[A][B], cnt = B-1, 1, cnt+1
            else:
                the_number_of_blocked_route.append(d)
        elif d == 1:
            if supportGameBoard[A+1][B] == 0:
                A, supportGameBoard[A][B], cnt = A+1, 1, cnt+1
            else:
                the_number_of_blocked_route.append(d)
        elif d == 2:
            if supportGameBoard[A][B+1] == 0:
                B, supportGameBoard[A][B], cnt = B+1, 1, cnt+1
            else:
                the_number_of_blocked_route.append(d)
        elif d == 3:
            if supportGameBoard[A-1][B] == 0:
                A, supportGameBoard[A][B], cnt = A-1, 1, cnt+1
            else:
                the_number_of_blocked_route.append(d)

        # 3-1. 4방향 모두 막혔다면 뒤로 가기
        if len(the_number_of_blocked_route) == 4:
            if the_number_of_blocked_route[3] == 0:
                B -= 1
                the_number_of_blocked_route = []
            elif the_number_of_blocked_route[3] == 1:
                A -= 1
                the_number_of_blocked_route = []
            elif the_number_of_blocked_route[3] == 2:
                B += 1
                the_number_of_blocked_route = []
            elif the_number_of_blocked_route[3] == 3:
                A += 1
                the_number_of_blocked_route = []
        
        # 3-2. 뒤로 갔는데 바다면 게임 종료하기
        if gameBoard[A][B] == 1: game_flag = False

    return cnt

startGame()


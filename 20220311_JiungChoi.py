''' 
얼음 군집 수 찾기
0 = 얼음, 1 = 칸막이
'''




def BFS(gameBoard, row, column):
    stackSpace =[]
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 위 오른쪽 아래 왼쪽
    gameBoard[row][column] = "1"
    now_pos = [row, column]
    flag = True

    
    while(flag):
        # 4방향 깊이 우선 탐색하기
        for dir in range(4):

            # 다음 방향으로 가보기
            next_pos = [now_pos[i] + direction[dir][i] for i in range(len(now_pos))]
            
            # 범위 밖이면 이동 x
            if not ((len(gameBoard) > next_pos[0] >= 0) and (len(gameBoard[0]) > next_pos[1] >= 0)):
                if dir is 3: 
                    if len(stackSpace) == 0: flag = False
                    else : now_pos = stackSpace.pop()
                    continue
                else: continue

            # 막힌 길이면 이동 x
            if gameBoard[next_pos[0]][next_pos[1]] == "1":
                if dir is 3: 
                    if len(stackSpace) == 0: flag = False
                    else : now_pos = stackSpace.pop()
                    continue
                else: continue

            stackSpace.append(now_pos)
            now_pos = next_pos
            gameBoard[now_pos[0]][now_pos[1]] = "1"
            break

        
    return gameBoard

# 게임 보드 생성
import sys

M, N = map(int, sys.stdin.readline().split())


cnt = 0
gameBoard, pos = [], [M, N]
for _ in range(M): gameBoard.append(list(sys.stdin.readline().rstrip("\n")))


# BFS 
for row in range(M):
    for column in range(N):
        if gameBoard[row][column] == "1": continue
        else : 
            gameBoard = BFS(gameBoard, row, column)
            cnt += 1

print(cnt)
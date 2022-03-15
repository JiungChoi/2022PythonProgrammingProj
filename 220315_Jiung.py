''' 
얼음 군집 수 찾기
0 = 얼음, 1 = 칸막이
'''




def DFS(gameBoard):
    stackSpace =[]
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # up right down left
    gameBoard[0][0] = "1"
    now_pos = [0, 0]
    gameBoard_row = len(gameBoard)
    gameBoard_column = len(gameBoard[0])
    dist = gameBoard_row * gameBoard_column + 1 # 최대거리
    flag = True

    
    while(flag):
        # 4방향 깊이 우선 탐색하기
        for dir in range(4):

            # 다음 방향으로 가보기
            next_pos = [now_pos[i] + direction[dir][i] for i in range(len(now_pos))]
            
            # 범위 밖이면 이동 x
            if not ((gameBoard_row > next_pos[0] >= 0) and (gameBoard_column > next_pos[1] >= 0)):
                if dir is 3: 
                    now_pos = stackSpace.pop()
                    continue
                else: continue

            # 막힌 길이면 이동 x
            if gameBoard[next_pos[0]][next_pos[1]] == "1":
                if dir is 3: 
                    now_pos = stackSpace.pop()
                    continue
                else: continue
            
            # 출구를 찾았다면
            if next_pos == [gameBoard_row-1, gameBoard_column-1]: dist = len(stackSpace)+2 if len(stackSpace)+2 < dist else dist
            
            stackSpace.append(now_pos)
            now_pos = next_pos
            gameBoard[now_pos[0]][now_pos[1]] = "1"
            break
    # 순회를 마쳤으면 
    else : return dist



if __name__=="__main__":
    import sys

    # 게임 보드 생성
    N, M = map(int, sys.stdin.readline().split())

    cnt = 0
    gameBoard, pos = [], [N, M]
    for _ in range(N): gameBoard.append(list(sys.stdin.readline().rstrip("\n")))
    
    print(DFS(gameBoard))

    # 미로찾기, DFS
    
            

N, M = map(int, input().split())

box = []
for _ in range(N):
    box.append(list(map(int, list(input()))))

move = {0:[0, -1], 1:[0, 1], 2:[-1, 0], 3:[1, 0]} # 상하좌우


def dfs_move(arr=box, start=[0, 0], visited=[]):
  visited.append(start)
  for C in range(4):
    node = [i + j for i, j in zip(start, move[C])]
    if node[0] >= 0 and node[1] >= 0 and node[0] < N and node[1] < M:
      if node not in visited and arr[node[0]][node[1]] == 0:
        dfs_move(start=node, visited=visited)
  return visited


visited = []
count = 0
for i in range(N):
  for j in range(M):
    if [i, j] not in visited and box[i][j]==0:
      visited = dfs_move(start=[i, j], visited=visited)
      count = count + 1
print(count)
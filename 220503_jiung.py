# 바닥 공사
# DP 는 한 번 계산한걸 저장해야한다.
# N개의 타일 말고 1부터 N-1까지 모든 경우의 수를 세면서 저장할 것
# 타일의 종류 1 x 2 , 2 x 1 , 2 x 2
# 결과 값은 796,796으로 나눈 나머지를 출력할 것

import sys

def makeFloor(X):
    floor = [ 0 for _ in range(X) ]
    
    for i in range(X):
        if i == 0: floor[i] = 1 # 첫 번째는 2 x 1 타일로만 채울 수 있음
        elif i == 1: floor[i] = 3 # 두 번째는 1 x 2, 2 x 1 , 2 x 2 중 하나의 타일로만 채울 수 있음
        else : floor[i] = floor[i-1] + 2*floor[i-2]

             
    return floor[-1] % 796796
    
print(makeFloor(int(sys.stdin.readline())))
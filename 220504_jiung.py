# 효율적인 화폐 구성
# 15원을 만들기 위해서는 14원 .. 13원을 만드는 방법이 최적화가 되어 있었으면 좋겠음
# 

import sys

def makeOtimizatedList(N, M):
    # Make Money List
    moneys = []
    for _ in range(N):
        moneys.append(int(sys.stdin.readline()))

    # Create will be Optimizated List
    primaryList = [ -1 for _ in range(M)]
    for money in moneys :
        if money<M: 
            primaryList[money-1] = 1 
    
    # Make Optimizated List
    for idx in range(M):
        for money in moneys:
            if (idx+1 > money): # 뺄 인덱스 위치가 있어야함
                if (primaryList[idx-money] != -1): # 뺀 인덱스는 가능한 구성이어야함
                    if (primaryList[idx] < 0): primaryList[idx] = primaryList[idx-money]+1
                    else : primaryList[idx] = min(primaryList[idx-money]+1, primaryList[idx])

    print(primaryList[-1])

N, M = map(int, sys.stdin.readline().split())
makeOtimizatedList(N, M)

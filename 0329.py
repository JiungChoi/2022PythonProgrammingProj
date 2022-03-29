# 떡복이 떡 만들기

import sys

N, M = map(int, sys.stdin.readline().split())
dduckAry = sorted(list(map(int, sys.stdin.readline().split())))

def dduck(ary, M):
    for H in range(ary[-1], 0, -1):    
        total = 0
        for idx in range(len(ary)):
            total += (ary[idx]-H) if ary[idx] > H else 0
        if total >= M: print(H)

dduck(dduckAry, M)



        
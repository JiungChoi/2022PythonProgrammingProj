# 떡복이 떡 만들기

import sys

N, M = map(int, sys.stdin.readline().split())
dduckAry = sorted(list(map(int, sys.stdin.readline().split())))

def dduck(ary, M):

    st = 0
    end = ary[-1]
    
    while(st<=end):
        H = (end+st)//2
        total = 0
        for idx in range(len(ary)):
            total += (ary[idx]-H) if ary[idx] > H else 0
        
        if total > M :
            st = H+1
            if not (st<=end): return H+1
        elif total < M :
            end = H-1
            if not (st<=end): return H-1
        else: return H

print(dduck(dduckAry, M))        
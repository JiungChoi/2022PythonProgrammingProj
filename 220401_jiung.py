# 1로 만들기
# DP 는 한 번 계산한걸 저장해야한다.
# 10 -> 9 -> 3 -> 1 인데
# 9 -> 3 -> 1 이다.
# 10을 계산할 때는 앞에서 구한 9를 이용해서 구하는 것이다.

import sys

def howStepToOne(X):
    calc_table = [ i-1 if i != 0 else 0 for i in range(0, X+1)] # 각 값에 도달하기 위한 최댓값(-1만 연산했을 때) 
    print(calc_table) #1 
    
    for idx in range(3, X+1):
        
        if (idx%5 == 0): calc_table[idx] = min(calc_table[idx//5]+1, calc_table[idx])
        if (idx%3 == 0): calc_table[idx] = min(calc_table[idx//3]+1, calc_table[idx])
        if (idx%2 == 0): calc_table[idx] = min(calc_table[idx//2]+1, calc_table[idx])
        calc_table[idx] = min(calc_table[idx-1]+1, calc_table[idx])
    
    print(calc_table)

howStepToOne(int(sys.stdin.readline()))


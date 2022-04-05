# 욕심쟁이 개미전사

from this import d
import numpy as np
import sys

def antWantManyMeals(N, meals):
    stealList = [0]
    while(True):
        idx = stealList[-1]

        # 식량 창고 맨 끝에서 두 칸 앞으로만 보겠다. 안 해주면 out of idx 일어날 것
        if idx <= N-3:
            if meals[idx]+meals[idx+2] <= meals[idx+1]:
                stealList.pop()
                stealList.append(idx+1)
            else: stealList.append(idx+2)
        else : break

    sumStealList(meals, stealList)

def sumStealList(meals, stealList):
    meals = np.array(meals)
    stealList = np.array(stealList)

    return print(np.sum(meals[stealList]))

antWantManyMeals(int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split())))

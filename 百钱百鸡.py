##question :
'''
公鸡数量：x，母鸡数量：y，小鸡数量：z
约束条件：1.整型约束
        2.取值约束:
            0<x<100/3
            0<y<100/2
            0<z<100/0.5
        3.等式约束
            x+y+z = 100
            3*x+2*y+0.5*z = 100
'''



#%%   method 1

x=0
y=0
z=0
##数量
n=1
##计数变量

for y in range(1,50):               #符合母鸡的取值约束
    for z in range(1,100-y):        #(符合小鸡的取值约束+数量非负约束+等式约束）
        x = 100-y-z                 #必定大于0,内涵x+y+z = 100
        if  3*x+2*y+0.5*z == 100:
            print(f"存在方案{n}:公鸡{x}只,母鸡{y}只,小鸡{z}只")
            n+=1
        else:
            continue


#%% method 2

import numpy as np
from pulp import LpMaximize,LpProblem, LpVariable

li = np.zeros(100)     #储存y值的变量
n = 0                 #计数变量
while True:
    model = LpProblem(name="integer_linear_equations", sense=LpMaximize)

    # 定义变量
    x = LpVariable(name="x", lowBound=1, upBound= 33,cat='Integer')
    y = LpVariable(name="y", lowBound=1, upBound = 50,cat='Integer')
    z = LpVariable(name="z", lowBound=1, upBound= 200, cat='Integer')


    model += 3*x + 2*y + 0.5*z == 100
    model += x+y+z == 100

    #加入已有解约束
    for i in range(n):
        model += y >= li[i]+1


        # 求解问题
    if    model.solve()==1:

        # 输出结果
        print(f"x = {x.varValue}")
        print(f"y = {y.varValue}")
        print(f"z = {z.varValue}")
        li[n] = y.varValue
        n+=1
    else:
        print(f"一共有{n}种解法")
        break









            



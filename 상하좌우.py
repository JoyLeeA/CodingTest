'''
5
R R R U D D
'''

dic = {'L':(0,-1), 'R':(0,1) , 'U':(-1,0), 'D':(1,0)}
N = int(input())
move = list(input().split())

x = 1
y = 1

for i in move:
    if 0< x+dic[i][0] <= N and 0< y+dic[i][1] <=N:
        x += dic[i][0]
        y += dic[i][1]
    
print(x, y)

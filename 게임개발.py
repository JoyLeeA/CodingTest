# 0-> 북 1-> 동 2->남 3->서
# 0 -> 육지 2-> 바다
'''
4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

N, M = map(int,input().split())
y, x, direction = map(int,input().split())
my_map = [list(map(int,input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]  
dy = [-1, 0, 1, 0] 

def turnleft():
    global direction
    if direction == 0:
        direction= 3
    else:
        direction -= 1

cnt = 0
time = 0
while True:
    turnleft()
    time += 1
    my_map[y][x] = 2
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0<= ny < N and 0 <= nx < M and not my_map[ny][nx]:
        y = ny
        x = nx
        time = 0
        cnt += 1
        continue
    if time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if my_map[ny][nx] == 2:
            cnt += 1
            break
        else:
            break
            
print(cnt)



# def iswall(y,x):
#     if 0 <= y < N and 0 <= x < M and not my_map[y][x]:
#         return True
#     return 
    
# cnt = 0
# mytry = 0
# while True:
#     if direction == 0:
#         direction = 3
#         mytry += 1
#     else:
#         direction -=1
#         mytry += 1

#     if direction == 0:
#         if iswall(y-1,x):
#             my_map[y][x] = 2
#             y -= 1
#             cnt += 1
#             mytry = 0
#             #visited.append((y,x))
#     elif direction == 1:
#         if iswall(y,x+1):
#             my_map[y][x] = 2
#             x += 1
#             #visited.append((y,x))
#             cnt += 1
#             mytry = 0
#     elif direction == 2:
#         if iswall(y+1,x):
#             my_map[y][x] = 2
#             y += 1
#             #visited.append((y,x))
#             cnt +=1
#             mytry = 0
#     elif direction == 3:
#         if iswall(y,x-1):
#             my_map[y][x] = 2
#             x -= 1
#             #visited.append((y,x))
#             cnt += 1
#             mytry = 0

#     if mytry == 4:
#         break

# print(cnt+1)
        


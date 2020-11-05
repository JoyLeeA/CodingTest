N, M = map(int,input().split())
tray = [list(map(int,input())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x, y):
    stack = []
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M and tray[nx][ny] == 0:
                tray[nx][ny] = -1
                stack.append((nx,ny))

result = 0
for i in range(N):
    for j in range(M):
        if tray[i][j]==0:
            result +=1
            dfs(i,j)

print(result)

'''
4 5
00110
00011
11111
00000
'''
    

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
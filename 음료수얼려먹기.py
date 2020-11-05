N, M = map(int,input().split())
tray = [list(map(int,input())) for _ in range(N)]

def dfs(x, y):
    if x <= -1 or x>= N or y <= -1 or y>=M:
        return False
    if not tray[x][y]:
        tray[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result +=1

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
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
'''
5 6
101010
111111
000001
111111
111111
'''
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if 0 <= nx < N and 0 <= ny < M  and maze[nx][ny] == 1:
            #     maze[nx][ny] = maze[x][y] + 1
            #     x = nx
            #     y = ny
            #     Q.append((x, y))
            #     visited.append((x,y))
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if not maze[nx][ny]:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                Q.append((nx,ny))

# 0이 괴물 / 1이 통로
N, M = map(int, input().split())
maze = [list(map(int,input())) for _ in range(N)]
bfs (0, 0)
print(maze[N-1][M-1])




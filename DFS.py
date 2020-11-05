# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = ' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

def dfs(graph, v):
    stack = []
    visited = [v]
    stack.append(v)
    while stack:
        v = stack.pop()
        print(v, end= " ")
        for i in graph[v]:
            if i not in visited:
                v = i
                visited.append(v)
                stack.append(v)
            
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4],
[7], [2, 6, 8], [1, 7] ]
#isited = [False] * 9
dfs(graph, 1)

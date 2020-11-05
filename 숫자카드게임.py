N, M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]

result = []
for i in range(N):
    result.append(min(array[i]))

print(max(result))

'''
3 3
3 1 2
4 1 4
2 2 2
'''
'''
2 4 
7 3 1 8
3 3 3 4
'''
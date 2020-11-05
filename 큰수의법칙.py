N, M, K = map(int,input().split())
data = list(map(int,input().split()))
data.sort(reverse = True)

cnt = 0
result = 0
for _ in range(M):
    if cnt == K:
        result += data[1]
        cnt = 0
    else:
        cnt += 1
        result += data[0]
print(result)
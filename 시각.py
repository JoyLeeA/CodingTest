N = int(input())
H = M =S = 0
cnt = 0
while True:
    S += 1
    if '3' in str(H) or '3' in str(M) or '3' in str(S):
        cnt +=1
    if H == N+1:
        break
    if S==60:
        M += 1
        S = 0
    if M ==60:
        H += 1
        M = 0
print(cnt)
dx = [-2,-1, -2, 1, 2, 1, -1, 2]
dy = [-1, -2, 1, -2, 1, 2, 2, -1]

temp = input()
row = int(temp[1])
column = ord(temp[0])-96

cnt = 0
for i in range(8):
    if 0 <column+dx[i] <=8 and 0< row+dy[i] <=8:
       cnt += 1

print(cnt)  

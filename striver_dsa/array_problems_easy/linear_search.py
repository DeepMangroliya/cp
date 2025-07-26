a = list(map(int, input().split()))
n = int(input())
flag = 0
for i in range(0, n):
    if a[i] == n:
        flag = i
        break

if flag:
    print(flag)
else:
    print(-1)

        
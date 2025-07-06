n=int(input())

for i in range(1, n+1):
    print(''.join('*' for j in range(0, n-i+1)))
    
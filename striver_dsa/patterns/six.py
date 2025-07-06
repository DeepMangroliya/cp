n = int(input())

for i in range(1,n+1):
    print(''.join(map(str, range(1,n-i+2))))
n = int(input())

for i in range(1,n+1):
    print(''.join(f'{j}' for j in range(0,i)))
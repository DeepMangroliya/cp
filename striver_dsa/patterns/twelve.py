n = int(input())
spaces=2*(n-1)
for i in range(1, n+1):
    #numbers
    for j in range(1, i+1):
        print(j, end='')
    #space
    for j in range(1, spaces+1):
        print(' ', end='')
    #numbers
    for j in range(i, 0, -1):
        print(j, end='')
    spaces-=2
    print()
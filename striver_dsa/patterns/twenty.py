n = int(input())
spaces = 2*n-2
for i in range(1, 2*n):
    #stars
    stars=i 
    if i > n:
        stars = 2*n-i
    for j in range(1,stars+1):
        print('*', end='')
    #spaces
    for j in range(1, spaces+1):
        print(' ', end='')
    #stars
    for j in range(1,stars+1):
        print('*', end='')
    print()
    if i<n: spaces-=2
    else: spaces+=2
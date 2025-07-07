n = int(input())

for i in range(0, 2*n-1):
    for j in range(0, 2*n-1):
        top = i
        bottom = (2*n-2)-i
        left = j
        right = (2*n-2)-j
        
        print(n-min(top,left,right,bottom), end='')
    print()
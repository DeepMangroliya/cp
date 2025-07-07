n = int(input())
start=0  
for i in range(1, n+1):
    #stars
    for j in range(0,n-i+1):
        print('*', end='')
     
    #spaces
    for j in range(1,start+1):
        print(' ', end='')
    start+=2
        
    #stars
    for j in range(0,n-i+1):
        print('*', end='')    
    print()
start-=2
for i in range(1, n+1):
    for j in range(1,i+1):
        print('*', end='')
    #spaces
    for j in range(1,start+1):
        print(' ', end='')
    start-=2
    #stars
    for j in range(1,i+1):
        print('*', end='')   
    print()
    
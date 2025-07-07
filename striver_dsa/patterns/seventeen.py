n = int(input())

for i in range(1,n+1):
    ch='A'
    #spaces
    for j in range(1,n-i+1):
        print(' ', end='')
    #char
    for j in range(2*i-1):
        print(ch, end='')
        if j < (2*i-1)//2:
            # print(f'in if iteration={i} and j value={j}')
            ch = chr(ord(ch)+1)
        else:
            ch = chr(ord(ch)-1)
    #spaces
    for j in range(1,n-i+1):
        print(' ', end='')
    print()
#     ch = chr(ord(ch)+1)
#     print()
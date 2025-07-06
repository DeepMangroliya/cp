n = int(input())
for i in range(1,n+1):
    for ch in range(ord('A'), ord('A')+i):
        print(chr(ch), end='')
    print()
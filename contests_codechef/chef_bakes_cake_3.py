# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count=0
    for i in range(0,n):
        if a[i]>b[i]:
            count+=(a[i]-b[i])
        else:
            continue
        
    print(count)
        
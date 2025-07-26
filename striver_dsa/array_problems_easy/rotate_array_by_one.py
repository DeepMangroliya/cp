a = list(map(int, input().split()))
temp = a[0]
n = len(a)
for i in range(1, len(a)):
    a[i-1] = a[i]
a[n-1] = temp

print(a)
    

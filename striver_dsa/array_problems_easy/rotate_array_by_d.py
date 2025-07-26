def rotate(a, d, n):
    if d == 0 or n <= 1:
        return
    temp = a[0]
    for i in range(1, n):
        a[i - 1] = a[i]
    a[n - 1] = temp
    rotate(a, d - 1, n)
    return a
    

a = list(map(int, input().split()))
d = int(input())
n = len(a)
d = d % n
print(d)
rotate(a, d, n)

print(a)
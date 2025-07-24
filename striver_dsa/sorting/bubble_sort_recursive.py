def bubble_sort(a, n):
    if n == 1:
        return
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    bubble_sort(a, n - 1)
    
a = list(map(int, input().split()))
bubble_sort(a, len(a))
print(a)
def insertion_sort(a, i):
    n = len(a)
    if i == n:
        return
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
    insertion_sort(a, i + 1)

a = list(map(int, input().split()))
insertion_sort(a, 1)
print(a)
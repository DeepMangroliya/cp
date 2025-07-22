def insertion_sort(a)->list:
    n = len(a)
    for i in range(len(a)):
        for j in range(i,0,-1):
            if a[j] < a [j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a

a = list(map(int, input().split()))
ans = insertion_sort(a)
print(ans)
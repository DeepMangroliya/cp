def partition(a, low, high):
    pivot = a[low]
    i, j = low, high
    while i < j:
        while a[i] <= pivot and i <= high - 1:
            i += 1
        while a[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[j], a[low] = a[low], a[j]
    
    return j
    
def quick_sort(a, low, high):
    if low < high:
        partition_index = partition(a, low, high)
        quick_sort(a, low, partition_index - 1)
        quick_sort(a, partition_index + 1, high)
    return a

a = list(map(int, input().split()))
ans = quick_sort(a,0,len(a)-1)
print(ans)
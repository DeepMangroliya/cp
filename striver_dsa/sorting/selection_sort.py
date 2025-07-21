# def selection_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]>arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     return arr

           
# arr = list(map(int,input().split()))
# ans = selection_sort(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = list(map(int, input().split()))
ans = selection_sort(arr)

print(arr)


    
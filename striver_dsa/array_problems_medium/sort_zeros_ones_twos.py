#Includes Dutch National Flag Algoritm (Optimal Approach)
# it says o to low-1 : all zeroes
# low to mid-1: all ones
# mid to high-1: unsorted
# high to n-1: all 2
# TC: O(N) and SC: O(1)

arr = list(map(int, input().split()))
low, mid, high = 0, 0, len(arr) - 1
while(mid <= high):
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)

#better approach O(2N), Sc-> O(1)
# arr = list(map(int, input().split()))
# count0, count1, count2 = 0,0,0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         count0 += 1
#     if arr[i] == 1:
#         count1 += 1
#     if arr[i] == 2:
#         count2 += 1
    
    
# for i in range(0, count0):
#     arr[i] = 0
# for i in range(count0, count0 + count1):
#     arr[i] = 1
# for i in range(count0 + count1, len(arr)):
#     arr[i] = 2

# print(arr)

# Tc: at worst case = O(3N)
# Sc: O(1)
arr = list(map(int, input().split()))
index = -1
for i in range(len(arr)-2, -1, -1):
    if arr[i] < arr[i+1]:
        index = i
        break
if index == -1:
    arr.reverse()
    
for i in range(len(arr)-1, index, -1):
    if arr[i] > arr[index]:
        arr[index], arr[i] = arr[i], arr[index]
        break

arr[index+1:] = arr[index+1:][::-1]
print(arr)
    
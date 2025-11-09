arr = list(map(int, input().split()))

for i in range(len(arr)-2, -1, -1):
    if arr[i] < arr[i+1]:
        index = i
        break
for i in range(len((arr)-1, index-1, -1)):
    if arr[i] > arr[index]:
        arr[index], arr[i] = arr[i], arr[index]

arr[index+1:] = arr[index+1:][::-1]
print(arr)
    
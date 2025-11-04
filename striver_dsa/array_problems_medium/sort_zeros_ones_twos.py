#Includes Dutch National Flag Algoritm


#better approach O(2N), Sc-> O(1)
arr = list(map(int, input().split()))
count0, count1, count2 = 0,0,0
for i in range(len(arr)):
    if arr[i] == 0:
        count0 += 1
    if arr[i] == 1:
        count1 += 1
    if arr[i] == 2:
        count2 += 1
    
    
for i in range(0, count0):
    arr[i] = 0
for i in range(count0, count0 + count1):
    arr[i] = 1
for i in range(count0 + count1, len(arr)):
    arr[i] = 2

print(arr)
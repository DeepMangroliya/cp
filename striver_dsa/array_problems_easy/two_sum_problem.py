arr = list(map(int, input().split()))
target = int(input())
# hashmap = defaultdict(int)
# need=0

# for i in range(0, len(arr)):
#     need = target - arr[i]
#     if need in hashmap:
#         print(i, hashmap[need])
#         break
#     hashmap[arr[i]] = i
# else:
#     print('Nahh')
arr.sort()
left, right = 0, len(arr) - 1
flag = True
while left < right:
    total = arr[left] + arr[right]
    if total != target:
        if total > target:
            right-=1
        elif total < target:
            left+=1
    else:
        print(arr[left], arr[right])
        flag = False
        break
    
if flag:
    print('Nothing Found')

# for i in range(0, len(arr)):
    
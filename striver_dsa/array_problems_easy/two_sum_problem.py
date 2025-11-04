arr = list(map(int, input().split()))
target = int(input())
#using a map TC: O(N*long(n)) in ordered_map or O(N) in unordered_map, SC  O(n)
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
#most optimal same TC as using a map-> O(N) + O(NlogN), but this is a 2 pointer.
# if asked for the indexes in the result, map is the optimal one, as this does need an extra array to maintain the indexes of the original array after we sorted thea array
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
    
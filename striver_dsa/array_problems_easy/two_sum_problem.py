from collections import defaultdict
arr = list(map(int, input().split()))
target = int(input())
hashmap = defaultdict(int)
need=0

for i in range(0, len(arr)):
    need = target - arr[i]
    if need in hashmap:
        print(i, hashmap[need])
        break
    hashmap[arr[i]] = i
else:
    print('Nahh')
    

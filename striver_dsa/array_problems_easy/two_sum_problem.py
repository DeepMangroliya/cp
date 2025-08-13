from collections import defaultdict
arr = list(map(int, input().split()))
target = int(input())
hashmap = defaultdict(int)
need=0

for i in range(0, len(arr)):
    need = target - arr[i]
    print(need)
    if need in hashmap:
        print('in')
        print(i, hashmap[need])
        break
    else:
        hashmap[need] = i

print(hashmap)
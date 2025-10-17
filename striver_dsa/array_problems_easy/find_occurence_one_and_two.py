a = list(map(int, input().split()))

# hashmap = defaultdict(int)

# for i in range(0, len(a)):
#     hashmap[a[i]]+=1

# for i in range(len(a)):
#     if hashmap[a[i]] == 1:
#         print(a[i])
#         break
        
xor1 = 0
for i in range(len(a)):
    xor1 = xor1 ^ a[i]
    
print(xor1)
    
#Variety 1, positive and negative elements are equal
# arr = list(map(int, input().split()))
# ans = [0] * len(arr)
# pos = 0
# neg = 1
# for i in range(len(arr)):
#     if arr[i] >= 0:
#         ans[pos] = arr[i]
#         pos += 2
#     else:
#         ans[neg] = arr[i]
#         neg += 2


#arrange ,and arrange rest at last.
arr = list(map(int, input().split()))
n = len(arr)
ans = [0] * len(arr)
pos = []
neg = []

for i in range(n):
    if arr[i] >= 0:
        pos.append(arr[i]) 
    else:
        neg.append(arr[i]) 
        
res = []
while i < len(pos) and i < len(neg):
    res.append(pos[i])
    res.append(neg[i])
    i += 1

# Add remaining elements (if any)
while i < len(pos):
    res.append(pos[i])
    i += 1

while i < len(neg):
    res.append(neg[i])
    i += 1

print(res)
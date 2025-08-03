a = list(map(int, input().split()))
max_sum, sum = 0, 0

for i in range(len(a)):
    if a[i] == 1:
        sum += 1
    else:
        sum = 0
    max_sum = max(max_sum, sum).  
print(max_sum)
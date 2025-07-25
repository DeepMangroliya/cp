a = list(map(int, input().split()))
result = 'Sorted'
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        result = 'Not ' + result
        break
print(result)
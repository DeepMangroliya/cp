a = list(map(int, input().split()))
largest = a[0]
second_largest = -1
for i in range(1,len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] < largest and a[i] > second_largest:
        second_largest = a[i]
print(second_largest)
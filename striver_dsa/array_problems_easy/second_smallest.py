import sys

a = list(map(int, input().split()))
smallest = a[0]
second_smallest = sys.maxsize
for i in range(1,len(a)):
    if a[i] < smallest:
        second_smallest = smallest
        smallest = a[i]
    elif a[i] > smallest and a[i] < second_smallest:
        second_smallest = a[i]
print(second_smallest)
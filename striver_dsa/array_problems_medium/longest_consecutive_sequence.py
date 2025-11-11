arr = list(map(int, input().split()))
temp = set(arr)
longest = 0
for element in temp:
    if (element - 1) not in temp:
        current = element
        count = 1
        while (current + 1) in temp:
            current += 1
            count += 1
        longest = max(count, longest)

print(longest)
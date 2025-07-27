# Space Complexity -> O(1) if union is not considered otherwise O(n+m)
# Time complexity -> O(n + m)

a1 = set(map(int, input().split()))
a2 = set(map(int, input().split()))

union = a1 | a2

print(union)
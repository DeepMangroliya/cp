# can be done with the set but ratehr use 2 pointer approach to get the tc = O(N). and Space Complexity = O(1)
def unique_element(a):
    i = 0
    n = len(a)
    for j in range(1, n):
        if a[j] != a[i]:
            a[i+1] = a[j]
            i+=1
    return i+1
a = list(map(int, input().split()))
size = unique_element(a)
print(a[:size])
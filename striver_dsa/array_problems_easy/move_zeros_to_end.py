# Brute Force
# time complexity O(n) + O(x) + O(n-x) x being non zero elements
# space compxity O(x), O(n) in worst case
def brute_move_zeros(a):
    n = len(a)
    temp = []
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])
    
    temp_n = len(temp)    
    for i in range(temp_n):
        a[i] = temp[i]

    
    for i in range(temp_n, n):
        a[i] = 0


        
a = list(map(int, input().split()))
brute_move_zeros(a)
print(a)
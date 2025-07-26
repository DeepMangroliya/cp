# Brute Force
# time complexity O(n) + O(x) + O(n-x) x being non zero elements = O(2n)
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

def optimal_move_zeroes(a):
    # time complexity O(n)
    # space complexity O(1)
    n = len(a)
    i = 0
    for j in range(1, n):
        if a[j] != 0 and a[i] == 0:
            a[j], a[i] = a[i], a[j]
            i+=1
        elif a[i] != 0:
            i+=1

a = list(map(int, input().split()))
# brute_move_zeros(a)
optimal_move_zeroes(a)
print(a)
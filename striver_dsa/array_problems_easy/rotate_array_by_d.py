def reverse(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start+=1
        end-=1

def rotate(a, d, n):
    # better O(n+d) is the time complexity and O(d) is the space complexity
    # temp = [ ]
    # for i in range(0, d):
    #     temp.append(a[i])
    
    # for i in range(d, n):
    #     a[i-d] = a[i]
    
    # for i in range(n-d, n):
    #     a[i] = temp[i - (n - d)]
    
    # brute O(n*d) is the time complexity and O(d) is the space complexity stack space
    # return a
    # if d == 0 or n <= 1:
    #     return
    # temp = a[0]
    # for i in range(1, n):
    #     a[i - 1] = a[i]
    # a[n - 1] = temp
    # rotate(a, d - 1, n)
    # return a
    
    # optimal in both manner i.e. time and space
    # this makes the time complexity to O(2n) nad space to O(1)
    # [1,2,3,4,5]
    # if d places i.e. 2
    # reverse till d place [2,1]
    # reverse from d to n place [5,4,3]
    # combine and reverse [3,4,5,1,2]

    reverse(a, 0, d - 1)
    reverse(a, d, n - 1)
    reverse(a, 0, n - 1)
    return a

a = list(map(int, input().split()))
d = int(input())
n = len(a)
d = d % n
print(d)
rotate(a, d, n)

print(a)


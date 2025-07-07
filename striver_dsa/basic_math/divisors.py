import math

n=int(input())

ls = []

for i in range(1,int(math.isqrt(n))+1):
    if n % i == 0:
        ls.append(i)
        if n//i != i:
            ls.append(n//i)
    
ls.sort()
for item in ls:
    print(item, end=' ')

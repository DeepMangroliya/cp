a = list(map(int, input().split()))
n = max(a)
# b=[]
# for i in range(0, max(a)):
#    if i in a:
#        continue
#    else:
#        b.append(i)

# print(b)

total_n = (n*(n+1))//2

total_a = sum(a)

print(total_n)
print(total_a)

print(total_n - total_a)

# or better use xor because that will never have a integer above 10^5 but with sum as it is int, 
# it can give out of range problem becuase of the limit of storage to 10^6 of int inside funcitons and 10^7 globally 
# in cpp and java though, not a problem in python
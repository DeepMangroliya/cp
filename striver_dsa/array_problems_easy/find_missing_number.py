a = list(map(int, input().split()))
b=[]
for i in range(0, max(a)):
   if i in a:
       continue
   else:
       b.append(i)

print(b)
import math

a=int(input())
b=int(input())

while(a>0 and b>0):
    if(a>b):
        a = a%b
    else:
        b = b%a

[print(b) if a==0 else print(a)]

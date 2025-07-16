import math # cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    grades = list(map(int, input().split()))
    total=0
    scholarship_lost = False
    for i in range(n):
        total+=grades[i]
        avg = total / (i + 1)
        if avg<40:
            scholarship_lost=True
            break
    
    print("No" if scholarship_lost else "Yes")
            
    
    
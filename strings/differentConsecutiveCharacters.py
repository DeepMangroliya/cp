# cook your dish here
T = int(input())

while T>0:
    n = int(input())
    s = input()
    operation=0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            operation+=1
        else:
            continue
    print(operation)
    T-=1
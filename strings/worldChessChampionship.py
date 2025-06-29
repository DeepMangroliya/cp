# cook your dish here
T = int(input())

while (T>0):
    #taking inputs
    x = int(input())
    results = input()
    
    #couting wins
    c = results.count('C')
    n = results.count('N')
    d = results.count('D')
    
    if c>n:
        prize = x*60
    elif c<n:
        prize = x*40
    else:
        prize = x*55
    print(prize)
    T-=1
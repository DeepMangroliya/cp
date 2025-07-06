# cook your dish here
t = int(input())

while(t):
    n = int(input())
    count_even, count_odd = 0,0
    
    for i in range(1,n+1):
        if n%i==0:
            if i==1 or i%2!=0:
                count_odd+=1
            else:
                count_even+=1
        else:
            continue
    print(f"{count_odd} {count_even}")
    t-=1
    
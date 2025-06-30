# cook your dish here
t = int(input())

while(t>0):
    carry=1
    n=input()
    n_list = list(n)
    i = len(n) - 1
    while i>=0 and carry==1:
        new_digit = int(n_list[i]) + carry
        if new_digit==10:
            n_list[i]='0'
            carry=1
        else:
            n_list[i] = str(new_digit)
            carry=0
        i-=1
    if carry:
        n_list.insert(0, str(carry))
    print(''.join(n_list))
    t-=1
t = int(input())
# aebcdefghij
while t > 0:
    s = input()
    # Your code goes here
    vowels=['a','e','i','o','u']
    flag=0
    for i in range(1, len(s)-2):
        if (s[i-1] in vowels and s[i] in vowels and s[i+1] in vowels):
            flag=1
            break
        else:
            continue

    if flag:
        print('Happy')
    else:
        print('Sad')
    
    t -= 1

t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    server='A'
    score_a, score_b=0, 0
    for winner in s:
        if server==winner:
            if server=='A':
                score_a+=1
            else:
                score_b+=1
        else:
            server=winner
    print(f"{score_a} {score_b}")
    t -= 1

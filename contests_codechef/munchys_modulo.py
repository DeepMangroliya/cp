def solve_munchys_modulo():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []

    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N

        max_mod = 0
        for j in range(N):
            for k in range(j+1, N):
                div1 = A[j] + A[k]

                for i in range(N):
                    if i != j and i != k:
                        max_mod = max(max_mod, A[i] % div1)
        
        results.append(str(max_mod))
    
    print("\n".join(results))

solve_munchys_modulo()

def sum_it(i):
    if i<1:
        return 0
    return i+sum_it(i-1)

def main():
    n = int(input())
    ans = sum_it(n)
    print(ans)
    
if __name__ == "__main__":
    main()
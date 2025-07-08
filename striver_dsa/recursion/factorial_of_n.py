def multiply_it(i):
    if i==1:
        return 1
    return i*multiply_it(i-1)

def main():
    n = int(input())
    ans = multiply_it(n)
    print(ans)
    
if __name__ == "__main__":
    main()
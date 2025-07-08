def print_it(i,n):
    if i>n:
        return
    print_it(i+1,n)
    print(i)

def main():
    n = int(input())
    print_it(1,n)

if __name__ == "__main__":
    main()
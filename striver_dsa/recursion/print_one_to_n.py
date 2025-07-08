def printit(i,n):
    if i<1:
        return
    printit(i-1,n)
    print(i)

def main():
    n = int(input())
    printit(n,n)
    
if __name__ == "__main__":
    main()
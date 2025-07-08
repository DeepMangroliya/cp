def printit(i, n):
    if i>n:
        return
    printit(i+1,n)
    print(i)

def main():
    n = int(input())
    printit(1, n)
    
if __name__ == "__main__":
    main()
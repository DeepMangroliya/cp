def printit(i, name):
    if i==1:
        return
    printit(i-1,name)
    print(name)

def main():
    n = int(input())
    name = input()
    printit(n, name)
    
if __name__ == "__main__":
    main()
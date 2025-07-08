def fibonnaci(n) -> int:
    if n<=1:
        return n
    return fibonnaci(n-1)+fibonnaci(n-2)
   
        

def main():
    n = int(input())
    print(fibonnaci(n))
    
if __name__ == "__main__":
    main()
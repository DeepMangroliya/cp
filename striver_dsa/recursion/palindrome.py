def palindrome(left, string, n) -> bool:
    if left > n/2:
        return True
    else:
        if string[left] != string[n-left-1]:
            return False
        else:
            return palindrome(left+1,string,n)
        

def main():
    string = input()
    ans = palindrome(0,string,len(string))
    if ans:
        print('Palindrome')
    else:
        print('Not Palindrome')
    
if __name__ == "__main__":
    main()
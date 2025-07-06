class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        temp=x
        while x > 0:
            last = x%10
            x//=10
            reverse = reverse * 10 + last
        return rev erse == temp
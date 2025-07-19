class Solution:
    def is_prime(self, x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int((x**0.5)) + 1):
            if x % i == 0:
                return False
        return True
        

    def splitArray(self, nums: List[int]) -> int:
        sumA, sumB = 0, 0
        for i, val in enumerate(nums):
            if self.is_prime(i):
                sumA += val
            else:
                sumB += val
        ans = sumA-sumB
        if ans>0:
            return ans
        else:
            return ans*-1
            
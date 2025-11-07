class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []
        n = len(nums)
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        threshold = n//3

        for idx, value in hashmap.items():
            if  value > threshold:
                result.append(idx)
        return result
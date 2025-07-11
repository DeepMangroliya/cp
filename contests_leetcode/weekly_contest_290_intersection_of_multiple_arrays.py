class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashmap = {}
        for item in nums:
            for i in item:
                if i in hashmap: 
                    value = hashmap[i]
                    value += 1
                    hashmap[i] = value
                else:
                    hashmap[i] = 1
        final_outcome = []

        for item in hashmap:
            if hashmap[item] == len(nums):
                final_outcome.append(item)
        final_outcome.sort()
        return final_outcome
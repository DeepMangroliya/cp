class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # from collections import Counter
        output = []
        if not words:
            return []

        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)
        
        # for key, freq in common.items():
        #     output.extend([key] * freq)
        # return output
        return list(common.elements())
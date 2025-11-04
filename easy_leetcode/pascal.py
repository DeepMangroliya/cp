class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pascal = [[1]] 
        for _ in range(n - 1):
            row = [1]
            prev = pascal[-1]
            for i in range(len(prev)-1):
                row.append((prev[i] + prev[i+1]))
            row.append(1)
            pascal.append(row)
        return pascal
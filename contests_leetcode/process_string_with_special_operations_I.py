class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in range(0,len(s)):
            if s[i].islower():
                result.append(s[i])
            elif s[i] == '*' and result:
                result.pop()
            elif s[i] == '#':
                result+=result.copy()
            else:
                result.reverse()
        return ''.join(result)
#we will take advantage of the fact that everyhting on the right has to be smaller for a particular number to be the leader in the array.
# Space Complexity O(N) and Time Compplexity is mentioned above.

import sys
arr = list(map(int, input().split()))
maxi = -sys.maxsize - 1
ans = []
# O(N)
for i in range(len(arr)-1,0,-1):
    if arr[i] > maxi:
        maxi = arr[i]
        ans.append(maxi)
# O(N*logN)
ans.sort()
print(ans)
    
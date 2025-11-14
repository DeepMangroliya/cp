import sys
nums = list(map(int,input().split()))
count1 = 0
count2 = 0
ele1 = -sys.maxsize
ele2 = -sys.maxsize
for i in range(len(nums)):
    if count1 == 0 and nums[i] != ele2:
        ele1 = nums[i]
        count1 += 1
    elif count2 == 0 and nums[i] != ele1:
        ele2 = nums[i]
        count2 += 1
    elif nums[i] == ele1:
        count1 += 1 
    elif nums[i] == ele2:
        count2 += 1
    else:
        count1 -= 1
        count2 -= 1

count1 = 0
count2 = 0
ans = []
mini = len(nums)//3
for i in range(len(nums)):
    if nums[i] == ele1:
        count1 += 1
    if nums[i] == ele2:
        count2 += 1
if count1 > mini:
    ans.append(ele1)
if count2 > mini:
    ans.append(ele2)
print(ans)
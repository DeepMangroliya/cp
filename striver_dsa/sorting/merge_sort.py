def merge(a, low, mid, high):
    left = low
    right = mid+1
    temp=[]
    while(left <= mid and right <= high):
        if a[left]<a[right]:
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            right += 1
    
    while(left<=mid):
        temp.append(a[left])
        left += 1
    
    while(right<=high):
        temp.append(a[right])
        right += 1
    
    for i in range(len(temp)):
        a[i+low] = temp[i]
   
    return a
 
def merge_sort(a, low, high):
    mid = (low+high)//2
    if low>=high:
        return
    merge_sort(a, low, mid)
    merge_sort(a, mid+1, high)
    ans = merge(a, low, mid, high)
    return ans
    
a = list(map(int, input().split()))
ans = merge_sort(a, 0, len(a)-1)
print(ans)
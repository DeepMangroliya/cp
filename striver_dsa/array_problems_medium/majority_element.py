#Moore's voting algorithm [Optimal] -> O(N) + O(N)
# Non need to verify if the question says alaways has a majority element Tc-> O(n)
# SC->O(1)
arr = list(map(int, input().split()))

count = 0
element = None
verify = 0

for i in range(len(arr)):
    if count == 0:
        count = 1
        element = arr[i]
    elif arr[i] == element:
        count += 1
    else:
        count -= 1

for i in range(len(arr)):
    if arr[i] == element:
        verify += 1
    
if verify > len(arr) // 2:
    print(f"Majority element is: {element}")
else:
    print("No majority element")'


#Other approach is hasmap ofc, it will have O(NlogN) + O(N) if ordered map, if unordered O(N2) + O(N)  in worst and O(N) + O(N) in best and average case.
    
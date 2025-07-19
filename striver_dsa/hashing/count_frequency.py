query = list(map(int, input().split()))
hashmap = {}
for element in query:
    if element in hashmap:
        hashmap[element] +=1
    else:
        hashmap[element] = 1
for element in hashmap:
    print(f"Element: {element} occured {hashmap[element]} times")


# Alternatively

# def countFreq(arr, n):
#     visited = [False] * n
#     for i in range(n):
#         if (visited[i] == True):
#             continue
#         count = 1
#         for j in range(i + 1, n):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)


# if __name__ == "__main__":
#     arr = [10,5,10,15,10,5]
#     n = len(arr)
#     countFreq(arr, n)
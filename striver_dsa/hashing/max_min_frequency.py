query = list(map(int, input().split()))
hashmap = {}
for element in query:
    if element in hashmap:
        hashmap[element] +=1
    else:
        hashmap[element] = 1
        
n = len(query)
    
maxele, maxelekey = 0,0
minele, minelekey = n,n
for element in hashmap:
    if hashmap[element] < minele:
        minele = hashmap[element]
        minelekey = element
    elif hashmap[element] > maxele:
        maxele = hashmap[element]
        maxelekey = element

print(f'Highest Freq. element is:{maxelekey}')
print(f'Lowest Freq. element is:{minelekey}')


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
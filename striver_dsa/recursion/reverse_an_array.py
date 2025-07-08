# def swap(left, right, array):
#     if right<left:
#         return
#     temp = array[left]
#     array[left] = array[right]
#     array[right] = temp
#     swap(left+1, right-1, array)
#     return array
    
# def main():
#     array = list(map(int, input().split()))
#     for item in array:
#         print(item)
#     swap(0, len(array)-1, array)
#     print("---------------------")
#     for item in array:
#         print(item)
    
#     # ans = swap(n)
#     # print(ans)
    
# if __name__ == "__main__":
#     main()

def swap(i, array):
    n = len(array)
    if i>n/2:
        return
    array[i], array[n-i-1] = array[n-i-1], array[i]
    swap(i+1, array)
    return array
    
def main():
    array = list(map(int, input().split()))
    for item in array:
        print(item)
    swap(0, array)
    print("---------------------")
    for item in array:
        print(item)
    
    # ans = swap(n)
    # print(ans)
    
if __name__ == "__main__":
    main()
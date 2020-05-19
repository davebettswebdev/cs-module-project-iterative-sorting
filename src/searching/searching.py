def linear_search(arr, target):
    
    for i, val in enumerate(arr):
        if val == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # find total size of arry
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) //2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1

    # we didn't find the element

    return -1  # not found

# binary search algorithm implementation

def binary_search(arr, target):
    sorted_arr = sorted(arr)
    left = 0
    right = len(sorted_arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example usage:
# arr = [4, 2, 7, 1, 3]
# target = 3
# result = binary_search(arr, target)
# print(result) 
# # Output: index of target in sorted array or -1 if not found
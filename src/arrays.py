def merge_sort(arr):
    if len(arr) <= 1: # If the array has zero or one element, it is already sorted
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid]) # O(log n)
    right_half = merge_sort(arr[mid:]) # O(log n)

    return merge(left_half, right_half) # Merge the two sorted halves O(n log n)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right): # O(n)
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    while left_index < len(left): # O(n)
        sorted_list.append(left[left_index])
        left_index += 1

    while right_index < len(right): # O(n)
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list



array = [38, 27, 43, 3, 9, 82, 10]

print("Before: ", array)
array_result = merge_sort(array)
print("After: ", array_result)

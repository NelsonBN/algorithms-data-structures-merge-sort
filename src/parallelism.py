import concurrent.futures

def merge_sort(arr):
    if len(arr) <= 1: # If the array has zero or one element, it is already sorted
        return arr

    mid = len(arr) // 2

    # Use parallel execution for sorting both halves
    with concurrent.futures.ThreadPoolExecutor() as executor:
        left_sorted = executor.submit(merge_sort, arr[:mid])
        right_sorted = executor.submit(merge_sort, arr[mid:])

        left_half = left_sorted.result()
        right_half = right_sorted.result()

    return merge(left_half, right_half)


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

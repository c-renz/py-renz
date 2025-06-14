B = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, -52321412]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # pivot is always the number at the very end of the array

    left = [x for x in arr[:-1] if x <= pivot]
    # everything on the left array is less than the pivot, it will traverse also to all values except the pivot(arr[:-1])
    right = [x for x in arr[:-1] if x > pivot]
    # everything on the right array is less than the pivot, it will traverse also to all values except the pivot(arr[:-1])

    left = quick_sort(left)
    # recursion, it means we always trigger the left and perform the sorting
    right = quick_sort(right)
    # recursion, it means we always trigger the right and perform the sorting
    return left + [pivot] + right  # Last step, concatenation of all array


print(quick_sort(B))

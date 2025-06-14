B = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, -52321412]


def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    m = n // 2
    left = arr[:m]  # :m means from start up until before m, excludes m
    right = arr[m:]  # from m to the end of the array

    left = merge_sort(left)  # <- recursion
    right = merge_sort(right)  # <- recursion
    l, r = 0, 0
    L_len = len(left)
    R_len = len(right)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if left[l] < right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r += 1
        i += 1
    while l < L_len:
        sorted_arr[i] = left[l]
        l += 1
        i += 1
    while r < R_len:
        sorted_arr[i] = right[r]
        r += 1
        i += 1
    return sorted_arr


print(merge_sort(B))

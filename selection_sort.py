# Selection Sort

B = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, -52321412]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selection_sort(B))

#  j traverse from after i until the last value, and every time its lower than the its lower than the current index,
# it will switch till got the lowest then i move forward and repeats the process

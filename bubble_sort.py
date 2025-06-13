# Bubble Sort, Time: O(n^2), space: O(1)

B = [2, 3, 4, 5, 22, 34234, 523]


def bubble_sort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            prev = i - 1  # meaning of getting the previous index from i index

            if arr[prev] < arr[i]:
                flag = True
                arr[i], arr[prev] = arr[prev], arr[i]
    return arr


print(bubble_sort(B))

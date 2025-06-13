# Insertion Sort, Time: O(n^2), Space: O(1)

B = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, 523]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            prev = j - 1
            if arr[prev] > arr[j]:
                arr[prev], arr[j] = arr[j], arr[prev]
            else:
                break
    return arr


print(insertion_sort(B))

# j traverse back to seccure all the previous values are sorted before i move forward in the array

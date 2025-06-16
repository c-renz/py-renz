A = [1, 2, 1, 4, 33, 21, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 4, 4]


def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)
    for x in arr:  # This part counts the number of frequency from 0 to max value
        counts[x] += 1  # for example how many 4 or 2, it counts the frequency
    i = 0  # initialization

    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            # ^ This insert the value on the counts[c] into the index in the arr
            i += 1
            # ^ This moves forward the i for it to insert another value in the next index on arr
            counts[c] -= 1
            # ^ This reduces the counts of the frequency recorded in the counts[]
    return arr


print(counting_sort(A))

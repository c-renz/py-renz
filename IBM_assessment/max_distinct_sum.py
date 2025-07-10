def max_distinct_split_sum(arr):
    n = len(arr)
    left_set = set()
    right_counter = {}

    # Initialize right part counter
    for num in arr:
        right_counter[num] = right_counter.get(num, 0) + 1

    max_sum = 0
    left_set = set()

    for i in range(n - 1):  # We must leave at least one element in the right subarray
        num = arr[i]
        left_set.add(num)

        right_counter[num] -= 1
        if right_counter[num] == 0:
            del right_counter[num]

        current_sum = len(left_set) + len(right_counter)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_distinct_split_sum([1, 3, 1, 2, 1]))

# Build Min Heap
# NOTE: Peeking Min Heap is O(1), having like an array A[0]
A = [0, -4, 1, 2, 3, 5, 10, 8, 12, 9]

import heapq

heapq.heapify(A)

print(A)

# Insert: heappush
heapq.heappush(A, 21)
print(A)

# Heap Pop

print(A, heapq.heappop(A))

# Heap Sort


def heapsort(arr):
    heapq.heapify(arr)
    new_list = []
    while arr:
        minn = heapq.heappop(arr)  # get the pop value
        # print("Pop value: ", minn)
        new_list.append(minn)
    return new_list


print(heapsort([0, -4, 1, 2, 3, 5, 10, 8, 12, 9, 5, 3213, 12, 3, 232, 213, 15155]))

# Heap Push Pop, inserting at the very and then popping the root

heapq.heappushpop(A, 9)
print(A)


B = [0, -4, 1, 2, 3, 5, 10, 8, 12, 9]

n = len(B)

for i in range(n):
    B[i] = -B[i]
heapq.heapify(B)
print("After Heapify: ", B)
print("Max Heap ", -heapq.heappop(B))

C = [0, -4, 1, 2, 3, 5, 10, 8, 12, 9]


def maxheap(arr):

    n = len(arr)
    for i in range(n):
        arr[i] = -arr[i]
    heapq.heapify(arr)
    print("After Heapify: ", arr)
    return "Max Heap", -heapq.heappop(arr)


print(maxheap(C))
# heapq.heappush(C, -7)

# print(maxheap(C))

# Build Heap from scratch

D = [0, -4, 1, 2, 3, 5, 10, 8, 12, 9]

heap = []

for x in D:
    heapq.heappush(heap, x)
    print(heap)

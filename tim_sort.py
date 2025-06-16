# In place (constant space)
B = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, -52321412]

B.sort()
print(B)


# Get new sorted array -  O(n)
C = [-34234, 2, 3, -4, 5, 5, 3, -22, 2, 5, 4, 5, 4, -52321412, 2312, 312312, 3]

sorted_B = sorted(C)
print(sorted_B)
# or
print(sorted(C))


# Sort an arrat of tuples

I = [
    (-5, 3),
    (-9, 4),
    (5, 6),
    (1, 2),
    (0, -3),
]  # commonly arise on the problems called intervals
sorted_I = sorted(I, key=lambda t: t[0])  # t[0] is always between 0 or 1

print(sorted_I)

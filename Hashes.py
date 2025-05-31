# SETS ====================================================================
# s = set()

# s.add(2)
# s.add(4)
# s.add(6)

# print(s)

# Lookup any values on the sets
# print(7 in s)

# s.remove(6 if 4 in s else 2) #// -> O(1)
# print(s)

# Set construction from string - O(S) - S is the length of the string
# string = "aaaaaaabbbcccddddddddeeeeeee111111111111111111"
# sett = set(string)  # The order here depends on the has values
# print(sett)
# for x in sett:
#     print(x)

# Hashmaps/Dictionaries
d = {"first": 1}  # initialization of key:val dictionaries/hashmaps
d["second"] = 2  # O(1)
d["third"] = 3
print(
    "yes third is here and has value of ",
    d["third"] if "third" in d else "Third is not here",
)

# Loop over the key:val pairs of the dictionary ->  O(n)
for (
    key,
    val,
) in (
    d.items()
):  # this sets that the key is one calling the first part of the dictionary which is the key, then the val is the one for second input which is the value
    # // naming convention is up to you
    print(f"'{key}' is the KEY with the value of '{val}'")

# Defaultdict
from collections import defaultdict

defa = defaultdict(int)

print(defa[3])


# one of the uses is for grouping data like below
# from collections import defaultdict

# students = [('Math', 'Alice'), ('Math', 'Bob'), ('Physics', 'Alice')]

# grouped = defaultdict(list)

# for subject, student in students:
#     grouped[subject].append(student)

# print(grouped)

# Counter can be used in some interviews on getting the most character present

from collections import Counter

user = input("Enter any 1 word string: ")

count = Counter(user)
print(
    "SHORTCUT: The highest frequency: " + max(count, key=count.get) if user else 000
)  # for shortcut
if user:
    highest_frequency = max(count, key=count.get)
    print("The highest frequency: ", highest_frequency)
else:
    print("There is nothing to process")

print(
    f"SHORTCUT: The highest frequency with key:val: {max(count.items(), key=lambda x: x[1])}"
    if user
    else 00
)  # for shortcut
if user:
    highest_freq_with_key = max(count.items(), key=lambda x: x[1])
    print("The highest frequency with key:val: ", highest_freq_with_key)
else:
    print(0)

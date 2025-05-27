# Singly Linked lists ====================================================================================


# class SinglyNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)


# Headd, aa, bb ,cc is just an andress, can be name anything
# Headd = SinglyNode(0)
# aa = SinglyNode(9)
# bb = SinglyNode(54)
# cc = SinglyNode(34)

# Headd.next = aa
# aa.next = bb
# bb.next = cc

# print("This is for simple printing of part of the linked list: ", Headd, "\n")

# Traverse the list - O(n)
# curr = Headd

# while curr:
#     print(curr)
#     curr = curr.next


# Get all values into list
# curr = Headd
# links = []
# while curr:
#     links.append(curr.val) // we use val to get the value itself, use curr if address only
#     curr = curr.next
# print(links)


# Other way to make it look like a linked lists
# def show(head):
#     curr = head
#     links = []
#     while curr:
#         links.append(str(curr.val))
#         curr = curr.next
#     print(" -> ".join(links))


# show(Headd)

# Search for a value // O(n), O(1) if the head


# def search(head, valu):
#     current = head
#     while current:
#         if valu == current.val:
#             print(
#                 True
#             )  # supposed to be return but not printing in this case so we used print
#         current = current.next
#     print(False)  # supposed to be return but not printing in this case so we used print


# search(Headd, 9) # Your choice but in this case is 9, True

######## TO TRY: GET THE NUMBERS ON THE LISTS THAT IS MULTIPLES OF 2 AND MAKE IT INTO LINKED LISTS

# Doubly Linked Lists ===================================================================================
# class DoublyNode:
#     def __init__(self, val, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

#     def __str__(self):
#         return str(self.val)


# Head = DoublyNode(00)
# A = DoublyNode(11)
# B = DoublyNode(22)
# C = DoublyNode(33)
# D = DoublyNode(44)

# Head.next = A
# A.next = B
# B.next = C
# C.next = D
# D.prev = C
# C.prev = B
# B.prev = A
# A.prev = Head

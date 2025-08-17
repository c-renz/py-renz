# # EASY
# class Solution:
#     def reverse(self, x: int) -> str:
#         i = 1
#         print("Output:")
#         while i <= x:
#             print(" " * (x - i) + "*" * i)
#             i += 1


# sol = Solution()
# sol.reverse(int(input("Input: ")))

# # gpt advised
# class Solution:
#     def rightAlignedTriangle(self, n: int) -> str:
#         rows = []
#         for i in range(1, n + 1):
#             rows.append(" " * (n - i) + "*" * i)
#         return "\n".join(rows)


# # Example usage
# sol = Solution()
# n = int(input("Input: "))
# print("Output:\n" + sol.rightAlignedTriangle(n))


# simple pyramid
class Solution:
    def pyr(self, x: int) -> str:
        start = 1
        for rows in range(1, x + 1):
            # this means (start, finish(but not include the end like in 4+1, hanggang 4 lang meaning))
            for cols in range(rows):
                print(start, end=" ")
                start += 1
            print()


sol = Solution()
print(sol.pyr(4))

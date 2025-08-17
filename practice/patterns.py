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


# simple number pyramid - medium
# class Solution:
#     def pyr(self, x: int) -> str:
#         start = 1
#         spaces = x
#         for rows in range(1, x + 1):
#             # this means (start, finish(but not include the end like in 4+1, hanggang 4 lang meaning))
#             print(" " * spaces, end="")
#             for cols in range(rows):
#                 print(start, end=" ")
#                 start += 1
#                 # spaces -= 1
#             print()
#             spaces -= 1


# sol = Solution()
# print(sol.pyr(4))


# HARD
# max path sum
class Solution:
    def maxpath(self, matrix: list) -> int:
        stripped = matrix.strip().splitlines()  # <- dito nagstrip pa lang
        # print(stripped)
        pyramid = [list(map(int, row.split())) for row in stripped]
        sum = 0
        # print(pyramid)
        # print(max(pyramid[0]))
        for x in range(0, len(pyramid)):
            # print(pyramid[x])
            sum += max(pyramid[x])
        return sum
        # print(sum)


sol = Solution()
data = """1 0 0
2 3 0
4 5 6"""

print(sol.maxpath(data))


class Test:
    def test(self, x: list) -> int:
        st = x.strip().splitlines()
        p = [list(map(int, r.split())) for r in st]
        sum = 0
        for i in range(0, len(p)):
            sum += max(p[i])
        print(sum)


dataa = """1 0 0
2 3 0
4 5 6
7 8 9"""


tes = Test()
tes.test(dataa)

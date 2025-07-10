# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         for x in range(n):
#             nums[x] = nums[x] * nums[x]
#         return sorted(nums)


# sol = Solution()
# print(sol.sortedSquares([-7, -3, 2, 3, 11]))


# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         for x in range(n):
#             nums[x] = nums[x] * nums[x]
#         left, right = 0, n - 1
#         result = [nums[right]]

#         while left < right:
#             if nums[left] < nums[right]:
#                 result.append(nums[right])
#                 right -= 1
#             elif nums[left] > nums[right]:
#                 result.append(nums[left])
#                 left += 1
#             else:
#                 result.append(nums[right])
#                 result.append(nums[left])
#                 right -= 1
#                 left += 1
#         return sorted(nums)


# sol = Solution()
# print(sol.sortedSquares([-7, -3, 2, 3, 11]))


# FASTER APPROACH

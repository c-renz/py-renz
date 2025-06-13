class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        indx = 0
        while left <= right:
            # mid = left + (right - left) // 2  ====> USED WHEN THERE IS A CHANCE TO OVERFLOW THE CONVENTIONAL WAY
            mid = (left + right) // 2
            if nums[mid] == target:
                # print(nums[mid])
                print(
                    f"Ohh! the nums = {nums}, where the target = {target} does exists in index {mid}! WOW!"
                )
                return mid
            elif nums[mid] > target:
                print(
                    f"hmmm.... it seems like the midpoint value {nums[mid]} is greater than the target {target} so we are crossing out the right side from index {mid}"
                )
                right = mid - 1
            else:
                print(
                    f"hmmm.... it seems like the midpoint value {nums[mid]} is less than the target {target} so we are crossing out the left side from index {mid}"
                )
                left = mid + 1
        return -1


sol = Solution()
print(sol.search([0, 6, 12, 33, 54, 67, 75, 87, 98], 67))


# Condition Based
# [F,F,F,T,T,T]

B = [False, False, True, True]  # NOTE: it should be fffttt no tft ftf
# B = [True, True, False, False]


def binary_condition(arr):
    L, R = 0, len(arr) - 1
    while L < R:
        M = L + (R - L) // 2
        if B[M]:  # NOTE: use not if searching for first false  like in tttffff
            R = M
        else:
            L = M + 1
    return L


print(binary_condition(B))

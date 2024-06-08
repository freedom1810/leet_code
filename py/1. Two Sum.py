# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res_i = -1
#         res_j = -1
#         for i, num in enumerate(nums):
#             for j, num2 in enumerate(nums[i+1:]):
#                 temp_sum = num + num2
#                 if temp_sum == target:
#                     res_i= i
#                     res_j = i + 1 + j
#                     break
#         res = [res_i, res_j]
#         return res

#O(nlogn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        i = 0
        j = len(nums_sorted) - 1
        while(nums_sorted[i] + nums_sorted[j] != target):
            
            if nums_sorted[i] + nums_sorted[j] < target:
                i += 1
            else:
                j -= 1
        
        res_i_value = nums_sorted[i]
        res_j_value = nums_sorted[j]
        res_i = -1
        res_j = -1
        for i in range(len(nums)):
            if res_i == -1 and res_i_value == nums[i]:
                res_i = i
            elif res_j_value == nums[i]:
                res_j = i
        res = [res_i, res_j]
        return res
class Solution:
    def findMedianSortedArrays(
        self, 
        # nums1: List[int], 
        # nums2: List[int]
        nums1,
        nums2
        ) -> float:
        i_nums1 = 0
        i_nums2 = 0
        i_res = (len(nums1) + len(nums2))

        
        num_all = []
        while i_nums1 != len(nums1) or i_nums2 != len(nums2):
            
            if i_nums1 == len(nums1):
                num_all = num_all + nums2[i_nums2:]
                break
            
            if i_nums2 == len(nums2):
                num_all = num_all + nums1[i_nums1:]
                break
            
            if nums1[i_nums1] < nums2[i_nums2]:
                num_all.append(nums1[i_nums1])
                i_nums1 += 1
            else:
                num_all.append(nums2[i_nums2])
                i_nums2 += 1
                
                
        if i_res % 2 == 0:
            i_res //=2
            res = (num_all[i_res] + num_all[i_res-1])/2
        else:
            i_res //=2
            res = num_all[i_res]
        return res
    
    
# nums1 =[1,3]
# nums2 = [2]

# nums1 =[1,3]
# nums2 = [2,4]


nums1 =[]
nums2 = [2,3]

sol  = Solution()
res = sol.findMedianSortedArrays(nums1, nums2)
print(res)
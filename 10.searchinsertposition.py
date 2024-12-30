class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        l,r = 0,len(nums) - 1

        while l <= r:
            mid = (l+r) // 2 

            if target == nums[mid]: #luckily what if we get value at mid
                return mid
            if target > nums[mid]:
                l = mid + 1
            else :
                r = mid - 1
        return l
    
nums = [1,2,3,4,6]
target = 5
result = Solution.searchInsert(nums,target)
print(result)


# we can 0(n) , we can do better since its sorted array , logn 
# using standard algorithm , Binary search . not gonna search nin every index of valye 
# left pointer , right pointer , middle pointer /
# l+r/2 = middle pointer .-> o(logn) > o(n).
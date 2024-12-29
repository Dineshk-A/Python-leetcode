class Solution:
    def remove( nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
nums = [0,1,2,2,3,0,4,2]
val = 2
result = Solution.remove(nums,val)
print(result)

# overwriting elements that are not equal to val to the front of the list.
# New length: The final length of the list, without the elements equal to val, is k.
# This technique is often used to modify lists in place, removing elements that match a certain value, and returning the new length of the list.
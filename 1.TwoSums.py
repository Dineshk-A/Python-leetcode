class Solution:
    def two_sums(nums: list[int],target: int) -> list[int]:
        result = []
        index_map = {}

        for i , n in enumerate(nums):
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
            
        return result
    
nums = [2,7,3,11]
target = 9

res = Solution.two_sums(nums,target)
print(res)

#enumerate and explain logic 


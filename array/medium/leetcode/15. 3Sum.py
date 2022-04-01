"""
First Approach: Two Pointer Approach
Time Complexity O(n*n), Space Complexity O(n)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []
        ans = []
        nums = sorted(nums)
        print(sorted(nums))
        self.twoSum(nums, 0, ans)
        for i in range(1, len(nums)-2):
            self.twoSum(nums, i, ans)
            
        return ans 
            
    def twoSum(self, nums, i, ans):
        target = 0-nums[i]
        
        start = i+1
        end   = len(nums)-1
        
        while (start < end):
            total = nums[start]+nums[end]
            #print(nums[start])
            #print(nums[end])
            if(total == target):
                val = [nums[i], nums[start], nums[end]]
                if (val not in ans):
                    ans.append(val)
                start +=1
                end -=1
                    
            elif(total< target):
                start += 1
                
            else:
                end -=1
            
            
            
            
            
            
            
        

"""
https://leetcode.com/problems/product-of-array-except-self/
"""

"""
First Solution: Time Complexity (O(n)), Space Complexity (O(n))
ဘယ်ကနေ မြှောက်လာတဲ့ တန်ဖိုးကို ရှာတယ်။
ညာကနေ မြှောက်လာတဲ့ တန်ဖိုးကို ရှာတယ်။

E.g.
Input: [1, 2, 3]
left = [1, 2, 6]
right = [6 , 6, 3]

index 1 ရဲ့တန်ဖိုး left[0(index-1)]*right[2(index+1)] = 1*3

 Note: 0 နဲ့ ပတ်သတ်ပြီး လည်သွားသေးတယ်။
"""

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if (len(nums)<2):
            return [nums[0]]
        
        ans = []
        prev = 1
        for i in range(len(nums)):
            ans.append(prev*nums[i])
            prev *= nums[i]
        print(ans)   
        reverse_ans = [0]*len(nums)
       
           
        i = len(nums)-1
        prev = 1
        while (i>=0):
            reverse_ans[i] =  prev*nums[i]
            prev *= nums[i]
            i -= 1
        print(reverse_ans) 
        product = []
        for i in range (len(nums)):
            if (i == 0):
                product.append(reverse_ans[i+1])
            elif(i == len(nums)-1):
                product.append(ans[-2])
            else:
                product.append(ans[i-1]*reverse_ans[i+1])
               
           
        return product

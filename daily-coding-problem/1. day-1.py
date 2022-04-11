Easy

'''Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

Solution:

'''
ဒီ problem က leet code မှာ ဖြေရှင်းနေကျ Two-Sum problem ပါ။
Sorting စီထားရင် Two Pointer (Time - O(n), Space - O(1)), Binary Search နဲ့ O(n) log(n) နဲ့ဖြေရှင်းလို့ရတယ်။
ခုမှာတော့ Sorting မစီထားလို့ dictionary approach ကို သုံးခဲ့တယ်။

'''
# Time Complexity O(n), Space Complexity O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {} 
        
        for i in range (len(nums)):
            
            # if target-num is in dic, we got the solution
            if (target - nums[i] in dic):
                return i, dic[target-nums[i]]
            
            # Otherwise we will put the num and index to the dic
            else:
                dic[nums[i]] = i

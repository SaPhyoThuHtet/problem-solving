"""
First Solution: Time Complexity - O(n), Space Complexity - O(1)
Used Regular Expression. But it would be dump solution. So try with Recursion and Dynamic Programming.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    
        p = "^"+p+"$"
        ans = re.search(p,s)
        
        if (ans != None):
                return True
                
        return False

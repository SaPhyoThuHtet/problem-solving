"""
First Solution: Time Complexity O(n), Space Complexity O(n)
"""


string = "abc"
def recursive_reverse_function (string):
    
    if (string == ""):
        return ""
        
    return recursive_reverse_function(string[1:])+string[0]
    
    
print(recursive_reverse_function (string))

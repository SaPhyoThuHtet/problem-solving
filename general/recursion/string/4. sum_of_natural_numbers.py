def sum_of_natural_number(num):
    
    """
    5 => 5+4+3+2+1+0
    """
    
    if (num<=1):
        return num
        
    return num+sum_of_natural_number(num-1)
    
    
    
print(sum_of_natural_number(2))
    

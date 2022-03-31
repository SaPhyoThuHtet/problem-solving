def decimal_to_binary(num):
    
    if (num == 0):
        return 0
        
    return num%2+10*decimal_to_binary(num//2)
    
    
    
print(decimal_to_binary(2))

""""This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid."""

''''Solution: Inplace Phyay Shin Tar, Really Nice Solution
''''
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab" #""
count = 1
start = 0
index = 0

while (index <len(s)-1):
    
    if (s[index] != s[index+1]):
        
        replace_val = str(count)+s[index]
        s = s[0:start]+replace_val+s[index+1:]
        index = start+len(replace_val)
        start = index
        count = 1
        
    else:
        index +=1
        count +=1
        
    
 

# for the last character
if (count == 1):
    s = s[0:start]+"1"+s[-1]
else:
    s = s[0:start]+str(count)+s[-1]

print(start)
print(s[0:start])
print(s)


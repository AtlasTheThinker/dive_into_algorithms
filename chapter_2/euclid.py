def gcd(a,b):
    smallest = min(a,b)
    biggest = max(a,b)
    
    remainder = biggest % smallest
    
    if(remainder == 0):
        return smallest
    else:
        return gcd(smallest, remainder)
        
print(gcd(72,36))
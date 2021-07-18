s = "AAAAA"
from collections import Counter

def alternate(s):
    s = list(s)
    a = ['A','B']
    remove = 0
    ind = a.index(s[0]) ^ 1 
    
    for val in s[1:]: 
        if a[ind] == val : 
            ind = ind ^ 1 
        else: 
            remove+=1
            
    return remove
    
if __name__ == '__main__':
    print(alternate(s))
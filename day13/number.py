

s = "1234"



def check_number(s,l): 
    sub_str = s[:l]
    val = int("".join(sub_str))
    index=l 
    while index < len(s):    
        next_val =  int("".join(s[index:(index+l)]))
        next_val_ =  int("".join(s[index:(index+l+1)]))
        
     #   print(val)
      #  print(next_val)
      #  print(next_val_)
        if (val+1) == next_val and s[index] != '0': 
            index += l 
            val = next_val
        elif (val+1) == next_val_ and s[index] != '0': 
            l += 1
            index += l  
            val = next_val_
        else: 
           return False             
    return True 
    

def seprate_number(s):
    s = list(s)
    for i in range(1,int(len(s)/2)+1): 
        if check_number(s,i):
            return "YES " + "".join(s[:i])
    return "NO"
            
if __name__ == '__main__':
    print(seprate_number("1234"))
    print(seprate_number("91011"))
    print(seprate_number("99100"))
    print(seprate_number("101103"))   
    print(seprate_number("010203"))
    print(seprate_number("1"))
    print(seprate_number("13"))
    
    


value = "aaabccddd"

def reduce(val): 
    if len(val) == 0: 
        return "Empty String"
    else: 
        for index in range(len(val)):
            if (index + 1) < len(val): 
                if val[index] == val[index+1]: 
                    val.pop(index)
                    val.pop(index)
                    return reduce(val)
        return "".join(val)
     
if __name__ == '__main__':
    
    val = list(value)
  #  print(len(val))
    print(reduce(val))
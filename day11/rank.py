s = "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
match= list("hackerrank") 

def rank(s): 
    index = 0 
    
    for _,i in enumerate(s): 
        if i == match[index%len(match)]: 
            index +=1
    
    return "YES" if index >= len(match) else "NO"
    
    
if __name__ == '__main__':
    print(rank(s))
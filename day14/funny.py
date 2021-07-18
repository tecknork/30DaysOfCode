s = 'ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq'

def funny(s): 
    s = list(s)
    
    for i in range(1,len(s)):
    
        start = abs(ord(s[i]) - ord(s[i-1]))
        #print(start)
        end = abs((ord(s[-i]) - ord(s[-i-1])))
       # print(str(start) +" " + str(end))
        if start != end: 
             return "Not Funny"
        
    return "Funny"


if __name__ == '__main__':
    print(funny(s))
    print(funny("holtm"))
    
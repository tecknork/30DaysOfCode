from collections import Counter
alpha = list("abcdefghijklmnopqrstuvwxyz")



def uniform(s,sum_check):
    
    s = list(s)
    count_s = Counter(s)
    sums = {}
    result = []
    #print(count_s)   
    uniform = 1
    for index in range(1,len(s)):
        if s[index] == s[index-1]: 
            uniform +=1 
        else:
            if index == 1: 
                uniform = 1  
                for count in range(uniform): 
                     sums[(alpha.index(s[index-1])+1) * (count+1)] = 1 
            else: 
                uniform = 1 
        for count in range(uniform): 
            
                    sums[(alpha.index(s[index])+1) * (count+1)] = 1 
                    #sums.append((alpha.index(s[index])+1) * (count+1))
       
    
    for sum_che in sum_check:
        result.append("YES") if sum_che in sums else result.append("NO")
            
    return result


if __name__ == '__main__':
    print(uniform("aaabbbbcccddd",[5,9,7,8,12,5]))
    
    
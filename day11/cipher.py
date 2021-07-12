
alpha = list("abcdefghijklmnopqrstuvwxyz")
def cipher(s,k):
    new_s = []
    for i in s: 
        if i.isalpha(): 
            index = alpha.index(i.lower())
            new_s.append(alpha[(index+k)%len(alpha)] if i.islower() else alpha[(index+k)%len(alpha)].upper())
        else:
            new_s.append(i)
    
    return "".join(new_s)            



if __name__ == '__main__':
    s= "middle-Outz"
    print(cipher(s,2))
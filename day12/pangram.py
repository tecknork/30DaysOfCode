


def pangram(s):
    
    s = s.replace(" ","")
    s = s.lower()
    
    s = list(s)
    s_set = set(s)
    return "pangram" if len(s_set) == 26 else "not pangram"
 


if __name__ == '__main__':
    print(pangram("We promptly judged antique ivory buckles for the next prize"))        
    print(pangram("We promptly judged antique ivory buckles for the prize"))        
    
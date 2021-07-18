b = "01100"


def binary(b):
    b = list(b)
    s = '010'
    count = 0 
    for i in range(2,len(b)): 
        sub_str = b[i-2:i+1]
        if "".join(sub_str) == s: 
            b[i] =str(int(b[i]) ^1 )
            count +=1
        
    return count


if __name__ == '__main__':
    print(binary(b))
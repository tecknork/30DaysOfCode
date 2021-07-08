arr= [1,1,0,-1,-1]

def fraction(arr):
    pos_list= [ item for item in arr if item >0]
    neg_list = [ item for item in arr if item <0]
    zero_list = [ item for item in arr if item == 0]
    size = len(arr)
    print ("{:.5f}".format(len(pos_list)/size))
    print ("{:.5f}".format(len(neg_list)/size))
    print ("{:.5f}".format(len(zero_list)/size))
    

if __name__ == '__main__':
    fraction(arr)
    
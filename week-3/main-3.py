 #print(ArrayChallenge([1, 2, 3, 4, 2])) # 3
# print(ArrayChallenge([1, 7, 1, 1, 1, 1])) # 2
# print(ArrayChallenge([1, 1,2,100,2,1, 1])) # -1
#print(ArrayChallenge([2, 3, 5, 6, 1])) # 2



data = [2,3,5,6,1]

def ArrayChallenge(data):
    max_val = max(data)
    array_length = len(data)
    max_val_index = data.index(max_val)
    
    hop_val = max_val
    current_index = max_val_index
    count = 0
    left_result = hop(hop_val,array_length, current_index,data,max_val_index,count,'left',[])
    right_result = hop(hop_val,array_length, current_index,data,max_val_index,count,'right',[])
    if(left_result == right_result == -1):
                return -1
    else:
            results = [r for r in [left_result, right_result] if r > 0]
            return(min(results))
   
def hop(hop_val,array_length,current_index,data,max_val_index,count,dir,index_reached):

    if dir == 'right':   
     hop_val,current_index = right(hop_val,array_length, current_index,data)
     #hop_val_l,current_index_l = left(hop_val,array_length, current_index,data)
    else:
      hop_val,current_index = left(hop_val,array_length, current_index,data)
    
    if (current_index in index_reached):
        return -1
    if current_index == max_val_index: 
         return count + 1
    elif current_index == max_val_index:  
         return count + 1 
    else: 
         left_result = hop(hop_val,array_length,current_index,data,max_val_index,count+1,'left',index_reached + [current_index])
         right_result = hop(hop_val,array_length,current_index,data,max_val_index,count+1,'right',index_reached + [current_index])
         if(left_result == right_result == -1):
                return -1
         else:
            results = [r for r in [left_result, right_result] if r > 0]
            return(min(results))

def right(hop_val,array_length,current_index,data):
       next_index = (current_index + hop_val) % array_length
       next_hop_val = data[next_index]
       #print(next_hop_val,next_index)
       return next_hop_val,next_index
    
def left(hop_val,array_length,current_index,data):
       next_index = (current_index - hop_val) % array_length
       next_hop_val = data[next_index]
       #print(next_hop_val,next_index)
       return next_hop_val,next_index
        
if __name__ == '__main__':
        print(ArrayChallenge(data))
        
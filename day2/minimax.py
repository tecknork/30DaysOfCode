
array = [1,2,3,4,5]


def mini_max(arr):
    list.sort(arr,reverse=True)
    max_val = sum(arr[:4])
    min_max_val = sum(arr[1:])
    
    return min_max_val, max_val

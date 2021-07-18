arr = ['abcdde', 'baccd', 'eeabg']


def stones(arr):
    
    arr_set = [set(list(i)) for i in arr]
    result = set.intersection(*arr_set)
    return len(result)
    
    
if __name__ == '__main__':
    stones(arr)
data = [45, 24, 35, 31, 40, 38, 11]

def max_profit(data): 
    
    max_profit = -1
    for index,item  in enumerate(data): 
        sub_data = [j[1]-item if j[0] > index else 0 for j in enumerate(data)] 
        profit = max(sub_data)
        if max_profit <= profit: 
           max_profit = profit

    if max_profit == 0: 
        return -1 
    else: 
        return max_profit
        
if __name__ == '__main__':
    print(max_profit(data))


def ArrayChallenge(arr):
    max_profit = -1
    for i, v in enumerate(arr):
        for d in arr[i + 1:]:
            profit = d - v
            if profit > max_profit:
                max_profit = profit
    if max_profit == 0:
        max_profit = -1
    return max_profit

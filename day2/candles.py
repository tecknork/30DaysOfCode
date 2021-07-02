arr = [3,2,1,3]
from collections import Counter


def blow_candle(arr):
    max_val = max(arr)
    count_dic = Counter(arr)
    return count_dic[max_val]

if __name__ == '__main__':
    print(blow_candle(arr))
    
    
## return candles.count(max(candles))

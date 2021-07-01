# "aabejiabkfabed" "abe"
# "123224" "null"
# "da2kr32a2" "a2"
# "sskfssbbb9bbb" "bbb"
import collections
from collections import Counter


data = "bbbbbbbbbbbb"
def longest_matching_substring(data):
    smallest_window = 2
    largest_window = int(len(data))
    window = [] 
    matching_substring = []
    for win in range(smallest_window,largest_window+1):
        for i in range(len(data)-win+1): 
            window.append(data[i:i+win])
            common = [item for item, count in collections.Counter(window).items() if count > 1]
            if len(common) > 0:
                matching_substring.extend(common)
    if len(matching_substring) > 0:
        longest_string = max(matching_substring,key=len)
        return longest_string
    return "null"


def SearchingChallenge(strParam):
    # ws = window size (2 --> len(strParam))
    # create windows --> set
    # check set for duplicates... if yes, figure out what
    # increasing ws

    duplicate = "no"
    result = "null"

    for ws in range(2, len(strParam)):
        windows = []
        for i in range(len(strParam) + 1 - ws):
            # 0 1
            # 1 2
            windows.append(strParam[i:i + ws])
        #print(windows)
        duplicates = [k for k, v in Counter(windows).items() if v > 1]
        #print(Counter(windows))
        if(len(duplicates) > 0):
            duplicate = "yes"
            result = duplicates[0]
    
    return  result

    
if __name__ == '__main__':
    print(longest_matching_substring(data))
    print(SearchingChallenge(data))
    
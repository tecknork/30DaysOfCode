"""
Using the Python language, have the function GasStation(strArr)
take strArr which will be an an array consisting of the following
elements:
N - the number of gas stations in a circular route
each subsequent element will be the string g:c
g - he amount of gas in gallons at that gas station
c - the amount of gallons of gas needed to get to the following gas station
For example strArr may be: ["4","3:1","2:2","1:2","0:1"].
Your goal is to return the index of the starting gas station
that will allow you to travel around the whole route once
otherwise return the string impossible.
For the example above, there are 4 gas stations, and your
program should return the string 1 because starting at station 1 you
receive 3 gallons of gas and spend 1 getting to the next station. Then
you have 2 gallons + 2 more at the next station and you spend 2 so you
have 2 gallons when you get to the 3rd station. You then have 3 but you
spend 2 getting to the final station, and at the final station you
receive 0 gallons and you spend your final gallon getting to your
starting point. Starting at any other gas station would make getting
around the route impossible, so the answer is 1. If there are multiple
gas stations that are possible to start at, return the smallest index
(of the gas station). N will be >= 2. 
Input:"4","1:1","2:2","1:2","0:1"
Output:"impossible"
Input:"4","0:1","2:2","1:2","3:1"
Output:"4"
"""

#data = ["4","3:1","2:2","1:2","0:1"]
data = ["4","2:2","1:2","0:1","3:1"]

def gas_station(data):
    total_gas_station = int(data[0])
    gas_station = data[1:]
    #print(gas_station)

    tuple_list = [(int(x.split(":")[0]),int(x.split(":")[1])) for x in gas_station]

    for index in range(total_gas_station): 
        
        gas_rotate = tuple_list[index:] + tuple_list[:index]
        print(gas_rotate)
        current_gallon = 0 
        for i in gas_rotate: 
            g = i[0]
            c = i[1]
            current_gallon = current_gallon + g 
            current_gallon = current_gallon - c 
            if current_gallon < 0:
                print("impossible") 
                break
        if current_gallon >= 0: 
            return index +1
    return "impossible"    
    
    
    
        
print(gas_station(data))
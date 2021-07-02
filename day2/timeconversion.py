#07:05:45PM
#07:05:45AM

time_str = "12:01:29PM"

def convert_time(time_str):
    time_str = list(time_str)
    val = time_str[-2:]
    if "".join(val) == "AM":
        hour = time_str[:2]
        return "{:02d}".format(hour%12) + "".join(time_str[2:-2])  
        return "".join(time_str[:-2])
    else:
        hour = int("".join(time_str[:2]))
        hour_24 = hour + 12
        if hour > 12: 
            return "{:02d}".format(hour_24%24) + "".join(time_str[2:-2])  
        else: 
            return "{:02d}".format(hour) + "".join(time_str[2:-2])
        
if __name__ == '__main__':
    print(convert_time(time_str))



# time = input().strip()
# h, m, s = map(int, time[:-2].split(':'))
# p = time[-2:]
# h = h % 12 + (p.upper() == 'PM') * 12
# print(('%02d:%02d:%02d') % (h, m, s))
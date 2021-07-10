numbers = list("0123456789")
lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = list("!@#$%^&*()-+")


def password(s): 
    val = list(s)
    set_val  = set(val)
    count = 0 
    if len(set_val.intersection(lower_case)) <= 0: 
        count += 1
    if len(set_val.intersection(numbers)) <= 0:
        count += 1
    if len(set_val.intersection(upper_case)) <= 0:
        count += 1
    if len(set_val.intersection(special_characters)) <= 0:
        count += 1
    if len(val) > 6 or (len(val) + count ) >= 6 : 
        return count
    else:  
        add = 6 - count - len(val)
        count = count + add 
        return count 
    

if __name__ == '__main__':
        print(password("2bb#A"))
        print(password("2bbbb"))
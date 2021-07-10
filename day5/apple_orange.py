
s = 7
t = 11 
a = 5 
b = 15 
app = [-2,2,1]
org = [5,-6]



def apple_orange(s,t,a,b,app,org):
    apple = 0 
    orange = 0 
    # for apple
    min_app = s-a 
    max_app = t-a 
    min_orange =  t - b
    max_orange =  s - b 
    
    for i in app:
        if i >= min_app and i <= max_app: 
            apple = apple + 1 
    for i in org: 
        if i <= min_orange and i >= max_orange: 
            orange = orange + 1
            
    print(apple)
    print(orange) 
    
if __name__ == '__main__':
    apple_orange(s,t,a,b,app,org)
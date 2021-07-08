
x1= 0 
v1 = 2 
x2 = 5 
v2 = 3 



def number_jump(x1,v1,x2,v2):
   print("YES" if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0 else "NO")
        
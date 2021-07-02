     #
    ##
   ###
  ####
 #####
######

# def staircase(n):
#     for i in range(1,n+1):
#         spaces = n-i 
#         for _ in range(spaces):
#             print(" ",end="")
#         for _ in range(i):
#             print("#",end="")
#         print("")
        

## better solution 

def staircase(n):
        for i in range(1, n + 1):
         print(str('#'*i).rjust(n))
         
         
if __name__ == '__main__':
    staircase(6)
    
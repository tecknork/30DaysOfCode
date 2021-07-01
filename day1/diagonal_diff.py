# 1 2 3
# 4 5 6
# 9 8 9 

#https://www.hackerrank.com/challenges/diagonal-difference/problem




if __name__ == '__main__':
    
    
    n = int(input().strip())

    datax = []

    for _ in range(n):
        datax.append(list(map(int, input().rstrip().split())))
    #datax = [[11,2,4],[4,5,6],[10,8,-12]]
    #datax = [[1,2,3],[4,5,6],[9,8,9]]
    
    size = len(datax[0])
    sum_a = 0 
    sum_b = 0 
    for i in range(size):
        sum_a = sum_a + datax[i][i]
        sum_b = sum_b + datax[i][size-1-i]
    
    print(abs(sum_a-sum_b))

    
    #for a in datax:
        
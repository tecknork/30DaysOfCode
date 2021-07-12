s = "SOSSOT"

sos = list("SOS")
def mars(s): 
    s = list(s)
    error = 0 
    for index,i in enumerate(s): 
        if  i != sos[index%len(sos)]: 
            error += 1
    return error


if __name__ == '__main__':
    print(mars(s))
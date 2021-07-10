
s = "saveChangesInTheEditor"
d = "oneTwoThree"


def camelcase(s):
    val = list(s)
    count = 0 
    for i in range(len(val)):
        if val[i].isupper():
            count = count+1

    return count+1


if __name__ == '__main__':
    print(camelcase(s))
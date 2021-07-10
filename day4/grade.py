

arr = [73,67,38,33]


def grade(arr):
    modified_grade = []
    for i in arr: 
        if i+2 < 40: 
            modified_grade.append(i)
        elif i % 5 < 3: 
            modified_grade.append(i)
        else:
            modified_grade.append(int(round(i/5.0)*5.0))
    return modified_grade


if __name__ == '__main__':
    print(grade(arr))
    
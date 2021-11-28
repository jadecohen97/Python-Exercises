student_heights = [120, 300, 200, 220, 990, 180]


def AverageHeight():
    total_height = 0
    student = 0
    for height in student_heights:
        total_height += height
        student += 1
    average = round(total_height/student)
    print(average)


AverageHeight()

student_list = ['satendra','vishwendra','brijmohan','saurabh']
place_list = ['pune','delhi','bangalore','hyderabad']
course_list = ['fs','ds','ds','ds']

while(True):
    operation = int(input('\n1.ADD\n2.SHOW DATA\n3.FIND INFO\n4.DELETE\n5.Quit\nChoose::: '))

    if(operation==1):
        student = input('Enter the name of student : ')
        if(student not in student_list):
            place = input('Where Does he live ? ')
            course = input('Course : ')
            student_list.append(student)
            place_list.append(place)
            course_list.append(course)
        else:
            print(f'{student} is already in our Institute.')
    elif(operation==2):
        for nam, loc, cou in zip(student_list, place_list, course_list):  # ('satendra', 'pune', 'fs')
            print(f' Student {nam} lives in {loc} , enrolled in {cou}')
    elif(operation==4):
        student = input('Enter the name of the student : ')
        if (student in student_list):
            ind = student_list.index(student)  # 0
            print(
                f'{student_list.pop(ind)} lives in {place_list.pop(ind)} enrolled in {course_list.pop(ind)} is removed from session.')
        else:
            print(f'{student} is not in our Institute')
    elif(operation==5):
        break



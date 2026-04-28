student_list1 = ['tim', 'drake', 'ashish', 'shubham']

student_list2 = ['andrew', 'chris', 'harshit', 'lary', 'shubham']

def checkStudent(student_list2):
    for student in student_list2:
        if student == 'chris':
            print('Available')

checkStudent(student_list2)
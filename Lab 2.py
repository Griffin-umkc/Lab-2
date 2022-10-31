print('**** Welcome to the LAB grade calculator! ****')
print()
name = input('Who are we calculating grades for? ==> ')
print()
l_grade = int(input('Enter the Labs grade? ==> '))
if l_grade < 0:
    print('The lab value should have been 0 or greater. It has been changed to zero.')
    l_grade = 0
    print()
elif l_grade > 100:
    print('The lab value should have been 100 or less. It has been changed to 100')
    l_grade = 100
    print()
print()
e_grade = int(input('Enter the EXAMS grade? ==> '))
print()
if e_grade < 0:
    print('The exam value should have been 0 or greater. It has been changed to zero.')
    e_grade = 0
    print()
elif e_grade > 100:
    print('The exam value should have been 100 or less. It has been changed to 100')
    e_grade = 100
    print()
a_grade = int(input('Enter the Attendance grade? ==> '))
print()
if a_grade < 0:
    print('The exam value should have been 0 or greater. It has been changed to zero.')
    a_grade = 0
    print()
elif a_grade > 100:
    print('The exam value should have been 100 or less. It has been changed to 100')
    a_grade = 100
    print()
weight = (l_grade)*.7 + (e_grade)*.2 + (a_grade)*.1
if weight >= 90:
    letter = 'A'
elif weight >= 80:
    letter = 'B'
elif weight >= 70:
    letter = 'C'
elif weight >= 60:
    letter = 'D'
elif weight >= 0:
    letter = 'F'
    
print('The weighted grade for',name,'is',weight)
print(name,'has a letter grade of',letter)

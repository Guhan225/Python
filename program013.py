def grade_to_gpa(grade):
    switcher={
            'A':4.0,
            'B':3.0,
            'C':2.0,
            'D':1.0,
            'F':0
            }
    return switcher.get(grade,("Invalid Grade"))
print(grade_to_gpa('A'))
print(grade_to_gpa('b'))
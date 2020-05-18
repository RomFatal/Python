###################################################################
# Target: The program calculate the average student's score sheet #
###################################################################


class Student:
    def __init__(self, id, firstName, lastName, marks):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.marks = marks

    def calculate_average(self):
        points = 0
        grades = 0
        for point, grade in self.marks.values():
            points += point
            grades += point * grade
        if 0 == points:
            return -1
        final_grade = round(grades / points)
        if 100 <= final_grade or 0 >= final_grade:
            return -2
        else:
            return final_grade


# The function get dict of student's and return the average student's score sheet


marks = {
    'Java': (3, 94),
    'Python': (5, 98),
    'Mobile': (4, 70),
    'Web': (2, 82),
    'Math': (5, 79),
    'English': (1, 100)
}

student = Student(312487512, 'Rom', 'Fatal', marks)
avg = student.calculate_average()
if -1 != avg and -2 != avg:
    print("Average grade of", student.firstName, "is:", avg)
elif -1 == avg:
    print('Error dividing by 0')
else:
    print('Error avg > 100 or avg <0')


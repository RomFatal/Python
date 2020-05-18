###################################################################
# Target: The program calculate the average student's score sheet #
###################################################################


student = {
    'id': "211214454",
    'firstName': "Rom",
    'lastName': "Fatal",

    'marks': {
        'Java': (3, 94),
        'Python': (5, 98),
        'Mobile': (4, 70),
        'Web': (2, 82),
        'Math': (5, 79),
        'English': (1, 100)
    }
}

# The function get dict of student's and return the average student's score sheet


def calculate_average(s):
    points = 0
    grade = 0
    # Get all student course name
    key_list = list(s['marks'].keys())
    for Course in key_list:
        points += s['marks'][Course][0]
        grade += s['marks'][Course][0]*s['marks'][Course][1]
    print("Average grade of", s['firstName'], "is:", grade/points)


calculate_average(student)



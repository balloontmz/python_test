class Student(object):

    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name

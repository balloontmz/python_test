

class Student(object):

    def __init__(self, name):
        self.__name=name

    def __str__(self):
        return 'Student name:%s'% self.__name
    __repr__ = __str__

print(Student('Thomas'))
a= Student('Thomas')
class Student(object):

    def __init__(self, student, score, gender='male'):
        self.__student = student
        self.__score = score
        self.__gender = gender

    def get_name(self):
        return self.__student

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s:%s' % (self.__student, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            return ValueError('bad score')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ['male', 'female', 'x']:
            self.__gender = gender
        else:
            return ValueError('bad gender')

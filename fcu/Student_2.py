class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('bad')
        if 0>=score or score>=100:
            raise ValueError('bad')
        self.__score=score


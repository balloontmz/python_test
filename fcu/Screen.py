class Screen(object):

    @property
    def width(self):
        return self.__wid

    @width.setter
    def width(self,value):
        self.__wid=value

    @property
    def height(self):
        return self.__hei

    @height.setter
    def height(self, value):
        self.__hei = value

    @property
    def resolution(self):
        return self.__hei * self.__wid
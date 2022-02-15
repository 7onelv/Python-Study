class Rectangle:

    # constructor
    def __init__(self, width, height):
        """
        初始化方法
        :param width: 宽
        :param height: 高
        """
        self._width = width
        self._height = height 
        
    # a public method 
    def getArea(self):
        return self._width * self._height 

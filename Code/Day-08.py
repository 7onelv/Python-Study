# class描述数字时钟
from time import sleep
from math import sqrt

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour # 通常使用_来标明是私密属性
        self._minute = minute
        self._second = second 
    
    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0 
            self._minute += 1 
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self.hour = 0
    
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' %(self._hour, self._minute, self._second)

# 坐标轴建立和移动
class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y
    
    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x 
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy
    
    def distance_to(self, other):
        """
        计算到另一个点的增量
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt (dx ** 2 + dy ** 2)
    
    def __str__(self):
        return '(%s, %s)' %(str(self.x), str(self.y))

def main():
    clock = Clock(23, 59, 58)
    while True:
    	print(clock.show())
   		sleep(1)
		clock.run()
		
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p1.move_by(1, 1)
    p1.move_to(3, 2)
    print(p1)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()

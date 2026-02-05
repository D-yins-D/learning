import math

class Shape:
    count = 0

    def __init__(self):
        self.__area = 0.0  # 私有属性
        Shape.count += 1

    def _set_area(self, value):
        self.__area = value

    def calc_area(self):
        pass

    def get_area(self):
        self.calc_area()
        return self.__area

class Circle(Shape):
    def __init__(self, radius):
        # 初始化时进行异常捕获
        try:
            if radius <= 0:
                raise ValueError("半径必须为正数")
            super().__init__()
            self.radius = radius
        except ValueError as e:
            print(f"图形创建失败：{e}")


    def calc_area(self):
        area = self.radius ** 2 * math.pi
        self._set_area(area)

class Rectangle(Shape):
    def __init__(self, height, width):
        try:
            if height <= 0 or width <= 0:
                raise ValueError("长度不能为负数")
            super().__init__()
            self.height = height
            self.width = width
        except ValueError as e:
            print(f"创建图形失败：{e}")
            raise

    def calc_area(self):
        area = self.width * self.height
        self._set_area(area)

c1 = Circle(2)
print(f"圆的面积：{c1.get_area():.2f}")
r1 = Rectangle(100, 200)
print(f"矩形面积：{r1.get_area():.2f}")
c2 = Circle(-2)
# print(f"圆的面积：{c2.get_area():.2f}")
print(f"创建图形数量：{Shape.count}")

class Line:
    def __init__(self, coordinate1: tuple[float, float], coordinate2: tuple[float, float]):
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def distance(self) -> float:
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self) -> float:
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (10, 20)
coordinate2 = (30, 40)
line = Line(coordinate1, coordinate2)
print("Distance:", line.distance())  # 28.284271247461902
print("Slope:", line.slope())        # 1.0
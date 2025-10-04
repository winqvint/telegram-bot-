class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            return True
        else:
            return False
    def get_triangle_area(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            p = (self.a+self.b+self.c) / 2
            area = (p *(p-self.a) * (p-self.b) *(p-self.c))**0.5
            return area
        else:
            return 0
t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())

# False
class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vertices = [self.x, self.y]

    def magnitude(self):
        return (self.x **2 +self.y**2)**0.5

    def normalise(self):
        mag = self.magnitude
        return Vec2(self.x/mag, self.y/mag)

    def dot(self, vector2):
        return self.x *vector2.x + self.y*vector2.y

    def __abs__(self):
        return self.magnitude()

    def __len__(self):
        return 2

    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Vector 2 ({self.x}, {self.y})"

    def __add__(self, vector2):
        return Vec2(self.x + vector2.x, self.y+vector2.y)
    def __iadd__(self, vector2):
        return Vec2(self.x + vector2.x, self.y+vector2.y)
    def __radd__(self, vector2):
        return Vec2(self.x + vector2.x, self.y+vector2.y)

    def __sub__(self, vector2):
        return Vec2(self.x - vector2.x, self.y - vector2.y)
    def __isub__(self, vector2):
        return Vec2(self.x - vector2.x, self.y - vector2.y)
    def __rsub__(self, vector2):
        return Vec2(-self.x + vector2.x, -self.y + vector2.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    def __imul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __eq__(self, vector2):
        if self.x == vector2.x and self.y == vector2.y:
            return True
        else:
            return False
    def __ne__(self, vector2):
        if self.x == vector2.x and self.y == vector2.y:
            return False
        else:
            return True

    def __bool__(self):
        if self.x == 0 and self.y == 0:
            return False
        else:
            return True
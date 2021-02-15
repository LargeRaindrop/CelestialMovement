import Constant
from Vector import Vector


class Star:
    def __init__(self, mass, pos, speed):
        self.mass = mass
        self.pos = pos
        self.speed = speed

    def distance(self, star):
        return abs(star.pos - self.pos)

    def rel_speed(self, star):
        """
        own speed relative to *star*
        """
        return self.speed - star.speed

    def gravity(self, star):
        """
        own gravity by *star*
        """
        dis = self.distance(star)
        fx = Constant.GRAVITY_CONST * self.mass * star.mass / dis ** 3 * (star.pos.x - self.pos.x)
        fy = Constant.GRAVITY_CONST * self.mass * star.mass / dis ** 3 * (star.pos.y - self.pos.y)
        return Vector(fx, fy)

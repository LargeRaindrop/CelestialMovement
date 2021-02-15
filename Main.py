from math import sqrt
import matplotlib.pyplot as plt

from Star import Star
from Vector import Vector


def deduce(stars, time_limit, time_step):
    """
    Perform planetary movement deduction.

    :param stars: the list of stars
    :param time_limit: maximum deduction time
    :param time_step: delta time
    :return: the positions and the speeds of each star
    """
    _pos = [[_star.pos] for _star in stars]
    _speed = [[_star.speed] for _star in stars]
    time = time_step
    stars_size = len(stars)
    while time <= time_limit:
        for i in range(stars_size):
            # update the position and the speed in order
            _star = stars[i]
            offset = _star.speed.dot_prod(time_step)
            _star.pos = _star.pos + offset
            gravity = Vector()
            for j in range(stars_size):
                if i == j:
                    continue
                other_star = stars[j]
                gravity = gravity + _star.gravity(other_star)
            acc = gravity.dot_prod(1 / _star.mass)
            _star.speed = _star.speed + acc.dot_prod(time_step)
            _pos[i].append(_star.pos)
            _speed[i].append(_star.speed)
        time = time + time_step
    return _pos, _speed


def track(poses_list, auto_size=True, window_size=None):
    """
    Draw the track graph.

    :param poses_list: the positions of each star, output of function deduce
    :param auto_size: whether to set the length and width of the track graph to 1:1
    :param window_size: Operant if parameter auto_size is true. Set according to the format [xmin, xmax, ymin, ymax].
    """
    poses_list_size = len(poses_list)
    for i in range(poses_list_size):
        poses = poses_list[i]
        xv = [_pos.x for _pos in poses]
        yv = [_pos.y for _pos in poses]
        plt.plot(xv, yv)
    if auto_size:
        xmin, xmax, ymin, ymax = plt.axis()
        xrange = xmax - xmin
        yrange = ymax - ymin
        if xrange / yrange > 4/3:
            ymid = (ymax + ymin) / 2
            ymin = ymid - 3/8 * xrange
            ymax = ymid + 3/8 * xrange
        else:
            xmid = (xmax + xmin) / 2
            xmin = xmid - 2/3 * yrange
            xmax = xmid + 2/3 * yrange
        plt.axis([xmin, xmax, ymin, ymax])
    elif window_size:
        plt.axis(window_size)
    plt.show()


if __name__ == '__main__':
    # definition of stars
    sun = Star(sqrt(3), Vector(0, 1), Vector(1, 0))
    earth = Star(sqrt(3), Vector(-sqrt(3)/2, -1/2), Vector(-1/2, sqrt(3)/2))
    star = Star(sqrt(3), Vector(sqrt(3)/2, -1/2), Vector(-1/2, -sqrt(3)/2))

    # deduce and track
    pos, speed = deduce([sun, earth, star], 2, 0.0001)
    track(pos)

    # use section to draw the track graph of sectional stars
    # track[pos[0:2]]

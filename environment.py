import vehicle

class Environment():


    def __init__(self, obstacles = []):
        self.obstacles = obstacles


class BoundedEnvironment(Environment):
    def __init__(self, xbounds, ybounds):
        self.x_min = xbounds[0]
        self.x_max = xbounds[1]

        self.y_min = ybounds[0]
        self.y_max = ybounds[1]
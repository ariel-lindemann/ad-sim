import numpy as np


class Car:
    def __init__(self, wheel_base = 1.5):
        self.x_p = 0
        self.y_p = 0
        self.angle_p = 0
        self.st_angle_p = 0
        self.v_p = 0
    
        self.v = 0
        self.angle = 0
        self.st_angle = 0

import numpy as np


class Car:
    def __init__(self, wheel_base=1.5, orientation=0):
       
        self.x_p = 0
        self.y_p = 0
        self.angle_p = 0
        self.st_angle_p = 0
        self.v_p = 0

        self.v = 0
        self.angle = orientation
        self.st_angle = 0

        self.wheel_base = wheel_base

    def update(self, st_angle_p, v_p, timestep=1):

        self.v += v_p * timestep
        # NOTE:timestep klein genug für lekradverlauf?
        self.st_angle += st_angle_p
        self.angle += (self.v * np.tan(self.st_angle) /
                       self.wheel_base) * timestep

        self.x_p = self.v * np.cos(self.angle)
        self.y_p = self.v * np.cos(self.angle)
        self.angle_p = self.v * np.tan(self.st_angle) / self.wheel_base
        self.st_angle_p = st_angle_p
        self.v_p = v_p

    def take_inputs(self, gas=0, brake=0, st_wheel_chg=0):
        c = - 0.25
        self.v_p = (gas - brake) * c * self.v ** 2
        self.st_angle_p = st_wheel_chg

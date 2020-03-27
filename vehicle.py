import numpy as np
import matplotlib.pyplot as plt


class Car:
    def __init__(self, wheel_base=1.5, orientation=0):

        self.x_p = 0
        self.y_p = 0
        self.angle_p = 0
        self.st_angle_p = 0
        self.v_p = 0

        self.v = 0
        self.orientation = orientation
        self.st_angle = 0

        self.wheel_base = wheel_base

    def update(self, timestep=1):

        self.v += self.v_p * timestep
        # NOTE:timestep klein genug für lekradverlauf?
        self.st_angle += self.st_angle_p
        self.orientation += (self.v * np.tan(self.st_angle) /
                             self.wheel_base) * timestep

        self.x_p = self.v * np.cos(self.orientation)
        self.y_p = self.v * np.cos(self.orientation)
        self.angle_p = self.v * np.tan(self.st_angle) / self.wheel_base

    # TODO sensible output
    def gen_acc(self, gas, v_max=160*3.6, a_max=7.5):
        return -((4*a_max)/(v_max**2)) * gas * self.v**2 + ((4*a_max)/v_max)*self.v

    def take_inputs(self, gas=0, brake=0, st_wheel_chg=0, inputs=None):
        #acc = self.gen_acc(gas)
        if inputs:
            gas = inputs[0]
            brake = inputs[1]
            st_wheel_chg = inputs[2]

        acc = gas
        self.v_p = acc*(1-brake)
        self.st_angle_p = st_wheel_chg

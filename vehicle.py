import numpy as np
import matplotlib.pyplot as plt
from math import pi


class Car:
    '''Single-Track model of a car.

    Attributes
    ----------
    x_p : float
        x-axis component of `v`.
    y_p : float
        y-axis component of `v``.
    ori_p : float
        Change in orientation in radians.
    st_angle_p : float
        Change in steering angle in radians.
    v_p : float
        Change in velocity i.e. acceleration.
    v : float
        Current car velocity.
    orientation : float
        Orientation (theta) in radians.
    st_angle : float
        Steering angle (phi) in radians.
    wheel_base : float
        Vehicle wheel base i.e. distance between front and rear wheels
    '''

    def __init__(self, wheel_base=1.5, orientation=0):
        self.x_p = 0
        self.y_p = 0
        self.ori_p = 0
        self.st_angle_p = 0
        self.v_p = 0

        self.v = 0
        self.orientation = orientation % (2 * pi)
        self.st_angle = 0

        self.wheel_base = wheel_base

    def adj_angles(self):
        '''Prevent angles from exceeding 2*pi or 360°.'''
        all_angles = [self.ori_p, self.st_angle_p,
                      self.orientation, self.st_angle]
        for a in all_angles:
            a = a % (2*pi)

    def update(self, timestep=1):

        self.v += self.v_p * timestep
        # NOTE:timestep klein genug für lekradverlauf?
        self.st_angle += self.st_angle_p
        self.orientation += (self.v * np.tan(self.st_angle) /
                             self.wheel_base) * timestep

        self.x_p = self.v * np.cos(self.orientation)
        self.y_p = self.v * np.sin(self.orientation)
        self.ori_p = self.v * np.tan(self.st_angle) / self.wheel_base

        self.adj_angles()

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

    def next_pos(self, pos=[0, 0], inputs=[0, 0, 0],  t_s=1):
        ''' Returns coordinates of Car after specified timestep based on given inputs'''

        pos_x = pos[0]
        pos_y = pos[1]

        gas, brake, st_wheel_chg = inputs

        self.take_inputs(gas, brake, st_wheel_chg)
        self.update(timestep=t_s)

        pos_x += self.x_p
        pos_y += self.y_p

        return pos_x, pos_y

    def get_trajectory(self, input_series, starting_pos=[0, 0], total_time=100,  t_s=1):
        ''' Returns series of posisions based on a series of inputs'''

        all_x = []
        all_y = []

        pos_x = starting_pos[0]
        pos_y = starting_pos[1]

        for i in range(total_time):

            if len(input_series) >= i:
                gas, brake, st_wheel_chg = input_series.pop(0)

            pos_x, pos_y = self.next_pos([pos_x, pos_y], [gas, brake, st_wheel_chg], t_s)
            all_x.append(pos_x)
            all_y.append(pos_y)

        return all_x, all_y

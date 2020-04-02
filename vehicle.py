import numpy as np
import math

from body import Body

class Car(Body):
    '''Single-Track model of a car.

    Attributes
    ----------
    length : float
        Car length in meters.
    width : float
        Car width in meters.
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
    input_buffer : list
        Stores gas, break and steering wheel cange inputs.
    '''

    def __init__(self, dimensions = [4.95, 1.85], wheel_base=2.95, orientation=0, inputs=None):
        
        self.length = dimensions[0]
        self.width =  dimensions[1]
        
        self.x_p = 0
        self.y_p = 0
        self.ori_p = 0
        self.st_angle_p = 0
        self.v_p = 0

        self.v = 0
        self.orientation = orientation % (2 * math.pi)
        self.st_angle = 0

        self.wheel_base = wheel_base

        if inputs:
            self.input_buffer = inputs
        else:
            self.input_buffer = []

    def adj_angles(self):
        '''Prevent angles from exceeding 2*pi or 360°.'''
        all_angles = [self.ori_p, self.st_angle_p,
                      self.orientation, self.st_angle]
        for a in all_angles:
            a = a % (2*math.pi)

    def load_inputs(self, file=None, in_list=None):
        ''' Load inputs either from file or from array'''
        if file:
            in_file = open(file)

            for line in in_file:
                self.input_buffer.append(line.split(',', 3))

            in_file.close()

        elif in_list:
            self.input_buffer += (in_list)

    def update(self, timestep=1):
        ''' Update location, speed and orientation'''
        self.v += self.v_p * timestep
        # NOTE:timestep klein genug für lekradverlauf?
        self.st_angle += self.st_angle_p    # NOTE timestep needed?
        self.orientation += (self.v * np.tan(self.st_angle) /
                             self.wheel_base) * timestep

        self.x_p = self.v * np.cos(self.orientation)
        self.y_p = self.v * np.sin(self.orientation)
        self.ori_p = self.v * np.tan(self.st_angle) / self.wheel_base

        self.adj_angles()

    # TODO sensible output
    def gen_acc(self, gas, v_max=160*3.6, a_max=7.5):
        return -((4*a_max)/(v_max**2)) * gas * self.v**2 + ((4*a_max)/v_max)*self.v

    def take_next_inputs(self, gas=0, brake=0, st_wheel_chg=0, inputs_l=None):
        ''' Takes inputs as values or reads them from a list'''
        #acc = self.gen_acc(gas)

        # TODO option to set inputs to 0 if no new inputs
        if inputs_l:
            gas, brake, st_wheel_chg = inputs_l.pop(0)

        gas = float(gas)
        brake = float(brake)
        st_wheel_chg = float(st_wheel_chg)
        st_wheel_chg = math.radians(st_wheel_chg)
        acc = gas  # NOTE temporary
        self.v_p = acc*(1-brake)
        self.st_angle_p = st_wheel_chg

    def next_pos(self, pos=[0, 0], inputs=[0, 0, 0],  t_s=1):
        ''' Returns coordinates of Car after specified timestep based on given inputs'''

        pos_x = pos[0]
        pos_y = pos[1]

        gas, brake, st_wheel_chg = inputs

        self.take_next_inputs(gas, brake, st_wheel_chg)
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

        if isinstance(input_series, str):
            self.load_inputs(input_series)
            input_series = self.input_buffer

        for i in range(total_time):

            if len(input_series) >= i:  # TODO maybe > instead of >=
                gas, brake, st_wheel_chg = input_series.pop(0)

            pos_x, pos_y = self.next_pos([pos_x, pos_y],
                                         [gas, brake, st_wheel_chg], t_s)
            all_x.append(pos_x)
            all_y.append(pos_y)

        return all_x, all_y

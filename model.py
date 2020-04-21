import numpy as np

import vehicle

from scipy.optimize import minimize


class MPC():

    def __init__(self, car, goal, horizon, timestep):

        self.car = car
        self.horizon = horizon
        self.t_s = timestep

        self.start = np.array([0, 0, car.orientation])

        self.goal = goal

    def cost(self, input_series):
        cost = 0.0
        car = self.car

        formatted_input = input_series.reshape(self.horizon, 3)

        states = car.get_trajectory(
            formatted_input, self.start, self.horizon, self.t_s)

        for i in range(self.horizon):
            #x, y, ori = states[i]

            x = states[0][i]
            y = states[1][i]
            ori = states[2][i]

            x_g, y_g, o_g = self.goal

            distance = np.sqrt((x-x_g)**2 + (y-y_g)**2)

            angle_dif = abs(ori - o_g)

            cost += distance**2 + angle_dif

            # TODO refine

        return cost

        # TODO optimimzer

    def gen_inputs(self, total_steps):

        # TODO total steps in other classes
        # TODO generate inputs
        # TODO better variable names

        ins = np.zeros((total_steps * 3))  # TODO maybe different index?

        # solution = np.zeros((total_steps, 3))  # TODO maybe different index?
        solution = []

        for i in range(total_steps + 1):
            # TODO

            # TODO refractor
            #            ins = np.delete(ins, 0)
            #            ins = np.delete(ins, 0)
            #            ins = np.delete(ins, 0)
            predicted_ins = np.zeros((self.horizon * 3))

            in_length = ins[i*3:(self.horizon + i)*3].size  # WATCH

            predicted_ins[0:in_length] += ins[i*3:(self.horizon + i)*3]

            opt_ins = minimize(self.cost, predicted_ins,
                               method='SLSQP', tol=1e-5).x

            ins[i*3:in_length + i*3] = opt_ins[0:in_length]

            gas = opt_ins[0]
            brake = opt_ins[1]
            steering = opt_ins[2]

            # TODO record precictions for visualisation

            self.car.take_next_inputs(gas, brake, steering)
            self.car.update(self.t_s)

            # solution[i] = ins[0]       # NOTE temp. until numpy inputs in Car supported
            solution.append([gas, brake, steering])

        return solution

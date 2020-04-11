import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import numpy as np

import vehicle

from matplotlib.animation import FuncAnimation


def display_trajectory(car, input_series, starting_pos=[0, 0],
                       TOTAL_TIME=100,  t_s=1):
    all_x, all_y, = car.get_trajectory(input_series, starting_pos,
                                       TOTAL_TIME, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()


def run_sim(car, options, inputs):

    FIGSIZE = options['FIGSIZE']
    TOTAL_TIME = options['TOTAL_TIME']
    TIMESTEP = options['TIMESTEP']
    X_BOUNDS = options['X_BOUNDS']
    Y_BOUNDS = options['Y_BOUNDS']

    fig = plt.figure(figsize=FIGSIZE)
    gs1 = gridspec.GridSpec(8, 8)
    # plt.axes(aspect='equal')

    #ax = plt.subplot(1, 1, 1)
    ax = fig.add_subplot(gs1[:8, :8])

    plt.xlim(X_BOUNDS)
    ax.set_ylim(Y_BOUNDS)

    ###

    trajectory = car.get_trajectory(inputs_file, [0, 0],
                                    TOTAL_TIME, TIMESTEP)

    # TODO maybe adjust position
    car_patch = mpatches.Rectangle((0, 0), car.length,
                                   car.width, car.orientation)
    ax.add_patch(car_patch)

    def animate(i):

        x, y, ori = trajectory[[0, 1, 2], [i]]

        # TODO pedals and steering mpatch

        car_patch.set_xy([x, y])
        car_patch.angle = np.rad2deg(ori)
        #ax.plot(x, y, '.')

    ani = FuncAnimation(fig, animate, frames=TOTAL_TIME,
                        interval=TIMESTEP * 1000)
    plt.show()


# DEMO

car = vehicle.Car()

options = {}
options['FIGSIZE'] = [8, 8]
options['TOTAL_TIME'] = 1000
options['TIMESTEP'] = 0.1
options['X_BOUNDS'] = [-50, 150]
options['Y_BOUNDS'] = [-50, 150]

inputs_file = 'inputs.csv'

#display_trajectory(car, inputs_file, [0, 0], TOTAL_TIME, TIMESTEP)
run_sim(car, options, inputs_file)

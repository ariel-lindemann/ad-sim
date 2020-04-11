import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import numpy as np

from matplotlib.animation import FuncAnimation

import vehicle


def display_trajectory(car, input_series, starting_pos=[0, 0],
                       TOTAL_TIME=100,  t_s=1):
    all_x, all_y, = car.get_trajectory(input_series, starting_pos,
                                       TOTAL_TIME, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()


def run_sim(car, OPTIONS, INPUTS_FILE):

    FIGSIZE = OPTIONS['FIGSIZE']
    TOTAL_TIME = OPTIONS['TOTAL_TIME']
    TIMESTEP = OPTIONS['TIMESTEP']
    X_BOUNDS = OPTIONS['X_BOUNDS']
    Y_BOUNDS = OPTIONS['Y_BOUNDS']

    fig = plt.figure(figsize=FIGSIZE)
    gs1 = gridspec.GridSpec(8, 8)
    # plt.axes(aspect='equal')

    # ax = plt.subplot(1, 1, 1)
    ax = fig.add_subplot(gs1[:8, :8])

    plt.xlim(X_BOUNDS)
    ax.set_ylim(Y_BOUNDS)

    ###

    trajectory = car.get_trajectory(INPUTS_FILE, [0, 0],
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

    ani = FuncAnimation(fig, animate, frames=TOTAL_TIME,
                        interval=TIMESTEP * 1000)
    plt.show()


# DEMO

car = vehicle.Car()

OPTIONS = {}
OPTIONS['FIGSIZE'] = [8, 8]
OPTIONS['TOTAL_TIME'] = 1000
OPTIONS['TIMESTEP'] = 0.1
OPTIONS['X_BOUNDS'] = [-50, 150]
OPTIONS['Y_BOUNDS'] = [-50, 150]

INPUTS_FILE = 'inputs.csv'

# display_trajectory(car, inputs_file, [0, 0], TOTAL_TIME, TIMESTEP)
run_sim(car, OPTIONS, INPUTS_FILE)

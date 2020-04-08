import matplotlib.pyplot as plt
import vehicle

from matplotlib.animation import FuncAnimation


def display_trajectory(car, input_series, starting_pos=[0, 0],
                       TOTAL_TIME=100,  t_s=1):
    all_x, all_y = car.get_trajectory(input_series, starting_pos,
                                      TOTAL_TIME, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()


def run_sim(car, options, inputs):

    TOTAL_TIME = options['TOTAL_TIME']
    TIMESTEP = options['TIMESTEP']

    fig = plt.figure()
    plt.axes(aspect='equal')
    ax1 = plt.subplot(1, 1, 1)

    all_x, all_y = car.get_trajectory(inputs_file, [0, 0],
                                      TOTAL_TIME, TIMESTEP)

    def animate(i):
        ax1.plot(all_x.pop(0), all_y.pop(0), '.')

    ani = FuncAnimation(fig, animate, frames=TOTAL_TIME,
                        interval=TIMESTEP * 1000)
    plt.show()


# DEMO

car = vehicle.Car()

options = {}
options['TOTAL_TIME'] = 100
options['TIMESTEP'] = 1

inputs_file = 'inputs.csv'

#display_trajectory(car, inputs_file, [0, 0], TOTAL_TIME, TIMESTEP)
run_sim(car, options, inputs_file)

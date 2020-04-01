import matplotlib.pyplot as plt
import vehicle


def display_trajectory(car, input_series, starting_pos=[0, 0], total_time=100,  t_s=1):
    all_x, all_y = car.get_trajectory(input_series, starting_pos, total_time, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()


car = vehicle.Car()

total_time = 100
timestep = 1

inputs_file = 'inputs.csv'

display_trajectory(car, inputs_file, [0, 0], total_time, timestep)

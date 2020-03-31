import matplotlib.pyplot as plt
import vehicle
import math


def display_trajectory(car, input_series, starting_pos=[0, 0], total_time=100,  t_s=1):
    all_x, all_y = car.get_trajectory(input_series, starting_pos, total_time, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()


car = vehicle.Car()

gas_pedal = 1
brake_pedal = 0
st_chg = math.radians(0.001)
total_time = 100
timestep = 1

display_trajectory(car, [[gas_pedal, brake_pedal, st_chg]], [0, 0], total_time, timestep)

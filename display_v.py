import matplotlib.pyplot as plt
import vehicle

from matplotlib.animation import FuncAnimation


def display_trajectory(car, input_series, starting_pos=[0, 0], total_time=100,  t_s=1):
    all_x, all_y = car.get_trajectory(input_series, starting_pos, total_time, t_s)
    plt.axes(aspect='equal')

    plt.plot(all_x, all_y, '.')
    plt.show()

def get_car_trajectory(car, input_series, starting_pos, total_time, t_s):
    return car.get_trajectory(input_series, starting_pos, total_time, t_s) 

# DEMO

car = vehicle.Car()

total_time = 100
timestep = 1

inputs_file = 'inputs.csv'

#display_trajectory(car, inputs_file, [0, 0], total_time, timestep)

fig = plt.figure()
plt.axes(aspect='equal')
ax1 = plt.subplot(1,1,1)


all_x, all_y = get_car_trajectory(car, inputs_file, [0, 0], total_time, timestep)


def animate(i):
    ax1.plot(all_x.pop(0), all_y.pop(0), '.')

ani = FuncAnimation(fig, animate, frames=total_time, interval = timestep * 1000)
plt.show()

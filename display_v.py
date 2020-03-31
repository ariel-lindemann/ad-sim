import matplotlib.pyplot as plt
import vehicle
import math

def next_pos(car, pos = [0, 0], inputs = [0, 0, 0],  t_s = 1):
    ''' Returns coordinates of Car after specified timestep based on given inputs'''

    pos_x = pos[0]
    pos_y = pos[1]

    gas, brake, st_wheel_chg = inputs

    car.take_inputs(gas, brake, st_wheel_chg)
    car.update(timestep = t_s)

    pos_x += car.x_p
    pos_y += car.y_p

    return pos_x, pos_y


def get_trajectory(car, input_series, starting_pos = [0, 0], total_time = 100,  t_s = 1):
    ''' Returns series of posisions based on a series of inputs'''

    all_x = []
    all_y = []

    pos_x = starting_pos[0]
    pos_y = starting_pos[1]

    plt.axes(aspect = 'equal')

    for i in range(total_time):

        if len(input_series) >= i:
            gas, brake, st_wheel_chg = input_series.pop(0)

        pos_x, pos_y = next_pos(car, [pos_x, pos_y], [gas, brake, st_wheel_chg], t_s)

        print(pos_x, pos_y)
        all_x.append(pos_x)
        all_y.append(pos_y)

    plt.plot(all_x,all_y, '.')
    plt.show()
    
    return all_x, all_y
    
car = vehicle.Car()

gas_pedal = 1
brake_pedal = 0
st_chg = math.radians(0.001)
total_time = 100
timestep = 1

get_trajectory(car, [[gas_pedal, brake_pedal, st_chg]], [0,0] , total_time, timestep)
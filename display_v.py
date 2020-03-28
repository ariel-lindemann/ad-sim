import matplotlib.pyplot as plt
import vehicle
import math

def show_car(car, gas = 0, brake = 0, st_wheel_chg = 0, total_time = 100, t_s = 1):
    
    pos_x = 0
    pos_y = 0

    all_x = []
    all_y = []

    plt.axes(aspect = 'equal')

    car.take_inputs(gas, brake, st_wheel_chg)

    for i in range(total_time):
        car.update()
        car.take_inputs(st_wheel_chg= 0)

        pos_x += car.x_p
        pos_y += car.y_p

        print(pos_x, pos_y)
        all_x.append(pos_x)
        all_y.append(pos_y)

    plt.plot(all_x,all_y, '.')
    plt.show()

    
car = vehicle.Car()

gas_pedal = 1
brake_pedal = 0
st_chg = math.radians(45)
total_time = 100
timestep = 1


show_car(car, gas_pedal, brake_pedal, st_chg, total_time, timestep)
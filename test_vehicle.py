import unittest
import math
import os

import vehicle


class TestCar(unittest.TestCase):

    def test_car_orientation(self):
        car = vehicle.Car(orientation=math.radians(360))
        self.assertEqual(car.orientation, 0)

    def test_load_inputs_from_file(self):
        car = vehicle.Car()

        inputs = [[0.5, 0.25, -15], [0, 0, 0]]

        test_inputs_file = open('test_inputs.csv', 'w')

        for i in range(len(inputs)):
            test_inputs_file.write(
                f'{inputs[i][0]},{inputs[i][1]},{inputs[i][2]}\n')
        test_inputs_file.close()

        car.load_inputs(file='test_inputs.csv')
        os.remove('test_inputs.csv')

        car_input_buffer = car.input_buffer

        for i in range(len(car_input_buffer)):
            for j in range(len(car_input_buffer[i])):
                car_input_buffer[i][j] = float(car_input_buffer[i][j])

        self.assertEqual(inputs, car_input_buffer)

    def test_load_inputs_from_array(self):
        car = vehicle.Car()

        inputs = [[0.5, 0.25, -15], [0, 0, 0]]
        car.load_inputs(in_list=inputs)

        self.assertEqual(inputs, car.input_buffer)

    def test_update(self):
        inputs = [[0.75, 0.0, -30]]
        car = vehicle.Car(orientation=30, inputs=inputs)

        t_s = 1

        car.take_next_inputs(input_series=car.input_buffer)
        car.update(timestep=t_s)

        # TODO

    def test_take_next_inputs(self):
        car = vehicle.Car()

        inputs = [[-0.5, 0.15, 15]]
        car.take_next_inputs(input_series=inputs)
        self.assertEqual(inputs, car.input_buffer)

        car.take_next_inputs(input_series=[])
        self.assertEqual(0, car.st_angle_p)

    def test_next_pos(self):
        t_s = 1
        car = vehicle.Car()

        inputs = [0, 0, 0]
        pos = [0, 0]

        x, y = car.next_pos(pos, inputs, t_s)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        # TODO more general test


if __name__ == '__main__':
    unittest.main()

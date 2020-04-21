# AD sim

Simulator capable of finding the optimal trajectory for a single-track vehicle model based on a given goal state.

## Usage

### Manual Mode

Specify your inputs in `inputs.csv`. AD sim will then plot the trajectory using matplotlib.

### Autonomous Mode

AD will generate the optimal inputs in order to reach the specified `goal_state`. 
This is done using Model Predictive Control (MPC). You can experiment with changing the folowing parameters:
* `goal` : the goal state (`[x_position, y_position, orientation]`)
* `horizon` : the predicion horizon i.e. amount of steps the optimizer can take into account
* `timestep` : duration of each step in seconds
* `total_steps` : exactly that
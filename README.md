#Usage
To start one or more simulations, run
```sh
roscd dl_turtlebot/launch
python multisim.py <number of sims> | roslaunch -
```
These simulation(s) will all be started headless. To view the gui for a
simulation, run

```sh
rosrun dl_turtlebot launch_gui <sim number to connect to>
```

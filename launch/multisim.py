#!/usr/bin/env python
import roslaunch
import time


if __name__ == "__main__":
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    for i in xrange(3):
        gazebo_node = roslaunch.core.Node('gazebo_ros', 'gzserver',
                                          args="-e ode worlds/empty.world",
                                          env_args=[('GAZEBO_MASTER_URI',"http://localhost:{}".format(11345+i))],
                                          namespace="/sim{}".format(i),
                                          name="gazebo")

        launch.launch(gazebo_node)

    launch.spin()

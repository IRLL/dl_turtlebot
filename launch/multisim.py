#!/usr/bin/env python
import roslaunch
import time
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_sims", type=int, help="number of simulators to launch")

    args = parser.parse_args()

    path_prefix = "multisim_templates/"

    headerf = open(path_prefix + "header.xml", "r")
    simf = open(path_prefix + "body.xml", "r")

    headertxt = "".join(headerf.readlines())
    simtxt = "".join(simf.readlines())

    print headertxt

    for i in xrange(args.number_of_sims):
        ns = "sim{}".format(i+1)
        print simtxt.format(namespace=ns, port=11345+i)

    print "</launch>"

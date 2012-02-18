#! /usr/bin/python


#
## echo_py
#
# print sys.argv,
# in python list notation,
# currently not including elem 0
#


import sys # sys.argv
import optparse # optparse.OptionParser class
import os # os.system
import subprocess # .call and .check_output
import tempfile # tempfile.NamedTemporaryFile class


print sys.argv[1:]


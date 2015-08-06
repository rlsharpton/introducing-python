__author__ = 'rls'

import sys

print("the command line arguments are:")
for i in sys.argv:
    print(i)

def path_Print():
    print(sys.path)

print('The PYTHONPATH is', sys.path)

import os
import sys
import datetime

from multiprocessing import Process

import numpy as np
from matplotlib import pyplot

LATTICE_SIZE = 100
SAMPLE_SIZE = 12000
STEP_ORDER_RANGE = [3, 7]
SAMPLE_FOLDER = 'samples'

def bc(i):
    if i+1 > LATTICE_SIZE-1:
        return 0
    if i-1 < 0:
        return LATTICE_SIZE - 1
    else:
        return i

def energy（system, N, M):
    return -1 * system[N, M] * (system[bc(N-1), M] \
                                + system[bc(N+1), M] \
                                + system[N, bc(M-1)] \
                                + system[N, bc(M+1)])

def build_system():
    system = np.random.randint(0, 1, (LATTICE_SIZE, LATTICE_SIZE))
    system[system==0] = -1
    return system

def main(T, index):


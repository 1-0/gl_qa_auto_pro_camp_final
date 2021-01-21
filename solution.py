#!/usr/bin/python3

import sys
import os
from os.path import join, dirname
import subprocess
from tools.params import load_params
from tools.remote_cmd import *



def main():
    p = load_params()
    # print(p)
    trace_b_log(p)
    create_dummy_file(p)
    remove_dummy_file(p)


if __name__ == '__main__':
    main()

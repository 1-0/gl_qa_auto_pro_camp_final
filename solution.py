#!/usr/bin/python3

import sys
import os
from os.path import join, dirname
import paramiko
from tools.params import load_params


def trace_log(path):
    pass


def main():
    p = load_params()
    print(p)
    trace_log(p)


if __name__ == '__main__':
    main()

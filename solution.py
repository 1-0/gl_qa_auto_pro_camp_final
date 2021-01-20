#!/usr/bin/python3

import argparse
import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv
import paramiko


def trace_log(path):
    pass


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Process testing 2 ways of linux mashins connections')
    parser.add_argument(
                        '-f', '--test_file', required=False, 
                        metavar='test_file', type=str, 
                        help='file name for testing connection speed'
                       )
    parser.add_argument(
                        '-s', '--test_file_size', required=False, 
                        metavar='test_file_size', type=float, 
                        help='file size in Mb, generated (if no test_file) for testing connection speed'
                       )
    parser.add_argument(
                        '-l2', '--linux2', required=False, 
                        metavar='linux2', type=str, 
                        help='linux 2 machine address'
                       )
    parser.add_argument(
                        '-p2', '--port2', required=False, 
                        metavar='port2', type=int, 
                        help='linux 2 machine ssh connection port'
                       )
    args = parser.parse_args()
    if args.test_file:
        test_file = args.test_file
    elif os.getenv("TEST_FILE"):
        test_file = os.getenv("TEST_FILE")
    else:
        test_file = None
    if args.test_file_size:
        test_file_size = args.test_file_size
    elif os.getenv("TEST_FILE_SIZE"):
        test_file_size = float(os.getenv("TEST_FILE_SIZE"))
    else:
        test_file_size = 100
    if args.linux2:
        linux2 = args.linux2
    elif os.getenv("LINUX2"):
        linux2 = os.getenv("LINUX2")
    else:
        linux2 = "Linux-B"
    if args.port2:
        port2 = args.port2
    elif os.getenv("PORT2"):
        port2 = int(os.getenv("PORT2"))
    else:
        port2 = 22

    print([test_file, test_file_size, linux2, port2])
    trace_log(linux2)
    


if __name__ == '__main__':
    main()

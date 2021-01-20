"""
The params module load and return param from:
 - command line args
 - .env file
 - default values

>>> import argparse; from dotenv import load_dotenv
>>> load_dotenv(); p = argparse.ArgumentParser(); a = p.parse_args()
True
>>> load_param(a, "test_file", str, "test_file.bin")
'test_file.bin'
>>> load_param(a, "test_file", str, None)
"""


import argparse
import os
from dotenv import load_dotenv


def load_param(args, param_name, param_type, default=None):
    """load_param - load and return param from args or .env or default"""
    try:  # for python38 and python39
        if getattr(args, param_name.lower()) is not None:
            return getattr(args, param_name.lower())
    except AttributeError:
        pass
    if os.getenv(param_name.upper()):
        return param_type(os.getenv(param_name.upper()))
    return default


def load_params():
    """load_params - load and return params dictionary"""

    res = {}
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Process testing 2 ways of linux mashins connections'
    )
    parser.add_argument(
        '-f', '--test_file', required=False,
        metavar='test_file', type=str,
        help='file name for testing connection speed'
    )
    parser.add_argument(
        '-s', '--test_file_size', required=False,
        metavar='test_file_size', type=float,
        help=('file size in Mb, generated ' +
              '(if no test_file) for testing connection speed')
    )
    parser.add_argument(
        '-l1', '--linux1', required=False,
        metavar='linux1', type=str,
        help='linux A machine address'
    )
    parser.add_argument(
        '-p1', '--port1', required=False,
        metavar='port1', type=int,
        help='linux A machine ssh connection port'
    )
    parser.add_argument(
        '-l2', '--linux2', required=False,
        metavar='linux2', type=str,
        help='linux B machine address'
    )
    parser.add_argument(
        '-p2', '--port2', required=False,
        metavar='port2', type=int,
        help='linux B machine ssh connection port'
    )

    args = parser.parse_args()
    res["test_file"] = load_param(args, "test_file", str)
    res["test_file_size"] = load_param(args, "test_file_size", float, 100.)
    res["linux1"] = load_param(args, "linux1", str, "Linux-A")
    res["port1"] = load_param(args, "port1", int, 22)
    res["user1"] = load_param(args, "user1", str, "ubuntu")
    res["password1"] = load_param(args, "password1", str)
    res["linux2"] = load_param(args, "linux2", str, "Linux-B")
    res["port2"] = load_param(args, "port2", int, 22)
    res["user2"] = load_param(args, "user2", str, "ubuntu")
    res["password2"] = load_param(args, "password2", str)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

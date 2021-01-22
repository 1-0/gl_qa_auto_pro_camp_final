#!/usr/bin/python3

"""
The params module load param from:
 - command line args
 - .env file
 - default values
"""


import argparse
import os
from dotenv import load_dotenv


class ParamsHolder:
    """ParamsHolder - class for holding params"""

    params = {
              "test_file":      [str, None],
              "test_file_size": [int, 100],
              "linux1":         [str, "Linux-A"],
              "port1":          [int, 22],
              "user1":          [str, "ubuntu"],
              "password1":      [str, ""],
              "linux2":         [str, "Linux-B"],
              "port2":          [int, 22],
              "user2":          [str, "ubuntu"],
              "password2":      [str, ""],
              "logs_folder":    [str, "./"],
              }


    def load_param(self, args, param_name, param_type, default=None):
        """load_param - load param
        from args or .env or default"""

        try:  # for python38 and python39
            if getattr(args, param_name) is not None:
                setattr(self, param_name, getattr(args, param_name))
                return
        except AttributeError:
            pass
        if os.getenv(param_name.upper()):
            setattr(
                    self,
                    param_name,
                    param_type(os.getenv(param_name.upper()))
                    )
            return
        setattr(self, param_name, default)


    @staticmethod
    def get_parser():
        """get_parser - create parser for command-line options"""

        description = 'Process testing 2 ways of Linux-PC connections'
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            '-l', '--log_folder', required=False,
            metavar='log_folder', type=str,
            help='folder to save log files'
        )
        parser.add_argument(
            '-f', '--test_file', required=False,
            metavar='test_file', type=str,
            help='file name for testing connection speed'
        )
        parser.add_argument(
            '-s', '--test_file_size', required=False,
            metavar='test_file_size', type=int,
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
        return parser


    def __init__(self):
        """__init__ - load params"""

        parser = self.get_parser()
        args = parser.parse_args()
        load_dotenv()
        for k in self.params:
            self.load_param(
                            args,
                            k,
                            self.params[k][0],
                            self.params[k][1],
                            )


if __name__ == '__main__':
    ph = ParamsHolder()
    print(ph)
    for i in ph.params:
        print([i, getattr(ph, i)])

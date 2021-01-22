#!/usr/bin/python3

from tools.remote_cmd import CommandsRunner


def main():
    cr = CommandsRunner()
    cr.run_sequence()


if __name__ == '__main__':
    main()

#!/usr/bin/python3

import logging
from tools.remote_cmd import CommandsRunner


def main():
    cr = CommandsRunner()
    logging.basicConfig(
        format='[%(levelname)s]%(asctime)s:\n%(message)s',
        filename=f'{cr.params.logs_folder}summary.log',
        level=logging.INFO,
    )
    cr.run_sequence()


if __name__ == '__main__':
    main()

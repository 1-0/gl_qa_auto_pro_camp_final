#!/usr/bin/python3

from tools.params import ParamsHolder
from tools.remote_cmd import CommandsRunner


def setup_topology(p):
    pass


def restore_topology(p):
    pass


def main():
    ph = ParamsHolder()
    cr = CommandsRunner(ph)
    res = [cr.trace_b_log(), ]
    with open(f'{ph.logs_folder}2.log', 'w') as f:
        f.write(res[-1])
    cr.create_dummy_file()
    res.append(cr.send_dummy_file())
    with open(f'{ph.logs_folder}4.log', 'w') as f:
        f.write(res[-1])
    cr.remove_dummy_file()
    setup_topology(ph)
    res.append(cr.trace_b_log())
    with open(f'{ph.logs_folder}6.log', 'w') as f:
        f.write(res[-1])
    cr.create_dummy_file()
    res.append(cr.send_dummy_file())
    with open(f'{ph.logs_folder}8.log', 'w') as f:
        f.write(res[-1])
    cr.remove_dummy_file()
    restore_topology(ph)
    # print(res)
    with open(f'{ph.logs_folder}summary.log', 'w') as f:
        f.write('\n\n'.join(res))


if __name__ == '__main__':
    main()

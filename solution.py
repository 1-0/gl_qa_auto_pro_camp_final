#!/usr/bin/python3

from tools.params import load_params
from tools.remote_cmd import (
        trace_b_log,
        create_dummy_file,
        send_dummy_file,
        remove_dummy_file,
        )


def setup_topology(p):
    pass


def restore_topology(p):
    pass


def main():
    p = load_params()
    res = [trace_b_log(p), ]
    with open(f'{p["logs_folder"]}2.log', 'w') as f:
        f.write(res[-1])
    create_dummy_file(p)
    res.append(send_dummy_file(p))
    with open(f'{p["logs_folder"]}4.log', 'w') as f:
        f.write(res[-1])
    remove_dummy_file(p)
    setup_topology(p)
    res.append(trace_b_log(p))
    with open(f'{p["logs_folder"]}6.log', 'w') as f:
        f.write(res[-1])
    create_dummy_file(p)
    res.append(send_dummy_file(p))
    with open(f'{p["logs_folder"]}8.log', 'w') as f:
        f.write(res[-1])
    remove_dummy_file(p)
    restore_topology(p)
    print(res)
    with open(f'{p["logs_folder"]}summary.log', 'w') as f:
        f.write('\n\n'.join(res))


if __name__ == '__main__':
    main()

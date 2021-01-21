"""
The remote_cmd module:

Connect to remote device and run shell command
"""


# import sys
# import os
# from os.path import join, dirname
# import subprocess
import paramiko


def connect_a(hostname, port, username, password, command='ls -l'):
    with paramiko.SSHClient() as client:
        client.load_system_host_keys()
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password
        )
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        return stdout.read().decode()[:]


def trace_b_log(p):
    return connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command='/usr/bin/tracepath ' + p["linux2"]
    )


def create_dummy_file(p):
    return connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command=f"dd if=/dev/urandom of=.dummy.file bs=1M count={p['test_file_size']} ; ls -al .dummy.file"
    )


def remove_dummy_file(p):
    return connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command=f"rm -v .dummy.file"
    )


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    from params import load_params
    p = load_params()
    trace_b_log(p)
    create_dummy_file(p)
    remove_dummy_file(p)

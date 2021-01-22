#!/usr/bin/python3

"""
The remote_cmd module:

Connect to remote device and run shell command
"""


import paramiko
from datetime import datetime


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
        out = stdout.read().decode() + str(stderr.read().decode())
        print(out)
    return out


def trace_b_log(ph):
    command = '/usr/bin/tracepath ' + ph.linux2
    r = connect_a(
        hostname=ph.linux1,
        port=ph.port1,
        username=ph.user1,
        password=ph.password1,
        command=command
    )
    return " -\n".join([datetime.now().isoformat(), command, r])


def create_dummy_file(ph):
    command = (f"dd if=/dev/urandom of=.dummy.file" +
               f" bs=1M count={ph.test_file_size}")
    return connect_a(
        hostname=ph.linux1,
        port=ph.port1,
        username=ph.user1,
        password=ph.password1,
        command=command
    )


def send_dummy_file(ph):
    command = (f"time $(sshpass -p {ph.password2}" +
    f" scp .dummy.file scp://{ph.user2}@{ph.linux2}:{ph.port2})")
    r = connect_a(
        hostname=ph.linux1,
        port=ph.port1,
        username=ph.user1,
        password=ph.password1,
        command=command
    )
    return " -\n".join([datetime.now().isoformat(), command, r])


def remove_dummy_file(ph):
    return connect_a(
        hostname=ph.linux1,
        port=ph.port1,
        username=ph.user1,
        password=ph.password1,
        command=f"rm -v .dummy.file"
    )


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    from params import ParamsHolder
    ph = ParamsHolder()
    trace_b_log(ph)
    create_dummy_file(ph)
    send_dummy_file(ph)
    remove_dummy_file(ph)
    trace_b_log(ph)
    create_dummy_file(ph)
    send_dummy_file(ph)
    remove_dummy_file(ph)

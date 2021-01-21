"""
The remote_cmd module:

Connect to remote device and run shell command
"""


import paramiko
import datetime


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
        #print(str(stderr.read().decode()))
    return out


def trace_b_log(p):
    command = '/usr/bin/tracepath ' + p["linux2"]
    r = connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command=command
    )
    return " -\n".join([datetime.datetime.now().isoformat(), command, r])


def create_dummy_file(p):
    return connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command=f'dd if=/dev/urandom of=.dummy.file bs=1M count={p["test_file_size"]}'
    )


def send_dummy_file(p):
    command = f'time $(sshpass -p {p["password2"]} scp .dummy.file scp://{p["user2"]}@{p["linux2"]}:{p["port2"]})'
    r = connect_a(
        hostname=p["linux1"],
        port=p["port1"],
        username=p["user1"],
        password=p["password1"],
        command=command
    )
    return " -\n".join([datetime.datetime.now().isoformat(), command, r])


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
    send_dummy_file(p)
    remove_dummy_file(p)
    trace_b_log(p)
    create_dummy_file(p)
    send_dummy_file(p)
    remove_dummy_file(p)

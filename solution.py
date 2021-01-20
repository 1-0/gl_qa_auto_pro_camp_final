#!/usr/bin/python3

import sys
import os
from os.path import join, dirname
import subprocess
import paramiko
from tools.params import load_params


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



def trace_log(url):
    # return subprocess.check_output(['/usr/bin/tracepath', url]).decode()
    pass


def main():
    p = load_params()
    # print(p)
    # print(trace_log(p["linux2"]))
    connect_a(
        hostname=p["linux1"], 
        port=p["port1"], 
        username=p["user1"], 
        password=p["password1"],
        command='/usr/bin/tracepath ' + p["linux2"]
        )


if __name__ == '__main__':
    main()

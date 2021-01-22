#!/usr/bin/python3

"""
The remote_cmd module:

Connect to remote device and run shell command
"""


from paramiko import SSHClient
from datetime import datetime
from .params import ParamsHolder


class CommandsRunner:

    commands = {

    }

    def __init__(self, params=None):
        if params:
            self.params = params
        else:
            self.params = ParamsHolder()

    def connect_a(self, command='ls -l'):

        with SSHClient() as client:
            client.load_system_host_keys()
            client.connect(
                hostname=self.params.linux1,
                port=self.params.port1,
                username=self.params.user1,
                password=self.params.password1
            )
            stdin, stdout, stderr = client.exec_command(command)
            out = stdout.read().decode() + str(stderr.read().decode())
            print(out)
        return out

    def trace_b_log(self):
        command = '/usr/bin/tracepath ' + self.params.linux2
        r = self.connect_a(command=command)
        return " -\n".join([datetime.now().isoformat(), command, r])

    def create_dummy_file(self):
        command = (f"dd if=/dev/urandom of=.dummy.file" +
                   f" bs=1M count={self.params.test_file_size}")
        return self.connect_a(command=command)

    def send_dummy_file(self):
        command = (f"time $(sshpass -p {self.params.password2}" +
                   f" scp .dummy.file scp://{self.params.user2}" +
                   f"@{self.params.linux2}:{self.params.port2})")
        r = self.connect_a(command=command)
        return " -\n".join([datetime.now().isoformat(), command, r])

    def remove_dummy_file(self):
        return self.connect_a(command=f"rm -v .dummy.file")


if __name__ == '__main__':
    ph = ParamsHolder()
    cr = CommandsRunner(ph)
    cr.trace_b_log()
    cr.create_dummy_file()
    cr.send_dummy_file()
    cr.remove_dummy_file()
    cr.trace_b_log()
    cr.create_dummy_file()
    cr.send_dummy_file()
    cr.remove_dummy_file()

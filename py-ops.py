#!/usr/bin/python3

#from __future__ import absolute_import, division, print_function

from getpass import getpass
import json
import netmiko
# from netmiko import ConnectHandler
# from netmiko.cisco import CiscoIosBase (device type: "cisco_ios", "cisco_xe")
# from netmiko.cisco import CiscoIosBase (device type: "cisco_xe")
import sys
import signal
import os
import time

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


def get_input(prompt=''):
    # try:
    #     line = raw_input(prompt)
    # except NameError:
    #     line = input(prompt)
    line = input(prompt)
    return line


def get_credentials():
    """Self-defined function to get your username/password."""
    username = get_input('Username(Please input your AD credentials): ')
    # password = None
    # while not password:
    #     password = getpass()
    #     password_verify = getpass ('Please retype your password:')
    #     if password != password_verify:
    #         print ('Passwords do not match. Please try again.')
    #         password = None
    password = getpass()
    return username, password


# netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
#                       netmiko.ssh_exception.NetMikoAuthenticationException)

netmiko_exceptions = netmiko.ssh_exception.NetMikoTimeoutException

os.system('clear')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# os.system('cd /home/jhu/PycharmProjects/netmiko/cmd-set-ops')
os.system('find /home/jhu/PycharmProjects/netmiko/cmd-set-ops/* |sed "s#.*/##"')
os.system('echo')
os.system('echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"')
command_file = input("Please select which ops command you want to run: \n\noperation command: ")
com_set = '/home/jhu/PycharmProjects/netmiko/cmd-set-ops/' + command_file

print()
print()
print('******************************')
# os.system('cd /home/jhu/PycharmProjects/netmiko/device-group')
os.system('find /home/jhu/PycharmProjects/netmiko/device-group/* |sed "s#.*/##"')  # remove path info
os.system('echo')
os.system('echo "******************************"')
device_group = input("Please select which device-group you want to apply to: \n\ndevice-group: ")
dev_grp = '/home/jhu/PycharmProjects/netmiko/device-group/' + device_group

username, password = get_credentials()
os.system('clear')
"""
Python will close the file immediately after the loop when using for line in 'with open'("filename"):, 
provided no further references to the file exist. In other Python implementations, closing the file 
may be delayed, but it will eventually be closed.
"""

with open(com_set) as cmd_file:
    commands = cmd_file.readlines()

with open(dev_grp) as dev_file:
    devices = json.load(dev_file)

for device in devices:
    device['username'] = username
    device['password'] = password
    file_name = command_file + ' of ' + device_group + '.rst'
    with open(file_name, 'a') as out_file:
        time.sleep(1)
        try:
            print('~' * 80)
            print('~' * 80, file=out_file)

            print('Connecting to device:', str.lstrip(device['ip']))
            print('Connecting to device:', str.lstrip(device['ip']), file=out_file)

            connection = netmiko.ConnectHandler(**device)
            time.sleep(1)

            for command in commands:
                print('\nRunning:\n' + command + '\nOutput: ')
                print('\nRunning:\n' + command + '\nOutput: ', file=out_file)

                print(connection.send_command(command))
                print(connection.send_command(command), file=out_file)
                time.sleep(1)
                """To keep 2 lines space between 2 devices"""
                print()
                print()


                #        with open(file_name, 'w') as out_file:
                #            out_file.write(connection.send_command(command))
            connection.disconnect()
        except netmiko_exceptions as e:
            print('Failed to ', device['ip'], e)
    #    sys.exit()

os.system('mv *.rst cmd-set-ops-result')
os.system('echo')
os.system('echo "   ************************************************************************"')
os.system('echo "    The result file has been saved in the the folder of cmd-set-ops-result"')
os.system('echo "   ************************************************************************"')
os.system('echo')
os.system('echo')
# """To close the opened file explicitly is a good habit."""
# cmd_file.close()
# dev_file.close()

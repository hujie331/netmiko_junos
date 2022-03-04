#!/usr/bin/python3

#from __future__ import absolute_import, division, print_function
#At the time of this writing(03/03/2022), this script works fine!
#Copyright: hujie.331@gmail.com
from getpass import getpass
import json
import netmiko
# from netmiko import ConnectHandler
import sys
import signal
import os
import time

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C

def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def get_input(prompt=''):
    # try:
    #     line = raw_input(prompt)
    # except NameError:
    #     line = input(prompt)
    line = input(prompt)
    return line


def get_credentials():
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
os.system('find /home/jhu/PycharmProjects/netmiko/cmd-set-cfg/* |sed "s#.*/##"')  # remove path info
os.system('echo')
os.system('echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"')
command_file = input("Please select which cfg command you want to run: \n\noperation command: ")
com_set = '/home/jhu/PycharmProjects/netmiko/cmd-set-cfg/' + command_file
print()
print()
print('******************************')
os.system('find /home/jhu/PycharmProjects/netmiko/device-group/* |sed "s#.*/##"')  # remove path info
os.system('echo')
os.system('echo "******************************"')
device_group = input("Please select which device-group you want to apply to: \n\ndevice-group: ")
dev_grp = '/home/jhu/PycharmProjects/netmiko/device-group/' + device_group

username, password = get_credentials()
os.system('clear')

with open(com_set) as cmd_file:
    commands = cmd_file.readlines()

with open(dev_grp) as dev_file:
    devices = json.load(dev_file)

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print('~' * 80)
        print('Connecting to device:', str.lstrip(device['ip']))
        connection = netmiko.ConnectHandler(**device)

        for command in commands:
            print_one_by_one(f'Running this command: {command}')
            connection.send_config_set(command, exit_config_mode=False)
        print()
        print_one_by_one('Committing......\n')
        connection.commit()
        time.sleep(3)
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device['ip'], e)

print()
print("    ************************************************************************")
print_one_by_one("     The script has been executed, please log in to the device(s) to verify\n")
print("    ************************************************************************")
print()

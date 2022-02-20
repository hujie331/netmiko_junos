#!/usr/bin/env python

#from __future__ import absolute_import, division, print_function

from getpass import getpass
import json
import netmiko
#from netmiko import ConnectHandler
#from netmiko.cisco import CiscoIosBase (device type: "cisco_ios", "cisco_xe")
#from netmiko.cisco import CiscoIosBase (device type: "cisco_xe")
import sys
import signal
import os
import time
#import commands

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C

def get_input(prompt=''):
    line = input(prompt)
    # try:
    #     line = raw_input(prompt)
    # except NameError:
    #    line = input(prompt)
    return line

def get_credentials():
    """Self-defined function to get your username/password."""
    username = get_input('Username(Please input your AD credentials): ')
    password = getpass()
    return username, password

# netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
#                       netmiko.ssh_exception.NetMikoAuthenticationException)

netmiko_exceptions = netmiko.ssh_exception.NetMikoTimeoutException

#os.system('clear')
username, password = get_credentials()

#str =os.popen('ls *.json).read
#a = str.split('\n')
#for b in a
#    print b
#os.system(' ls *.json ')
#os.system('echo')
#p = os.popen("ls -l *.json | awk '{ print $9 }'", 'r')
#print('p.read()')
#p.close()
#commands.getstatusoutput('ls *.json')
#subprocess.check_output([ls -l *json | awk { print $9 }])
print()
print()
print('^' * 30)
os.system('find /home/jhu/PycharmProjects/netmiko/device-group/* |sed "s#.*/##"')
os.system('echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"')
#devicegroup = raw_input("Please select what device-group you want to backup: \n\ndevice-group: ")
device_group = input("Please select what device-group you want to backup \n\ndevice-group: ")
dev_grp = '/home/jhu/PycharmProjects/netmiko/device-group/' + device_group

os.system('clear')
with open(dev_grp) as dev_file:
    devices = json.load(dev_file)

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print('~' * 80)
        print('Connecting to device:', device['ip'])
        connection = netmiko.ConnectHandler(**device)
#        filename = connection.base_prompt + '.cfg'
        filename = device['ip'] + '.cfg'
#        print()
#        print('"' + filename + '"' + ' has been saved')
        time.sleep(2)
        print()
        print()
        with open(filename, 'w') as out_file:
#            print(connection.send_command('terminal length 0'))
#            out_file.write(connection.send_command('show running-config') + '\n\n')
            out_file.write(connection.send_command('show configuration | no-more') + '\n\n')
        print()
        print('"' + filename + '"' + ' has been saved')
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device['ip'], e)

folder = 'cfg-bk-for-' + device_group
os.system('mkdir %s ' %(folder))
os.system('mv *.cfg %s' %(folder))
os.system('echo')
os.system('echo "       **************************************************************"')
os.system('echo "        All cfg-bk files have been saved in the corresponding folder"')
os.system('echo "       **************************************************************"')
os.system('echo')
os.system('echo')

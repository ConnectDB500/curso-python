from netmiko import ConnectHandler

import datetime

time_now = datetime.datetime.now().isoformat(timespec="seconds")

def read_from_filename(filename):
  with open(filename) as f:
    lines = f.read().splitlines()
    return lines

def connect_and_check(config_lines, devices_lines):
  for IP in devices_lines:
    device = {
      "device_type": "cisco_ios",
      "ip": IP,
      "username": "cisco",
      "password": "cisco"
    }

  net_connect = ConnectHandler(**device)

  file = open (IP + "_output.txt", "w")

  for command in config_lines:
    print("-" * 30)
    cmd_output = net_connect.send_command(command)
    print(cmd_output)
    print("\n")
    file.write("\n")
    file.write("-" * 30)
    file.write("\n")
    file.write("\n")

  file.close()

config_lines = read_from_filename("commands.txt")

devices_lines = read_from_filename("devices.txt")

connect_and_check(config_lines, devices_lines)
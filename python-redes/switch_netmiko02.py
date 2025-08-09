from netmiko import ConnectHandler

iosv_12_s1 = {
  "device_type": "cisco_ios",
  "ip": "192.168.0.99",
  "username": "cisco",
  "password": "cisco"
}

iosv_12_s2 = {
  "device_type": "cisco_ios",
  "ip": "192.168.0.98",
  "username": "cisco",
  "password": "cisco"
}

iosv_12_s3 = {
  "device_type": "cisco_ios",
  "ip": "192.168.0.97",
  "username": "cisco",
  "password": "cisco"
}

with open("iosv_12_cisco_design.txt") as f:
  lines = f.read().splitlines()
print(lines)

all_devices = [iosv_12_s1, iosv_12_s2, iosv_12_s3]

for devices in all_devices:
  net_connect = ConnectHandler(**devices)
  output = net_connect.send_config_set(lines)
  print(output)
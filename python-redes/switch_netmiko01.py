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

all_devices = [iosv_12_s1, iosv_12_s2, iosv_12_s3]

for devices in all_devices:
  net_connect = ConnectHandler(**devices)
  for n in range(12, 17):
    print("Creating VLAN " + str(n)) 
    config_commands = ['vlan' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)

net_connect = ConnectHandler(**iosv_12)
output = net_connect.send_command("show ip int brief")
print(output)

for n in range(90, 100):
  print("Creating VLAN " + str(n))
  config_commands = ["vlan " + str(n), "name Python_VLAN " + str(n)]
  output = net_connect.send_config_set(config_commands)
  print(output)


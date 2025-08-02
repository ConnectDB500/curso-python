from netmiko import ConnectHandler

iosv_12 = {
  'device_type': 'cisco_ios',
  'ip': '192.168.0.99',
  'username': 'cisco',
  'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_12)
output = net_connect.send_command('show ip int brief')
print(output)

for n in range(90, 100):
  print("Creating VLAN " + str(n))
  config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
  output = net_connect.send_config_set(config_commands)
  print(output)
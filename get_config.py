""" This program connects to our desired router/switch with SSH using the netmiko module.
    We hardcode the required credentials with the view that this program needs to run automatically on a daily basis,
    taking configurations from the Network device and saving it in the local device."""

from netmiko import ConnectHandler

def SSH():
	global ip
	global output
	
	
	# Device to monitor
	ip = '10.10.10.10'
	
	# Credentials details
	username = 'cisco'
	password = '123'
	
	# Device type for netmiko function
	device_type = 'cisco_ios'
	
	# Cisco command to retrieve configurations
	command = 'show running-config'
	
	# Lets connect to our device via SSH using netmiko
	session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password)
	
	# Entering enable mode
	enable = session.enable()
	
	# Sending our command
	output = session.send_command(command)
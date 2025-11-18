
from netmiko import ConnectHandler

cisco_router = {
	'device_type' : 'cisco_ios',
	'host' : 'sandbox-iosxr-1.cisco.com',
	'username' : 'admin',
	'password' : 'C1sco12345',
	'port' : 22,
}

ssh = ConnectHandler(**cisco_router)

def acces_netmiko():

	output1 = ssh.send_command('show clock')

	output = ssh.send_command('show ip int br')

print(result1)
with open ('interfaces.txt') as f:

	ssh.send_command('show ip int br')
	print(f.read())


def dire_salut():
	print("Salut, Git!")


dire_salut()

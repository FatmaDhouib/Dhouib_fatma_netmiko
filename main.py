
from netmiko import ConnectHandler
cisco_router = {
	'device_type' : 'cisco_ios',
	'host' : ' 'sandbox-iosxr-1.cisco.com',
	'username' : 'admin',
	'password' : 'C1sco12345',
	'port' : 22,
}
ssh = ConnectHandler(**cisco_router)

def acces_netmiko()

	result1 = ssh.send_command('show clock')

	result2 = ssh.send_command('show ip int br')> interfaces.txt


def dire_salut():
	print("Salut, Git!")


dire_salut()

Mon Projet Netmiko

I. Initialiser un dépôt Git local 

Create a new folder ‘Dhouib_fatma_netmiko’ 

Git init (initialize a repo) 

 

II. Ajouter et commiter des fichiers 

Nano README.MD 

Modifier le fichier (ajout de “hello git “) 

Git add . 

Git commit –m “Ajout de Readme.md” 

Nano main.py 

Git add . 

Gir commit –m “Ajout de script python principal” 

Git log 

III. Créer et fusionner des branches : 

Git checkout –b feature/netmiko 

Nano main.py 

******Script python ajoute: 

 	From netmiko import ConnectHandler 

	Cisco_router = { 

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
 

 

 

Git add . 

Git commit –m “Ajout de la fonction acces_netmiko” 

Git checkout master 

Git merge feature/netmiko 

 

IV. Travailler avec un dépôt distant sur GitHub 

		 

git remote add origin https://github.com/FatmaDhouib/Dhouib_fatma_netmiko.git 

 
git branch -M main 

git push -u origin main 

Git fetch origin 

Git checkout feature/salut 

***modification sur main.py (ajout de la fonction salut) 

Git add . 

Git commit –m “Ajout de la fonction feature/salut” 

Git push origin feature/salut 

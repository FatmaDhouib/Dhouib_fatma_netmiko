Mon Projet Netmiko



Commands used:



I. Initialiser un dépôt Git local 



Create a new folder ‘Dhouib\_fatma\_netmiko’ 



Git init (initialize a repo) 



&nbsp;



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



\*\*\*\*\*\*Script python ajoute: 



&nbsp;	From netmiko import ConnectHandler 



&nbsp;	Cisco\_router = { 



'device\_type' : 'cisco\_ios', 



&nbsp;'host' : ' 'sandbox-iosxr-1.cisco.com',  



'username' : 'admin', 



&nbsp;'password' : 'C1sco12345',  



'port' : 22, 



&nbsp;           }  



ssh = ConnectHandler(\*\*cisco\_router) 



def acces\_netmiko() 



&nbsp; result1 = ssh.send\_command('show clock') 

&nbsp;

&nbsp;  result2 = ssh.send\_command('show ip int br')> interfaces.txt 

&nbsp;



&nbsp;



&nbsp;



Git add . 



Git commit –m “Ajout de la fonction acces\_netmiko” 



Git checkout master 



Git merge feature/netmiko 



&nbsp;



IV. Travailler avec un dépôt distant sur GitHub 



&nbsp;		 



git remote add origin https://github.com/FatmaDhouib/Dhouib\_fatma\_netmiko.git 



&nbsp;

git branch -M main 

&nbsp;



git push -u origin main 



&nbsp;



Git fetch origin 



Git checkout feature/salut 



\*\*\*modification sur main.py (ajout de la fonction salut) 



Git add . 



Git commit –m “Ajout de la fonction feature/salut” 



Git push origin feature/salut 


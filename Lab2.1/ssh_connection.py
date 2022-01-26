import paramiko
import time

BUF_SIZE = 2000
TIMEOUT = 1

#create ssh-connection
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host_url = 'http://10.31.70.209/'
ssh_connection.connect(host_url, username='restapi', password='j0sg1280-7@', look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT*1)


session.send("\n")
session.recv(BUF_SIZE)
session.send("show run\n")
time.sleep(TIMEOUT*2)
s = session.recv(BUF_SIZE).decode()

session.close()

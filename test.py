import paramiko
from getpass import getpass
import time

ip = input("Please enter your IP address: ")
username = input("Please enter your username: ")
password = getpass()
hostname=input("Please enter the devices new name: ")

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,  
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)

remote_conn.send("conf t\n")
time.sleep(.5)
output = remote_conn.recv(65535)
#print =(output)

hostname1="hostname "+hostname+"\n"
remote_conn.send(hostname1)
time.sleep(.5)

remote_conn.send("end\n")
time.sleep(.5)

remote_conn.send("wr\n")
time.sleep(.5)

remote_conn.close()

print("#------------------------------------\nThe new device name is :"+hostname+"\n")


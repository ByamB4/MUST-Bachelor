from pwn import *
import paramiko

HOSTNAME = '192.168.33.10'
USERNAME = 'vagrant'
PASSWORD = 'vagrant'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=HOSTNAME, username=USERNAME, password=PASSWORD)
success('Successfully connected')
print('[D]ownload file from remote server')
print('[U]pload file to remote server')

_ = input(': ')

if 'D' in _:
    ftp_client = ssh_client.open_sftp()

    ftp_client.get(
        '/home/vagrant/copyme', 'copiedfile')
    ftp_client.close()
else:
    ftp_client = ssh_client.open_sftp()
    ftp_client.put('toupload', '/home/vagrant/toupload')
    ftp_client.close()

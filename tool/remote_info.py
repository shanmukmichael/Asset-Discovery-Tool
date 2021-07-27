import socket
import paramiko
import json

Hostname = '34.224.2.243'
Username = 'ec2-user'
key = 'G:/Projects/Python/Asset-Discovery-Tool/tool/s.pem'


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("8.8.8.8", 53))
        return "conneted to the Internet!"
    except OSError:
        pass
    return "Please Connect to the Internet!"


is_connected()
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Hostname, username=Username, key_filename=key)
except paramiko.AuthenticationException:
    print("Failed to connect to {} due to wrong username/password".format(Hostname))
    exit(1)
except:
    print("Failed to connect to {} ".format(Hostname))
    exit(2)

# commands
_, stdout_1, _ = ssh.exec_command("hostname")
_, stdout_2, _ = ssh.exec_command("hostname -I | awk '{print $1}'")
_, stdout_3, _ = ssh.exec_command("cat /sys/class/net/eth0/address")
_, stdout_4, _ = ssh.exec_command(
    "awk -F= '$1=={} {{ print $2 ;}}' /etc/os-release".format('"NAME"'))
_, stdout_5, _ = ssh.exec_command("whoami")
_, stdout_6, _ = ssh.exec_command("last -F")
_, stdout_7, _ = ssh.exec_command("netstat -tnpa | grep 'ESTABLISHED.*sshd'")
#_, stdout_8, _ = ssh.exec_command("sudo {}/24".format())
#  egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}' --IP-address
# ---------------------------------


def remote_data_1():
    output_1 = stdout_1.readlines()
    output_2 = stdout_2.readlines()
    output_3 = stdout_3.readlines()
    output_4 = stdout_4.readlines()
    output_5 = stdout_5.readlines()
    remote_data_1 = {
        'Hostname': '',
        'IP': '',
        'MAC': '',
        'OS': '',
        'Currentuser': '',
    }

    remote_data_1['Hostname'] = output_1[0].strip('\n')
    remote_data_1['IP'] = output_2[0].strip('\n')
    remote_data_1['MAC'] = output_3[0].strip('\n')
    remote_data_1['OS'] = output_4[0][1:-1].strip('\"')
    remote_data_1['Currentuser'] = output_5[0].strip('\n')

    return json.dumps(remote_data_1, indent=4)

# ----------------------------------


def remote_data_2_():
    output = stdout_6.readlines()
    data_ = []
    filter_ = []
    remote_data_2 = {
        'Hostname': [],
        'IP': [],
        'MAC': [],
        'Lastseen': [],
        'Status': [],
    }

    for i in output:
        data_.append(i.split(' '))

    for i in data_:
        filter_.append(list(filter(None, i)))

    for i in range(len(filter_)-3):
        remote_data_2['Hostname'].append(filter_[i][0])
        remote_data_2['IP'].append(filter_[i][2])
        remote_data_2['MAC'].append('not found')
        remote_data_2['Lastseen'].append(' '.join(filter_[i][3:8]))
        if 'logged' in filter_[i][9]:
            remote_data_2['Status'].append('Active')
        else:
            remote_data_2['Status'].append('Inactive')
        # ssh.close()
    return remote_data_2

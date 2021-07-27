from getmac import get_mac_address as mac
import socket
import json
import os
import platform

#Works Both Windows & Linux 

def local_data_1():
    local_data_1 = {
        'Hostname': '',
        'IP': '',
        'MAC': '',
        'OS': '',
        'Currentuser':'',
    }

    try:
        host_name = socket.gethostname()
        local_data_1['Hostname'] = host_name
    except:
        local_data_1['Hostname'] = '-'

    try:
        local_ip = ([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
                    for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        local_data_1['IP'] = local_ip
    except:
        local_data_1['IP'] = '-'

    try:
        local_data_1['MAC'] = str(mac())
    except:
        local_data_1['MAC'] = '-'

    try:
        os_ = platform.uname()[0].lower()
        #os_ = platform.platform()
        local_data_1['OS'] = os_
    except:
        local_data_1['OS'] = '-'

    try:
        current_user = os.getlogin()
        local_data_1['Currentuser'] = current_user
    except:
        local_data_1['Currentuser'] = '-'

    print(json.dumps(dict(local_data_1), indent=4))

    return  json.dumps(dict(local_data_1), indent=4)

   

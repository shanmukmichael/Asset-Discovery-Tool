import platform
import local_info
import remote_info

system = platform.system().lower()

## Local System

if system == 'windows':
    local_info.local_data_1()

elif system == 'linux' or 'linux2':
    local_info.local_data_1()

else:
    print("Can't determine OS!!!")

## Remote System | SSH
    

# Place to import modules
import hashlib
import os
#import time 


# global declarations
os.environ['version']=''

def get_hash(filename):
    hash=hashlib.md5()
    with open (filename, 'rb') as f:
        file_content = f.read()
        hash.update(file_content)
        file_hash = hash.hexdigest()
        f.close()
        return file_hash

def read_file(file):
    file_object = open(file, "r")
    file_content = file_object.read()
    file_object.close()
    return(file_content)

def check_version(file, version):
    if(get_hash(file) == version):
        return False
    else:
        os.environ['version'] = get_hash(file)
        return(True) 
file="ssh-log"
if(check_version(file, os.getenv('version'))):
    os.system('last >ssh-log')
    data=read_file(file)
    print(data)
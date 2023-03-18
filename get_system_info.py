import platform
import socket
import re
import cpuinfo
import psutil
import os
import uuid
import json
import logging
from create_hash import create_hash
from screeninfo import get_monitors
import nmap
import ipaddress

def screen_resolution(): 
    for m in get_monitors():
            if m.is_primary: 
                resolution = [int(m.width), int(m.height)]
    return resolution

def get_ip_addr(): 
    # ip = ip = requests.get('https://checkip.amazonaws.com').text.strip()
    ip  = os.popen('curl -s ifconfig.me').readline()
    return ip
    
def number_of_open_ports(): 
    # t_IP = str(socket.gethostbyname(socket.gethostname())) # to get ip address of servser
    t_IP = "127.0.0.1" # to get ip address of servser
    # print ('Starting scan on host: ', t_IP)    
    open_port = []
    for i in range(1, 8000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            open_port.append(i)
        s.close()
    return open_port


# Collect all system information data from user system and sent to server ip address
def get_system_info(*args):
    try:
        hash = create_hash()
        resolution = screen_resolution()
        print(resolution)
        open_ports = number_of_open_ports()
        info = {
            "platform": str(platform.system()), "platform_release": str(platform.release()),
            "platform_version": str(platform.version()), "architecture": str(platform.machine()),
            "hostname": str(socket.gethostname()), 
            # "ip_address": str(socket.gethostbyname(socket.gethostname())),
            "ip_address": str(get_ip_addr()),
            "mac": str(":".join(re.findall("..", '%012x' % uuid.getnode()))),
            "processor": str(cpuinfo.get_cpu_info()["brand_raw"]),
            "ram": str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB",
            "number_of_core": str(os.cpu_count()),  # comment for testing
            "app_hash": hash, 
            "screen_resolution": resolution,
            "open_ports": open_ports,
            "cname": args[0]
            # "platform_model": args[0], "platform_serial_number": args[1],
            # "is_vm": args[2],
            # "processor-manufacturer": args[3]
        }
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

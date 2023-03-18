from tkinter import messagebox
# import selenium.common.exceptions
from open_browser import open_browser
from dotenv import load_dotenv
import os
from config import *
import get_system_info
from vm_detection import virtual_machine
import requests
import json
load_dotenv()  # take environment variables from .env.


# option to detection virtual machine
vmd_1 = "model_detection"
vmd_2 = "serial_detection"
vmd_3 = "pm_detection"
vmd_4 = "imvirt_detection"
vmd_5 = "vmd_by_facter_virtual"
vmd_6 = "systemd_detection_virt_detection"
vmd_7 = "lspci_detection"
vmd_8 = "virt_what_detection"
vmd_9 = "lsusb_detection"
vmd_10 = "lshw_detection"
vmd_11 = "lscpu_detection"
# protocol = "http://"
# protocol = os.getenv('HOST')

# From EXAM MODE it will open isolate chrome browser with SERVER IP ADDRESS AND COMPUTER ID.
def clicked_from_exam_mode(firstsubnet, secondsubnet, thirdsubnet, fourthsubnet, computerid, protocol, url_value, is_url):
    url_value = url_value.get().strip()
    if is_url and url_value != "" or not is_url and firstsubnet.get() != '' and secondsubnet.get() != '' and thirdsubnet.get() != '' and fourthsubnet.get() != '':
        if is_url: 
            serverip = url_value
        else:
            serverip = firstsubnet.get().strip() + "." + secondsubnet.get() .strip() + "." + \
                   thirdsubnet.get().strip() + "." + fourthsubnet.get().strip()
        
        if computerid.get() != '':
            computer_id = computerid.get().strip()  # get computer id from computer id fields
            # print(computer_id)
            if protocol.get() != "Select Protocol":
                protocol = protocol.get().lower()
                url = protocol + "://" + serverip + "/api/v1/lab/device"# server ip address url with http
                
                try:
                    ''' 1. Here you can plug virtual machine detection method which you want. 
                        By default here all method are plug you can change it by removing from here.'''

                    ''' 2. virtual_machine() return list of containing True or False values. If list contain all False value 
                        then it means machine in physical or if it contain alteast one True value it means machine is virtual'''

                    is_vm = virtual_machine(vmd_1, vmd_2, vmd_3, vmd_4, vmd_5, vmd_6, vmd_7,vmd_8, vmd_9, vmd_10, vmd_11)
                    # print(is_vm)

                    # To get system information json data from get_system_info function
                    system_info_data = get_system_info.get_system_info(computer_id)

                    # It send all system information to the server using post method
                    headers = {'Content-type': 'application/json'}
                    r = requests.post(url , data=system_info_data, headers=headers)  # send json data to server ip address
                    resp = r.json()  # response from backend
                    nixcad_url = resp["url"] + "/checkServer?url=" + serverip
                    # print(nixcad_url)
                    ''' if data successfully sent to server then status code is 200 otherwise we will get Error message
                        Server Refused To Connect '''
                    if r.status_code == 200:
                        ''' if all condition are satisfied then only browser will open otherwise it will return message
                        "Your system not supported" '''
                        # print(is_vm, "vm")
                        if "PackageError" not in is_vm:
                            if True not in is_vm:
                                open_browser(nixcad_url)  # open isolate chrome browser in kiosk mode
                            else:
                                messagebox.showerror("Virtual Error", "Your System Not Supported !!!")
                        else:
                            messagebox.showerror("Package Error", "Connection Failed!!!\nPackage Not Found")
                    else:
                        messagebox.showerror("Server Error", "Oops!!! \nServer Refused To Connect")

                except Exception as e:
                    print(e)
                    messagebox.showerror("IP Address Error", "Connection not established.\nPlease Enter Correct IP Address")
            else: 
                messagebox.showerror("Error", "Please Select Protocol")
        else:
            messagebox.showerror("Error", "Invalid Computer Id")
    else:
        messagebox.showerror("Error", "Incorrect Server IP Address")

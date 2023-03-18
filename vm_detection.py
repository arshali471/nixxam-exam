import subprocess
import os
import platform

'''
To detect virtual machine there are some method used: 
1. 'vmd_by_product_name()' : It detect virtual machine using product name.

2. 'vmd_by_serial_number()' : If system is physical then some serial number come otherwise it get 0.

3. 'vmd_by_processor_manufacturer()' : If system is physical then it return processor manufacturer name but in case of 
    virtual machine it doesn't return anything.  
      
4. 'vmd_by_imvirt()' :  It return Physical when system is physical otherwise return KVM.
 
5. 'vmd_by_facter_virtual()' : It return physical when system is physical otherwise return kvm.

6. 'vmd_by_systemd_detect_virt()' : When system is physical then it return status 0 (none/error) and if system is
                                    virtual it 
    return non-zero (vendor name)
    
7. 'vmd_by_lspci()' : It detect virtual machine through 'VGA compatible controller / graphic card'.  
 
8. 'vmd_by_virt_what' : If nothing is printed and the script exits with code 0 (no error), then it can mean either that 
                        the program is running on bare-metal or the program is running inside a type of virtual machine 
                        which we don't know about or cannot detect.

9. 'vmd_by_lsusb' : It detect virtual machine by usb port.

10. 'vmd_by_lshw' : It is the most powerful virtual machine detection method. It checks all vendor and product related
                    information to detect virtual machine. 
                    
11. "vmd_by_lscpu" : It detect virtaul machine by using Hypervisor vendor. If machine is physical it raise error and 
                     if machine is virtual it return value kvm. 

Note: 
1. All the above code used to detect virtual machine only in linux platform. 
2.'imvirt' command doesn't come preinstalled by default we have to install using "sudo apt-get install imvirt" command. 
3. 'facter' command doesn't come preinstalled by default we have to install using "sudo apt-get install facter" command. 
4. 'lspci' command doesn't come preinstalled by default we have to install using "sudo apt-get install lspci" command. 
5. 'virt-what' command doesn't come preinstalled by default we have to install using "sudo apt-get install virt-what" command. 
6. 'lsusb' command doesn't come preinstalled by default we have to install using "sudo apt-get install lsusb" command. 
7. 'lshw' command doesn't come preinstalled by default we have to install using "sudo apt-get install lshw" command. 
8. All methods turn True or False. If system is physical it return False otherwise return True.
'''

virtual_machine_list = [
    "VirtualBox",
    "Standard PC (Q35 + ICH9, 2009)",
    "VMware SVGA II Adapter",
    "xen",
    "xen-domU",
    "kvm",
    "virtualbox",
    "vmware",
    "VBOX",
    "innotek GmbH"
]


# python default module to detect virtual machine
# vmd = VMDetect()
# virtual_machine = vmd.is_vm()


class CheckVirtualBox:
    system = platform.system()

    @staticmethod
    def vmd_by_product_name():
        system_procduct_name = str(subprocess.check_output("pkexec dmidecode -s system-product-name",
                                                           stderr=open(os.devnull, 'w'), shell=True))[2:-3]
        if system_procduct_name not in virtual_machine_list or system_procduct_name is not None:
            return False
        else:
            return True

    @staticmethod
    def vmd_by_serial_number():
        serial_number = str(subprocess.check_output("pkexec dmidecode -s system-serial-number",
                                                    stderr=open(os.devnull, 'w'), shell=True))[2:-3]
        if serial_number != "0":
            return False
        else:
            return True

    @staticmethod
    def vmd_by_processor_manufacturer():
        processor_manufacturer = str(subprocess.check_output("pkexec dmidecode -s processor-manufacturer",
                                                             stderr=open(os.devnull, 'w'),
                                                             shell=True))[2:-3]
        if processor_manufacturer != '':
            return False
        else:
            return True

    @staticmethod
    def vmd_by_imvirt():
        try:
            imvirt = str(subprocess.check_output("imvirt", stderr=open(os.devnull, 'w'), shell=True))[2:-3]
            if imvirt == "Physical":
                return False
            return True
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_facter_virtual():
        try:
            facter_virtual = str(subprocess.check_output("facter virtual", stderr=open(os.devnull, 'w'),
                                                         shell=True))[2:-3]
            if facter_virtual == "physical":
                return False
            return True
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_lspci():
        try:
            lspci_vm_detect = str(subprocess.check_output("lspci | grep 'VGA'", stderr=open(os.devnull, 'w'),
                                                          shell=True))[2:-3].split(":")[2].strip()
            if lspci_vm_detect not in virtual_machine_list:
                return False
            return True
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_systemd_detect_virt():
        try:
            systemd_detect_virt = str(subprocess.check_output("systemd-detect-virt",
                                                              stderr=open(os.devnull, 'w'),
                                                              shell=True))[2:-3]
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def vmd_by_virt_what():
        try:
            virt_what = str(subprocess.check_output("pkexec virt-what", stderr=open(os.devnull, 'w'),
                                                    shell=True))[2:-3]
            if virt_what not in virtual_machine_list:
                return False
            return True
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_lsusb():
        try:
            lsusb = str(subprocess.check_output("lsusb", stderr=open(os.devnull, 'w'), shell=True))[2:-3].lower()
            for vm_list in virtual_machine_list:
                if vm_list.lower() in lsusb:
                    return True
            return False
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_lshw():
        try:
            lshw = str(subprocess.check_output("pkexec lshw | egrep 'vendor|product'", stderr=open(os.devnull, 'w'),
                                               shell=True))[2:-3].lower()
            for vm_list in virtual_machine_list:
                if vm_list.lower() in lshw:
                    return True
            return False
        except subprocess.CalledProcessError:
            return "PackageError"

    @staticmethod
    def vmd_by_lscpu():
        try:
            lscpu = str(subprocess.check_output("lscpu | grep 'Hypervisor vendor'", stderr=open(os.devnull, 'w'),
                                                shell=True))[2:-3].split(":")[1].lower().strip()
            if lscpu in virtual_machine_list:
                return True
        except subprocess.CalledProcessError:
            return False


def virtual_machine(*args):
    """ Create object of vm_detection and call all methods to check virtual machine """
    virtual_box = CheckVirtualBox()
    vm_list = []
    if 'model_detection' in args:
        model_detection = virtual_box.vmd_by_product_name()
        vm_list.append(model_detection)
    if 'serial_detection' in args:
        serial_detection = virtual_box.vmd_by_serial_number()
        vm_list.append(serial_detection)
    if 'pm_detection' in args:
        pm_detection = virtual_box.vmd_by_processor_manufacturer()
        vm_list.append(pm_detection)
    if 'imvirt_detection' in args:
        imvirt_detection = virtual_box.vmd_by_imvirt()
        vm_list.append(imvirt_detection)
    if 'vmd_by_facter_virtual' in args:
        facter_virtual_detection = virtual_box.vmd_by_facter_virtual()
        vm_list.append(facter_virtual_detection)
    if 'systemd_detection_virt_detection' in args:
        systemd_detect_virt_detection = virtual_box.vmd_by_systemd_detect_virt()
        vm_list.append(systemd_detect_virt_detection)
    if "lspci_detection" in args:
        lspci_detection = virtual_box.vmd_by_lspci()
        vm_list.append(lspci_detection)
    if "virt_what_detection" in args:
        virt_what_detection = virtual_box.vmd_by_virt_what()
        vm_list.append(virt_what_detection)
    if "lsusb_detection" in args:
        lsusb_detection = virtual_box.vmd_by_lsusb()
        vm_list.append(lsusb_detection)
    if "lshw_detection" in args:
        lshw_detection = virtual_box.vmd_by_lshw()
        vm_list.append(lshw_detection)
    if "lscpu_detection" in args:
        lscpu_detection = virtual_box.vmd_by_lscpu()
        vm_list.append(lscpu_detection)

    return vm_list

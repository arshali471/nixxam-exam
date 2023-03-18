# Enixm


## Virtual Machine Detection 

- Before creating compile code you have to make sure that which virtual machine detection method you want. 
- By default all eleven method is pluged to detect vitual machine. 
- If you want to change you have to unplug method from clicked_from_lanscapemode.py file. 
- Go to line number 41 and remove  vmd's from virtual_machine method which you don't want. 

### Protocol 
- default protocol used is `http:// `
- if you want to use `https://` protocol then you can change value of variable protocol in clicked_from_exam_mode.py and clicked_from_lanscapemode.py 

## To create compile code 

- Install all additional python module mentioned in the requirement.txt
- Run command 'pip3 install pyinstaller' to install pyinstaller module
- Run command 'pyinstaller online_protected_exam.py --onefile" to create compile code
- It will create two directory name with build and dist
    - Inside dist directory complile code 'online_protected_exam' created

## To create Debian Package from compile code 

- Create directory name with OnlineProtectedAssessment_1.0 
- Inside OnlineProtectedAssessment_1.0 create two directory
    - `DEBIAN` 
    - `usr`
- Inside `DEBIAN` directory create Two file name with 
    - `control` 
    - `postinst`
- Open control file and add these content 
    - ```http 
        Package:OnlineProtectedAssessment 
        Version:1.0
        Maintainer: Maintainer Name [email]
        Architecture:all
        Description: online proctected exam is a debian platform to organize secured examination.
      ```
    - And save 
- Open postinst file and add these content 
    - ```http
        chmode 777 /usr/local/bin/online_protected_exam
        chmode 777 /usr/local/bin/build/online_protected_exam
        chmode 777 /usr/share/applications
        echo "done"
      ```
    - And save
- Inside `usr` directory create these directory structure
    - ```http
        local/bin
        share/applications
      ```
    - go to `bin` directory and paste here build directory and compile code which are generated above.
        - eg: build directory and only online_protected_exam compile file which is inside dist directory is paste here not dist directory.
        - Directory structure should be same as below
            ```http
                usr/local/bin/build
                usr/local/bin/online_protected_exam
            ```
    - inside applications directory create `OnlineProtectedAssessment.desktop` file and write these statement in the file 
    -  ```http
            [Desktop Entry]
            Version=1.0
            Name=OnlineProtectedExam
            Exec=/usr/local/bin/online_protected_exam
            Icon=/usr/local/bin/build/online_protected_exam/IconName here 
            Terminal=False
            Type=Application
            Categories=Education
        ```
- Come out from `OnlineProtectedAssessment_1.0` directory 
- open terminal and run command to create .deb file 
    ```http 
        dpkg-deb --build OnlineProtectedAssessment_1.0
    ```
    - It will create successfully `OnlineProtectedAssessment_1.0.deb`
- If error occured saying like 
    ```http
        dpkg-deb: error: maintainer script 'postint' has bad permission 644 (must be >=0555 and <=0775)
    ```
- Go to file location `OnlineProtectedAssessment_1.0/DEBIAN` Then run this command from terminal 
    ```http
        chmod 0775 postinst
    ```
- And then run above build command again. Now it will create OnlineProtectedExam_1.0.deb file successfully.
    

### To install `OnlineProtectedAssessment_1.0.deb`
 
- First You have to install these packages in your linux system otherwise you will get error like "Connection Failed Due To Package Error".

  - 1. "imvirt" command doesn't come preinstalled by default we have to install using "sudo apt-get install imvirt" command.

  - 2. "facter" command doesn't come preinstalled by default we have to install using "sudo apt-get install facter" command.

- All the package requirement should be install in your system otherwise you will get error like package error 
- Then To install OnlineProtectedAssessment.deb package you have to run below command in the terminal. 
    ```http 
     sudo dpkg -i OnlineProtectedAssessment_1.0.deb
    ```
- To Uninstall OnlineProtectedAssessment.deb package from you computer you have to run below commant in the terminal 
    ```http 
     sudo dpkg -r OnlineProtectedExam
    ```

## Required Linux Packages 

Note: 
1. All the above code used to detect virtual machine only in linux platform. 
2.'imvirt' command doesn't come preinstalled by default we have to install using "sudo apt-get install imvirt" command. 
3. 'facter' command doesn't come preinstalled by default we have to install using "sudo apt-get install facter" command. 
4. 'lspci' command doesn't come preinstalled by default we have to install using "sudo apt-get install lspci" command. 
5. 'virt-what' command doesn't come preinstalled by default we have to install using "sudo apt-get install virt-what" command. 
6. 'lsusb' command doesn't come preinstalled by default we have to install using "sudo apt-get install lsusb" command. 
7. 'lshw' command doesn't come preinstalled by default we have to install using "sudo apt-get install lshw" command. 
8. All methods turn True or False. If system is physical it return False otherwise return True.


#########################################################################
# File Name: install.sh
# Author: Bill
# mail: XXXXXX
# Created Time: 2016-08-31 17:25:20
#########################################################################
#!/bin/bash
cp -rf ./ssh_menu/ /opt/
ln -s /opt/ssh_menu/sshmenu.py /bin/ww
chmod 777 /opt/ssh_menu/sshmenu.py

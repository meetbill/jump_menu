#########################################################################
# File Name: install.sh
# Author: Bill
# mail: XXXXXX
# Created Time: 2016-08-31 17:25:20
#########################################################################
#!/bin/bash
cp -rf ./ssh_menu/ /opt/
if [[ ! -f "/bin/ww" ]]
then
    ln -s /opt/ssh_menu/sshmenu.py /bin/ww
fi
chmod +x -R /opt/ssh_menu/

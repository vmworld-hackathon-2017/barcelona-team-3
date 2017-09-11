#!/bin/sh

##
## Hackathon H5PXE Project - Team 3 - VMworld 2017 Barcelona
##

## Requirements

# python for Django and bpython for interactive shell for playground
apt-get install -y python-pip bpython
pip install django


# Clone the code for h5pxe appliance (django project)
# git clone https://github.com/tsugliani/hackathon-h5pxe
#

# dhcp server
# TODO configure iface in /etc/default/isc-dhcp-server
apt-get install -y isc-dhcp-server
sed -i.bak -e s/INTERFACESv4=\"\"/INTERFACESv4=\"ens160\"/g /etc/default/isc-dhcp-server


# tftp server
apt-get install -y tftpd-hpa
# root directory /root/hackathon-h5pxe/repository"
sed -i.bak -e s/TFTP_DIRECTORY=\".*\"/TFTP_DIRECTORY=\"\\/root\\/hackathon-h5pxe\\/repository\"/g /etc/default/tftpd-hpa
sed -i.bak -e s/TFTP_OPTIONS=\".*\"/TFTP_OPTIONS=\"--secure\ -v\ -p\"/g /etc/default/tftpd-hpa


# Nice colors for dhcp/tftp logs (grc tail -f /var/log/syslog)
apt-get install -y grc

# Clone the code for h5pxe appliance (django project)
# git clone https://github.com/tsugliani/hackathon-h5pxe
#

echo "h5pxe-v1.0" > /etc/h5pxe-release

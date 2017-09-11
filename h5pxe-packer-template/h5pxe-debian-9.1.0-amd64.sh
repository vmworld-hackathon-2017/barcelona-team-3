#!/bin/sh

PACKER_LOG=0 packer build \
       -var 'packer_remote_host=172.16.81.128' \
       -var 'packer_remote_datastore=PACKER' \
       -var 'packer_remote_network=VM Network' \
       -var 'packer_remote_username=root' \
       -var 'packer_remote_password=VMware1!' \
       h5pxe-debian-9.1.0-amd64.json

mv h5pxe-debian-9.1.0-amd64/h5pxe-debian-9.1.0-amd64 Appliance/ &&
rm -rf h5pxe-debian-9.1.0-amd64



# H5PXE Packer template

## Requirements

- Packer 1.0.4 (`brew install packer` on macOS, or download from [here](https://www.packer.io/downloads.html))
- OVFTool 4.2.0
- [vSphere 6.0 U3 OVA Appliance](http://www.virtuallyghetto.com/2017/05/updated-nested-esxi-6-0u3-6-5d-virtual-appliances.html)
- `esxcli system settings advanced set -o /Net/GuestIPHack -i 1`
- Add FW rules for VNC: [fw.sh](https://gist.githubusercontent.com/jasonberanek/4670943/raw/0749993b9043b581cd41c8f8b9886f93153f9b3f/vnc_config_5_1.sh)

## Build process

Clone this repository

`$ git clone https://github.com/xyz`

Setup the remote ESXi builder required settings & credentials in the `h5pxe-debian-9.1.0-amd64.sh` file

- `packer_remote_host`: VMware ESXi 6.0 U3 Appliance Management IP
- `packer_remote_datastore`: Datastore Name, large enough to hold the ISO & VM
- `packer_remote_network`: Network name, defaults to `VM Network`
- `packer_remote_username`: defaults to `root`
- `packer_remote_password`: defaults to `VMware1!`

Launch the appliance build process

`./h5pxe-debian-9.1.0-amd64.sh`

This will install a debian 9.1.0 VM and prepare it for the H5PXE developer environment.

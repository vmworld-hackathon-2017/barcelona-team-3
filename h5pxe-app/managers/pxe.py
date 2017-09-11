from django.template import Context, loader
from django.conf import settings

from managers.models import Host, Hypervisor

class PxeManager(object):
    """
    Will create all pxelinux.cfg files for hosts that are in status "SCHEDULED"
    """
    def __init__(self):
        super(PxeManager, self).__init__()


    def createConfig(self):

        for curItem in Host.objects.all():
            if curItem.status == "SCHEDULED":
                # host needs to be installed, so pxe files are needed.

                t = loader.get_template('pxe/base.cfg')
                c = {
                    'hostname'      : curItem.hostname,
                    'hypervisor'    : curItem.hypervisor.name,
                    'H5PXEServer'   : settings.H5PXE_SERVER_IP,
                    'vlan'          : curItem.vlan,
                }

                # write pxe file, update dhcp host group
                print "PXE Configuration for host : %s" % curItem.hostname
                print t.render(c)
                print "==="

                cleanMac = curItem.mac.replace(":", "-")

                pxefile = "%s/01-%s" % (settings.H5PXE_DIR_REPOSITORY_PXE, cleanMac.lower())

                print " -> Writing PXE Config file %s" % pxefile

                fHandle = open(pxefile, "w+")
                fHandle.write(t.render(c))
                fHandle.close()



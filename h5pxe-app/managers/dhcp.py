from django.template import Context, loader
from django.conf import settings

from managers.models import Host

class DhcpManager(object):
    """
    Will manage creation of dhcp server config file for hosts that are in
    status "SCHEDULED"
    """

    configType = "PXE"

    def __init__(self):
        super(DhcpManager, self).__init__()

    def createConfig(self):
        """
        create dhcp config file.
        """
        hostList = []

        for host in Host.objects.all():
            if host.status == "SCHEDULED":
                hostList.append(host)

        dhcp = settings.H5PXE_DHCP

        # generating template for dhcp :)
        t = loader.get_template('dhcp/base.cfg')
        c = {
            'dhcp'      : dhcp,
            'hostList'  : hostList,
        }

        # Generate dhcp configuration file.
        print "DHCPD Configuration File"
        print t.render(c)
        print "==="

        # write everything to dhcpd config file.
        fHandle = open(settings.H5PXE_CFG_DHCPD_FILE, "w+")
        fHandle.write(t.render(c))
        fHandle.close()


    def setConfigType(self, configType):
        """
        pxe, gpxe
        """

        # this will be done later ...
        if configType == "PXE" or configType == "gPXE":
            self.configType = configType



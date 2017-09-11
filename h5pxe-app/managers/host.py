import re

from managers.models import Host
from managers.pxe import PxeManager
from managers.dhcp import DhcpManager
from managers.service import ServiceManager



class HostManager(object):

    """docstring for HostManager"""
    def __init__(self):
        super(HostManager, self).__init__()

    def register(self, hostname, mac):
        """
        register host with mac address
        """

        # diff mac formats (with ":" or "-")
        regexp = '([a-fA-F0-9]{2}[:|\-]?){6}' # this is the regex

        a = re.compile(regexp).search(mac)
        if a:
            print "Valid Mac address, Registering host [%s]" % mac

            for hosts in Host.objects.all():
                if hosts.hostname != hostname and hosts.mac != mac:
                    pass


    def prepare(self):
        """docstring for prepare"""

        for hosts in Host.objects.all():
            if hosts.status == "SCHEDULED":
                # create pxe files
                p = PxeManager()
                p.createConfig()

        # in any case regenerate & restart dhcp for pending changes.
        d = DhcpManager()
        d.createConfig()

        s = ServiceManager()
        s.restart("dhcpd")

from django.template import Context, loader, Template
from django.http import HttpResponse

from managers.models import Host, Kickstart, Script

from managers.dhcp import DhcpManager
from managers.pxe import PxeManager
from managers.service import ServiceManager



def hostname(request, hostname):

    print "Kickstart request for host : %s" % hostname
    host = None

    try:
        host = Host.objects.get(hostname=hostname)
    except:
        pass

    if host:
        host.status = "POSTCONF"
        host.save()

        # block install loop at next reboot.
        d = DhcpManager()
        d.createConfig()

        # clean pxe files, p = PxeManager(), p.cleanHost(host)
        s = ServiceManager()
        r = s.restart("dhcpd")


        kickstart = Kickstart.objects.get(name=host.kickstart)

        print kickstart.name
        print kickstart.data

        # Probably would be wise to add an introspected environment
        # not just only 'host' access for more generic templates

        t = Template(kickstart.data)
        c = Context ({
            'host': host,
        })

        ks = t.render(c)

        for script in host.scripts.all():
            print "Processing script %s" % script.name
            ks += "\n# %s" % script.name
            ks += "\n%s" % script.data

        return HttpResponse(ks)

    return HttpResponse("No kickstart for host %s" % hostname)


def hostname_status(request, hostname, status):
    print "Kickstart request for host : %s" % hostname
    host = None

    try:
        host = Host.objects.get(hostname=hostname)
    except:
        pass

    if host:
        print "Current Host %s status is [%s]" % (host.hostname, host.status)
        print "Setting Host %s status to [%s]" % (host.hostname, status)
        return HttpResponse("Setting host %s status from %s to %s" % (
            host.hostname,
            host.status,
            status
            )
        )


    return HttpResponse("No kickstart for host %s" % hostname)


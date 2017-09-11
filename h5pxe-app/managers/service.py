from subprocess import Popen, PIPE
from managers.models import Service

class ServiceManager(object):
    """
    Class that will manage system services
    """

    def __init__(self):
        super(ServiceManager, self).__init__()


    def register(self, name, script):

        # check if script/name wasn't already registered
        for service in Service.objects.all():
            if service.name == name or service.script == script:
                print "Service %s or %s script has already been registered !" % (name, script)
                return False

        # create new service
        s = Service()
        s.name = name
        s.script = script
        s.save()

        return True


    def execute(self, serviceScript, command):
        """
        Using init script directly as many diff services managers exist today.
        """
        cmd = "%s %s" % (serviceScript, command)

        try:
            result = Popen(cmd.split(" "), stdout=PIPE).wait()
        except Exception, e:
            print "ERROR in self.execute() : %s" % e
            raise e

        return result

    def run(self, name, action):
        result = None

        print "Service Manager Called, service name : [%s] action : [%s]" % (name, action)
        # check into registered services
        for curService in Service.objects.all():
            if curService.name == name:
                # additional checks for "security"
                if action in "start" or action in "stop" or action in "restart":
                    result = self.execute(curService.script, action)


        return result


    def start(self, name):
        return self.run(name, "start")

    def stop(self, name):
        return self.run(name, "stop")

    def restart(self, name):
        return self.run(name, "restart")

    def list(self):
        return Service.objects.all()

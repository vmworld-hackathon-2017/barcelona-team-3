from subprocess import Popen, PIPE
from django.conf import settings

from managers.models import Hypervisor

import os

class HypervisorManager(object):

    """
    This will manage ESXi builds

    Everything should be stored into a proper
    directory structure with the build names.

    /esxi/b<num>/<files>

    from settings import ESXI_BASE_DIR

    """

    isofile = None

    def __init__(self):
        super(HypervisorManager, self).__init__()


    def execute(self, command):
        result = None

        try:
            p = Popen(command.split(" "), stdout=PIPE)
            result = p.wait()
            output = p.communicate()[0]
        except Exception, e:
            raise e

        return result, output

    def checkValidType(self):

        cmd = "file %s" % self.isofile
        result, output = self.execute(cmd)


        print "checkValidType result: %s" % (result)

        # clean garbage and fetch only interesting information.
        filetype = output.split(":")[1].splitlines()[0]

        if "ISO 9660" in filetype:
            return True
        else:
            return False


    def mountVMwareISO(self):
        """
        Mount iso file temporary to extract needed files
        """
        r = 0
        # check if this directory exists first ...
        cmd = "mkdir -vp %s" % settings.H5PXE_DIR_TMP
        result, output = self.execute(cmd)

        r += result

        # check if there isn't a mounted file already ...
        cmd = "sudo mount -o loop %s %s" % (self.isofile, settings.H5PXE_DIR_TMP)
        result, output = self.execute(cmd)

        r += result

        if r == 0:
            print "ISO Mounted in %s" % settings.H5PXE_DIR_TMP
            return True
        else:
            print "ISO Mount failed."
            return False

    def umountVMwareISO(self):
        """
	    Umount iso file from temporary folder
        """

        # check if this directory exists first ...
        cmd = "sudo umount %s" % settings.H5PXE_DIR_TMP
        result, output = self.execute(cmd)

        if result == 0:
            return True
        else:
            return False


    def copyVMwareFiles(self):
        """
        At the moment just copy all files, we will clean this later.
        ISO name format : VMware-VMvisor-Installer-4.1.0-260247.x86_64.iso
        """

        r = 0
        # fixes list of files later ...
        # VMwareFiles = ["*"]

        version = self.isofile.split("-")
        repositoryName = "VMwareESXi-%s-%s" % (version[3], version[4].split(".")[0])

        print "Repository Name : [%s]" % repositoryName

        # check in database if hypervisor wasn't already registered...
        for hypervisorObj in Hypervisor.objects.all():
            if hypervisorObj.name == repositoryName:
                print "Hypervisor Already registered, skipping..."
                return False

        # create repository directory
        cmd = "mkdir -vp %s/%s" % (settings.H5PXE_DIR_REPOSITORY_HYPERVISOR, repositoryName)
        result, output = self.execute(cmd)
        r += result

        # copy all files
        print "Copying ESXi Files to repository [%s/%s]..." % (settings.H5PXE_DIR_REPOSITORY_HYPERVISOR, repositoryName)
        cmd = "cp -vaf %s/. %s/%s" %   (settings.H5PXE_DIR_TMP, settings.H5PXE_DIR_REPOSITORY_HYPERVISOR, repositoryName)
        result, output = self.execute(cmd)

        r += result

        # Umount Hypervisor ISO file
        self.umountVMwareISO()

        cmd = "chmod -R 755 %s" % (settings.H5PXE_DIR_REPOSITORY_HYPERVISOR)
        self.execute(cmd)

        repositoryDirectory = "%s/%s" % (settings.H5PXE_DIR_REPOSITORY_HYPERVISOR, repositoryName.strip())

        cmd = "sed -e \"s#/##g\" -e \"3s#^#prefix=/hypervisor/%s\\n#\" -i.bak %s/boot.cfg" % (repositoryName, repositoryDirectory)
        print "cmd = [%s]" % (cmd)
        os.system(cmd)

        # Add a database entry only if results are ok !
        if r == 0:
            h = Hypervisor()
            h.name = repositoryName
            h.repository = "%s/%s" % (settings.H5PXE_DIR_REPOSITORY_HYPERVISOR, repositoryName)
            h.save()
            return True
        else:
            print "Something went wrong creating Hypervisor Repository."
            return False


    def register(self, isofile):
        """
        Do necessary steps to mount, fetch vmware vgz files.
        """

        self.isofile = isofile

        status = False

        # check if entered file is a ISO
        # should do more checks about this is a VMware file or not ...
        validType = self.checkValidType()

        if validType:
            print "Mounting ISO to fetch VMware core components..."
            self.mountVMwareISO()
            status = self.copyVMwareFiles()

        return status


    def verify(self, name):
        "Check that all esxi files are there and correct using md5/sha1"
        # verify MD5 file for imagedd.bz2
        pass

    def list(self):
        """
        List available hypervisors
        """

        for hypervisor in Hypervisor.objects.all():
            print "Hypervisor : [%s]" % hypervisor

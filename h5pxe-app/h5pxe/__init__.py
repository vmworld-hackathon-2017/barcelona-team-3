from django.conf import settings
from os import stat
import os

# check Sexi directory structure (initialize if isn't present).
for item in dir(settings):
    if "H5PXE_DIR" in item:
        objItem = "settings.%s" % item

        # get object
        s = eval(objItem)

        result = None
        try:
            result = stat(s)
        except:
            pass

        # create directory structure
        if not result:
            try:
                os.mkdir(s)
            except Exception, e:
                raise e

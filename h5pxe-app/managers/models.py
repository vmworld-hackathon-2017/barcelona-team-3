# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Kickstart(models.Model):
    name        = models.CharField(max_length=256, unique=True) # we use ks name for auto-generate
    info        = models.CharField(max_length=256)
    data        = models.TextField()

    def __unicode__(self):
        return self.name

class Hypervisor(models.Model):
    name        = models.CharField(max_length=256, unique=True)
    repository  = models.CharField(max_length=256, unique=True)
    status      = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Script(models.Model):
    name        = models.CharField(max_length=256, unique=True)
    desc        = models.CharField(max_length=256)
    data        = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.name, self.desc)

class Host(models.Model):
    hostname    = models.CharField(max_length=256, unique=True)
    mac         = models.CharField(max_length=18, unique=True)
    vlan        = models.PositiveIntegerField(default=0)
    ip          = models.CharField(max_length=32)
    netmask     = models.CharField(max_length=32)
    gateway     = models.CharField(max_length=32)
    dns         = models.CharField(max_length=256)

    hypervisor  = models.ForeignKey(Hypervisor)
    kickstart   = models.ForeignKey(Kickstart)
    scripts     = models.ManyToManyField(Script)

    # This will set the status of the host (SCHEDULED/INSTALLED/POSTCONF/DISABLED)
    STATUS_CHOICES = (
        ('SCHEDULED', 'SCHEDULED'),
        ('INSTALLED', 'INSTALLED'),
        ('POSTCONF',  'POSTCONF'),
        ('DISABLED',  'DISABLED'),
    )
    status      = models.CharField(max_length=32,
                                   choices=STATUS_CHOICES,
                                   default='DISABLED')

    class Meta:
        ordering = ['hostname']

    def __unicode__(self):
        return "%s - %s- %s" % (self.hostname, self.hypervisor, self.ip)

    def save(self, *args, **kwargs):
        super(Host, self).save(*args, **kwargs) # Call the "real" save() method.

        # Dirty trick to avoid creating a nice html form // callbacks // views
        from managers.host import HostManager
        hosts = HostManager()
        hosts.prepare()


class Service(models.Model):
    name    = models.CharField(max_length=32, unique=True)
    script  = models.CharField(max_length=256, unique=True)
    status  = models.CharField(max_length=256)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.script)


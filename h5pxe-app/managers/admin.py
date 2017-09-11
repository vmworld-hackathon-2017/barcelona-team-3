# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from managers.models import Hypervisor, Host, Kickstart, Service, Script
from django.contrib import admin

# Register your models here.

def hosts_disable(modeladmin, request, queryset):
    queryset.update(status='DISABLED')
hosts_disable.short_description = "Mark selected hosts as disabled"

def hosts_enable(modeladmin, request, queryset):
    queryset.update(status='SCHEDULED')
hosts_enable.short_description = "Mark selected hosts as scheduled"

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'status', 'kickstart', 'ip', 'mac')
    list_filter = ('kickstart', 'status')

    actions = [hosts_disable, hosts_enable]

admin.site.register(Hypervisor)
admin.site.register(Host, HostAdmin)
admin.site.register(Kickstart)
admin.site.register(Service)
admin.site.register(Script)


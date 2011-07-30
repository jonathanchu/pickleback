from django.contrib import admin
from pickleback.apps.packages.models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'canonical')

admin.site.register(Package, PackageAdmin)

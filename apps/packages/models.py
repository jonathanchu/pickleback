from django.db import models
from django.utils.translation import ugettext_lazy as _

class Package(models.Model):
    """
    Packages app
    """
    name        = models.CharField(_("Name"), max_length=100)
    url         = models.URLField(_("URL of repo"))
    description = models.TextField(_("Description"), blank=True)

    def __unicode__(self):
        return self.name

from django.db import models
from django.utils.translation import ugettext_lazy as _

REPO_CHOICES = (
    ('git', _('Git')),
    ('hg', _('Mercurial')),
    ('svn', _('Subversion')),
    ('pypi', _('PyPI')),
)

class Package(models.Model):
    """
    Packages app
    """
    name        = models.CharField(_("Name"), max_length=100)
    repo_type   = models.CharField(_("Repo type"), max_length=30,
                                   choices=REPO_CHOICES, blank=True)
    url         = models.URLField(_("URL of repo"), verify_exists=False)
    description = models.TextField(_("Description"), blank=True)
    canonical   = models.CharField(_("Canonical name"), max_length=100,
                                   help_text="Most likely used for PyPI",
                                   blank=True)

    def __unicode__(self):
        return self.name

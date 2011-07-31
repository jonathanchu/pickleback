from django.db import models
from django.utils.translation import ugettext_lazy as _

ADMIN_CHOICES = (
    ('yes', _('Yes')),
    ('no', _('No')),
)

DB_CHOICES = (
    ('postgresql', _('PostgreSQL')),
    ('mysql', _('MySQL')),
    ('sqlite3', _('SQLite3')),
    ('oracle', _('Oracle')),
)


class Preference(models.Model):
    """
    Retrieve basic info for settings of project
    """
    name        = models.CharField(_("Name"), max_length=100,
                                        help_text="Name of project")
    admin       = models.CharField(_("Admin enabled"), max_length=10,
                                        choices=ADMIN_CHOICES, default="yes")
    database    = models.CharField(_("Database"), max_length=20,
                                        choices=DB_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return self.name

from __future__ import unicode_literals

from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return ('%s' % self.name).encode('ascii', errors='replace')
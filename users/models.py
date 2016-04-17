from __future__ import unicode_literals
from base.utils import NiceChoices
from django.db import models
import hashlib

class User(models.Model):
    device_id = models.CharField(max_length=500, null=True, blank=True)
    secret_key = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.secret_key = hashlib.sha1("{0}_{1}".format(self.id,self.device_id)).hexdigest()
        if not User.objects.filter(device_id=self.device_id).last():
            super(User, self).save(*args, **kwargs)

class Device(models.Model):
    STATE_CHOICES = NiceChoices(*[(1, 'ACTIVE'),
                                    (2, 'INACTIVE'),
                                    (3, 'UNINSTALLED'),
                                    (4, 'INVALID')])

    user = models.ForeignKey(User, related_name='devices')
    device_model = models.CharField(max_length=50, null=True)
    os = models.CharField(max_length=50, null=True)
    os_version = models.CharField(max_length=50, null=True)
    device_id = models.CharField(max_length=50, null=True)
    app_version = models.CharField(max_length=50, null=True)
    notification_token = models.CharField(max_length=300, null=True)
    state = models.IntegerField(blank=True, null=True, choices=STATE_CHOICES, default=1)
    last_seen = models.IntegerField(blank=True, null=True)
    unique_hash = models.CharField(editable=True, max_length=40, unique=True,null=True)

    def save(self, *args, **kwargs):
        self.unique_hash = hashlib.sha1("{0}_{1}".format(self.user.id,self.notification_token)).hexdigest()
        if not Device.objects.filter(device_id=self.device_id).last():
            super(Device, self).save(*args, **kwargs)


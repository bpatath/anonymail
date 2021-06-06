from django.db import models
from django.conf import settings

class Recipient(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipients')
    enabled = models.BooleanField()

    def __str__(self):
        return '%s <%s> (owned by %s)' % (self.name, self.address, self.owner.username)

from django.db import models
from django.conf import settings

from apps.domain.models import Domain

class Alias(models.Model):
    name = models.CharField(max_length=255)
    localpart = models.CharField(max_length=255)
    isLocalpartRandom = models.BooleanField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='aliases')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aliases')
    enabled = models.BooleanField()

    def __str__(self):
        return '%s <%s@%s> (owned by %s)' % (self.name, self.localpart, self.domain.address, self.owner.username)
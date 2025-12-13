from django.db import models

# Create your models here.
class media(models.Model):
    facebook = models.URLField(max_length=300, blank=True, null=True)
    instagram = models.URLField(max_length=300, blank=True, null=True)
    twitter = models.URLField(max_length=300, blank=True, null=True)
    linkidn = models.URLField(max_length=300, blank=True, null=True)
    youtube = models.URLField(max_length=300, blank=True, null=True)

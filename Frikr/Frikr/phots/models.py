# -*- coding:UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

LICENSES = (
    ('RIG', 'Copyright'),
    ('LEF', 'Copyleft'),
    ('CC', 'Creative commons'),
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Publica'),
    (VISIBILITY_PRIVATE, 'Privada'),
)

class Photo(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True) #optional
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now_add=True,auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility= models.CharField(max_length=3, choices=VISIBILITY)

    def __unicode__(self):
        return self.name
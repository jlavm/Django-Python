from django.db import models

# Create your models here.

LICENSES = (
    ('RIG', 'Copyright'),
    ('LEF', 'Copyleft'),
    ('CC', 'Creative commons'),
)
class Photo(models.Model):

    name=models.CharField(max_length=150)
    url=models.URLField()
    description=models.TextField(blank=True) #optional
    createdAt=models.DateTimeField(auto_now_add=True)
    modifiedAt=models.DateTimeField(auto_now_add=True,auto_now=True)
    license=models.CharField(max_length=3,choices=LICENSES)

    def __unicode__(self):
        return self.name
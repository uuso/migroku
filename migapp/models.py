from django.db import models

# Create your models here.

class GreatObject(models.Model):
    title = models.TextField()
    value = models.SmallIntegerField(default=0)
    def __str__(self):
        return '%s -- %d' % (self.title, self.value)
from django.db import models

# Create your models here.

class GreatObject(models.Model):
    title = models.TextField()
    value = models.SmallIntegerField(default=0)
    dummy = models.CharField(max_length = 30, default="dummy")
    def __str__(self):
        return '%s -- %d [%s]' % (self.title, self.value, self.dummy)
from django.db import models

class DocumentState(models.Model):
    date = models.DateTimeField()

    class Meta:
        abstract = True
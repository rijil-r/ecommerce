from django.db import models


# an abstract model to add created and updated fields
class ActivityLogger(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

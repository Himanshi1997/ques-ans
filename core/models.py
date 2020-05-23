from django.db import models

# Create your models here.


class BaseModel(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True, editable=False)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True
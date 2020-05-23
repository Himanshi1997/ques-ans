from django.db import models

from core.models import BaseModel


class Question(BaseModel):
    title = models.CharField(max_length=500)
    created_by = models.ForeignKey("users.Users", on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title





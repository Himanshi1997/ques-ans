from django.db import models

from core.models import BaseModel


class Answer(BaseModel):
    ques = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    created_by = models.ForeignKey("users.Users", on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.body



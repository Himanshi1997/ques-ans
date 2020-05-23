from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_ID = models.EmailField()
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % self.user_name

    @property
    def ques(self):
        return self.question_set.all()


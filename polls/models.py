from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    create_user = models.ForeignKey(User,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    voters = models.ManyToManyField(User, related_name='questions',blank=True) #중복 방지를 위한 필드
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Bar_code(models.Model):
    code = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=30, null=False)
    charge = models.IntegerField(null=False)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    # author = models.ForeignKey(related_name='bar_code_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Img(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

class Review(models.Model):
    code_name = models.ForeignKey(Bar_code, on_delete=models.CASCADE) # 외래키이므로 위에 question을 참조하고 삭제되면 같이 삭제
    review_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text
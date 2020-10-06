import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Bar_code(models.Model):
    code = models.CharField(max_length=20, primary_key=True, null=False)
    charge = models.IntegerField(null=False)
    name = models.CharField(max_length=30, null=False)
    image = models.ImageField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    id = models.IntegerField(blank=True, null=True)
    # author = models.ForeignKey(related_name='bar_code_set', on_delete=models.CASCADE)

    total = models.IntegerField(blank=True, null=True)
    provision = models.FloatField(blank=True, null=True)
    kcal = models.FloatField(blank=True, null=True)
    carbo = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    sat_fat = models.FloatField(blank=True, null=True)
    tra_fat = models.FloatField(blank=True, null=True)
    colestrol = models.FloatField(blank=True, null=True)
    natrium = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name

class Upload_Img(models.Model):
    image = models.ImageField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

class Upload_Code(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published', default=timezone.now)

class Review(models.Model):
    code_name = models.ForeignKey(Bar_code, on_delete=models.CASCADE) # 외래키이므로 위에 question을 참조하고 삭제되면 같이 삭제
    review_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.review_text

class Choice(models.Model):
    code_name = models.ForeignKey(Bar_code, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Upload(models.Model):
    image = models.FileField()
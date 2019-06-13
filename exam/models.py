from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
    	return self.name


class Question(models.Model):

    name = models.CharField(max_length=1000, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    choice = models.ForeignKey('exam.Choice', on_delete='SET_NULL',
                               null=True, blank=True, related_name='choice')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Choice(models.Model):
    choice_text = models.CharField(max_length=100, unique=True)
    question = models.ForeignKey(
        Question, on_delete='SET_NULL', null=True, blank=True, related_name='question')

    def __str__(self):
        return str(self.choice_text) + " -- " + str(self.question)

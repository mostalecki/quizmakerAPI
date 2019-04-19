from django.db import models
import json

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    totalPoints = models.IntegerField()

    class Meta:
        verbose_name_plural = "Quizzes"

class Question(models.Model):
    text = models.CharField(max_length=200)
    points = models.IntegerField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

class Answer(models.Model):
    text = models.CharField(max_length=100)
    isCorrect = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

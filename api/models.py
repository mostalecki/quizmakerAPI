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
    answers = models.CharField(max_length=200)
    isCorrect = models.CharField(max_length=50)
    points = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def set_answers(self, x):
        self.answers = json.dumps(x)

    def get_answers(self):
        return json.loads(self.answers)

    def set_isCorrect(self, x):
        self.isCorrect = json.dumps(x)

    def get_isCorrect(self):
        return json.loads(self.isCorrect)
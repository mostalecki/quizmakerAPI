from rest_framework import generics

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer

class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

from rest_framework import generics

from .models import Quiz, Question
from .serializers import QuizSerializer, QuizListSerializer

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer

class QuizDetail(generics.RetrieveAPIView):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class QuizCreate(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

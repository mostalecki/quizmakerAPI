from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Quiz, Question
from .serializers import QuizSerializer, QuizListSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Custom authetication class used to omit csrf authentication"""
    def enforce_csrf(self, request):
        return

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer

class QuizDetail(generics.RetrieveAPIView):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class QuizCreate(generics.CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

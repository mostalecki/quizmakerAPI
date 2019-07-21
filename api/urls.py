from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("quizzes/", views.QuizList.as_view(), name="quiz-list"),
    path("quizzes/<int:pk>/", views.QuizDetail.as_view(), name="quiz-detail"),
    path("quizzes/create/", csrf_exempt(views.QuizCreate.as_view()), name="quiz-create")
]

urlpatterns = format_suffix_patterns(urlpatterns)
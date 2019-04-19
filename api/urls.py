from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("quizzes/", views.QuizList.as_view(), name="quiz-list"),
    path("quizzes/<int:pk>/", views.QuizDetail.as_view(), name="quiz-detail"),
    path("quizzes/create/", views.QuizCreate.as_view(), name="quiz-create")
]

urlpatterns = format_suffix_patterns(urlpatterns)
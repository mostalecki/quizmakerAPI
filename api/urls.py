from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("quizzes/", views.QuizList.as_view(), name="quiz_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
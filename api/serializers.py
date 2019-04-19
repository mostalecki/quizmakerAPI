from rest_framework import serializers
from .models import Quiz, Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('text', 'answers', 'isCorrect', 'points')

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=True)

    class Meta:
        model = Quiz
        fields = ('title', 'totalPoints', 'answers')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(quiz=quiz, **question_data)
        return quiz

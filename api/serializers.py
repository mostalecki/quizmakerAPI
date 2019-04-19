from rest_framework import serializers
from .models import Quiz, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text', 'isCorrect')

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = ('text', 'answers', 'points')

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=True)

    class Meta:
        model = Quiz
        fields = ('title', 'totalPoints', 'questions')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(quiz=quiz, **question_data)

            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)
            question.save()

        return quiz

import datetime
from rest_framework import serializers
from surveys.models import Survey, SurveyDepartment, Question, Answer, User_Answer



class SurveySerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format="%Y-%m-%d")
    expired_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyDepartment
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    # question = models.CharField(max_length=500, blank=True, trim_whitespace=False)
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {'question': {'trim_whitespace': False}}

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        extra_kwargs = {'answer': {'trim_whitespace': False}}

class User_AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Answer
        fields = '__all__'
        extra_kwargs = {
            'shortAnswer': {'trim_whitespace': False},
            'paragraph': {'trim_whitespace': False}
        }



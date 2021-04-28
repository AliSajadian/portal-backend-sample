from rest_framework import viewsets, permissions

from surveys.models import Survey, SurveyDepartment, Question, Answer, User_Answer
from .serializers import SurveySerializer, SurveyDepartmentSerializer, QuestionSerializer, AnswerSerializer, User_AnswerSerializer


class SurveysViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = SurveySerializer

class UsedSurveysViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = SurveySerializer
    
    def get_queryset(self):
        userID = self.kwargs['id']
        return Survey.used_survey_objects.get_usedsurvey(userID)

class UnusedSurveysViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = SurveySerializer
    
    def get_queryset(self):
        userID = self.kwargs['id']
        return Survey.unused_survey_objects.get_unusedsurvey(userID)

class SurveyDepartmentViewSet(viewsets.ModelViewSet):
    queryset = SurveyDepartment.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = SurveyDepartmentSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = AnswerSerializer
    
class User_AnswerViewSet(viewsets.ModelViewSet):
    queryset = User_Answer.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = User_AnswerSerializer





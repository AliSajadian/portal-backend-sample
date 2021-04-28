from rest_framework import routers

from .views import SurveysViewSet, SurveyDepartmentViewSet, UnusedSurveysViewSet, UsedSurveysViewSet, \
         QuestionViewSet, AnswerViewSet, User_AnswerViewSet


router = routers.DefaultRouter()
router.register('api/surveys', SurveysViewSet, 'surveys')
router.register('api/unusedsurveys/(?P<id>\d+)', UnusedSurveysViewSet, 'unusedsurveys')
router.register('api/usedsurveys/(?P<id>\d+)', UsedSurveysViewSet, 'usedsurveys')
router.register('api/surveydepartment', SurveyDepartmentViewSet, 'surveydepartment')
router.register('api/Questions', QuestionViewSet, 'Questions')
router.register('api/Answers', AnswerViewSet, 'Answers')
router.register('api/userAnswers', User_AnswerViewSet, 'userAnswers')

urlpatterns = router.urls

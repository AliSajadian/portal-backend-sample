from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from baseInfo.models import Department, SurveyType


class UnusedSueveyManager(models.Manager):
    def get_unusedsurvey(self, userID):
        from django.db import connection
        from collections import defaultdict

        # userID = HttpRequest["userID"]
        with connection.cursor() as cursor:
            # cursor.execute(
                # '''SELECT s.id, s.description, s.surveyTypeID_id, s.created_date, s.expired_date
                # FROM tbl_survey s
                # WHERE s.id not in 
                # (SELECT s.id 
                # FROM tbl_survey s inner join tbl_survey_question q 
                # on s.id = q.surveyID_id inner join tbl_survey_user_answer a 
                # on q.id = a.questionID_id 
                # group by s.id, s.description, a.userID_id having a.userID_id = %s)''', [userID]
                # %s ''', (userID,)) id = row[0], s.id, 
            cursor.execute('''SELECT s.id, s.description , s.surveyType_id, s.created_date, s.expired_date
                            FROM tbl_survey_survey s 
                            WHERE s.id in 
                            (select sd.survey_id as id from tbl_survey_department sd)
                            and
                            s.id not in 
                            (SELECT s.id 
                            FROM tbl_survey_survey s inner join tbl_survey_question q 
                            on s.id = q.survey_id inner join tbl_survey_user_answer a 
                            on q.id = a.question_id 
                            group by s.id, s.description, a.user_id having a.user_id = %s)''', [userID])
            result_list = []
            for row in cursor.fetchall():
                s = self.model(id = row[0], description = row[1],  
                    surveyType_id = row[2], created_date = row[3], expired_date = row[4])
                result_list.append(s)

            return result_list

class UsedSueveyManager(models.Manager):
    def get_usedsurvey(self, userID):
        from django.db import connection
        from collections import defaultdict

        # userID = HttpRequest["userID"]
        with connection.cursor() as cursor:
            cursor.execute('''SELECT s.id, s.description , s.surveyType_id, s.created_date, s.expired_date
                            FROM tbl_survey_survey s 
                            WHERE s.id in 
                            (select sd.survey_id as id from tbl_survey_department sd)
                            and
                            s.id in 
                            (SELECT s.id 
                            FROM tbl_survey_survey s inner join tbl_survey_question q 
                            on s.id = q.survey_id inner join tbl_survey_user_answer a 
                            on q.id = a.question_id 
                            group by s.id, s.description, a.user_id having a.user_id = %s)''', [userID])
                # %s ''', (userID,)) id = row[0], s.id, 

            result_list = []
            for row in cursor.fetchall():
                s = self.model(id = row[0], description = row[1], 
                    surveyType_id = row[2], created_date = row[3], expired_date = row[4])
                result_list.append(s)

            return result_list

class Survey(models.Model):
    surveyType = models.ForeignKey(SurveyType,
         related_name="SurveyType_Survey", 
         on_delete=models.CASCADE, null=True)
    created_date = models.DateField(default=datetime.now, blank=True)
    expired_date = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length=500)

    objects = models.Manager()
    unused_survey_objects = UnusedSueveyManager()
    used_survey_objects = UsedSueveyManager()

    class Meta:
        db_table = "tbl_survey_survey"

class SurveyDepartment(models.Model):
    department = models.ForeignKey(Department,
        related_name="Department_SurveyDepartment", 
        on_delete=models.CASCADE, null=True)
    survey = models.ForeignKey(Survey,
        related_name="Survey_SurveyDepartment",
        on_delete=models.CASCADE, null=True)         

    class Meta:
        db_table = "tbl_survey_department"
        # constraints = [
        # models.UniqueConstraint(fields=['department', 'survey'], name='department_survey_unique_constraint')
        # ]
        unique_together = ('department', 'survey')

class Question(models.Model):
    survey = models.ForeignKey(Survey,
                                 related_name="Survay_Question",
                                 on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=500, blank=True)
    questionType = models.PositiveSmallIntegerField()
    isRequired = models.BooleanField(default=False)
    objects = models.Manager()  

    class Meta:
        db_table = "tbl_survey_question"

class Answer(models.Model):
    question = models.ForeignKey(Question,
                                    related_name="Question_Answer",
                                    on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=500, blank=True)
    objects = models.Manager()  
    
    class Meta:
        db_table = "tbl_survey_answer"

class User_Answer(models.Model):
    user = models.ForeignKey(User,
                                related_name="User_UserAnswers",
                                on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question,
                                    related_name="Question_UserAnswer",
                                    on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer,
                                    related_name="Answer_UserAnswer",
                                    on_delete=models.CASCADE, null=True)
    shortAnswer = models.CharField(max_length=200, blank=True)
    paragraph = models.CharField(max_length=1000, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = "tbl_survey_user_answer"



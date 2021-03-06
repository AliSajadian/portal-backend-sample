# Generated by Django 3.0.10 on 2021-05-29 08:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_base_company',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Company_Department', to='baseInfo.Company')),
            ],
            options={
                'db_table': 'tbl_base_department',
            },
        ),
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_doctorType',
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_base_jobPosition',
            },
        ),
        migrations.CreateModel(
            name='SurveyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_surveyType',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Company_Project', to='baseInfo.Company')),
            ],
            options={
                'db_table': 'tbl_base_project',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('expired_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('read_status', models.BooleanField(default=False, null=True)),
                ('notifier_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Group_Notification', to='auth.Group')),
                ('notifier_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_Notification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_base_notification',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personel_code', models.CharField(max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('gender', models.BooleanField(default=False)),
                ('picture', models.FileField(null=True, upload_to='employee_pix')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=256)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Department_Employee', to='baseInfo.Department')),
                ('jobPosition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='JobPosition_Employee', to='baseInfo.JobPosition')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project_Employee', to='baseInfo.Project')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_base_employee',
            },
        ),
    ]

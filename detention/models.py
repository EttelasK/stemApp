from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

QUESTIONS_LIST = (
        ('1','What is the name of the street you grew up on?'),
        ('2','What is the name of your childhood best friend?'),
        ('3','What is the name of your first pet?'),
    )

GRADE_LIST = (('1','09'),
              ('2','10'),
              ('3','11'),
              ('4','12'),
              )

class StudentProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    security_question = models.CharField(max_length=100, choices=QUESTIONS_LIST)
    security_answer = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=2, choices = GRADE_LIST)
    advisor = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.datetime.now)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class ParentProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    security_question = models.CharField(max_length=100, choices=QUESTIONS_LIST)
    security_answer = models.CharField(max_length=100)
    student_username = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.datetime.now)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Demerit(models.Model):
    date_assigned = models.DateTimeField(default=datetime.datetime.now)
    assigned_by = models.CharField(max_length=50)
    student = models.ForeignKey(StudentProfile)
    infraction = models.CharField(max_length=200)
    demerit_quantity = models.IntegerField()
    def __str__(self):
        return '%s-%s' % (self.date_assigned, self.student)

class Detention(models.Model):
    detention_date = models.DateField()
    start_time = models.TimeField()
    location = models.CharField(max_length=50)
    parent_profile = models.ForeignKey(ParentProfile)
    parent_approval = models.BooleanField(default=False)
    parent_approval_date = models.DateField(default=datetime.datetime.now)
    demerit = models.ManyToManyField(Demerit)


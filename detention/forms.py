from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from .models import *

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = StudentProfile
        fields = ('first_name',
                  'last_name',
                  'email',
                  'username',
                  'password',
                  'security_question',
                  'security_answer',
                  'grade_level',
                  'advisor',
                  )

class ParentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = ParentProfile
        fields = ('first_name',
                  'last_name',
                  'email',
                  'username',
                  'password',
                  'security_question',
                  'security_answer',
                  'student_username',
                  )

class ChangeParentProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = ParentProfile
        fields = ('email',
                  'username',
                  'password',
                  )

class ChangeStudentProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = ParentProfile
        fields = ('email',
                  'username',
                  'password',
                  )
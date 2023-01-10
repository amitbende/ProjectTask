from django import forms
from .models import Student

class StudentForms(forms.Form):
    class Meta:
        Model = Student
        fields = '__all__'
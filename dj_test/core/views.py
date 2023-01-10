from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForms
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

def StudentView(request):
    form = StudentForms()
    template_name = 'core/studentform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist_url')
    return render(request, template_name, context)

def StudentList(request):
    data = Student.objects.all()
    template_name = 'core/showstudent.html'
    context = {'object': data}
    return render(request, template_name, context)

def StudentUpdate(request, id):
    data = Student.objects.get(student_id = id)
    form = StudentForms(instance = data)
    template_name = 'core/studentform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForms(request.POST, instance = data)
        if form.is_valid():
            form.save()
            return redirect('studentlist_url')
    return render(request, template_name, context)

def StudentDelete(request, id):
    data = Student.objects.get(student_id = id)
    template_name = 'core/confirmdelete.html'
    context = {'object': data}
    if request.method == 'POST':
        data.delete()
        return redirect('studentlist_url')
    return render(request, template_name, context)
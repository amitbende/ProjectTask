from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'age', 'current_position', 'timestamp']

admin.site.register(Student, StudentAdmin)

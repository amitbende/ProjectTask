from django.urls import path
from . import views


urlpatterns = [
    path('sf/', views.StudentView, name='studentform_url'),
    path('sl/', views.StudentList, name='studentlist_url'),
    path('sl/<int:page>/', views.StudentList, name='studentlist_url'),
    path('uc/<int:id>/', views.StudentUpdate, name='update_url'),
    path('dc/<int:id>/', views.StudentDelete, name='delete_url')
]
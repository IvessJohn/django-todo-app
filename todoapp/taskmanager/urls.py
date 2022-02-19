from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='list'),
    path('about/', views.about, name='about'),
    path('task/<str:task_id>/', views.updateTask, name='task'),
    path('delete_task/<str:task_id>/', views.deleteTask, name='delete_task'),
]
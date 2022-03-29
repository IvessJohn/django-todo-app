from django.urls import path

from . import views


urlpatterns = [
    # Authentication
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    # Main functionality
    path('', views.index, name='list'),
    path('task/<str:task_id>/', views.updateTask, name='task'),
    path('delete_task/<str:task_id>/', views.deleteTask, name='delete_task'),
    # Extras
    path('about/', views.about, name='about'),
]
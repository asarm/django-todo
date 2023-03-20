from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='detail'),
    path('task-create/', views.taskCreate, name='create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='delete'),
]
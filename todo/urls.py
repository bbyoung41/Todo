from django.urls import path
from . import views


urlpatterns = [
    path('addTask/', views.add_task, name='addtask'),
    path('completetask/<int:pk>/', views.complete_task, name='completed'),

    #edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #delete task
    path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),

    #udone
    path('udone/<int:pk>/', views.undone, name='undone'),
]

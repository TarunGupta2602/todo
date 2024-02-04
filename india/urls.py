# yourapp/urls.py

from django.urls import path
from .views import todo_list, create_todo, delete_todo, register, login_view, logout_view

urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', create_todo, name='create_todo'),
    path('todo/delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


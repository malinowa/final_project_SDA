from django.urls import path
from . import views

app_name = 'quizz'
urlpatterns = [
    path('user-form/', views.UserFormView.as_view(), name='user-form'),
    path('', views.hello, name='aaa')
]
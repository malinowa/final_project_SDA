from django.urls import path
from . import views

app_name = 'quizz'
urlpatterns = [
    path('player-form/', views.PlayerCreateView.as_view(), name='player-form'),
    path('', views.main_menu, name='main-menu'),
    path('start-quiz/', views.start_quiz, name='start-quiz'),
    path('results-table/', views.ResultsListView.as_view(), name='results-table'),
]
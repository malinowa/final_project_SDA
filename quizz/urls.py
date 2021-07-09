from django.urls import path
from . import views

app_name = 'quizz'
urlpatterns = [
    path('player-form/', views.PlayerCreateView.as_view(), name='player-form'),
    path('', views.main_menu, name='main-menu'),
    path('question-show/<pk>', views.QuestionShowView.as_view(), name='question-show'),
    path('results-table/', views.ResultsListView.as_view(), name='results-table'),
    path('congratulations-page/', views.show_congratulations, name='congratulations-page'),
]
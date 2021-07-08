from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from quizz.forms import PlayerModelForm
from quizz.models import Player, Quiz, Question, Answer


class PlayerCreateView(CreateView):
    template_name = 'player-form.html'
    form_class = PlayerModelForm
    success_url = reverse_lazy('quizz:main-menu')


def start_quiz(request):
    return HttpResponse('Quizz started')


def main_menu(request):
    return render(
        request,
        template_name='main_menu.html',
    )


class ResultsListView(ListView):
    model = Player
    template_name = 'results-table.html'










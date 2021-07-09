from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView
from django.urls import reverse_lazy, reverse
from django.views import View
from django.http import HttpResponseRedirect

from quizz.forms import PlayerModelForm
from quizz.models import Player, Quiz, Question, Answer
import random


class QuestionShowView(View):
    def get(self, request, pk):
        quiz = Quiz.objects.all()[len(Quiz.objects.all()) - 1]
        question = quiz.questions.all()[int(pk)-1]
        answers = Answer.objects.filter(question=question)
        next_question_pk = int(pk) + 1
        return render(
            request,
            template_name='question_template.html',
            context={'question': question, 'answers': answers, 'next_question_pk': next_question_pk},
        )


def main_menu(request):
    return render(
        request,
        template_name='main_menu.html',
    )


def show_congratulations(request):
    player = Player.objects.all()[len(Player.objects.all()) - 1]

    return render(
        request,
        template_name='congratulations_template.html',
        context={},
    )


class PlayerCreateView(CreateView):
    template_name = 'player_form.html'
    form_class = PlayerModelForm
    success_url = f"/quizz/question-show/1"

    def form_valid(self, form):
        result = super().form_valid(form)
        quiz = Quiz.objects.create(author=self.object, title=f"{self.object.nickname}'s quiz!")
        questions = random.sample(list(Question.objects.all()), 5)
        for question in questions:
            question.quiz = quiz
            question.save()
        for question in quiz.questions.all():
            print(question)
        return result


class ResultsListView(ListView):
    model = Player
    template_name = 'results_table.html'


def main_menu_redirect(request):
    return HttpResponseRedirect(reverse('quizz:main-menu'))










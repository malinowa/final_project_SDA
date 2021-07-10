from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

from quizz.forms import PlayerModelForm, QuestionForm
from quizz.models import Player, Quiz, Question, Answer
import random


class QuestionShowView(View):
    def get(self, request, next_question_pk):
        quiz = Quiz.objects.all()[len(Quiz.objects.all()) - 1]
        question = random.choice(quiz.questions.all())
        answers = self.__prepare_answers(question.id)
        question.quiz = None
        question.save()
        form = QuestionForm(answers=answers)
        return render(
            request,
            template_name='question_template.html',
            context={"form": form, 'question': question.question_text, 'next_question_pk': int(next_question_pk)}
        )

    def __prepare_answers(self, question_id):
        answers = Answer.objects.filter(question=question_id)
        return [(answer.id, answer.text) for answer in answers]

    def post(self, request, next_question_pk):
        player = Player.objects.all()[len(Player.objects.all()) - 1]

        answer_id = request.POST.get("answer")
        answer = Answer.objects.get(id=answer_id)
        print(answer)

        if answer.correct:
            player.points += 1
            player.save()

        if int(next_question_pk) == 1:
            return HttpResponseRedirect(f'/quizz/congratulations-page/')
        return HttpResponseRedirect(f'/quizz/question-show/{int(next_question_pk) - 1}')


def main_menu(request):
    return render(
        request,
        template_name='main_menu.html',
    )


def show_congratulations(request):
    return render(
        request,
        template_name='congratulations_template.html',
        context={'player': Player.objects.all()[len(Player.objects.all())- 1]},
    )


class PlayerCreateView(CreateView):
    template_name = 'player_form.html'
    form_class = PlayerModelForm
    success_url = "/quizz/question-show/5"

    def form_valid(self, form):
        result = super().form_valid(form)
        nickname = form.cleaned_data['nickname']
        author = Player.objects.get(nickname=nickname)
        quiz = Quiz.objects.create(author=author, title=f"{author.nickname}'s quiz!")
        questions = random.sample(list(Question.objects.all()), 5)
        for question in questions:
            question.quiz = quiz
            question.save()
        return result


class ResultsListView(ListView):
    model = Player
    template_name = 'results_table.html'


def main_menu_redirect(request):
    return HttpResponseRedirect(reverse('quizz:main-menu'))










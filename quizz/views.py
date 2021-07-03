from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy

from quizz.forms import UserModelForm
from quizz.models import User

class UserFormView(FormView):

    template_name = 'user-form.html'
    form_class = UserModelForm
    success_url = reverse_lazy('quizz:aaa')

    def form_valid(self, form):
        result = super().form_valid(form)
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        age = form.cleaned_data['age']
        User.objects.create(name=name, surname=surname, age=age)
        return result

def hello(request):
    return HttpResponse('hello')








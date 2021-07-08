from django import forms
from quizz.models import Player


class PlayerModelForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('nickname', )
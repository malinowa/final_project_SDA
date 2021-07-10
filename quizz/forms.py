from django import forms
from quizz.models import Player, Answer


class PlayerModelForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('nickname', )


class QuestionForm(forms.Form):
    answer = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        self.answers = kwargs.pop('answers')
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget = forms.RadioSelect(choices=self.answers)
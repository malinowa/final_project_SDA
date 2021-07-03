from django import forms
from quizz.models import User

class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
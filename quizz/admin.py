from django.contrib import admin
from quizz.models import Quiz, Question, Answer, Player

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Player)

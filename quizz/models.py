from django.db import models


class Player(models.Model):
    nickname = models.CharField(max_length=30)
    points = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nickname


class Quiz(models.Model):
    author = models.ForeignKey(Player, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    times_taken = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['id']

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        related_name='questions',
        on_delete=models.CASCADE
    )
    question_text = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.DO_NOTHING
    )
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
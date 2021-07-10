# Generated by Django 3.2.3 on 2021-07-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0008_auto_20210710_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
    ]

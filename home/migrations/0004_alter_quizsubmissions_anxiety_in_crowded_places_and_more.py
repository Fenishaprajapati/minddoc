# Generated by Django 4.2.3 on 2024-01-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_quizsubmission_quizsubmissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsubmissions',
            name='anxiety_in_crowded_places',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='are_you_satisfied_with_work_life',
            field=models.CharField(max_length=210),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='comfortable_enclosed_spaces',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='difficulty_concentrating',
            field=models.CharField(max_length=201),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='feeling_overwhelmed',
            field=models.CharField(max_length=201),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='overthinking_decisions',
            field=models.CharField(max_length=201),
        ),
        migrations.AlterField(
            model_name='quizsubmissions',
            name='public_speaking_anxiety',
            field=models.CharField(max_length=201),
        ),
    ]

# Generated by Django 4.2.3 on 2024-01-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeling_overwhelmed', models.CharField(max_length=20)),
                ('being_judged', models.CharField(max_length=20)),
                ('sleep_patterns', models.CharField(max_length=20)),
                ('confront_challenges', models.CharField(max_length=20)),
                ('comfortable_enclosed_spaces', models.CharField(max_length=20)),
                ('public_speaking_anxiety', models.CharField(max_length=20)),
                ('anxiety_in_crowded_places', models.CharField(max_length=20)),
                ('fear_of_missing_out', models.CharField(max_length=20)),
                ('panic_or_fear', models.CharField(max_length=20)),
                ('are_you_satisfied_with_work_life', models.CharField(max_length=20)),
                ('difficulty_concentrating', models.CharField(max_length=20)),
                ('overthinking_decisions', models.CharField(max_length=20)),
            ],
        ),
    ]

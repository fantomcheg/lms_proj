# Generated by Django 4.2 on 2023-04-25 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название курса')),
                ('description', models.TextField(max_length=200, verbose_name='Описание курса')),
                ('start_date', models.DateField(verbose_name='Старт курса')),
                ('duration', models.PositiveIntegerField(verbose_name='Продолжительность')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='Цена')),
                ('count_lessons', models.PositiveIntegerField(verbose_name='Кол-во уроков')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.TextField(max_length=100, verbose_name='Описание урока')),
                ('start_date', models.DateField(verbose_name='Старт курса')),
                ('duration', models.PositiveIntegerField(verbose_name='Продолжительность')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='Цена')),
                ('count_lessons', models.PositiveIntegerField(verbose_name='Кол-во уроков')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['course'],
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BinaryField(default=None, verbose_name='Пройден?')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='learning.lesson', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ученик')),
            ],
            options={
                'ordering': ['-user'],
            },
        ),
    ]
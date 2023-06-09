# Generated by Django 4.2 on 2023-04-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='count_lessons',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='price',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='start_date',
        ),
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(default='default title', max_length=25, unique=True, verbose_name='Название урока'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-04-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0004_alter_gamegenremodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegenremodel',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Описание жанра'),
        ),
        migrations.AlterField(
            model_name='gamegenremodel',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Название жанра'),
        ),
    ]

# Generated by Django 4.2 on 2023-04-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0003_remove_gamegenremodel_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegenremodel',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]

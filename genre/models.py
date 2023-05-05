from django.db import models


class GameGenreModel(models.Model):
    name = models.CharField("Название жанра", max_length=40, unique=True, null=False, blank=False)
    description = models.TextField("Описание жанра", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

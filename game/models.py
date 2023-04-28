from django.db import models
from django.shortcuts import reverse
from genre.models import GameGenreModel
from game_platform.models import GamePlatformModel

class GameModel(models.Model):
    name = models.CharField("Название игры", max_length=70, unique=True, null=False, blank=False)
    description = models.TextField("Описание", max_length=255, null=True, blank=True)
    buy = models.BooleanField("Куплена", default=False, help_text="Куплена игра или нет")
    beta = models.BooleanField("Игра в бете", default=False, help_text="Игра находится в бета тестировании или нет")
    passed = models.BooleanField("Игра пройдена", default=False, help_text="Игра пройдена или нет")
    publisher = models.CharField("Издатель", max_length=70, null=True, blank=True)
    developer = models.CharField("Разработчик", max_length=70, null=True, blank=True)
    genres = models.ManyToManyField(GameGenreModel, blank=True)
    game_platform = models.ManyToManyField(GamePlatformModel, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game", kwargs={"id": self.id})



from django.db import models

class GamePlatformModel(models.Model):
    name = models.CharField("Название платформы", max_length=40, null=False, blank=False)
    description = models.TextField("Описание платформы", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

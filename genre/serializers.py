from rest_framework import serializers

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)


'''    name = models.CharField("Название игры", max_length=70, unique=True, null=False, blank=False, db_index=True)
    description = models.TextField("Описание", max_length=255, null=True, blank=True)
    buy = models.BooleanField("Куплена", default=False, help_text="Куплена игра или нет")
    beta = models.BooleanField("Игра в бете", default=False, help_text="Игра находится в бета тестировании или нет")
    passed = models.BooleanField("Игра пройдена", default=False, help_text="Игра пройдена или нет")
    publisher = models.CharField("Издатель", max_length=70, null=True, blank=True)
    developer = models.CharField("Разработчик", max_length=70, null=True, blank=True)
    genres = models.ManyToManyField(GameGenreModel, blank=True)
    game_platform = models.ManyToManyField(GamePlatformModel, blank=True)'''

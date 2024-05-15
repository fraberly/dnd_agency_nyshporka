from django.db import models


class World(models.Model):
    id = models.IntegerField(), 'primary_key=True'
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False  # Це важливо, щоб Django не спробував створити таблицю
        db_table = 'world' # Назва таблиці у вашій базі даних MySQL


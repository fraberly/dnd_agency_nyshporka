from django.db import models


# class World(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     info = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         managed = False  # Це важливо, щоб Django не спробував створити таблицю
#         db_table = 'world' # Назва таблиці у вашій базі даних MySQL


class Worlds(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Світ'
        verbose_name_plural = 'Світи'


class Users(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=32)


class Dice(models.Model):
    name = models.CharField(max_length=8)
    description = models.CharField(max_length=128)


from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Головна'
        verbose_name_plural = 'Головні'


class Mechanics(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Механіка'
        verbose_name_plural = 'Механіки'


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


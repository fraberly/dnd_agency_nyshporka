from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()
    type = models.IntegerField()
    typeclass = models.IntegerField()
    img = models.ImageField(upload_to='weapon/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зброя'
        verbose_name_plural = 'Зброї'

class Armor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()
    type = models.IntegerField()
    img = models.ImageField(upload_to='weapon/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '<Броня>'
        verbose_name_plural = 'Броні'

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()
    img = models.ImageField(upload_to='weapon/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спорядження'
        verbose_name_plural = 'Спорядження'


class Tools(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()
    img = models.ImageField(upload_to='weapon/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Інструмент'
        verbose_name_plural = 'Інструменти'
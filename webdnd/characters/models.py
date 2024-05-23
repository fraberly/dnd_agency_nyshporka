from django.db import models


class Characters(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    info = models.TextField()
    charakteristic = models.IntegerField()
    img = models.ImageField(upload_to='characters/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пресонаж'
        verbose_name_plural = 'Пресонажі'
from django.db import models

from scraping.services import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    company = models.CharField(max_length=300, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT)
    programming_language = models.ForeignKey(ProgrammingLanguage, verbose_name='Язык программирования',
                                             on_delete=models.PROTECT)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тег', blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100,verbose_name='Задание')
    description = models.TextField(verbose_name='Описание задания')
    due_date = models.DateField(verbose_name='Срок выполнения', null=True, blank=True)
    completed = models.BooleanField(default=False, verbose_name='Завершено')
    creation_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)

    def __str__(self):
        return f'Задание {self.id}: {self.description}, Завершено: {self.completed}'
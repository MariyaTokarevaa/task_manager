from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Задание', max_length=100)
    description = models.TextField('Описание')
    due_date = models.DateField('Сделать до', null=True, blank=True)
    tags = models.CharField('Примечания', max_length=100, blank=True)
    completed = models.BooleanField('Завершено', default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
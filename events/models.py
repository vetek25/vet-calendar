from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  # кто создал запись
    title = models.CharField(max_length=255, verbose_name='Имя клиента')            # имя клиента
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')  # телефон (необяз.)
    comment = models.TextField(blank=True, verbose_name='Комментарий')              # комментарий
    date = models.DateField(verbose_name='Дата')                                    # дата записи
    time = models.TimeField(verbose_name='Время')                                   # время записи
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')    # дата создания

    def __str__(self):
        return f"{self.title} – {self.date} {self.time}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['date', 'time']  # сортировка по дате и времени

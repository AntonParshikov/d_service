from django.db import models
from users.models import NULLABLE


class DistributionClient(models.Model):
    # Переделать модель клиентов рассылки, указать связь с моделью рассылки ManyToMany.
    # Написать команды для рассылки в commands через  https://schedule.readthedocs.io/en/stable/
    first_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=100, **NULLABLE, verbose_name='Фамилия')
    email = models.EmailField(max_length=250, unique=True, **NULLABLE, verbose_name='Адрес электронной почты')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email} - {self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Клиент рассылки'
        verbose_name_plural = 'Клиенты рассылки'


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Тема сообщения')
    body = models.TextField(**NULLABLE, verbose_name='Текст сообщения')

    def __str__(self):
        return f'{self.subject}: {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Distribution(models.Model):
    sending_frequency_daily = 'daily'
    sending_frequency_weekly = 'weekly'
    sending_frequency_monthly = 'monthly'

    sending_frequency = (
        (sending_frequency_daily, 'daily'),
        (sending_frequency_weekly, 'weekly'),
        (sending_frequency_monthly, 'monthly')
    )

    status_created = 'created'
    status_started = 'started'
    status_completed = 'completed'

    statuses = (
        (status_created, 'created'),
        (status_started, 'started'),
        (status_completed, 'completed')
    )

    start_time = models.TimeField(**NULLABLE, verbose_name='Время начала рассылки')
    end_time = models.TimeField(**NULLABLE, verbose_name='Время начала рассылки')
    frequency = models.CharField(max_length=50, choices=sending_frequency, default=sending_frequency_daily,
                                 verbose_name='Период рассылки')
    status = models.CharField(max_length=50, choices=statuses, default=status_created, verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='Сообщение')
    distribution_client = models.ManyToManyField(DistributionClient, verbose_name='Клиент рассылки')

    def __str__(self):
        return f'{self.frequency} - {self.start_time}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

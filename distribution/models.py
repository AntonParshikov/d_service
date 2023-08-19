from django.db import models

from users.models import Users

NULLABLE = {'blank': True, 'null': True}


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

    time = models.TimeField(verbose_name='Время отправки')
    frequency = models.CharField(max_length=50, choices=sending_frequency, default=sending_frequency_daily,
                                 verbose_name='Период рассылки')
    status = models.CharField(max_length=50, choices=statuses, default=status_created, verbose_name='Статус рассылки')

    message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.frequency} - {self.time}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class DistributionClient(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Клиент')
    distribution_settings = models.ForeignKey(Distribution, on_delete=models.CASCADE, verbose_name='Настройки рассылки')

    def __str__(self):
        return f'{self.user} - {self.distribution_settings}'

    class Meta:
        verbose_name = 'Клиент рассылки'
        verbose_name_plural = 'Клиенты рассылки'

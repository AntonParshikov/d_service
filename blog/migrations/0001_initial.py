# Generated by Django 4.2.4 on 2023-08-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Ссылка')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='statistic/', verbose_name='Превью')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('publication_feature', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('views_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]

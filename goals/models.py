from django.db import models


class GoalCategory(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(verbose_name='Название', max_length=255)
    user = models.ForeignKey('core.User', verbose_name='Автор', on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)
    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата последнего обновления')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Goal(models.Model):
    class Status(models.IntegerChoices):
        to_do = 1, 'К выполнению'
        in_progress = 2, 'В процессе'
        done = 3, 'Выполнено'
        archived = 4, 'Архив'

    class Priority(models.IntegerChoices):
        low = 1, 'Низкий'
        medium = 2, 'Средний'
        high = 3, 'Высокий'
        critical = 4, 'Критический'

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey('core.User', verbose_name='Автор', on_delete=models.PROTECT)
    due_date = models.DateField(verbose_name='Дата выполнения')
    category = models.ForeignKey(GoalCategory, verbose_name='Категор', related_name='goals', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Дата создания')
    updated = models.DateTimeField(verbose_name='Дата последнего обновления')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус', choices=Status.choices, default=Status.to_do
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет', choices=Priority.choices, default=Priority.medium
    )

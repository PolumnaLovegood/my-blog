from django.db import models



class Contact(models.Model):
    last_name = models.CharField(max_length=30,  verbose_name='Фамилия', blank=False)
    first_name = models.CharField(max_length=20, verbose_name='Имя', blank=False)
    patronymic = models.CharField(max_length=20, verbose_name='Отчество', blank=True)
    description = models.CharField(max_length=100, verbose_name='Описание', blank=True)
    birthday = models.DateField(blank=False, null=True, verbose_name='Дата рождения')
    number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=False)
    email = models.EmailField(max_length=50, verbose_name='Электронная почта', blank=True)
    social_networks = models.CharField(max_length=300, verbose_name='Соц.сети', blank=True)

    def __str__(self):
         return self.last_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
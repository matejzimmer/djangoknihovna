# Import třídy User z balíčku django.contrib.auth.models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Čtenář(models.Model):
    uživatelské_jméno = models.CharField(max_length=80, verbose_name='Uživatelské jméno', help_text='Zadejte uživatelské jméno',
                                         error_messages={'blank': 'Uživatelské jméno musí být vyplněno'})
    email = models.EmailField(verbose_name='Emailová adresa', help_text='Zadejte emailovou adresu',
                              error_messages={'blank': 'Emailová adresa musí být vyplněna'})
    datum_registrace = models.DateField(auto_now_add=True, verbose_name='Datum registrace')
    aktivní = models.BooleanField(default=True, verbose_name='Aktivní účet')

    class Meta:
        ordering = ['uživatelské_jméno']
        verbose_name = 'Čtenář'
        verbose_name_plural = 'Čtenáři'

    def __str__(self):
        return f'{self.uživatelské_jméno}'


class Půjčka(models.Model):
    čtenář = models.ForeignKey('projektapp.Čtenář', on_delete=models.CASCADE, verbose_name='Čtenář')
    datum_půjčení = models.DateField(auto_now_add=True, verbose_name='Datum půjčení')
    datum_vrácení = models.DateField(blank=True, null=True, verbose_name='Datum vrácení')

    class Meta:
        ordering = ['datum_půjčení']
        verbose_name = 'Půjčka'
        verbose_name_plural = 'Půjčky'

    def __str__(self):
        return f'Půjčka pro {self.čtenář}'


class Knihovna(models.Model):
    název = models.CharField(max_length=100, verbose_name='Název knihovny', help_text='Zadejte název knihovny',
                             error_messages={'blank': 'Název knihovny je povinný údaj'})
    adresa = models.CharField(max_length=200, verbose_name='Adresa knihovny', help_text='Zadejte adresu knihovny',
                              error_messages={'blank': 'Adresa knihovny je povinný údaj'})
    telefon = models.CharField(max_length=15, verbose_name='Telefonní číslo', help_text='Zadejte telefonní číslo knihovny')
    email = models.EmailField(verbose_name='Email knihovny', help_text='Zadejte emailovou adresu knihovny')

    class Meta:
        ordering = ['název']
        verbose_name = 'Knihovna'
        verbose_name_plural = 'Knihovny'

    def __str__(self):
        return f'{self.název}'


class Knihovník(models.Model):
    jméno = models.CharField(max_length=80, verbose_name='Jméno knihovníka', help_text='Zadejte jméno knihovníka',
                             error_messages={'blank': 'Jméno knihovníka musí být vyplněno'})
    příjmení = models.CharField(max_length=50, verbose_name='Příjmení knihovníka', help_text='Zadejte příjmení knihovníka',
                                error_messages={'blank': 'Příjmení knihovníka musí být vyplněno'})
    knihovna = models.ForeignKey('Knihovna', on_delete=models.CASCADE, verbose_name='Knihovna')

    class Meta:
        ordering = ['příjmení', 'jméno']
        verbose_name = 'Knihovník'
        verbose_name_plural = 'Knihovníci'

    def __str__(self):
        return f'{self.jméno} {self.příjmení}'


class Rezervace(models.Model):
    čtenář = models.ForeignKey('projektapp.Čtenář', on_delete=models.CASCADE, verbose_name='Čtenář')
    datum_rezervace = models.DateField(auto_now_add=True, verbose_name='Datum rezervace')
    stav = models.CharField(max_length=20, choices=[('čekající', 'Čekající'), ('vyzvednuto', 'Vyzvednuto')],
                            default='čekající', verbose_name='Stav rezervace')

    class Meta:
        ordering = ['datum_rezervace']
        verbose_name = 'Rezervace'
        verbose_name_plural = 'Rezervace'

    def __str__(self):
        return f'Rezervace pro {self.čtenář} - {self.stav}'

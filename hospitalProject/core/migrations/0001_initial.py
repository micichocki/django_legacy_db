# Generated by Django 5.0.2 on 2024-02-27 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaneLogowania',
            fields=[
                ('id_dane_logowania', models.AutoField(db_column='ID_dane_logowania', primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255)),
                ('haslo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dane_logowania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pracownicy',
            fields=[
                ('id_pracownicy', models.AutoField(db_column='ID_pracownicy', primary_key=True, serialize=False)),
                ('imie', models.CharField(blank=True, max_length=255, null=True)),
                ('nazwisko', models.CharField(blank=True, max_length=255, null=True)),
                ('stanowisko', models.CharField(blank=True, max_length=255, null=True)),
                ('data_zatrudnienia', models.DateField(blank=True, null=True)),
                ('adres', models.CharField(blank=True, max_length=255, null=True)),
                ('telefon', models.CharField(blank=True, max_length=255, null=True)),
                ('wynagrodzenie_brutto', models.CharField(blank=True, db_column='wynagrodzenie brutto', max_length=255, null=True)),
                ('lekarz_kontraktowy', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pracownicy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leki',
            fields=[
                ('id_leki', models.AutoField(db_column='ID_leki', primary_key=True, serialize=False)),
                ('nazwa_leku', models.CharField(blank=True, max_length=255, null=True)),
                ('firma', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'leki',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oddzialy',
            fields=[
                ('id_oddzialy', models.AutoField(db_column='ID_oddzialy', primary_key=True, serialize=False)),
                ('nazwa_oddzialu', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'oddzialy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pacjenci',
            fields=[
                ('id_pacjenci', models.AutoField(db_column='ID_pacjenci', primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('pesel', models.CharField(db_column='PESEL', max_length=11)),
                ('telefon', models.CharField(blank=True, max_length=255, null=True)),
                ('adres', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('data_urodzenia', models.DateField(blank=True, null=True)),
                ('plec', models.CharField(blank=True, max_length=17, null=True)),
            ],
            options={
                'db_table': 'pacjenci',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pobyty',
            fields=[
                ('id_pobyty', models.AutoField(db_column='ID_pobyty', primary_key=True, serialize=False)),
                ('czas_rozpoczecia', models.DateField(blank=True, null=True)),
                ('czas_zakonczenia', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pobyty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pokoje',
            fields=[
                ('id_pokoje', models.AutoField(db_column='ID_pokoje', primary_key=True, serialize=False)),
                ('czy_dostepny', models.IntegerField(blank=True, null=True)),
                ('numer_pokoju', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pokoje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recepty',
            fields=[
                ('id_recepty', models.AutoField(db_column='ID_recepty', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recepty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specjalizacje',
            fields=[
                ('id_specjalizacje', models.AutoField(db_column='ID_specjalizacje', primary_key=True, serialize=False)),
                ('nazwa_specjalizacji', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'specjalizacje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypyKont',
            fields=[
                ('id_typy_kont', models.AutoField(db_column='ID_typy_kont', primary_key=True, serialize=False)),
                ('typ_konta', models.CharField(blank=True, max_length=255, null=True)),
                ('uprawnienia', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'typy_kont',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypyZabiegow',
            fields=[
                ('id_typy_zabiegow', models.AutoField(db_column='ID_typy_zabiegow', primary_key=True, serialize=False)),
                ('nazwa_zabiegu', models.CharField(blank=True, max_length=255, null=True)),
                ('opis', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'typy_zabiegow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wizyty',
            fields=[
                ('id_wizyty', models.AutoField(db_column='ID_wizyty', primary_key=True, serialize=False)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('zakonczono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wizyty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zabiegi',
            fields=[
                ('id_zabiegi', models.AutoField(db_column='ID_zabiegi', primary_key=True, serialize=False)),
                ('wynik', models.TextField(blank=True, null=True)),
                ('data_zabiegu', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zabiegi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LekarzeSpecjalizacje',
            fields=[
                ('id_lekarze', models.OneToOneField(db_column='ID_lekarze', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.pracownicy')),
            ],
            options={
                'db_table': 'lekarze_specjalizacje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LekarzeTypyZabiegow',
            fields=[
                ('id_lekarze', models.OneToOneField(db_column='ID_lekarze', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.pracownicy')),
            ],
            options={
                'db_table': 'lekarze_typy_zabiegow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PracownicyTypyKont',
            fields=[
                ('id_pracownicy', models.OneToOneField(db_column='ID_pracownicy', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.pracownicy')),
            ],
            options={
                'db_table': 'pracownicy_typy_kont',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReceptyLeki',
            fields=[
                ('id_recepty', models.OneToOneField(db_column='ID_recepty', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.recepty')),
            ],
            options={
                'db_table': 'recepty_leki',
                'managed': False,
            },
        ),
    ]
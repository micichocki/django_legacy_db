# Generated by Django 5.0.2 on 2024-02-28 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('account_type_id', models.AutoField(db_column='ID_typy_kont', primary_key=True, serialize=False)),
                ('account_type', models.CharField(blank=True, db_column='typ_konta', max_length=255, null=True)),
                ('permissions', models.CharField(blank=True, db_column='uprawnienia', max_length=255, null=True)),
            ],
            options={
                'db_table': 'typy_kont',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(db_column='ID_wizyty', primary_key=True, serialize=False)),
                ('appointment_date', models.DateTimeField(blank=True, db_column='data', null=True)),
                ('completed', models.BooleanField(blank=True, db_column='zakonczono', null=True)),
            ],
            options={
                'db_table': 'wizyty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(db_column='ID_oddzialy', primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, db_column='nazwa_oddzialu', max_length=255, null=True)),
            ],
            options={
                'db_table': 'oddzialy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(db_column='ID_pracownicy', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='imie', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, db_column='nazwisko', max_length=255, null=True)),
                ('position', models.CharField(blank=True, db_column='stanowisko', max_length=255, null=True)),
                ('hire_date', models.DateField(blank=True, db_column='data_zatrudnienia', null=True)),
                ('address', models.CharField(blank=True, db_column='adres', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_column='telefon', max_length=255, null=True)),
                ('gross_salary', models.CharField(blank=True, db_column='wynagrodzenie_brutto', max_length=255, null=True)),
                ('contract_doctor', models.BooleanField(blank=True, db_column='lekarz_kontraktowy', null=True)),
            ],
            options={
                'db_table': 'pracownicy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('login_data_id', models.AutoField(db_column='ID_dane_logowania', primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(db_column='haslo', max_length=255)),
            ],
            options={
                'db_table': 'dane_logowania',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('medication_id', models.AutoField(db_column='ID_leki', primary_key=True, serialize=False)),
                ('medication_name', models.CharField(blank=True, db_column='nazwa_leku', max_length=255, null=True)),
                ('company', models.CharField(blank=True, db_column='firma', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='opis', max_length=255, null=True)),
            ],
            options={
                'db_table': 'leki',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(db_column='ID_pacjenci', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='imie', max_length=255)),
                ('last_name', models.CharField(db_column='nazwisko', max_length=255)),
                ('pesel', models.CharField(db_column='PESEL', max_length=11)),
                ('phone', models.CharField(blank=True, db_column='telefon', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='adres', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, db_column='data_urodzenia', null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], db_column='plec', max_length=1, null=True)),
            ],
            options={
                'db_table': 'pacjenci',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(db_column='ID_recepty', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recepty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('procedure_id', models.AutoField(db_column='ID_zabiegi', primary_key=True, serialize=False)),
                ('result', models.TextField(blank=True, db_column='wynik', null=True)),
                ('procedure_date', models.DateTimeField(blank=True, db_column='data_zabiegu', null=True)),
            ],
            options={
                'db_table': 'zabiegi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcedureType',
            fields=[
                ('procedure_type_id', models.AutoField(db_column='ID_procedure_type', primary_key=True, serialize=False)),
                ('procedure_name', models.CharField(blank=True, db_column='nazwa_zabiegu', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='opis', max_length=255, null=True)),
            ],
            options={
                'db_table': 'typy_zabiegow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(db_column='ID_pokoje', primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(blank=True, db_column='czy_dostepny', null=True)),
                ('room_number', models.IntegerField(blank=True, db_column='numer_pokoju', null=True)),
            ],
            options={
                'db_table': 'pokoje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specialization_id', models.AutoField(db_column='ID_specjalizacje', primary_key=True, serialize=False)),
                ('specialization_name', models.CharField(blank=True, db_column='nazwa_specjalizacji', max_length=50, null=True)),
            ],
            options={
                'db_table': 'specjalizacje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('stay_id', models.AutoField(db_column='ID_pobyty', primary_key=True, serialize=False)),
                ('start_time', models.DateField(blank=True, db_column='czas_rozpoczecia', null=True)),
                ('end_time', models.DateField(blank=True, db_column='czas_zakonczenia', null=True)),
            ],
            options={
                'db_table': 'pobyty',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='DaneLogowania',
        ),
        migrations.RemoveField(
            model_name='lekarzespecjalizacje',
            name='id_lekarze',
        ),
        migrations.RemoveField(
            model_name='lekarzetypyzabiegow',
            name='id_lekarze',
        ),
        migrations.DeleteModel(
            name='Leki',
        ),
        migrations.DeleteModel(
            name='Oddzialy',
        ),
        migrations.DeleteModel(
            name='Pacjenci',
        ),
        migrations.DeleteModel(
            name='Pobyty',
        ),
        migrations.DeleteModel(
            name='Pokoje',
        ),
        migrations.RemoveField(
            model_name='pracownicytypykont',
            name='id_pracownicy',
        ),
        migrations.RemoveField(
            model_name='receptyleki',
            name='id_recepty',
        ),
        migrations.DeleteModel(
            name='Specjalizacje',
        ),
        migrations.DeleteModel(
            name='TypyKont',
        ),
        migrations.DeleteModel(
            name='TypyZabiegow',
        ),
        migrations.DeleteModel(
            name='Wizyty',
        ),
        migrations.DeleteModel(
            name='Zabiegi',
        ),
        migrations.CreateModel(
            name='DoctorsProcedureType',
            fields=[
                ('doctor_id', models.OneToOneField(db_column='ID_lekarze', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.employee')),
            ],
            options={
                'db_table': 'lekarze_typy_zabiegow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorsSpecialization',
            fields=[
                ('doctor_id', models.OneToOneField(db_column='ID_lekarze', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.employee')),
            ],
            options={
                'db_table': 'lekarze_specjalizacje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeAccountType',
            fields=[
                ('employee_id', models.OneToOneField(db_column='ID_pracownicy', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.employee')),
            ],
            options={
                'db_table': 'pracownicy_typy_kont',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrescriptionMedication',
            fields=[
                ('prescription_id', models.OneToOneField(db_column='ID_recepty', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.prescription')),
            ],
            options={
                'db_table': 'recepty_leki',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='LekarzeSpecjalizacje',
        ),
        migrations.DeleteModel(
            name='LekarzeTypyZabiegow',
        ),
        migrations.DeleteModel(
            name='Pracownicy',
        ),
        migrations.DeleteModel(
            name='PracownicyTypyKont',
        ),
        migrations.DeleteModel(
            name='Recepty',
        ),
        migrations.DeleteModel(
            name='ReceptyLeki',
        ),
    ]

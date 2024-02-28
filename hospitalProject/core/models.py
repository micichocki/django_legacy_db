from django.db import models


class LoginData(models.Model):
    login_data_id = models.AutoField(db_column='ID_dane_logowania', primary_key=True)
    employee_id = models.ForeignKey('Employee', models.DO_NOTHING, db_column='ID_pracownicy', blank=True, null=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255,db_column='haslo')

    class Meta:
        managed = False
        db_table = 'dane_logowania'


class DoctorsSpecialization(models.Model):
    doctor_id = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ID_lekarze', primary_key=True)
    specialization_id = models.ForeignKey('Specialization', models.DO_NOTHING, db_column='ID_specjalizacje')

    class Meta:
        managed = False
        db_table = 'lekarze_specjalizacje'
        unique_together = (('doctor_id', 'specialization_id'),)


class DoctorsProcedureType(models.Model):
    doctor_id = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ID_lekarze', primary_key=True)
    procedure_type_id = models.ForeignKey('ProcedureType', models.DO_NOTHING, db_column='ID_typy_zabiegow')

    class Meta:
        managed = False
        db_table = 'lekarze_typy_zabiegow'
        unique_together = (('doctor_id', 'procedure_type_id'),)


class Medication(models.Model):
    medication_id = models.AutoField(db_column='ID_leki', primary_key=True)
    medication_name = models.CharField(max_length=255,db_column='nazwa_leku', blank=True, null=True)
    company = models.CharField(max_length=255,db_column='firma', blank=True, null=True)
    description = models.CharField(max_length=255,db_column='opis', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leki'


class Department(models.Model):
    department_id = models.AutoField(db_column='ID_oddzialy', primary_key=True)
    department_name = models.CharField(max_length=255,db_column='nazwa_oddzialu', blank=True, null=True)
    head_id = models.ForeignKey('Employee', models.DO_NOTHING, db_column='ID_ordynatorzy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oddzialy'


class Patient(models.Model):
    patient_id = models.AutoField(db_column='ID_pacjenci', primary_key=True)
    first_name = models.CharField(max_length=255,db_column='imie')
    last_name = models.CharField(max_length=255,db_column='nazwisko')
    pesel = models.CharField(max_length=11,db_column='PESEL')
    phone = models.CharField(max_length=255,db_column='telefon', blank=True, null=True)
    address = models.CharField(max_length=255,db_column='adres', blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True,db_column='data_urodzenia', null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, db_column='plec', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacjenci'


class Stay(models.Model):
    stay_id = models.AutoField(db_column='ID_pobyty', primary_key=True)
    patient_id = models.ForeignKey(Patient, models.DO_NOTHING, db_column='ID_pacjenci', blank=True, null=True)
    room_id = models.ForeignKey('Room', models.DO_NOTHING, db_column='ID_pokoje', blank=True, null=True)
    start_time = models.DateField(db_column='czas_rozpoczecia',blank=True, null=True)
    end_time = models.DateField(db_column='czas_zakonczenia',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pobyty'


class Room(models.Model):
    room_id = models.AutoField(db_column='ID_pokoje', primary_key=True)
    department_id = models.ForeignKey(Department, models.DO_NOTHING, db_column='ID_oddzialy', blank=True, null=True)
    is_available = models.BooleanField(db_column='czy_dostepny',blank=True, null=True)
    room_number = models.IntegerField(db_column='numer_pokoju',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokoje'


class Employee(models.Model):
    employee_id = models.AutoField(db_column='ID_pracownicy', primary_key=True)
    first_name = models.CharField(max_length=255,db_column='imie', blank=True, null=True)
    last_name = models.CharField(max_length=255,db_column='nazwisko', blank=True, null=True)
    position = models.CharField(max_length=255,db_column='stanowisko', blank=True, null=True)
    hire_date = models.DateField(blank=True,db_column='data_zatrudnienia', null=True)
    address = models.CharField(max_length=255,db_column='adres', blank=True, null=True)
    phone = models.CharField(max_length=255,db_column='telefon', blank=True, null=True)
    gross_salary = models.CharField(max_length=255,db_column='wynagrodzenie brutto', blank=True, null=True)
    contract_doctor = models.BooleanField(db_column='lekarz_kontraktowy',blank=True, null=True)
    department_id = models.ForeignKey(Department, models.DO_NOTHING, db_column='ID_oddzialy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pracownicy'


class EmployeeAccountType(models.Model):
    employee_id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID_pracownicy', primary_key=True)
    account_type_id = models.ForeignKey('AccountType', models.DO_NOTHING, db_column='ID_typy_kont')

    class Meta:
        managed = False
        db_table = 'pracownicy_typy_kont'
        unique_together = (('employee_id', 'account_type_id'),)


class Prescription(models.Model):
    prescription_id = models.AutoField(db_column='ID_recepty', primary_key=True)
    doctor_id = models.ForeignKey(Employee, models.DO_NOTHING, db_column='ID_lekarze', blank=True, null=True)
    patient_id = models.ForeignKey(Patient, models.DO_NOTHING, db_column='ID_pacjenci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recepty'


class PrescriptionMedication(models.Model):
    prescription_id = models.OneToOneField(Prescription, models.DO_NOTHING, db_column='ID_recepty', primary_key=True)
    medication_id = models.ForeignKey(Medication, models.DO_NOTHING, db_column='ID_leki')

    class Meta:
        managed = False
        db_table = 'recepty_leki'
        unique_together = (('prescription_id', 'medication_id'),)


class Specialization(models.Model):
    specialization_id = models.AutoField(db_column='ID_specjalizacje', primary_key=True)
    specialization_name = models.CharField(max_length=50,db_column='nazwa_specjalizacji', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specjalizacje'


class AccountType(models.Model):
    account_type_id = models.AutoField(db_column='ID_typy_kont', primary_key=True)
    account_type = models.CharField(max_length=255,db_column='typ_konta', blank=True, null=True)
    permissions = models.CharField(max_length=255,db_column='uprawnienia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typy_kont'


class ProcedureType(models.Model):
    procedure_type_id = models.AutoField(db_column='ID_typy_zabiegow', primary_key=True)
    procedure_name = models.CharField(max_length=255, db_column='nazwa_zabiegu', blank=True, null=True)
    description = models.CharField(max_length=255, db_column='opis', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typy_zabiegow'


class Appointment(models.Model):
    appointment_id = models.AutoField(db_column='ID_wizyty', primary_key=True)
    patient_id = models.ForeignKey(Patient, models.DO_NOTHING, db_column='ID_pacjenci', blank=True, null=True)
    doctor_id = models.ForeignKey(Employee, models.DO_NOTHING, db_column='ID_lekarze', blank=True, null=True)
    appointment_date = models.DateTimeField(blank=True,db_column='data', null=True)
    completed = models.BooleanField(blank=True,db_column='zakonczono', null=True)

    class Meta:
        managed = False
        db_table = 'wizyty'


class Procedure(models.Model):
    procedure_id = models.AutoField(db_column='ID_zabiegi', primary_key=True)
    doctor_id = models.ForeignKey(Employee, models.DO_NOTHING, db_column='ID_lekarze', blank=True, null=True)
    patient_id = models.ForeignKey(Patient, models.DO_NOTHING, db_column='ID_pacjenci', blank=True, null=True)
    procedure_type_id = models.ForeignKey(ProcedureType, models.DO_NOTHING, db_column='ID_typy_zabiegow', blank=True, null=True)
    result = models.TextField(db_column='wynik',blank=True, null=True)
    procedure_date = models.DateTimeField(db_column='data_zabiegu',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zabiegi'

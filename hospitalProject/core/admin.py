from django.contrib import admin
from .models import LoginData, DoctorsSpecialization, DoctorsProcedureType, Medication, Department, Patient, Stay, Room, Employee, EmployeeAccountType, Prescription, PrescriptionMedication, Specialization, AccountType, ProcedureType, Appointment, Procedure

@admin.register(LoginData)
class LoginDataAdmin(admin.ModelAdmin):
    pass

@admin.register(DoctorsSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    pass

@admin.register(DoctorsProcedureType)
class DoctorProcedureTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Medication)
class MedicinesAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Patient)
class PatientsAdmin(admin.ModelAdmin):
    pass

@admin.register(Stay)
class StaysAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeesAdmin(admin.ModelAdmin):
    pass

@admin.register(EmployeeAccountType)
class EmployeeAccountTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Prescription)
class PrescriptionsAdmin(admin.ModelAdmin):
    pass

@admin.register(PrescriptionMedication)
class PrescriptionMedicinesAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialization)
class SpecializationsAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountType)
class AccountTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(ProcedureType)
class ProcedureTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Procedure)
class ProceduresAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Students,Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','surname']

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','surname','age','classroom']   
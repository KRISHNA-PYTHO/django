from django.contrib import admin
from . models import CollegeAdmission
# Register your models here.

@admin.register(CollegeAdmission)
class CollegeAdmission(admin.ModelAdmin):
    list_display =['id','name','last_name']

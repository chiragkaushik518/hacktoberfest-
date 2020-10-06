from django.contrib import admin
from testapp import models
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['pdate','loc','sal','qual']

admin.site.register(models.Job, JobAdmin)

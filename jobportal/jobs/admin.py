from django.contrib import admin
from .models import Job, Application
from accounts.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Application)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    filterset_fields = ['location', 'salary']
    search_fields = ['title', 'company']


from django.contrib import admin
from .models import algorithm

@admin.register(algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    search_fields = ['name', "description"]

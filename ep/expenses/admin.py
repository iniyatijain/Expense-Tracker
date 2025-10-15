from django.contrib import admin
from .models import expense, category

# Register your models here.
admin.site.register(expense)
admin.site.register(category)
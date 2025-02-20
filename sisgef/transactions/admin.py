from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name"]

class TransactionAdmin(admin.ModelAdmin):
    search_fields = ["category", "value", "date", "user"]
    list_display = ["id", "category", "value", "date"]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Transaction, TransactionAdmin)

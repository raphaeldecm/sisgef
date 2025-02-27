from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    readonly_fields = ["updated_by", "created_at"]
    list_display = ["name", "description", "type"]

class IncomeAdmin(admin.ModelAdmin):
    search_fields = ["category", "value", "date", "payment_method", "description",
    "payment_proof"]
    readonly_fields = ["updated_by", "created_at"]
    list_display = ["id", "category", "value", "date"]

class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ["category", "value", "date", "payment_method", "description",
    "payment_proof"]
    readonly_fields = ["updated_by", "created_at"]
    list_display = ["id", "category", "value", "date"]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Income, IncomeAdmin)
admin.site.register(models.Expense, ExpenseAdmin)


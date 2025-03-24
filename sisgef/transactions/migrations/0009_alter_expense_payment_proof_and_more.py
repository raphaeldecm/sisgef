# Generated by Django 5.0.12 on 2025-03-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_alter_expense_description_alter_expense_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='payment_proof',
            field=models.ImageField(blank=True, null=True, upload_to='payment_proofs/expense/'),
        ),
        migrations.AlterField(
            model_name='income',
            name='payment_proof',
            field=models.ImageField(blank=True, null=True, upload_to='payment_proofs/income/'),
        ),
    ]

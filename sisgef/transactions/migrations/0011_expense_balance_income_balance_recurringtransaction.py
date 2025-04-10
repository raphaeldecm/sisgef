# Generated by Django 5.0.12 on 2025-04-11 14:06

import django.db.models.deletion
import sisgef.core.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balances', '0001_initial'),
        ('transactions', '0010_income_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='balances.balance', verbose_name='Balanço'),
        ),
        migrations.AddField(
            model_name='income',
            name='balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='balances.balance', verbose_name='Balanço'),
        ),
        migrations.CreateModel(
            name='RecurringTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('start_date', models.DateField(verbose_name='Data de Início')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data de Fim')),
                ('frequency', models.CharField(choices=[('monthly', 'Mensal'), ('weekly', 'Semanal'), ('daily', 'Diária')], default='monthly', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.category')),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET(sisgef.core.models.get_sentinel_user), related_name='created_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET(sisgef.core.models.get_sentinel_user), related_name='updated_%(app_label)s_%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

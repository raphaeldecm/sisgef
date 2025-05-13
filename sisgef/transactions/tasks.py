from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from sisgef.transactions.models import Expense
from sisgef.transactions.models import Income

from .utils import add_months


@shared_task
def generate_recurring_transactions():
    today = timezone.now().date()
    total_created = 0

    for model in (Income, Expense):
        recurring_transactions = model.objects.filter(
            is_recurring=True,
            date__lte=today,
        )

        for base in recurring_transactions:
            existing_count = base.recurrences.count()
            next_date = base.date

            while True:
                if base.recurrence_frequency == base.Frequency.DAILY:
                    next_date += timedelta(days=1)
                elif base.recurrence_frequency == base.Frequency.WEEKLY:
                    next_date += timedelta(weeks=1)
                elif base.recurrence_frequency == base.Frequency.MONTHLY:
                    next_date = add_months(next_date, 1)
                elif base.recurrence_frequency == base.Frequency.YEARLY:
                    next_date = add_months(next_date, 12)
                else:
                    break

                if next_date.date() > today:
                    break

                if base.recurrence_end_date and next_date.date() > base.recurrence_end_date:
                    break

                if base.recurrence_count and existing_count >= base.recurrence_count:
                    break

                if model.objects.filter(parent_transaction=base, date=next_date).exists():
                    existing_count += 1
                    continue

                model.objects.create(
                    status=base.PaymentStatus.PENDING,
                    description=base.description,
                    value=base.value,
                    date=next_date,
                    category=base.category,
                    payment_method=base.payment_method,
                    is_recurring=False,
                    parent_transaction=base,
                    balance=base.balance,
                )
                total_created += 1
                existing_count += 1

    return f"{total_created} transações (Income/Expense) geradas com sucesso."

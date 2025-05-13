from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from .models import Expense  # ou apenas use o modelo específico
from .models import Income  # ou apenas use o modelo específico
from .models import Transaction  # ou apenas use o modelo específico
from .utils import add_months


@shared_task
def generate_recurring_transactions():
    today = timezone.now().date()

    # Pega todas as transações recorrentes com data anterior a hoje
    recurring_transactions = Transaction.objects.filter(
        is_recurring=True,
        date__lte=today,
    )

    created_total = 0

    for transaction in recurring_transactions:
        next_date = transaction.date
        created_count = 0

        # Limite baseado em data
        while True:
            # Gerar próxima data
            if transaction.recurrence_frequency == Transaction.Frequency.DAILY:
                next_date += timedelta(days=1)
            elif transaction.recurrence_frequency == Transaction.Frequency.WEEKLY:
                next_date += timedelta(weeks=1)
            elif transaction.recurrence_frequency == Transaction.Frequency.MONTHLY:
                next_date = add_months(next_date, 1)
            elif transaction.recurrence_frequency == Transaction.Frequency.YEARLY:
                next_date = add_months(next_date, 12)
            else:
                break  # Frequência inválida

            if next_date.date() > today:
                break  # Só criamos até hoje

            if transaction.recurrence_end_date and next_date.date() > transaction.recurrence_end_date:
                break

            if transaction.recurrence_count and created_count >= transaction.recurrence_count:
                break

            # Verifica se já existe uma transação filha com essa data
            if Transaction.objects.filter(parent_transaction=transaction, date=next_date).exists():
                continue

            model = transaction.__class__

            model.objects.create(
                status=Transaction.PaymentStatus.PENDING,
                description=transaction.description,
                value=transaction.value,
                date=next_date,
                category=transaction.category,
                payment_method=transaction.payment_method,
                is_recurring=False,
                parent_transaction=transaction,
                balance=transaction.balance,
            )
            created_count += 1
            created_total += 1

    return f"{created_total} transações recorrentes geradas."

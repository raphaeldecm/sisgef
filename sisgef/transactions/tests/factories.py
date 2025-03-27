import factory
from django.utils import timezone
from faker import Faker

from sisgef.transactions.models import Category
from sisgef.transactions.models import Expense
from sisgef.transactions.models import Income
from sisgef.transactions.models import Transaction

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda _: fake.sentence())
    type = factory.Iterator([Category.Type.INCOME, Category.Type.EXPENSE])

class TransactionFactory(factory.django.DjangoModelFactory):

    status = factory.Iterator([
        Transaction.PaymentStatus.PENDING,
        Transaction.PaymentStatus.PAID,
        Transaction.PaymentStatus.CANCELED,
        Transaction.PaymentStatus.OVERDUE,
    ])
    description = factory.LazyAttribute(lambda _: fake.sentence())
    value = factory.LazyAttribute(
        lambda _: fake.pydecimal(left_digits=4, right_digits=2, positive=True))
    date = factory.LazyAttribute(
        lambda _: timezone.make_aware(fake.date_time_this_year()))
    category = factory.Iterator(Category.objects.all())
    payment_method = factory.Iterator(
        [
            Transaction.PaymentMethod.CASH, Transaction.PaymentMethod.CREDIT_CARD,
            Transaction.PaymentMethod.DEBIT_CARD, Transaction.PaymentMethod.PIX,
            Transaction.PaymentMethod.TRANSFER, Transaction.PaymentMethod.BOLETO,
            Transaction.PaymentMethod.CHEQUE, Transaction.PaymentMethod.OTHER,
         ])

class IncomeFactory(TransactionFactory):
    class Meta:
        model = Income

class ExpenseFactory(TransactionFactory):
    class Meta:
        model = Expense

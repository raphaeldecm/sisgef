from dateutil.relativedelta import relativedelta


def add_months(sourcedate, months):
    return sourcedate + relativedelta(months=months)

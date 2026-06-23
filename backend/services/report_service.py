from backend.database.invoices_db import get_invoices


def total_sales():

    invoices = get_invoices()

    total = 0

    for invoice in invoices:
        total += invoice[5]

    return total
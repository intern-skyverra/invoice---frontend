from backend.database.db import get_connection


def save_invoice(
    invoice_no,
    customer_name,
    subtotal,
    gst,
    grand_total,
    invoice_date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO invoices
    (
        invoice_no,
        customer_name,
        subtotal,
        gst,
        grand_total,
        invoice_date
    )
    VALUES
    (
        ?, ?, ?, ?, ?, ?
    )
    """,
    (
        invoice_no,
        customer_name,
        subtotal,
        gst,
        grand_total,
        invoice_date
    ))

    conn.commit()
    conn.close()


def get_invoices():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM invoices"
    )

    data = cursor.fetchall()

    conn.close()

    return data
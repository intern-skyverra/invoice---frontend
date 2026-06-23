from backend.database.db import get_connection
from backend.config import DATABASE_PATH

print("Using DB:", DATABASE_PATH)

def add_customer(
    name,
    phone,
    email,
    gst_number,
    address
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM customers
        WHERE LOWER(name)=LOWER(?)
        """,
        (name,)
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE customers
            SET
            phone=?,
            email=?,
            gst_number=?,
            address=?
            WHERE id=?
            """,
            (
                phone,
                email,
                gst_number,
                address,
                existing[0]
            )
        )

    else:

        cursor.execute(
            """
            INSERT INTO customers
            (
                name,
                phone,
                email,
                gst_number,
                address
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                name,
                phone,
                email,
                gst_number,
                address
            )
        )

    conn.commit()
    conn.close()


def get_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers ORDER BY name"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def get_customer_by_name(name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM customers
        WHERE LOWER(name)=LOWER(?)
        """,
        (name,)
    )

    customer = cursor.fetchone()

    conn.close()

    return customer

def get_customer_names():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name
        FROM customers
        ORDER BY name
        """
    )

    data = cursor.fetchall()

    conn.close()

    return [row[0] for row in data]
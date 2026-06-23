from backend.database.db import get_connection


def add_inventory(
    item_name,
    sku,
    quantity,
    price,
    gst_percent,
    entry_date,
    sale_date
):

    gst_amount = price * gst_percent / 100

    amount = price + gst_amount

    total = amount * quantity

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, pending_stock
        FROM inventory
        WHERE LOWER(item_name)=LOWER(?)
        """,
        (item_name,)
    )

    existing = cursor.fetchone()

    if existing:

        item_id = existing[0]

        current_stock = existing[1]

        new_stock = current_stock + quantity

        cursor.execute(
            """
            UPDATE inventory
            SET
                sku=?,
                quantity=?,
                price=?,
                gst_percent=?,
                gst_amount=?,
                amount=?,
                total=?,
                pending_stock=?,
                entry_date=?,
                sale_date=?
            WHERE id=?
            """,
            (
                sku,
                quantity,
                price,
                gst_percent,
                gst_amount,
                amount,
                total,
                new_stock,
                entry_date,
                sale_date,
                item_id
            )
        )

    else:

        cursor.execute(
            """
            INSERT INTO inventory
            (
                item_name,
                sku,
                quantity,
                price,
                gst_percent,
                gst_amount,
                amount,
                total,
                pending_stock,
                entry_date,
                sale_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                item_name,
                sku,
                quantity,
                price,
                gst_percent,
                gst_amount,
                amount,
                total,
                quantity,
                entry_date,
                sale_date
            )
        )

    conn.commit()
    conn.close()


def get_inventory():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM inventory
        ORDER BY item_name
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data

def get_pending_stock(item_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT pending_stock
        FROM inventory
        WHERE LOWER(item_name)=LOWER(?)
        """,
        (item_name,)
    )

    item = cursor.fetchone()

    conn.close()

    if item:
        return item[0]

    return None


def reduce_stock(item_name, sold_qty):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT pending_stock
        FROM inventory
        WHERE LOWER(item_name)=LOWER(?)
        """,
        (item_name,)
    )

    item = cursor.fetchone()

    if not item:

        conn.close()
        return False, "Item not found in inventory"

    current_stock = item[0]

    if current_stock < sold_qty:

        conn.close()
        return False, (
            f"Insufficient stock for {item_name}. "
            f"Available: {current_stock}"
        )

    new_stock = current_stock - sold_qty

    cursor.execute(
        """
        UPDATE inventory
        SET pending_stock=?
        WHERE LOWER(item_name)=LOWER(?)
        """,
        (
            new_stock,
            item_name
        )
    )

    conn.commit()
    conn.close()

    return True, "Stock updated"
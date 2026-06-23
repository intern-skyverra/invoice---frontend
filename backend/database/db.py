import sqlite3

from backend.config import DATABASE_PATH


def get_connection():

    return sqlite3.connect(
        DATABASE_PATH
    )


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # ==========================
    # CUSTOMERS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    gst_number TEXT,
    address TEXT
)
""")

    # ==========================
    # INVENTORY
    # ==========================

    cursor.execute("""
   CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    sku TEXT,
    quantity INTEGER,
    price REAL,
    gst_percent REAL,
    gst_amount REAL,
    amount REAL,
    total REAL,
    pending_stock INTEGER,
    entry_date TEXT,
    sale_date TEXT
    )
    """)

    # ==========================
    # COMPANY
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company (
    id INTEGER PRIMARY KEY,
    company_name TEXT,
    gstin TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    category TEXT,
    password TEXT,
    logo_path TEXT
    )
    """)

    # ==========================
    # COMPANY USERS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_name TEXT NOT NULL,

    gstin TEXT,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    phone TEXT,

    address TEXT,

    category TEXT,

    logo_path TEXT

    )
    """)


    # ==========================
    # INVOICES
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_no TEXT,
        customer_name TEXT,
        subtotal REAL,
        gst REAL,
        grand_total REAL,
        invoice_date TEXT
    )
    """)

    conn.commit()

    conn.close()
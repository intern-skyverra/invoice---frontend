from backend.database.db import get_connection


def save_company(
    company_name,
    gstin,
    email,
    phone,
    address
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO company
    (
        id,
        company_name,
        gstin,
        email,
        phone,
        address
    )
    VALUES
    (
        1,
        ?, ?, ?, ?, ?
    )
    """,
    (
        company_name,
        gstin,
        email,
        phone,
        address
    ))

    conn.commit()
    conn.close()


def get_company():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM company WHERE id=1"
    )

    data = cursor.fetchone()

    conn.close()

    return data

    def create_company_user(
    company_name,
    gstin,
    email,
    password,
    phone,
    address,
    category,
    logo_path
):

     conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO company_users
        (
            company_name,
            gstin,
            email,
            password,
            phone,
            address,
            category,
            logo_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company_name,
            gstin,
            email,
            password,
            phone,
            address,
            category,
            logo_path
        )
    )

    conn.commit()
    conn.close()


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM company_users
        WHERE email=?
        AND password=?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def email_exists(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM company_users
        WHERE email=?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None
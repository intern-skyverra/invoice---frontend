from backend.database.db import get_connection


def register_company(
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
        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?
        )
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


def login_company(
    email,
    password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM company_users
        WHERE email=?
        AND password=?
        """,
        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user
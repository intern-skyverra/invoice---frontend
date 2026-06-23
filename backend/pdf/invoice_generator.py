from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Spacer,
    Paragraph,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

from backend.services.number_to_words import number_to_words


def generate_invoice(data, filename):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=20,
        rightMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==========================
    # HEADER
    # ==========================

    try:
        logo = Image(
            "assets/logo.jpeg",
            width=60,
            height=60
        )
    except:
        logo = ""

    header = Table([
        [
            logo,

            Paragraph("""
            <b>SkyVerra Consulting</b><br/>
            The Status Road, BSNL Colony<br/>
            Harni, Vadodara, Gujarat - 390018<br/>
            Phone: 8511236347<br/>
            Email: info@skyverraconsulting.com
            """, styles["Normal"]),

            Paragraph("""
            <b>TAX INVOICE</b>
            """, styles["Title"])
        ]
    ], colWidths=[70, 300, 150])

    header.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "TOP")
    ]))

    elements.append(header)
    elements.append(Spacer(1, 10))

    # ==========================
    # CUSTOMER + INVOICE DETAILS
    # ==========================

    details = Table([
        [
            "Customer Name",
            data["customer"],
            "Invoice No",
            data["invoice_no"]
        ],

        [
            "Address",
            data["address"],
            "Invoice Date",
            data["date"]
        ],

        [
            "GSTIN",
            data["gstin"],
            "Phone",
            data["phone"]
        ],

        [
            "Email",
            data["email"],
            "",
            ""
        ]
    ], colWidths=[90, 220, 90, 140])

    details.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))

    elements.append(details)
    elements.append(Spacer(1, 10))

    # ==========================
    # PRODUCTS
    # ==========================

    product_rows = [[
        "No",
        "Description",
        "Qty",
        "Rate",
        "GST %",
        "Amount"
    ]]

    total_amount = 0

    for i, item in enumerate(data["items"], start=1):

        total_amount += float(item["total"])

        product_rows.append([
            str(i),
            item["product"],
            item["qty"],
            item["rate"],
            item["gst"],
            f"{item['total']:.2f}"
        ])

    products = Table(
        product_rows,
        colWidths=[35, 170, 70, 50, 70, 60, 90]
    )

    products.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER")
    ]))

    elements.append(products)
    elements.append(Spacer(1, 10))

    # ==========================
    # TOTAL
    # ==========================

    totals = Table([
        [
            "Amount In Words",
            number_to_words(total_amount)
        ],

        [
            "Grand Total",
            f"₹ {total_amount:,.2f}"
        ]
    ], colWidths=[180, 385])

    totals.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))

    elements.append(totals)
    elements.append(Spacer(1, 15))

    # ==========================
    # QR SECTION
    # ==========================

    qr = Table(
        [["QR / SCANNER"]],
        colWidths=[120],
        rowHeights=[120]
    )

    qr.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE")
    ]))

    elements.append(qr)
    elements.append(Spacer(1, 20))

    # ==========================
    # FOOTER
    # ==========================

    footer = Table([
        [
            Paragraph("""
            <b>Terms & Conditions</b><br/>
            Goods once sold will not be taken back.
            """, styles["Normal"]),

            Paragraph("""
            <b>For SkyVerra Consulting</b><br/><br/><br/>
            Authorized Signature
            """, styles["Normal"])
        ]
    ], colWidths=[300, 265])

    footer.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))

    elements.append(footer)

    doc.build(elements)
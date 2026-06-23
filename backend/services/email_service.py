import smtplib

from email.message import EmailMessage



def send_email(
        receiver,
        invoice_file
):


    sender = "YOUR_GMAIL@gmail.com"

    password = "YOUR_APP_PASSWORD"



    msg = EmailMessage()


    msg["Subject"] = (
        "SkyVerra Consulting Invoice"
    )

    msg["From"] = sender

    msg["To"] = receiver



    msg.set_content(
        """
        Dear Customer,

        Please find your invoice attached.

        Thank you,
        SkyVerra Consulting
        """
    )



    with open(
        invoice_file,
        "rb"
    ) as file:


        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="pdf",
            filename="Invoice.pdf"
        )



    server = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    )


    server.login(
        sender,
        password
    )


    server.send_message(
        msg
    )


    server.quit()
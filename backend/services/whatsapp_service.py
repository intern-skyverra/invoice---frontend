import urllib.parse
import webbrowser


def send_whatsapp(phone, invoice_file):

    message = (
        "Hello,\n\n"
        "Your invoice from SkyVerra Consulting is ready.\n\n"
        "Invoice File: "
        + invoice_file
    )


    url = (
        "https://wa.me/"
        + phone
        +
        "?text="
        +
        urllib.parse.quote(message)
    )


    webbrowser.open(url)
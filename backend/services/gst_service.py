def calculate_gst(amount, gst_percent):

    gst_amount = (
        amount * gst_percent
    ) / 100

    total = amount + gst_amount

    return gst_amount, total
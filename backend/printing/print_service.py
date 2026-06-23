import os

def print_file(pdf_path):

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"{pdf_path} not found"
        )

    try:
        os.startfile(
            pdf_path,
            "print"
        )

    except Exception as e:
        print("Print Error:", e)
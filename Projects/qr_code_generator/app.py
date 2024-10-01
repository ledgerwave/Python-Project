"""
QR code generator program
"""

import qrcode


def generate_qr_code(data, file_name):
    """
    Generate a QR code from the given data and save it to the given file name
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


QR_DATA = "https://sarmad-portfolio.vercel.app/"

generate_qr_code(QR_DATA, "QRs/qr_code.png")
print("QR code generated successfully")

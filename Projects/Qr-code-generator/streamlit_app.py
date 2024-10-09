"""
QR code generator streamlit app
"""

import streamlit as st
import qrcode


def generate_qr_code(url: str):
    """
    Generates a QR code

    Args:
        url (string): link to be converted to qr code

    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    if url:
        st.image(img.get_image())


def main():
    """
    Main function
    """
    st.header("QR code generator")
    link = st.text_input(placeholder="Enter link here...", label="Link")

    generate_qr_code(link)


if __name__ == "__main__":
    main()

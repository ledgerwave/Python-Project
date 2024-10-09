"""
Image background remover streamlit app
"""

from rembg import remove
from PIL import Image
import streamlit as st


def image_bg_remover(image_path: str):
    """
    Removes background of the given image
    """
    if image_path:
        input_image = Image.open(image_path)
        output = remove(input_image)
        st.write(output)


def main():
    """
    Main function
    """
    st.header("Image background remover")
    image_path = st.camera_input(label="Insert picture")
    image_bg_remover(image_path)


if __name__ == "__main__":
    main()

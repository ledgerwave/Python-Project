"""
Image background remover streamlit app
"""

from io import BytesIO
from rembg import remove
from PIL import Image
import streamlit as st

st.title("Image Background Remover")


def image_bg_remover(image):
    """
    Removes background of the given image
    """
    if image:
        input_image = Image.open(image)
        output = remove(input_image)
        return output
    return None


def main():
    """
    Main function
    """
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if image_file:
        st.image(image_file, caption="Original Image", use_column_width=True)

        # Process the image to remove the background
        output_image = image_bg_remover(image_file)

        if output_image:
            st.image(
                output_image,
                caption="Image with Background Removed",
                use_column_width=True,
            )

            # Convert the image to a BytesIO object to enable downloading
            img_bytes = BytesIO()
            output_image.save(img_bytes, format="PNG")
            img_bytes.seek(0)

            # Add a download button
            st.download_button(
                label="Download Image with Background Removed",
                data=img_bytes,
                file_name="background_removed.png",
                mime="image/png",
            )


if __name__ == "__main__":
    main()

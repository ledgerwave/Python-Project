"""
Markdown formatting remover using REGEX and streamlit
"""

import re
import streamlit as st


def remove_markdown_formatting(text: str) -> str:
    """
    Removes markdown formatting from the given text.
    """
    # Remove headers
    text = re.sub(r"^\s*#{1,6}\s*", "", text, flags=re.MULTILINE)
    # Remove emphasis (single * or _)
    text = re.sub(r"(\*|_)(.*?)\1", r"\2", text)
    # Remove strong emphasis (double ** or __)
    text = re.sub(r"(\*\*|__)(.*?)\1", r"\2", text)
    # Remove inline code
    text = re.sub(r"`([^`]*)`", r"\1", text)
    # Remove links and images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # Images
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)  # Links
    # Remove blockquotes
    text = re.sub(r"^\s*>\s*", "", text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r"^\s*(\-{3,}|\*{3,})\s*$", "", text, flags=re.MULTILINE)

    return text


# Streamlit app
st.title("Markdown Formatting Remover")

# Textarea for markdown input
markdown_text = st.text_area("Enter Markdown Text", height=300)

# Button to remove markdown formatting
if st.button("Remove Formatting"):
    unformatted_text = remove_markdown_formatting(markdown_text)
    st.text_area("Unformatted Text", unformatted_text, height=300)

    # Button to copy unformatted text
    st.code(unformatted_text, language="text")

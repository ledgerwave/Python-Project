"""
Program to remove markdown formatting from a string.
"""

import re


def remove_markdown_formatting(text: str):
    """
    Removes markdown formatting and returns the cleaned text.
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


# Example usage
INPUT_TEXT = """
# Header 1
## Header 2
This is a *sample* text with **bold** and _italic_ formatting.
Here is some `inline code`.
> This is a blockquote.
Here is a [link](http://example.com).
![Image](http://example.com/image.jpg)
---
"""
cleaned_text = remove_markdown_formatting(INPUT_TEXT)
print(cleaned_text)

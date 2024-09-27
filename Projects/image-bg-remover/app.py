"""
Python Image background remover using rembg
"""

from typing import Any

from rembg import remove
from PIL import Image

INPUT_PATH = "input-img.jpg"
OUTPUT_PATH = "output.png"

INPUT_IMAGE = Image.open(INPUT_PATH)
output: Any = remove(INPUT_IMAGE)
output.save(OUTPUT_PATH)

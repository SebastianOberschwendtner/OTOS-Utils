# OTOS - Open Tec Operating System
# Copyright (c) 2022 Sebastian Oberschwendtner, sebastian.oberschwendtner@gmail.com
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
### Details
- *File:*     FontGenerator/BitConverter.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

## Description
Converts a TTF font to a bitmap which can be used by OTOS.

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com

---

## Code
"""
# === Modules ===
from PIL import Image, ImageFont, ImageDraw

# === Functions ===

def create_canvas(height_px: int, width_px: int) -> Image:
    """Creates a canvas for the font.
    Args:
        height_px (int): 1x1 [px] The height of the canvas.
        width_px (int): 1x1 [px] The width of the canvas.
    Returns:
        PIL.Image: 1x1 [-] The canvas.


    ---
    """
    return Image.new("1", (width_px, height_px), 0)

def get_max_width(font: ImageFont.FreeTypeFont) -> int:
    """Get the maximum required width of the font in pixels.

    Args:
        font (ImageFont.FreeTypeFont): 1x1 [-] The current font type with requested font size.

    Returns:
        int: 1x1 [px] The maximum width of the font in pixels.

    ---
    """
    # Get the maximum width of the font
    max_width = 0
    for iChar in range(256):
        left, top, right, bottom = font.getbbox(chr(iChar))
        width = right - left
        if width > max_width:
            max_width = width

    return max_width

def get_max_offset(font: ImageFont.FreeTypeFont) -> int:
    """Get the maximum offset in y direction to fit all characters.

    Args:
        font (ImageFont.FreeTypeFont): 1x1 [-] The current font type with requested font size.

    Returns:
        int: 1x1 [px] The maximum Y offset of the font in pixels.

    ---
    """
    # Get the maximum width of the font
    max_offset = 0
    for iChar in range(256):
        left, top, right, bottom = font.getbbox(chr(iChar))
        if bottom > max_offset:
            max_offset = top

    return max_offset

def convert_pixel_sequence(sequence) -> int:
    """Converts a pixel sequence to a byte.

    Args:
        sequence (list): 1x8 [px] The pixel sequence.

    Returns:
        int: 1x1 [-] The converted byte.

    ---
    """
    # Convert the sequence to a byte
    byte = 0
    for i in range(8):
        byte |= sequence[i] << i

    return byte

# === Classes ===


class FontConverter:
    """Converts a TTF font to a bitmap which can be used by OTOS.

    ---
    """
    # === Properties ===
    @property
    def fontname(self) -> str:
        """Gets the name of the font.

        Returns:
            str: 1x1 [-] The name of the font.

        ---
        """
        _name = self.font.getname()[0]
        return _name.replace(" ", "")

    @property
    def height_px(self) -> int:
        return self._height_px

    @property
    def width_px(self) -> int:
        return self._width_px

    # === Constructor ===
    def __init__(self, font_path: str, font_size: int):
        """Creates a new font converter.

        Args:
            font_path (str): 1x1 [-] The path to the font file.
            font_size (int): 1x1 [px] The font size in pixels.

        ---
        """
        # Save the font path
        self.font_path = font_path
        self._height_px = font_size

        # Load the font
        try:
            self.font = ImageFont.truetype(font_path, font_size)
        except:
            raise FileNotFoundError("Font file not found.")

        # Get the maximum width of the font
        self._width_px = get_max_width(self.font)

    # === Methods ===
    def convert_character(self, character: int) -> list:
        """Converts a character to a bitmap.

        Args:
            character (int): 1x1 [-] The character to convert. 

        Returns:
            list: 1x1 [-] The bitmap.

        ---
        """
        # Create the canvas
        y_offset = get_max_offset(self.font)
        canvas = create_canvas(self.height_px, self.width_px)

        # Draw the font
        draw = ImageDraw.Draw(canvas)
        draw.text((0, -y_offset), chr(character), font=self.font, fill=1)

        # Convert the canvas to a bitmap
        bytes_y = self.height_px // 8
        bitmap = []
        for x in range(self.width_px):
            for y in range(bytes_y):
                # Get the pixel sequence
                sequence = []
                for i in range(8):
                    sequence.append(canvas.getpixel((x, (bytes_y-1-y)*8+i)))

                # Convert the sequence to a byte
                byte = convert_pixel_sequence(sequence)

                # Append the byte to the bitmap
                bitmap.append(byte)

        return bitmap

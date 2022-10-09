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
- *File:*     test_BitConverter.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com
"""
# === Modules ===
import pytest, pathlib

# === UUT ===
from utils.FontGenerator import BitConverter as UUT

# === Test list ===
# ▢ Create a canvas according to the desired font size and width
# ▢ Draw the character on the canvas
# ▢ Preview the character
# ▢ Convert the canvas to a numpy array

# === Fixtures ===
@pytest.fixture
def Path_Test_Font() -> pathlib.Path:
    yield pathlib.Path("./test/Stubs/DelugiaMonoPL.ttf")

# === Tests ===

class Test_Basic_Canvas():
    """Test group to test the basic canvas creation."""
    def test_create_canvas(self):
        """Test if a canvas can be created."""
        # Arrange
        # Act
        canvas = UUT.create_canvas(8, 8)
        # Assert
        assert canvas.size == (8, 8)
        assert canvas.mode == "1"

    def test_get_max_width(self, Path_Test_Font: pathlib.Path):
        """Test if the max width is returned correctly."""
        # Arrange
        font = UUT.ImageFont.truetype(str(Path_Test_Font), 32)
        # Act
        max_width = UUT.get_max_width(font)
        # Assert
        assert max_width == 20

    def test_get_max_offset(self, Path_Test_Font: pathlib.Path):
        """Test if the max width is returned correctly."""
        # Arrange
        font = UUT.ImageFont.truetype(str(Path_Test_Font), 32)
        # Act
        max_offset = UUT.get_max_offset(font)
        # Assert
        assert max_offset == 6

    def test_converting_pixel_sequence(self):
        """Test if the pixel sequence is converted correctly."""
        # Arrange
        pixel_sequence = [0, 0, 0, 0, 0, 0, 0, 0]
        # Act
        converted = UUT.convert_pixel_sequence(pixel_sequence)
        # Assert
        assert converted == 0

        # Arrange
        pixel_sequence = [1, 0, 0, 0, 0, 0, 0, 0]
        # Act
        converted = UUT.convert_pixel_sequence(pixel_sequence)
        # Assert
        assert converted == 1

        # Arrange
        pixel_sequence = 8*[1,]
        # Act
        converted = UUT.convert_pixel_sequence(pixel_sequence)
        # Assert
        assert converted == 255

class Test_Font_Converter():
    """Test group to test the font converter."""
    def test_convert_character_8px(self, Path_Test_Font: pathlib.Path):
        """Test if the char is converted correctly."""
        # Arrange
        Converter = UUT.FontConverter(str(Path_Test_Font), 8)

        # Act
        char = Converter.convert_character(ord("A"))

        # Assert
        assert len(char) == 5
        assert char[0] == 0b00100000
        assert char[1] == 0b00011100
        assert char[2] == 0b00010010
        assert char[3] == 0b00111100
        assert char[4] == 0b00100000

    def test_convert_character_16px(self, Path_Test_Font: pathlib.Path):
        """Test if the char is converted correctly."""
        # Arrange
        Converter = UUT.FontConverter(str(Path_Test_Font), 16)

        # Act
        char = Converter.convert_character(ord("A"))

        # Assert
        assert len(char) == 20
        assert char[0] == 0b00010000
        assert char[1] == 0b00000000
        assert char[2] == 0b00011110
        assert char[3] == 0b00000000
        assert char[4] == 0b00000111
        assert char[5] == 0b11100000
        assert char[6] == 0b00000011
        assert char[7] == 0b01111110
        assert char[8] == 0b00000011
        assert char[9] == 0b00000110

    def test_convert_character_24px(self, Path_Test_Font: pathlib.Path):
        """Test if the char is converted correctly."""
        # Arrange
        Converter = UUT.FontConverter(str(Path_Test_Font), 24)

        # Act
        char = Converter.convert_character(ord("A"))

        # Assert
        assert len(char) == 45
        assert char[0] == 0b00000000
        assert char[1] == 0b00000000
        assert char[2] == 0b00000000
        assert char[3] == 0b00000111
        assert char[4] == 0b00000000
        assert char[5] == 0b00000000
        assert char[6] == 0b00000111
        assert char[7] == 0b11110000
        assert char[8] == 0b00000000

    def test_get_fontname(self, Path_Test_Font: pathlib.Path):
        """Test if the font name is returned correctly."""
        # Arrange
        Converter = UUT.FontConverter(str(Path_Test_Font), 8)

        # Act
        fontname = Converter.fontname

        # Assert
        assert fontname == "DelugiaPLMono"

    def test_open_invalid_font(self):
        """Test correct handling of invalid font files."""
        # Arrange
        # Act
        with pytest.raises(FileNotFoundError):
            Converter = UUT.FontConverter("invalid_font.ttf", 8)
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
- *File:*     test_FontGenerator.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com
"""
# === Modules ===
import pytest, pathlib

# === UUT ===
from src import FontGenerator as UUT

# === Test list ===
# ▢ Font Data Type:
#   ▢ has name property
#   ▢ has size property
#   ▢ has width property
#   ▢ has stride property
#   ▢ has data property with 256 entries
# ▢ Font Class:
#   ▢ has a data container
#   ▢ has a converter

# === Fixtures ===
@pytest.fixture
def FontConverter_Mock(mocker):
    """Mock the FontConverter class."""
    _mock = mocker.patch.multiple(
        "src.FontGenerator.BitConverter.FontConverter",
        __init__=mocker.DEFAULT,
        convert_character=mocker.DEFAULT,
        fontname = "TestFont",
        height_px = 8,
        width_px = 5,
    )
    _mock["__init__"].return_value = None
    _mock["convert_character"].return_value = [0, 1, 2, 3, 4]
    yield _mock

# === Tests ===


class Test_Font_Data_Type():
    """Test group to test the font data type."""
    def test_has_name_property(self):
        """Test if the font data type has a name property."""
        # Arrange
        font = UUT.FontData()
        # Assert attribute
        assert hasattr(font, "name")
        # Act
        font.name = "Test"
        # Assert
        assert font.name == "Test"

    def test_has_size_property(self):
        """Test if the font data type has a size property."""
        # Arrange
        font = UUT.FontData()
        # Assert attribute
        assert hasattr(font, "size")
        # Act
        font.size = 8
        # Assert
        assert font.size == 8

    def test_has_width_property(self):
        """Test if the font data type has a width property."""
        # Arrange
        font = UUT.FontData()
        # Assert attribute
        assert hasattr(font, "width")
        # Act
        font.width = 8
        # Assert
        assert font.width == 8

    def test_has_stride_property(self):
        """Test if the font data type has a stride property."""
        # Arrange
        font = UUT.FontData()
        # Assert attribute
        assert hasattr(font, "stride")
        # Act
        font.stride = 8
        # Assert
        assert font.stride == 8

    def test_has_data_property_with_256_entries(self):
        """Test if the font data type has a data property with 256 entries."""
        # Arrange
        font = UUT.FontData()
        # Assert attribute
        assert hasattr(font, "data")
        # Assert
        assert len(font.data) == 256

class Test_Font_Class():
    """Test group to test the font class."""
    def test_init(self, FontConverter_Mock):
        """Test if the font class has a data container."""
        # Arrange
        font_source = pathlib.Path("test/test_FontGenerator/test_font.ttf")
        font = UUT.Font(font_source, 12)
        # Assert attribute
        assert hasattr(font, "data")
        assert hasattr(font, "converter")
        # Assert
        assert isinstance(font.data, UUT.FontData)
        FontConverter_Mock["__init__"].assert_called_once_with(str(font_source), 12)

    def test_convert(self, FontConverter_Mock):
        """Test the converting of a font."""
        # Arrange
        font_source = pathlib.Path("test/test_FontGenerator/test_font.ttf")
        font = UUT.Font(font_source, 12)
        # Act
        font.convert()
        # Assert
        assert font.data.name == "TestFont"
        assert font.data.size == 8 #FontConverter_Mock["height_px"]
        assert font.data.width == 5 #FontConverter_Mock["width_px"]
        assert font.data.stride == 1
        assert FontConverter_Mock["convert_character"].call_count == 256
        assert font.data.data[0] == [0,1,2,3,4]

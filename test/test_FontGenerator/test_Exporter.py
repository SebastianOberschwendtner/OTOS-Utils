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
- *File:*     test_Exporter.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com
"""
# === Modules ===
import pytest, pathlib

# === UUT ===
from utils.FontGenerator import Exporter as UUT

# === Test list ===
# ▢ File formatting:
#   ▢ Size in pixels sets the namespace correctly
# ▢ File export:
#   ▢ Copyright header is written correctly
#   ▢ Array line is written correctly
#   ▢ lookup table is written correctly
#   ▢ Font name is written correctly
#   ▢ Font data struct is written correctly


# === Fixtures ===

# === Tests ===

class Test_File_Formatting():
    """Test group to test file formatting."""
    def test_size_in_pixels_sets_namespace_correctly(self):
        """Test if the size in pixels sets the namespace correctly."""
        # Act
        name = UUT.get_namespace_for_size(8)
        # Assert
        assert len(name) == 4
        assert name == "_8px"


class Test_File_Export():
    """Test group to test file export."""
    def test_copyright_header_is_written_correctly(self, tmp_path: pathlib.Path):
        """Test if the copyright header is written correctly."""
        # Arrange
        expected = UUT._OTOS_Copyright
        file = tmp_path / "test.txt"

        # Act
        UUT.write_copyright_header(file)

        # Assert
        assert file.read_text().startswith(expected)

    def test_array_line_is_written_correctly(self, tmp_path: pathlib.Path):
        """Test if the lookup table is written correctly."""
        # Arrange
        expected = "0x00, 0x01, 0x02, 0x03, // 0x00\n"
        file = tmp_path / "test.txt"

        # Act
        UUT.write_array_line(file, 0, [0,1,2,3])

        # Assert
        assert file.read_text().startswith(expected)
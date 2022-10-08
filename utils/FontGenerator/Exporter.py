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
- *File:*     FontGenerator/Exporter.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

## Description
Exporter for the font generator.

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com
"""
# === Modules ===
import pathlib

# === Functions ===

def get_namespace_for_size(size: int) -> str:
    """Converts the font size to a namespace.

    Args:
        size (int): 1x1 [px] The font size in pixels.

    Returns:
        str: 1xn [str] The namespace for the font size.
    
    ---
    """
    return f"_{size}px"

def write_copyright_header(file: pathlib.Path):
    """Writes the copyright header to the file.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.

    ---
    """
    # Write the header
    file.write_text(_OTOS_Copyright)

def write_array_line(file: pathlib.Path, line_number: int, array: list):
    """Writes a line of an array to the file.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.
        line_number (int): 1x1 [-] The line number of the array in the file.
        array (list): 1xn [-] The array to write.

    ---
    """
    # Convert every element in the array to a hex string
    line_string = ""
    for Item in array:
        line_string += f"{Item:#04x}, "

    # End the line with the line number as comment
    line_string += f"// {line_number:#04x}"
    
    # Write the line
    with  open (file, 'a') as f:
        f.write(line_string + "\n")


# === Constants ===
_OTOS_Copyright: str = """/**
 * OTOS - Open Tec Operating System
 * Copyright (c) 2022 Sebastian Oberschwendtner, sebastian.oberschwendtner@gmail.com
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */
 """
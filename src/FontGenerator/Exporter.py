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
- *File:*     `FontGenerator/Exporter.py`
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

## Description
Exporter for the font generator.

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com

---
## Code

---
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


def get_array_line(line_number: int, array: list) -> str:
    """Get the line of an array as a string.

    Args:
        line_number (int): 1x1 [-] The line number of the array in the file.
        array (list): 1xn [-] The array to write.

    Returns:
        str: 1x1 [-] The line of the array.

    ---
    """
    # Convert every element in the array to a hex string
    line_string = ""
    for Item in array:
        line_string += f"{Item:#04x}, "  # pylint: disable=consider-using-join

    # End the line with the line number as comment
    if chr(line_number).isprintable() and line_number != 0x5C:
        line_string += f"// {line_number:#04x}: {chr(line_number)}" + "\n"
    else:
        line_string += f"// {line_number:#04x}" + "\n"

    # Return the line
    return line_string


def write_lookup_table_preamble(file: pathlib.Path, font_name: str):
    """Write the preamble of the lookup table.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.
        font_name (str): 1x1 [-] The name of the font.

    ---
    """
    # Write the beginning of the lookup table
    with open(file, "a", encoding="utf-8") as File:
        File.write(_OTOS_LookUp_Preamble.format(Name_Upper=font_name.upper()))
        File.write(r"{" + "\n")


def write_lookup_table_begin(file: pathlib.Path, font_name: str, size: tuple):
    """Write the beginning of the lookup table.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.
        font_name (str): 1x1 [-] The name of the font.
        size (tuple): 1x2 [px] The (width, height) of the font.

    ---
    """
    # Write the beginning of the lookup table
    with open(file, "a", encoding="utf-8") as File:
        File.write(
            _OTOS_LookUp_Begin.format(Name=font_name, Width=size[0], Height=size[1])
        )
        File.write(r"{" + "\n")


def write_lookup_table_end(
    file: pathlib.Path, font_name: str, size: tuple, stride: int
):
    """Write the end of the lookup table.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.
        font_name (str): 1x1 [-] The name of the font.
        size (tuple): 1x2 [px] The (width, height) of the font.
        stride (int): 1x1 [-] The stride of the font.

    ---
    """
    # Write the end of the lookup table
    with open(file, "a", encoding="utf-8") as File:
        File.write(
            _OTOS_LookUp_End.format(
                Namespace=get_namespace_for_size(size[1]),
                Name=font_name,
                Width=size[0],
                Height=size[1],
                Stride=stride,
            )
        )


def finalize_file(file: pathlib.Path, font_name: str):
    """Finalize the file.

    Args:
        file (pathlib.Path): 1x1 [-] The file to write to.
        font_name (str): 1x1 [-] The name of the font.

    ---
    """
    # Write the end of the file
    with open(file, "a", encoding="utf-8") as File:
        File.write(f"}};\n#endif /* {font_name.upper()}_H_ */")


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

_OTOS_LookUp_Preamble: str = """
#ifndef {Name_Upper}_H_
#define {Name_Upper}_H_

// === Includes ===
#include "font_base.h"

namespace Font
"""

_OTOS_LookUp_Begin: str = """    /**
     * @brief Ascii font lookup table
     * @details width: {Width:d} px, height: {Height:d} px
     */
    constexpr unsigned char Lookup_{Name}_{Height:d}px[] = """

_OTOS_LookUp_End: str = """    }};

    // === Font Information ===
    // {Name}: {Height:d}px
    namespace {Namespace}
    {{
        constexpr Font::Base_t {Name} = {{
            .data = Lookup_{Name}_{Height:d}px,
            .width_px = {Width:d},
            .height_px = {Height:d},
            .stride = {Stride:d}}};
    }};
"""

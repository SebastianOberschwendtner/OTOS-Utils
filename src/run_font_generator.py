#!python
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
- *File:*     run_font_generator.py
- *Details:*  Python 3.9
- *Date:*     2022-10-08
- *Version:*  v1.0.0

## Description
CLI interface for the font generator.

### Author
Sebastian Oberschwendtner, :email: sebastian.oberschwendtner@gmail.com

---
## Code

---
"""
# === Modules ===
import pathlib
import argparse
import FontGenerator as FG


# === Functions ===
def main(font_file: pathlib.Path, sizes: list, outdir: pathlib.Path):
    """Runs the font generator.

    Args:
        font (pathlib.Path): 1x1 [-] The font file to use.
        size (int): 1x1 [px] The font size in pixels.
        outdir (pathlib.Path): 1x1 [-] The output directory.

    Raises:
        FileNotFoundError: The font file is not available on the system.

    ---
    """
    # Inform the user
    print(f"Generating font file for {font_file} with {sizes} px.")
    print(f"Output directory: {outdir}")

    # Create font and check whether the font is valid
    try:
        fonts = FG.Fonts(font_file, sizes)
    except FileNotFoundError:
        print("The font is not available on your system. :|")

    # Convert the font
    print("Converting the font...")
    fonts.convert()

    # Export the font
    print("Exporting the font...")
    fonts.export(outdir)
    print("Done. :D")


# === Main ===
if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Generate font files for the OTOS Graphics library."
    )

    # Add arguments
    # - Font file
    parser.add_argument(
        "--font",
        "-f",
        type=pathlib.Path,
        help="Path or Name of the font file.",
        required=True,
    )
    # - Font size
    parser.add_argument(
        "--size",
        "-s",
        type=int,
        nargs="+",
        help="Size(s) of the font in pixels.",
        required=True,
    )
    # - Output file
    parser.add_argument(
        "--output",
        "-o",
        type=pathlib.Path,
        help="Path to the output file.",
        required=True,
    )
    # - Version
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s: {FG.__name__}, Version: {FG.__version__}",
    )

    # Parse arguments
    args = parser.parse_args()

    # Call main function
    main(args.font, args.size, args.output)

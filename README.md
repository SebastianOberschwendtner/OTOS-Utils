# :wrench: OTOS Utils 
![tag](https://img.shields.io/github/v/tag/SebastianOberschwendtner/otos-utils?color=green)
![release](https://img.shields.io/github/v/release/SebastianOberschwendtner/otos-utils?color=green)
![issues](https://img.shields.io/github/issues-raw/SebastianOberschwendtner/otos-utils)
![bugs](https://img.shields.io/github/issues/SebastianOberschwendtner/otos-utils/bug?color=red)

Utility functions for developing with the OTOS operating system.


## Software Framework
![GitHub Test Status](https://img.shields.io/github/workflow/status/SebastianOberschwendtner/otos-utils/Unit%20Test?label=test)
![GitHub top language](https://img.shields.io/github/languages/top/SebastianOberschwendtner/otos-utils?color=brightgreen)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/SebastianOberschwendtner/otos-utils)
![GitHub](https://img.shields.io/github/license/SebastianOberschwendtner/otos-utils)

Available Packages:
- [Font Generator](#font-generator)

The packages are briefly described in the following:

### Font Generator
The font generator tool can be used to convert *TrueType* fonts to bitmaps which can be used by the Graphics Library of *OTOS*.
Here is the the output of `run_font_converter.py -h`:
```bash
usage: run_font_generator.py [-h] --font FONT --size SIZE [SIZE ...] --output
                             OUTPUT [--version]

Generate font files for the OTOS Graphics library.

optional arguments:
  -h, --help            show this help message and exit
  --font FONT, -f FONT  Path or Name of the font file.
  --size SIZE [SIZE ...], -s SIZE [SIZE ...]
                        Size(s) of the font in pixels.
  --output OUTPUT, -o OUTPUT
                        Path to the output file.
  --version, -v         show program's version number and exit
```
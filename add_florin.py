import fontforge
import psMat
import sys
import os

# Paths to input and output fonts
font_A_path = sys.argv[1]
font_B_path = sys.argv[2]
new_font_dir = "output/"

# Load fonts A and B
font_A = fontforge.open(font_A_path)
font_B = fontforge.open(font_B_path)

# characters need to copy
CHARS = ["ƒ"]


def copy_char(s: str) -> None:
    # Find the "ƒ" character in font A
    unicode_f = ord(s)
    char_f_A = font_A[unicode_f]

    # Scale the "ƒ" character from font A to match the em size of font B
    scaling_factor = font_B.em / font_A.em
    char_f_A.transform(psMat.scale(scaling_factor))

    # Paste the copied "ƒ" character into font C
    font_A.selection.select(unicode_f)
    font_A.copy()
    font_B.selection.select(unicode_f)
    font_B.paste()


for c in CHARS:
    copy_char(c)


# Save font C
font_B.generate(new_font_dir + os.path.basename(font_B_path))

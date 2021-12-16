"""
Pdf file to Word document converter
"""

from pathlib import Path

import pdftotext


def to_txt(in_file: str, out_file: str) -> None:
    with open(in_file, "rb") as f_in:
        pdf = pdftotext.PDF(f_in)

    with open(out_file, "w") as f_out:
        f_out.write("\n\n".join(pdf))

# The Kutip Converter
# by Samuel Sandi

import pyperclip

namaFile = input("Masukkan nama file:")
f = open(namaFile, "r",encoding="utf8")
clipBoard = ""
buka = True

for line in f:
    buka = True
    for char in line:
        if char == "\"":
            if buka:
                clipBoard = clipBoard + "“"
                buka = False
            else:
                clipBoard = clipBoard + "”"
        else:
            clipBoard = clipBoard + char

f.close()

pyperclip.copy(clipBoard)
import os
from PIL import Image
from PyPDF2 import PdfMerger

path = "F:/New folder (2)/"
i = 1

# for files in os.listdir(path):
#     img = Image.open(path + files)
#     img.convert("RGB")
#     img.save(path + "files-" + str(i) + ".pdf", "PDF")
#     i += 1
for files in os.listdir(path):
    if files.endswith(".pdf"):
        PdfMerger().append(path + files)
PdfMerger().write(path + "Files.pdf")

from PIL import Image
from pypdf import PdfWriter
from os import listdir

path = "F:/New folder (2)/"
merger = PdfWriter()
i = 1
for files in listdir(path):
    if files.endswith(".png"):
        pics = Image.open(path + files)
        pics.convert("RGB")
        pics.save(path + "pics" + str(i) + ".pdf", "PDF")
        i += 1

    pics.close()
    if files.endswith(".pdf"):
        merger.append(path + files)
merger.write('E:/Cartoon/Alcatraz/' + "Merged.pdf")
merger.close()

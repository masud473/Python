import os

i = 1
for files in os.listdir("E:/Cartoon/Alcatraz - Copy (2)/"):
    if files.endswith(".png"):
        os.rename(
            "E:/Cartoon/Alcatraz - Copy (2)/" + files,
            "E:/Cartoon/Alcatraz - Copy (2)/" + "photo-" + str(i) + ".png",
        )
        i += 1
        
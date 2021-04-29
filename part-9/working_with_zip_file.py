from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")  # current folder ei files.zip namer ekta zip file toiri hobe, r second argument hisebe "w"
                           # dewa hoiche, karon amra ei zip file a write korbo tai.

# Path("..//part-9")  # ekhon ei part-9 folder/directori er sob file ke zip korbo ba zip file a write korbo. ei jonno
                    #  part-9 file er path object toiri kore nilam. ekhon ei folder/directori er upore iterate kore
                    # er file guloke zip file a write korte hobe.

with ZipFile("files.zip", "w") as zip:
    for path in Path("..//part-9").rglob("*.*"):
        zip.write(path)

# with ZipFile("files.zip") as zip:
print(zip.namelist())               # zip file er vetorer file gulor list pawa jabe.
info = zip.getinfo("../part-9/files.zip")  # list er jekono ekta path output theke eikhane dewa hoiche, info dekhar jonno
print(info.file_size)
print(info.compress_size)

zip.extractall("extract") # zip file ta extract kora hoilo. eikhane  .extractall() method er moddhe jei file a extract
                         # kora hobe, tar name define kora holo. oi namer folder toiri kore tar moddhe extract korbe
                         #


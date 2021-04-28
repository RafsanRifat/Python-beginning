from pathlib import Path
from time import ctime          # human read able time er jonno.
import shutil



path = Path("practice.py")
print(path.exists())

print(path.stat())    # it returnes information about the file. it will return  a stat result ibject.

print(ctime(path.stat().st_ctime))    # It will print the creation time of this file


# some methods for reading data from a file --->>>

path.read_bytes()           # it return the content of the file as byte code
path.read_text()            # it returnes the content of the file as string
path.write_text()           # file a kichu add korar jonno.
path.write_bytes()          # same
# uporer method gulor khetre file open r close er kono jhamela thakena.

with open("practice.py", "r") as file:  # eivabeo file open kore read kora jay. er chaite filename.read_text() use kora
                                        # better... ... ...
    print(file)


# kono file ke onno location  a copy korar jonno --->>

source = Path("ecommerce/init.py")
target = Path() / "__init__.py"   # present path close kore target hisebe ei file select kora holo.
target.write_text(source.read_text())  # prothome source code read kore target a write kora holo.

# uporer ei upai ta kothin r jhamelar.  shutil namer ekta Module, jeita import korle file copy r move related kaj gulo
# onek easily kora jay.
shutil.copy(source, target)
from pathlib import Path

Path("C:\\rafsan\\practice\\python-4785225_960_720.jpg")   # eivabe windows operating system a path object toiri kora
                                                           # jay.
Path(r"C:\rafsan\practice\python-4785225_960_720.jpg")     # boro path er khetre Raw string use koa hoy. tokhon single
                                                           # slash use kora jay, r single slash tokhon r escape hisebe
                                                           # kaj na kore double slash er motoi kaj kore.

Path() / Path("ecommerce")              # here we combined 2 path object.
Path() / "ecommerceee"                  # here we combined a string with path object.

path = Path("ecommerce/__init__.py")
path.exists()                       # to check, the directory exist or not
path.is_file()                      # path kono file represent kore kina
path.is_dir()
print(path.name)                    # this will return only the file name in this path
print(path.stem)                    # this will return only the file name without the extension
print(path.suffix)                    # this will return only the file  the extension
print(path.parent)                    # this will return the parent
path = path.with_name("file.txt")
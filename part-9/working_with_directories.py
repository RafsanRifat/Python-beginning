from pathlib import Path
path = Path("C:\\rafsan\\practice\\python\\Mosh-paid-course\\part-9")
# print(path.exists())     ---> the path exist or not
# path.mkdir()          ---> to creat directories
# path.rmdir()            --->  to remove directories
# path.rename()           ---> to rename a directories


print(path.iterdir())          # with this method, we can get the files and directories in this path.  eita amaderke
                               # ekta generator object return korbe.

for p in path.iterdir():        # if we loop over it, it will return all the files and directories in this path.
                                # ei kaj tai amra list comprehension use kore korte pari.
    print(p)


paths = [p for p in path.iterdir()]
print(paths)                            # eikhane amra list akare kichu WindowsPath object pabo. pathlib module er Path
                                        # class er 2ta base class holo ---> WindowsPath r PosixPath,   PosixPath holo
                                        # unix,linux,mac er jonno. r WindowsPath holo windows er jonne... ... ...

paths = [p for p in path.iterdir() if p.is_file()]   # eikhane extra ekta condition use kora holo---> j sudhu file gulo,
                                                     # bamer p te return korbe
print(paths)

# path.iterdir()  function ta useful, kintu eitar limitation ache. eita, recursively search and pattern search korte parena.
# eikharone amader glob() method use korte hoy.

glob_all_file_search = [p for p in path.glob("*.*")]        # "*.*" eita dara all file bujhay
print(glob_all_file_search)
glob_py_file_search = [p for p in path.glob("*.py")]        # "*.py" eita dara joto .py file ache segulo ke bujhacche
print(glob_py_file_search)

rglob_py_file_search = [p for p in path.rglob("*.py")]        # rglob() use kora hoy recursively search korar jonno.
print(rglob_py_file_search)

# JSON = javaScript Object Notation
# JSON is the format, using that we can send data from server to client site and ckient side to server side.

import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)  #  To get a string that includes our movies data formated as string. json.dump() json format
                          # a convert er kaje use kora hoy.

print(data)
Path("movies.json").write_text(data)  # current directory te movies.json namer ekta file toiri korlam, r seita te
                                      # data variable er data gulo write korlam.

# kono json file read korar jonno =================================== --->>>
read_data = Path("movies.json").read_text() # eikhane json format er data gulo string akare read_data variable a store holo.
read_movies = json.loads(read_data)  # this will return an array of dictionaries. string type json ke array kora hocche

print(read_movies)
print(read_movies[0])
print(read_movies[0] ["title"])


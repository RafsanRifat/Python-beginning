import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())   # movies.json file k sudhu read kore movie te store korle eita
                                                      # ekta string return kore. jar karone eitake json.loads() er vetore
                                                      # diyea pass kora hoyeache, jate array return kore.

# conneciton = sqlite3.connect("db.sqlite3")  # sqlite3 object er ekta connect method ache. ei connect method er moddho diyea database er name pass
                   # korte hoy. jodi oi namer database, thake taile connect hobe, r na thakle oi namer database create
                   # korbe.  eita ekta connection object return korbe. r eita oi type er object, jeitar kaj howar pore
                   # close korte hoy.   so, eikaj with diyea korai valo.

with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT OR IGNORE INTO Movies VALUES(?, ?, ?)"      # our movie table will have 3 columns
    for movie in movies:
        connection.execute(command, tuple(movie.values()))
    connection.commit()             # All those changes will be returned to the database with this


# how to read data from our existing database ========>>>>>>

with sqlite3.connect("db.sqlite3") as connection:  # to read the data from the database, we need to connect to the databse.
    command_to_read_data = "SELECT * FROM Movies"  # Here we have selected all the data of the table-->"Movies"
    cursor = connection.execute(command_to_read_data)  # this will return us a cursor type object. that is Iterable.
    # for single_data in cursor:   # eita active rakhle nicher way ta kaj korbena. coz, after we iterate of the cursor,
                                   # we will get to the end of the cursor
    #     print(single_data)
    table_data_list = cursor.fetchall()  # we will get all the movie list of the table from this way as an/a array/list
    print(table_data_list)

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
    

con = sqlite3.connect('cinemasKaro.db')
cur = con.cursor()
print(theatresDicti)
cur.execute("""CREATE TABLE IF NOT EXISTS cinemas_karo( 
                     cinema_id INTEGER,
                     cinema_name TEXT,
                     cinema_address TEXT,
                     cinema_metro TEXT, 
                     cinema_phone TEXT)""")
con.commit()
theatresFordb = [theatresDicti.["data-id"].values(), theatresDicti.keys(), theatresDicti["address"].values(), theatresDicti["metro"].values(), theatresDicti["phone"].values()]
cur.executemany(f"insert or replace into cinemas_karo values(?,?,?,?,?)", theatresFordb)
con.commit()
cur.execute("""CREATE TABLE films_karo(
                    cinema_id INTEGER,  
                    film TEXT,
                    format TEXT,
                    times TEXT)

""")
con.commit()
id = None
film = None
format = None
for id, film in filmsByIds.items():
    print(id, film)
    cur.execute(f'insert or replace into films_karo(cinema_id) values ("{id}")')
    cur.execute(f'insert or replace into films_karo(film) values ("{film}")')
    for format, times in film:
        print(format, times)
        cur.execute(f'insert or replace into films_karo(format, times) values ("{format}", "{times}")')
con.commit()
cur.close()
con.close()
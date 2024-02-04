import sqlite3

conn = sqlite3.connect("music.db")
c = conn.cursor()

c.execute("CREATE TABLE song(idSong INTEGER PRIMARY KEY AUTOINCREMENT, interpret text, name text, datet date, fkSt int, FOREIGN KEY(fkSt) REFERENCES songType(idSt))")
c.execute("CREATE TABLE songType(idSt INTEGER PRIMARY KEY AUTOINCREMENT, label text)")
c.execute("CREATE TABLE user(idUser INTEGER PRIMARY KEY AUTOINCREMENT, pseudo text)")
c.execute("CREATE TABLE score(idScore INTEGER PRIMARY KEY AUTOINCREMENT, valeur int, serie int, fkUser, FOREIGN KEY(fkUser) REFERENCES user(idUser))")

c.execute("INSERT INTO songType(label) VALUES('variete')")
c.execute("INSERT INTO songType(label) VALUES('rap')")
c.execute("INSERT INTO songType(label) VALUES('jazz')")
c.execute("INSERT INTO songType(label) VALUES('rock')")
c.execute("INSERT INTO songType(label) VALUES('classique')")
c.execute("INSERT INTO songType(label) VALUES('pop')")

c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Vengaboys', 'Boom Boom Boom Boom', '1998-10-01', 6)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Tatu', 'All The Things She Said', '2002-08-19', 4)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Maitre Gims', 'J me tire', '2013-03-15', 2)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Vianney', 'Je m en vais', '2016-10-17', 1)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Boulevard des airs', 'Bruxelles', '2015-06-01', 1)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Psy 4 de la rime', 'Inaya', '2008-05-26', 2)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Soprano', 'Roule', '2016-10-14', 2)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('M Pokora', 'Si on disait', '2020-12-04', 1)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Ray Charles', 'Hit the road Jack', '1961-10-09', 3)")
c.execute("INSERT INTO song(interpret, name, datet, fkSt) VALUES('Beethoven', 'Ode a la joie', '1824-05-07', 5)")


conn.commit()
conn.close()
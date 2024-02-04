import sqlite3

def getAll():
    '''
    Input : None
    Output : res : list of k-tuple
    Return all songs and their informations from DB
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()
    res = []
    for i in c.execute('SELECT * FROM song'):
        res.append(i)
    conn.close()
    return res

def getDateOverd(d):
    '''
    Input : d : string (date)
    MUST BE FORMATED : 'yyyy-mm-dd'
    Output : res : list of k-tuple
    Return all songs and their informations with 'datet > d' from DB
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()
    res = []
    for i in c.execute('SELECT * FROM song WHERE datet > ?', (d,)):
        res.append(i)
    conn.close()
    return res

def getType(t):
    '''
    Input : t : string (song type)
    Output : res : list of k-tuple
    Return all songs and their informations with 'songType.label = t' from DB
    Return None if t doesn't exist in DB 
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()
    res = []
    for i in c.execute('SELECT * FROM song JOIN songType ON songType.idSt = song.fkSt WHERE songType.label = ?', (t,)):
        res.append(i)
    conn.close()
    return res

def create_score(s, u=None):
    '''
    Input : 
        s : int (score)
        u : int (user id)

    Output : res : idScore 

    Create score for current game and return id of the row
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()
    if u == None:
        c.execute('INSERT INTO score(valeur, serie) VALUES (?, 0)', (s,))
        res = c.execute('SELECT max(idScore) from score')
        print(res.fetchall())
    else:
        c.execute('UPDATE score SET valeur = ? WHERE idScore = ?', (s, u))
        res = c.execute('SELECT idScore from score WHERE idScore = ?', (u,))
        print(res.fetchall())
    conn.close()
    return res

def update_score(s, u=None):
    '''
    Input : 
        s : (int int) tuple (idScore, value)
        u : int (user id)

    Output : None
    
    Update current score of user
    '''
    conn = sqlite3.connect("music.db")
    c = conn.cursor()

    # TODO : Mettre à jour le score dans la base en fonction d'un identifiant donné.
    # ...
    conn.close()

create_score(5, "toto")
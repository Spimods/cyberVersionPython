import mysql.connector
from datetime import datetime

def etape1start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key1` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime2'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time1 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape1'
    else:
        connexion.close()
        return "Cookie non défini dans la session"
    
def etape2start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key2` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime3'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time2 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape2'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape3start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key3` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time3 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape3'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape4start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key4` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime5'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time4 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape4'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape5start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key5` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime6'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time5 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape5'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape6start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key6` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time6 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape6'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape7start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key7` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime8'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time7 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape7'
    else:
        connexion.close()
        return "Cookie non défini dans la session"


def etape8start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key8` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'starttime9'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time8 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape8'
    else:
        connexion.close()
        return "Cookie non défini dans la session"

def etape9start(cookie):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor(buffered=True)
        requete.execute("SELECT `key9` FROM `timepython` WHERE `cookie`= %s", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            connexion.close()
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor(buffered=True)
            requeteUpdate.execute("UPDATE timepython SET time9 = %s WHERE cookie = %s", (temps_debut, valeur_cookie))
            connexion.commit()
            connexion.close()
            return 'etape9'
    else:
        connexion.close()
        return "Cookie non défini dans la session"



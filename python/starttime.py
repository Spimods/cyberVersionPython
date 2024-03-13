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

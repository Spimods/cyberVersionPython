from datetime import datetime

def etape1start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key1` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime2'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time1 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape1'
    else:
        return "Cookie non défini dans la session"
    
def etape2start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key2` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime3'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time2 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape2'
    else:
        return "Cookie non défini dans la session"

def etape3start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key3` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time3 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape3'
    else:
        return "Cookie non défini dans la session"

def etape4start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key4` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime5'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time4 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape4'
    else:
        return "Cookie non défini dans la session"

def etape5start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key5` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime6'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time5 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape5'
    else:
        return "Cookie non défini dans la session"

def etape6start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key6` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time6 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape6'
    else:
        return "Cookie non défini dans la session"

def etape7start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key7` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime8'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time7 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape7'
    else:
        return "Cookie non défini dans la session"


def etape8start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key8` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'starttime9'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time8 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape8'
    else:
        return "Cookie non défini dans la session"

def etape9start(cookie , connexion):

    import pytz
    tz = pytz.timezone('Europe/Paris')
    datetime.now(tz)
    if 'ctfId' in cookie:
        valeur_cookie = cookie['ctfId']
        requete = connexion.cursor()
        requete.execute("SELECT `key9` FROM `timepython` WHERE `cookie`= ?", (valeur_cookie,))
        resultat = requete.fetchone()
        print(resultat)
        if resultat != (None,):
            return 'python'
        else:
            temps_debut = datetime.now().strftime("%d %H %M %S")
            requeteUpdate = connexion.cursor()
            requeteUpdate.execute("UPDATE timepython SET time9 = ? WHERE cookie = ?", (temps_debut, valeur_cookie))
            connexion.commit()
            return 'etape9'
    else:
        return "Cookie non défini dans la session"



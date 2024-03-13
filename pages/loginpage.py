import mysql.connector
import os
import uuid
import socket


def verification(adresseIP,query_params ):
    serveur = "localhost"
    utilisateur = "root"
    motDePasse = ""
    baseDeDonnees = "ctf"
    connexion = mysql.connector.connect(host=serveur,
                                        user=utilisateur,
                                        password=motDePasse,
                                        database=baseDeDonnees)

    session = {}
    cursor = connexion.cursor(dictionary=True)

    serveur = "localhost"
    utilisateur = "root"
    motDePasse = ""
    baseDeDonnees = "ctf"

    try:
        proxy_headers = [
            'HTTP_VIA',
            'HTTP_X_FORWARDED_FOR',
            'HTTP_FORWARDED_FOR',
            'HTTP_X_FORWARDED',
            'HTTP_FORWARDED',
            'HTTP_CLIENT_IP',
            'HTTP_FORWARDED_FOR_IP',
            'VIA',
            'X_FORWARDED_FOR',
            'FORWARDED_FOR',
            'X_FORWARDED',
            'FORWARDED',
            'CLIENT_IP',
            'FORWARDED_FOR_IP',
            'HTTP_PROXY_CONNECTION'
        ]
        for header in proxy_headers:
            if header in os.environ:
                print("Vous êtes derrière un proxy!")
        nom = query_params.get('nom', [None])[0]

        if 'ctfcookies' in session and 'ctfId' in session:
            valeurCookie = session['ctfcookies']
            valeurCookieID = session['ctfId']
            sql = "SELECT cookie, n_modele, ip, nom FROM ctfuser WHERE id = %s"
            cursor.execute(sql, (valeurCookieID,))
            result = cursor.fetchone()
            if result:
                if valeurCookie == result['cookie']:
                    if adresseIP == result['ip']:
                        print("La valeur du cookie correspond à celle de la base de données.")
                        cursor.execute("UPDATE ctfuser SET n_connect = n_connect + 1 WHERE id = %s", (valeurCookieID,))
                        connexion.commit()
                        url = 'home.php?nom=' + result['nom']
                        return url
                    else:
                        print("<br>Merci de ne pas déconnecter votre PC")
                else:
                    session.clear()
                    print("refresh: 0")
                    exit()
        else:
            sql = "SELECT * FROM ctfuser WHERE ip = %s"
            cursor.execute(sql, (adresseIP,))
            result = cursor.fetchone()
            if result:
                if result['ip'] == adresseIP:
                    if result['nom'] is not None:
                        session['ctfId'] = result['id']
                        session['ctfcookies'] = result['cookie']
                        session['ctfNOM'] = result['nom']
                        url = 'home.php?nom=' + result['nom']
                        return url
                else:
                    print("Adresse IP non conforme.")
            else:
                print("La valeur de 'nom' est None. Veuillez vérifier la base de données.")
                codeAleatoire = str(uuid.uuid4())
                session['ctfcookies'] = codeAleatoire
                sql = "INSERT INTO ctfuser (cookie, n_modele, ip, nom) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (codeAleatoire, "user_agent_string", adresseIP, nom))
                connexion.commit()
                idAutoIncrement = cursor.lastrowid
                sql = "INSERT INTO prog (nom, cookie) VALUES (%s, %s)"
                cursor.execute(sql, (nom, codeAleatoire))
                connexion.commit()
                idprog = cursor.lastrowid
                sql = "INSERT INTO python (nom, cookie) VALUES (%s, %s)"
                cursor.execute(sql, (nom, codeAleatoire))
                connexion.commit()
                idpython = cursor.lastrowid
                session['ctfId'] = idAutoIncrement
                session['ctfIdprog'] = idprog
                session['ctfIdpython'] = idpython
                session['ctfNOM'] = nom
                url = 'home.php?nom=' + result['nom']
                return url
    finally:
        connexion.close()


if __name__ == "__main__":
    pass

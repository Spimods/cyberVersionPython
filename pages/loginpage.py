import sqlite3
import uuid
import requests

def verification(adresseIP, query_params, cookie, connexion):
    cursor = connexion.cursor()
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

    nom = query_params.get('nom')[0]
    print(nom)

    if 'ctfId' in cookie:
        cursor.execute("SELECT * FROM ctfuser WHERE ip = ?", (adresseIP,))
        result = cursor.fetchone()
        print(result)
        if result:
            print(result[6])
            if result[6] == adresseIP:
                url = 'homepage?nom=' + result[1]
                return url
    else:
        print(f"nouvelle utilisateur nommé {nom}")
        codeAleatoire = str(uuid.uuid4())
        print('7', (str(codeAleatoire), str(adresseIP), str(nom)))
        sql = "INSERT INTO ctfuser (cookie, ip, nom) VALUES (?, ?, ?)"
        cursor.execute(sql, (codeAleatoire, adresseIP, nom))
        connexion.commit()
        idAutoIncrement = cursor.lastrowid
        sql = "INSERT INTO timepython (nom, cookie) VALUES (?, ?)"
        cursor.execute(sql, (str(nom), codeAleatoire))
        connexion.commit()
        idprog = cursor.lastrowid
        sql = "INSERT INTO python (nom, cookie) VALUES (?, ?)"
        cursor.execute(sql, (str(nom), codeAleatoire))
        connexion.commit()
        idpython = cursor.lastrowid
        cookies_list = [
            ('ctfId', str(codeAleatoire)),
            ('ctfIdprog', str(idprog)),
            ('ctfIdpython', str(idpython)),
            ('ctfNOM', nom)
        ]
        url = 'homepage?nom=' + nom
        return url, cookies_list

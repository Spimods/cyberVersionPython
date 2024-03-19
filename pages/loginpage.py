import mysql.connector
import os
import uuid
import socket
import http.cookies
import requests
from flask import request, make_response, Flask

from werkzeug.wrappers import Request

def verification(adresseIP, query_params, cookie):
    serveur = "localhost"
    utilisateur = "root"
    motDePasse = ""
    baseDeDonnees = "ctf"
    connexion = mysql.connector.connect(host=serveur,
                                        user=utilisateur,
                                        password=motDePasse,
                                        database=baseDeDonnees)

    cursor = connexion.cursor(dictionary=True)

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

        nom = query_params.get('nom')[0]
        print(nom)

        if 'ctfId' in cookie:
            cursor.execute("SELECT * FROM ctfuser WHERE ip = %s", (adresseIP,))
            result = cursor.fetchone()
            if result:
                if result['ip'] == adresseIP:
                        url = 'homepage?nom=' + result['nom']
                        return url
        else:
            print(f"nouvelle utilisateur nommé {nom}")
            codeAleatoire = str(uuid.uuid4())
            print('7', (str(codeAleatoire), str(adresseIP), str(nom)))
            sql = "INSERT INTO ctfuser (cookie, ip, nom) VALUES (%s, %s, %s)"
            cursor.execute(sql, (codeAleatoire, adresseIP, nom))
            connexion.commit()
            idAutoIncrement = cursor.lastrowid
            sql = "INSERT INTO timepython (nom, cookie) VALUES (%s, %s)"
            cursor.execute(sql, (str(nom), codeAleatoire))
            connexion.commit()
            idprog = cursor.lastrowid
            sql = "INSERT INTO python (nom, cookie) VALUES (%s, %s)"
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

    finally:
        connexion.close()

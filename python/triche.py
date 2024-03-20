import mysql.connector
from mysql.connector import Error
from datetime import datetime
import requests

def triche(query_params ,cookie):
    etape = query_params.get('etape', [''])[0]
    try:
        connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        liste = {
                "etape1": "key1",
                "etape2": "key2",
                "etape3": "key3",
                "etape4": "key4",
                "etape5": "key5",
                "etape6": "key6",
                "etape7": "key7",
                "etape8": "key8",
                "etape9": "key9"
            }
        cursor = connexion.cursor()

        if 'ctfId' in cookie:
            idcookie = cookie['ctfId']
            nom = cookie['ctfNOM']
            cursor.execute("INSERT INTO triche (nom, etape, cookie) VALUES (%s, %s, %s)", (nom, etape, idcookie))
            connexion.commit()
            cle = liste.get(etape)
            cursor.execute(f"UPDATE timepython SET {cle} = 1 WHERE cookie = %s", (idcookie,))
            connexion.commit()
            if etape in ["etape1", "etape2", "etape3"]:
                cursor.execute("UPDATE python SET flag1 = 'triche' WHERE cookie = %s", (idcookie,))
            elif etape in ["etape4", "etape5", "etape6"]:
                cursor.execute("UPDATE python SET flag2 = 'triche' WHERE cookie = %s", (idcookie,))
            elif etape in ["etape7", "etape8", "etape9"]:
                cursor.execute("UPDATE python SET flag3 = 'triche' WHERE cookie = %s", (idcookie,))
            connexion.commit()
            print("Données insérées avec succès.")
            html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suspicion de triche</title>
    <link rel="stylesheet" href="main.css">

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif !important;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #d9534f;
            font-family: Arial, sans-serif !important;
            font-size: 24px !important;
        }
        p {
            color: #333;
            font-family: Arial, sans-serif !important;
            font-size: 17px !important;
            letter-spacing: 0 !important;
        }
        span {
            text-decoration: none !important;
            width: 50%;
            height: 15%;
            position: relative;
        }
        .discord {
            left: 0;
        }
        .quit {
            right: 0;
        }
        #btn {
            background-color: #bd0000b3;
            color: #fff;
            padding: 10px 10px;
            font-size: 15px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            width: 120px;
        }

        #btn:hover {
            background-color: #910000b3;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Suspicion de triche détectée pour l'{{etape}}</h1>
        <p>En raison d'une suspicion de triche, le flag ne vous sera pas attribué.</p>
        <p>Pour toute assistance, veuillez contacter notre équipe en ouvrant un ticket sur Discord.</p>
        <p style="display: inline-flex;">
            <span class="discord"><a href="https://discord.gg/9KGbRhw292" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#424242" class="bi bi-discord" viewBox="0 0 16 16"> <path d="M13.545 2.907a13.227 13.227 0 0 0-3.257-1.011.05.05 0 0 0-.052.025c-.141.25-.297.577-.406.833a12.19 12.19 0 0 0-3.658 0 8.258 8.258 0 0 0-.412-.833.051.051 0 0 0-.052-.025c-1.125.194-2.22.534-3.257 1.011a.041.041 0 0 0-.021.018C.356 6.024-.213 9.047.066 12.032c.001.014.01.028.021.037a13.276 13.276 0 0 0 3.995 2.02.05.05 0 0 0 .056-.019c.308-.42.582-.863.818-1.329a.05.05 0 0 0-.01-.059.051.051 0 0 0-.018-.011 8.875 8.875 0 0 1-1.248-.595.05.05 0 0 1-.02-.066.051.051 0 0 1 .015-.019c.084-.063.168-.129.248-.195a.05.05 0 0 1 .051-.007c2.619 1.196 5.454 1.196 8.041 0a.052.052 0 0 1 .053.007c.08.066.164.132.248.195a.051.051 0 0 1-.004.085 8.254 8.254 0 0 1-1.249.594.05.05 0 0 0-.03.03.052.052 0 0 0 .003.041c.24.465.515.909.817 1.329a.05.05 0 0 0 .056.019 13.235 13.235 0 0 0 4.001-2.02.049.049 0 0 0 .021-.037c.334-3.451-.559-6.449-2.366-9.106a.034.034 0 0 0-.02-.019Zm-8.198 7.307c-.789 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.45.73 1.438 1.613 0 .888-.637 1.612-1.438 1.612Zm5.316 0c-.788 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.451.73 1.438 1.613 0 .888-.631 1.612-1.438 1.612Z"/></svg></a></span>
            <span class="quit"><button id="btn" onclick="window.location.href = 'python';">Quitter</button></span>
        </p>
    </div>
</body>
</html>

"""
        html_content = html_content.replace("{{etape}}", str(etape))
        return html_content
    except Error as e:
        print("Erreur lors de la connexion à MySQL :", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()
            print("Connexion MySQL fermée.")


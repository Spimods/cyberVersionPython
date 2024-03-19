import mysql.connector
from datetime import datetime
import re

def save(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time1 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut, heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time1 = %s, key1 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime2"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

def save2(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time2 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time2 = %s, key2 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime3"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content



def save3(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time3 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time3 = %s, key3 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="python"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content


def save4(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time4 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time4 = %s, key4 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime5"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

def save5(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time5 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time5 = %s, key5 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime6"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

def save6(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time6 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time6 = %s, key6 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="python"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

def save7(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time7 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time7 = %s, key7 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime8"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

def save8(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    if code:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ctf"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT time8 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        if result:
            timedebut = result[0]
            jourdebut , heuredebut, mindebut, secdebut = map(int, timedebut.split())
            tempsFin = datetime.now()
            tempsFin = tempsFin.strftime("%d %H %M %S")
            jourfin, heurefin, minfin, secfin = map(int, tempsFin.split())
            jour = 0
            heure = heurefin - heuredebut
            minute = minfin - mindebut
            seconde = secfin - secdebut
            if heure < 0:
                jour -= 1
                heure += 60
            if minute < 0:
                heure -= 1
                minute += 60
            if seconde < 0:
                minute -= 1
                seconde += 60

            if minute < 2.5:
                notetime = 0
            elif minute <= 5:
                notetime = 1
            elif minute <= 7.5:
                notetime = 2
            elif minute <= 10:
                notetime = 3
            elif minute <= 12.5:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            lignes = code.split("\n")
            lignes_de_code = list(filter(lambda ligne: not ligne.strip().startswith('#'), lignes))
            nombre_de_lignes = len(lignes_de_code)
            nombre_de_caracteres = sum(len(ligne) for ligne in lignes_de_code)
            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))
            if nombre_de_lignes <= 2 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0
            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"
            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')", (nomcookie, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()
            cursor.execute("UPDATE timepython SET time8 = %s, key8 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10
            html_content = """<!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Score</title>
                <link rel="stylesheet" href="main.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                    }
                    .container {
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        padding: 20px;
                        text-align: center;
                        width:500px;
                        z-index: 2;
                    }
                    .note {
                        font-size: 50px;
                        font-weight: bold;
                        color: #b90012;
                        margin-bottom: 30px;
                    }
                    .details {
                        margin-top: 20px;
                        color: #333;
                    }
                    .progress-bar {
                        position: relative;
                        left: 50%;
                        top: -36px;
                        margin-top: 16px;
                        width: 50%;
                        height: 20px;
                        background-color: #ecf0f1;
                        border-radius: 10px;
                        overflow: hidden;
                    }
                    .progress {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_lignes}}px;
                    }
                    .progress2 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width: {{progress_caracteres}}px;
                    }
                    .progress3 {
                        height: 100%;
                        background-color: #b90012;
                        border-radius: 10px;
                        width:{{progress_temps}}px;
                    }
                    p {
                        font-size: 16px;
                        display: flex;
                    }
                    .button {
                        background-color: #b90012;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                        margin-top: 20px;
                    }
                    .button:hover {
                        background-color: #780105;
                    }
                    #confetti-canvas {
                        position: fixed; 
                        z-index: 1; 
                        top: 0; 
                        left: 0; 
                        width: 100vw; 
                        height: 100vh; 
                        pointer-events: none;
                    }
                    .svgfleche{
                        fill: #fff;
                        width: 25px;
                        margin-bottom: -6.7px;
                    }
                    *::selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-moz-selection {
                        background-color: #b6000065; 
                        color: #fff; 
                    }
                    *::-webkit-selection {
                        background-color: #b6000065; 
                        color: #fff;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="note">{{note}} / 10</div>
                    <div class="details">
                        <p>Nombre de lignes :</p><div class="progress-bar"><div class="progress"></div></div>
                        <p>Nombre de caractères :</p><div class="progress-bar"><div class="progress2"></div></div>
                        <p>Temps total :</p><div class="progress-bar"><div class="progress3"></div></div>
                    </div>
                    <button class="button" onClick='location.href="starttime9"'>Niveau Suivant <svg xmlns="http://www.w3.org/2000/svg" class="svgfleche" class="bi bi-chevron-double-right" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/> <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/> </svg></button>
                </div>
                <canvas id="confetti-canvas"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <script type="text/javascript">
                    const canvas = document.querySelector('#confetti-canvas');
                    window.addEventListener("load", (event) => {
                        var myConfetti = confetti.create(canvas, {
                            resize: true,
                            useWorker: true
                        });
                        myConfetti({
                            particleCount: 500,
                            spread: 200
                        });
                    });
                </script>
            </body>
            </html>
            """
            html_content = html_content.replace("{{note}}", str(round(note, 1)))
            html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
            html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
            html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
            return html_content

#il reste le dernier
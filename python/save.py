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


def save9(query_params, cookie):
    idcookie = cookie['ctfId']
    nomcookie = cookie['ctfNOM']
    code = query_params.get('code', [''])[0]
    nom = cookie['ctfNOM']
    if code:
        connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ctf"
            )
        cursor = connection.cursor()
        cursor.execute("SELECT time9 FROM timepython WHERE cookie = %s", (idcookie,))
        result = cursor.fetchone()
        timedebut = result[0] if result else None

        temps_fin = datetime.now()
        temps_fin_timestamp = temps_fin.timestamp()
        temps_fin = temps_fin.strftime("%d %H %M %S")
        jourfin, heurefin, minfin, secfin = map(int, temps_fin.split())

        if timedebut:
            jourdebut, heuredebut, mindebut, secdebut = map(int, timedebut.split())
            jour = jourfin - jourdebut
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

            if minute < 4:
                notetime = 0
            elif minute <= 7:
                notetime = 1
            elif minute <= 8:
                notetime = 2
            elif minute <= 9:
                notetime = 3
            elif minute <= 13:
                notetime = 4
            elif minute <= 15:
                notetime = 5
            elif minute <= 17.5:
                notetime = 7
            elif minute <= 20:
                notetime = 8
            else:
                notetime = 10

            nombre_de_lignes = len([line for line in code.split('\n') if line.strip() and not line.strip().startswith('#')])
            nombre_de_caracteres = sum(len(line) for line in code.split('\n') if line.strip() and not line.strip().startswith('#'))

            note = 10 - ((nombre_de_lignes * 0.1) / 2 + (notetime / 2) + nombre_de_caracteres * 0.01)
            note = max(0, min(10, note))

            if nombre_de_lignes <= 7 and notetime < 9:
                note = 10
                nombre_de_lignes = 0
                nombre_de_caracteres = 0
                notetime = 0

            time = f"{heure}-{minute}-{seconde}"
            timeend = f"{heure}h{minute}min{seconde}sec"

            cursor.execute("INSERT INTO score (nom, note, timetotal, caracteretotal, lignetotal, codecomplet, cookie, etape) VALUES (%s, %s, %s, %s, %s, %s, %s, 'python')",
                        (nom, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
            connection.commit()

            cursor.execute("SELECT time7, time8 FROM timepython WHERE cookie = %s", (idcookie,))
            result = cursor.fetchone()
            time1, time2 = result if result else (None, None)

            if time1 and time2:
                val1, val2, val3 = map(int, time1.split('h')[1].split('min')[0].split('sec')[0].split())
                val12, val22, val32 = map(int, time2.split('h')[1].split('min')[0].split('sec')[0].split())
                heure = val1 + val12 + heure
                min_ = val2 + val22 + minute
                sec = val3 + val32 + seconde
                if sec > 60:
                    sec -= 60
                    min_ += 1
                if min_ > 60:
                    min_ -= 60
                    heure += 1
                time = f"{heure}h {min_}min {sec}sec"
            progress_caracteres = 100 - nombre_de_caracteres / 4 if (nombre_de_caracteres / 4) < 100 else 4
            progress_lignes = 100 - nombre_de_lignes * 2 if (nombre_de_lignes * 2) < 100 else 4
            progress_temps = 100 - notetime * 10

            cursor.execute("UPDATE python SET time_flag_3 = %s, flag3 = 1 WHERE cookie = %s", (time, idcookie))
            connection.commit()

            cursor.execute("UPDATE timepython SET time9 = %s, key9 = 1 WHERE cookie = %s", (timeend, idcookie))
            connection.commit()

        cursor.close()
        connection.close()
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
            z-index: 3; 
            top: 0; 
            left: 0; 
            width: 100vw; 
            height: 100vh; 
            pointer-events: none;
        }



        .content {
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            display : none;
        }

        .content__coins {
            z-index: 5;
            position: relative;
            width: 160px;
            height: 160px;
            animation-timing-function: ease-in-out;
            animation-duration: 2s;
            animation-fill-mode: forwards;
            animation-name: initial-animation; 
        }

        .currency-soft-3d {
            position: absolute;
            width: 160px;
            height: 160px;
            transform: rotateY(0deg);
            transform-origin: center center;
            transform-style: preserve-3d;
        }

        @keyframes initial-animation {
            0% {
                transform: translateY(-600px); 
            }
            100% {
                transform: translateY(0); 
            }
        }

        .currency-soft-3d_state_left {
            animation-name: coins-item-left-animation;
        }

        .currency-soft-3d_state_half_left {
            animation-name: coins-item-half-left-animation;
        }

        .currency-soft-3d::before {
            content: "";
            position: absolute;
            z-index: 1;
            top: 0;
            left: 50%;
            width: 20px;
            height: 100%;
            margin-left: -10px;
            transform: rotateY(-90deg);
            transform-origin: 100% 50%;
            background-color: #FD002E;
            border-radius: 2px;
        }

        .currency-soft-3d__front_inside {
            position: absolute;
            z-index: -1;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background-color: #FD002E;
            transform: translateZ(-1px);
        }

        .currency-soft-3d__front {
            position: absolute;
            z-index: 2;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            transform: translateZ(0);
            border-radius: 50%;
            background-color: #FD002E;
            background-image: url('../images/piecepython1.png');
            background-repeat: no-repeat;
            background-position: center center;
            background-size: 108%;
        }
        .end {
            animation-timing-function: ease-in-out;
            animation-duration: 1s;
            animation-fill-mode: forwards;
            animation-name: end-animation; 
        }
        @keyframes end-animation {
            0% {
                transform: translateY(0); 
            }
            100% {
                transform: translateY(600px); 
            }
        }

        .currency-soft-3d__back {
            position: absolute;
            z-index: 1;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            transform: rotateY(180deg) translateZ(20px);
            border-radius: 50%;
            background-color: #FD002E;
            background-image: url('../images/piecepython1.png');
            background-repeat: no-repeat;
            background-position: center center;
            background-size: 108%;
        }
        .message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            z-index: 2;
            display: none;
        }

        .currency-soft-3d__back_inside {
            position: absolute;
            z-index: -2;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            transform: translateZ(-19px);
            border-radius: 50%;
            background-color: #FD002E;
        }

        body {
            overflow: hidden;
            margin: 0;
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
        .texte-fondu {
            display: none;
            color: #fff;
            opacity: 0; 
            transition: opacity 1s ease-in-out;
        }
        .fin{
            display: none;
            display: block;
            text-decoration: none;
            color: #a90000;
            opacity: 0;
            transition: opacity 1s ease-in-out;
            cursor: default;
        }
        .texte-visible {
            text-align: center;
            display: block;
            opacity: 1; 
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
    <div class="message" id="message">
    </div>
    <div class="texte-fondu">
    Félicitations pour avoir brillamment achevé l'épreuve de Python du Ozanam CyberQuest ! <br>
    Votre maîtrise rapide et précise de la programmation démontre un talent exceptionnel. Continuez ainsi !<br>
    <a class='fin' href="../python.php">Terminer</a>
    </div>

    <div class="content">
        <span class="content__coins" onclick="casse()">
            <span class='currency-soft-3d currency-soft-3d_state_left'>
            <span class="currency-soft-3d__front_inside"></span>
            <span class="currency-soft-3d__front"></span>
            <span class="currency-soft-3d__back"></span>
            <span class="currency-soft-3d__back_inside"></span>
            </span>
        </span>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

    <script>

        function start(){

            document.querySelector('.content').style.display = "inherit"
            document.querySelector('.container').style.display = "none"
            document.querySelector('.message').style.display = "block"
            const canvas = document.querySelector('#confetti-canvas');
                setTimeout(() => {
                    var end = Date.now() + (8 * 1000);
                    var colors = ['#bb0000', '#ffffff'];
                    (function frame() {
                    confetti({
                        particleCount: 2,
                        angle: 60,
                        spread: 55,
                        origin: { x: 0 },
                        colors: colors
                    });
                    confetti({
                        particleCount: 2,
                        angle: 120,
                        spread: 55,
                        origin: { x: 1 },
                        colors: colors
                    });
                    if (Date.now() < end) {
                        requestAnimationFrame(frame);
                    }
                    }());
                }, 2000);
        }
        nombre = 0

        function casse() {
            const back = document.querySelector('.currency-soft-3d__back');
            const back2 = document.querySelector('.currency-soft-3d__front');

            if (nombre == 0) {
                back.style.backgroundColor = "#270013";
                back2.style.backgroundColor = "#270013";
                back.style.backgroundImage = "url(../images/piecepythoncasse1.png)";
                back2.style.backgroundImage = "url(../images/piecepythoncasse1.png)";
            } else if (nombre == 1) {
                back.style.backgroundImage = "url(../images/piecepythoncasse2.png)";
                back2.style.backgroundImage = "url(../images/piecepythoncasse2.png)";
            } else if (nombre == 2) {
                back.style.backgroundImage = "url(../images/piecepythoncasse3.png)";
                back2.style.backgroundImage = "url(../images/piecepythoncasse3.png)";
            } else if (nombre == 3) {
                back.style.backgroundImage = "url(../images/piecepythoncasse4.png)";
                back2.style.backgroundImage = "url(../images/piecepythoncasse4.png)";
            } else if (nombre == 4) {
                document.querySelector('.content__coins').classList.add('end');
                setTimeout(() => {
                    document.querySelector('.message').style.display = "none"
                }, 400);
                setTimeout(() => {
                    document.querySelector(".content").style.display = "none";
                    document.querySelector(".texte-fondu").classList.add("texte-visible");
                    document.querySelector(".fin").style.display = "block";
                    setTimeout(() => {
                        document.querySelector(".fin").classList.add("texte-visible");
                        document.querySelector(".fin").style.cursor = "pointer";
                    }, 2000);
                }, 900);
            }

            console.log(nombre);
            nombre = nombre + 1;
            console.log(nombre);
        }
        const container = document.querySelector('.currency-soft-3d');
        let isMouseDown = false;
        let initialX;
        const speed = 0.5; 
        document.addEventListener('mousedown', (event) => {
        if (event.button === 0) {
            isMouseDown = true;
            initialX = event.clientX;
        }
        });
        document.addEventListener('mouseup', () => {
            isMouseDown = false;
        });
        document.addEventListener('mousemove', (event) => {
        if (isMouseDown) {
            const movementX = event.clientX - initialX;
            container.style.transform = `rotateY(${speed * movementX}deg)`; 
        }
        });
    </script>



</body>
</html>
            """
        print(note)
        html_content = html_content.replace("{{note}}", str(round(note, 1)))
        html_content = html_content.replace("{{progress_caracteres}}", str(progress_caracteres))
        html_content = html_content.replace("{{progress_lignes}}", str(progress_lignes))
        html_content = html_content.replace("{{progress_temps}}", str(progress_temps))
        return html_content


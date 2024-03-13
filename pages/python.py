from flask import Flask, render_template, request, redirect, session
import mysql.connector
import re
import http.cookies

def parseTime(timeString):
    match = re.match(r'(\d+)h (\d+)min (\d+)sec', timeString)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        return hours * 3600 + minutes * 60 + seconds
    return 0

def totalTime(times):
    totalSeconds = sum(parseTime(time) for time in times if time is not None)
    hours = totalSeconds // 3600
    minutes = (totalSeconds % 3600) // 60
    seconds = totalSeconds % 60
    return f"{hours:02d}h {minutes:02d}min {seconds:02d}sec"

def parseTime(timeString):
    if isinstance(timeString, str):
        match = re.match(r'(\d+)h (\d+)min (\d+)sec', timeString)
        if match:
            hours = int(match.group(1))
            minutes = int(match.group(2))
            seconds = int(match.group(3))
            return hours * 3600 + minutes * 60 + seconds
    return 0

def home(cookie):
    cookie = cookie['ctfId']
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT time1, time2, time3, time4, time5, time6, time7, time8, time9, nom, key1, key2, key3, key4, key5, key6, key7, key8, key9 FROM timepython WHERE cookie = %s", (cookie,))
    row = cursor.fetchone()
    if row is not None:
        row = [0 if value is None else value for value in row]
        time1, time2, time3, time4, time5, time6, time7, time8, time9, nom, key1, key2, key3, key4, key5, key6, key7, key8, key9 = row
    else:
        time1, time2, time3, time4, time5, time6, time7, time8, time9, nom, key1, key2, key3, key4, key5, key6, key7, key8, key9 = [0] * 19  # Toutes les valeurs initialisées à 0
    print("Python flags and times:", time1, time2, time3,time4, time5, time6,time7, time8, time9, nom, key1, key2 , key3, key4, key5, key6, key7, key8, key9)
    connection.close()
    part1 = 1 if (key1 == 1 and key2 == 1 and key3 == 1) else 0
    part2 = 1 if (key4 == 1 and key5 == 1 and key6 == 1) else 0
    part3 = 1 if (key7 == 1 and key8 == 1 and key9 == 1) else 0
    part1calc = 1 if (key1 == 1 and key2 == 1 and key3 == 1) else 0
    part2calc = 1 if (key4 == 1 and key5 == 1 and key6 == 1) else 0
    part3calc = 1 if (key7 == 1 and key8 == 1 and key9 == 1) else 0
    if part1 == 0:
        part2 = 1
        part3 = 1
    elif part2 == 0:
        part3 = 1
    print(f'valeur des points : {part1calc}, {part2calc}, {part3calc}')

    times = [int(time1), int(time2), int(time3), int(time4), int(time5), int(time6), int(time7)]
    print(times)
    total_time = totalTime(times)
    print("Total time:", total_time)
    total_point = part1calc + part2calc + part3calc

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, shrink-to-fit=no">
    <meta name="viewport" content="initial-scale=1.25"/>
    <meta name="viewport" content="user-scalable=no"/>
    <title>Ozanam CyberQuest | Python</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="bootstrap4-neon-glow.min.css">
    <link rel='stylesheet' href='//cdn.jsdelivr.net/font-hack/2.020/css/hack.min.css'>
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="python.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
</head>
<body class="imgloaded">
    <div class="glitch">
        <div class="glitch__img"></div>
        <div class="glitch__img"></div>
        <div class="glitch__img"></div>
        <div class="glitch__img"></div>
        <div class="glitch__img"></div>
    </div>
    <div class="navbar-dark text-white">
        <div class="container">
            <nav class="navbar px-0 navbar-expand-lg navbar-dark">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <a href="homepage" class="pl-md-0 p-3 text-decoration-none text-light">
                            <h3 class="bold"><span class="color_danger">Ozanam</span><span class="color_white">CyberQuest</span></h3>
                        </a>
                    </div>
                    <div class="navbar-nav ml-auto">
                        <a href="homepage" class="p-3 text-decoration-none text-light bold">Accueil</a>
                        <a href="intro" class="p-3 text-decoration-none text-white bold">Commencer</a>
                    </div>
                </div>
            </nav>
        </div>
    </div>
    <div class="jumbotron bg-transparent mb-0 pt-3 radius-0">
        <div class="container">
            <div class="row">
                <div class="col-xl-8">
                    <div class="container">
                        <div class="stack" style="--stacks: 3;">
                            <span style="--index: 0;">Python : {total_point}/3</span>
                            <span style="--index: 1;">Python : {total_point}/3</span>
                            <span style="--index: 2;">Python : {total_point}/3</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
<br>
<div class={'box1end' if part1 != 0 else 'box1'} {'' if part1 != 0 else "onclick='location.href=`tuto`"};' ><span class='text'>Débutant</span></div>
<div class={'box2end' if part2 != 0 else 'box2'}  {'' if part1 != 0 else "onclick='location.href=`starttime4`"};' ><span class='text'>Intermédiaire</span></div>
<div class={'box3end' if part3 != 0 else 'box3'}  {'' if part1 != 0 else "onclick='location.href=`starttime7`"};' ><span class='text'>Maître</span></div>
</body>
</html>
"""
    return html_content


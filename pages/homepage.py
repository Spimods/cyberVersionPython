from flask import Flask, render_template, request, redirect, session
import mysql.connector
import re
import http.cookies
import datetime


def totalTime(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        time_components = time_str.replace(' ', '').split('h')  # Supprimer les espaces et séparer les heures
        if len(time_components) == 1:  # Si la séparation n'a pas fonctionné, cela signifie qu'il n'y a pas d'heures
            h = 0
            if 'min' in time_components[0]:
                m, s = map(int, time_components[0].replace('min', ':').replace('sec', '').split(':'))
            else:
                m, s = 0, 0
        else:
            h, rest = time_components
            if 'min' in rest:
                m, s = map(int, rest.replace('min', ':').replace('sec', '').split(':'))
            else:
                m, s = 0, 0
            h = int(h)
        total_seconds += datetime.timedelta(hours=h, minutes=m, seconds=s).total_seconds()
    total_seconds = int(total_seconds)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{hours}h{minutes}min{seconds}sec"

def parseTime(timeString):
    if isinstance(timeString, str):
        match = re.match(r'(\d+)h (\d+)min (\d+)sec', timeString)
        if match:
            hours = int(match.group(1))
            minutes = int(match.group(2))
            seconds = int(match.group(3))
            return hours * 3600 + minutes * 60 + seconds
    return 0

def home(query_params, cookie):
    if query_params :
        nom = query_params.get('nom', [None])[0]
    else :
        nom = cookie['ctfNOM']

    cookie = cookie['ctfId']
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT finish FROM ctfuser WHERE cookie = %s", (cookie,))
    finish = cursor.fetchone()#[0]
    print("Finish:", finish)

    cursor.execute("SELECT flag1, flag2, flag3, nom FROM python WHERE cookie = %s", (cookie, ))
    flag1, flag2, flag3, nom = cursor.fetchone()
    print("Python flags and times:", flag1, flag2, flag3, nom)
    cursor.execute("SELECT time1, time2, time3, time4, time5, time6, time7, time8, time9 FROM timepython WHERE cookie = %s", (cookie, ))
    time1, time2, time3, time4, time5, time6, time7, time8, time9 = cursor.fetchone()
    print("Python flags and times:", time1, time2, time3, time4, time5, time6, time7, time8, time9)

    flag4 = flag5 = flag6 = flag7 = 1
    connection.close()

    part1 = 1 if (flag1 == 1 and flag2 == 1 and flag3 == 1) else 0
    part2 = 1 if (flag4 == 1 and flag5 == 1 and flag6 == 1) else 0
    part3 = 1 if flag7 == 1 else 0
    times = [time1, time2, time3, time4, time5, time6, time7, time8, time9]
    times = [time_str if time_str and time_str != '0' else '0h0min0sec' for time_str in times]
    print(times)
    total_time = totalTime(times)
    print("Total time:", total_time)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, shrink-to-fit=no">
    <meta name="viewport" content="initial-scale=1.25"/>
    <meta name="viewport" content="user-scalable=no"/>
    <title>Ozanam CyberQuest</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="bootstrap4-neon-glow.min.css">
    <link rel='stylesheet' href='//cdn.jsdelivr.net/font-hack/2.020/css/hack.min.css'>
    <link rel="stylesheet" href="main.css">
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
                            <span style="--index: 0;">{nom.capitalize()} : {total_time}</span>
                            <span style="--index: 1;">{nom.capitalize()} : {total_time}</span>
                            <span style="--index: 2;">{nom.capitalize()} : {total_time}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
<br>
<div class={'box1end' if part1 != 0 else 'box1'} onclick='location.href=`python`;' ><span class='text'>Python</span></div>
<div class='box2end' onclick='location.href=`redirect`;' ><span class='text'>Programmation</span></div>
<div class='box3end' onclick='location.href=`redirect`;' ><span class='text'>Réseaux sociaux</span></div>
</body>
</html>
"""
    return html_content


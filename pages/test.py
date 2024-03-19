from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import mysql.connector
from datetime import datetime

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)

        if 'code' in query:
            code = query['code'][0]
            idcookie = self.idcookie
            name = self.name

            connection = mysql.connector.connect(
                host="your_host",
                user="your_username",
                password="your_password",
                database="your_database"
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
                               (name, note, time, nombre_de_caracteres, nombre_de_lignes, code, idcookie))
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

                cursor.execute("UPDATE python SET time_flag_3 = %s, flag3 = 1 WHERE cookie = %s", (time, idcookie))
                connection.commit()

                cursor.execute("UPDATE timepython SET time9 = %s, key9 = 1 WHERE cookie = %s", (timeend, idcookie))
                connection.commit()

            cursor.close()
            connection.close()

server_address = ('', 8080)

httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()

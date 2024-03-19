from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pages import css, home, intro, js, font, login, loginpage, homepage, python
from python import tuto, starttime, etape, save
from http import cookies
import urllib.parse
import subprocess
import tempfile
import json

css_paths = {
    '/main.css': css.generate_main_css,
    '/bootstrap4-neon-glow.css': css.generate_bootstrap4_neon_glow_css,
    '/bootstrap4-neon-glow.min.css': css.generate_bootstrap4_neon_glow_min_css,
    '/editor.css': css.generate_editor_css,
    '/final.css': css.generate_final_css,
    '/prog.css': css.generate_prog_css,
    '/python.css': css.generate_python_css,
    '/reseaux.css': css.generate_reseaux_css,
    '/scrollbar.css': css.generate_scrollbar_css,
    '/select.css': css.generate_select_css
}

js_paths = {
    '/chart.js': js.generate_chart_js,
    '/menu.js': js.generate_menu_js,
    '/preloader.js': js.generate_preloader_js,
    '/timer.js': js.generate_timer_js,
    '/timerCSS.js': js.generate_timer_css_js,
    '/timerHTML.js': js.generate_timer_html_js,
    '/timerreseaux.js': js.generate_timer_reseaux_js,
    '/script.js': js.scriptjs
}

font_paths = {
    '/Doctor Glitch.otf': font.generate_Doctor,
    '/PhelixBoomgartner.otf': font.generate_phelix,
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith('/execute'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = post_data.decode('utf-8')
            post_data = urllib.parse.unquote(post_data, encoding='latin1')
            if post_data.startswith("code="):
                code = post_data[5:]
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                    tmp_file.write(code)
                try:
                    output = subprocess.check_output(["python", tmp_file.name], stderr=subprocess.STDOUT, universal_newlines=True)
                    response = {
                        'output': output.strip(),
                        'error': ''
                    }
                except subprocess.CalledProcessError as e:
                    response = {
                        'output': e.output.strip(),
                        'error': e.output.strip()
                    }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No Python code provided.'}).encode())

    def do_GET(self):
        print("Requête GET reçue:", "http://localhost:8000" + self.path) 
        if self.path in css_paths:
            print("Chemin correspondant à", self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            css_content = css_paths[self.path]()
            self.wfile.write(css_content.encode('utf-8'))
        elif self.path in js_paths:
            print("Chemin correspondant à", self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            js_content = js_paths[self.path]()
            self.wfile.write(js_content.encode('utf-8'))
        elif self.path == '/home':
            print("Chemin correspondant à /page1:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = home.generate_page1_html()
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path == '/intro':
            print("Chemin correspondant à /page2:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = intro.generate_page2_html()
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path == '/login':
            print("Chemin correspondant à /login:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = login.generate_login_html()
            self.wfile.write(html_content.encode('utf-8'))

        elif self.path.startswith('/homepage'):
            print("Chemin correspondant à /homepage:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_string = self.path.split('?')[-1]
            parameters = {}
            if query_string is not None:
                pairs = query_string.split('&')
                for pair in pairs:
                    if '=' in pair:
                        key, value = pair.split('=')
                        parameters[key] = value
                    else:
                        key = pair
                        value = None
                        parameters[key] = value
                parsed_url = urlparse(self.path)
                query_params = parse_qs(parsed_url.query)
            else:
                print("Aucune chaîne de requête trouvée.")
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = homepage.home(query_params, cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))

        elif self.path.startswith('/python'):
            print("Chemin correspondant à /python:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = python.home(cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))

        elif self.path.startswith('/loginpage'):
            print("Chemin correspondant à /loginpage:", "http://localhost:8000" + self.path)
            query_string = self.path.split('?')[-1]
            parameters = {}
            if query_string:
                pairs = query_string.split('&')
                for pair in pairs:
                    key, value = pair.split('=')
                    if key in parameters:
                        parameters[key].append(value)
                    else:
                        parameters[key] = value
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            print(query_params, self.client_address[0])
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            print("Cookies reçus")
            print(query_params, self.client_address[1])
            html_content = loginpage.verification(self.client_address[0], query_params, cookie_dict)
            print('html :',html_content)
            if html_content:
                if len(html_content) == 2:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    print(html_content[1])
                    for cookie_name, cookie_value in html_content[1]:
                        c = cookies.SimpleCookie()
                        print(cookie_name, cookie_value)
                        c[cookie_name] = cookie_value
                        self.send_header("Set-Cookie", c.output(header='')) # Ajout des cookies dans l'en-tête
                    self.end_headers()
                    script_content = f"""
                    <script>
                    window.location.href = '{html_content[0]}';
                    </script>
                    """
                    self.wfile.write(script_content.encode('utf-8'))
                else:
                    script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
                    self.wfile.write(script_content.encode('utf-8'))

        elif self.path.startswith('/tuto'):
            print("Chemin correspondant à /tuto:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = tuto.tuto(cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))

        elif self.path.startswith('/saveun'):
            print("Chemin correspondant à /saveun:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_string = self.path.split('?')[-1]
            parameters = {}
            if query_string:
                pairs = query_string.split('&')
                for pair in pairs:
                    key, value = pair.split('=')
                    if key in parameters:
                        parameters[key].append(value)
                    else:
                        parameters[key] = value
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            print(query_params, self.client_address[0])
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            print("Cookies reçus")
            print(query_params, self.client_address[1])
            html_content = save.save(query_params, cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))

        elif self.path.startswith('/savedeux'):
            print("Chemin correspondant à /savedeux:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_string = self.path.split('?')[-1]
            parameters = {}
            if query_string:
                pairs = query_string.split('&')
                for pair in pairs:
                    key, value = pair.split('=')
                    if key in parameters:
                        parameters[key].append(value)
                    else:
                        parameters[key] = value
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            print(query_params, self.client_address[0])
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            print("Cookies reçus")
            print(query_params, self.client_address[1])
            html_content = save.save2(query_params, cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))



        elif self.path.startswith('/starttime1'):
            print("Chemin correspondant à /starttime1:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape1start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))

        elif self.path.startswith('/starttime2'):
            print("Chemin correspondant à /starttime2:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape2start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/starttime3'):
            print("Chemin correspondant à /starttime3:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape3start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/starttime4'):
            print("Chemin correspondant à /starttime4:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape4start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/starttime5'):
            print("Chemin correspondant à /starttime5:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape5start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/starttime6'):
            print("Chemin correspondant à /starttime6:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape6start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/starttime7'):
            print("Chemin correspondant à /starttime7:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape7start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))

        elif self.path.startswith('/starttime8'):
            print("Chemin correspondant à /starttime8:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape8start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))

        elif self.path.startswith('/starttime9'):
            print("Chemin correspondant à /starttime9:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = starttime.etape9start(cookie_dict)
            script_content = f"""
                    <script>
                    window.location.href = '{html_content}';
                    </script>
                    """
            self.wfile.write(script_content.encode('utf-8'))


        elif self.path.startswith('/etape1'):
            print("Chemin correspondant à /etape1:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = etape.etape1start(cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path.startswith('/etape2'):
            print("Chemin correspondant à /etape1:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            cookie_string = self.headers.get('Cookie')
            cookie_dict = {}
            if cookie_string:
                c = cookies.SimpleCookie()
                c.load(cookie_string)
                for key, morsel in c.items():
                    cookie_dict[key] = morsel.value
            html_content = etape.etape2start(cookie_dict)
            self.wfile.write(html_content.encode('utf-8'))




        elif self.path.startswith('/execute'):
            print("Chemin correspondant à /execute:", "http://localhost:8000" + self.path)
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            code = post_data.split('=')[1]
            if code:
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
                    temp.write(code)
                    temp_file_path = temp.name
                try:
                    process = subprocess.Popen(['python', temp_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    output, error = process.communicate()
                    response = {
                        'output': output.strip(),
                        'error': error.strip() if process.returncode != 0 else ''
                    }
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())
                finally:
                    import os
                    os.unlink(temp_file_path)
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Aucun code Python fourni.'}).encode())

        else:
            print("Chemin non reconnu:", "http://localhost:8000" + self.path)
            self.send_error(404, 'Not Found')


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

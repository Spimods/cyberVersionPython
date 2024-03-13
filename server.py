from http.server import HTTPServer, BaseHTTPRequestHandler
from pages import css, home, intro, js , font, login, loginpage
from urllib.parse import urlparse, parse_qs

# Liste des chemins correspondant aux fichiers CSS
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

# Liste des chemins correspondant aux fichiers JavaScript
js_paths = {
    '/chart.js': js.generate_chart_js,
    '/menu.js': js.generate_menu_js,
    '/preloader.js': js.generate_preloader_js,
    '/timer.js': js.generate_timer_js,
    '/timerCSS.js': js.generate_timer_css_js,
    '/timerHTML.js': js.generate_timer_html_js,
    '/timerreseaux.js': js.generate_timer_reseaux_js
}
font_paths = {
    '/Doctor Glitch.otf': font.generate_Doctor,
    '/PhelixBoomgartner.otf': font.generate_phelix,

}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Requête GET reçue:", "http://localhost:8000" + self.path)  
        if self.path in css_paths:  # Vérifie si le chemin correspond à un fichier CSS
            print("Chemin correspondant à", self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            css_content = css_paths[self.path]()  # Appelle la fonction de génération correspondante
            self.wfile.write(css_content.encode('utf-8'))
        elif self.path in js_paths:  # Vérifie si le chemin correspond à un fichier JavaScript
            print("Chemin correspondant à", self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            js_content = js_paths[self.path]()  # Appelle la fonction de génération correspondante
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
        elif self.path.startswith('/loginpage'):
            print("Chemin correspondant à /loginpage:", "http://localhost:8000" + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_string = self.path.split('?')[-1]
            parameters = {}
            if query_string:
                pairs = query_string.split('&')
                for pair in pairs:
                    key, value = pair.split('=')
                    parameters[key] = value
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            html_content = loginpage.verification(self.client_address[0], query_params)
            print(html_content)
            if html_content:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                script_content = f"""
                <script>
                window.location.href = '{html_content}';
                </script>
                """
                self.wfile.write(script_content.encode('utf-8'))

        else:
            print("Chemin non reconnu:", "http://localhost:8000" + self.path)
            self.send_error(404, 'Not Found')

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

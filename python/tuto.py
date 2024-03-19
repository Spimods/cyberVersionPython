import mysql.connector
import re
import http.cookies

def tuto(cookie):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ctf"
    )
    cursor = connection.cursor()
    if 'ctfId' in cookie:
        valeurCookie = cookie['ctfId']
        cursor.execute("SELECT key1 FROM timepython WHERE cookie = %s", (valeurCookie,))
        key1 = cursor.fetchone()[0]
        if key1 is not None:
            print('redirect_to_timestartetape1()')
            exit()
    else :
        print("pas de cookie")
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Pair ou impair ?</title>
        <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/3.0.1/js.cookie.min.js"></script>
        <link rel="stylesheet" href="editor.css">
        <link rel="stylesheet" href="select.css">
        <style>
    .messagetuto {
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
        z-index: 1000000;
    }
    .messagebox{
        background: #fffefe;
        border-radius: 5px;
        padding: 1px 10px;
        color: black;
        font-size: 15px;
        position: relative;
        text-align: center;
    }
    .valid {
        padding: 5px;
        cursor: pointer;
        color: #fff;
        border: 2px solid #e62117;
        border-radius: 5px;
        font-size: 16px;
        margin-bottom: 10px;
        transform-style: preserve-3d;
        perspective: 800px;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
        box-shadow: 0 0 10px rgba(230, 33, 23, 0);
        background-color: #1a1a1a;
    }
        </style>
    </head>
    <body>
    <div class="messagetuto" id="message">
        <div class="messagebox" id="messagebox"><p id="textebox">Bienvenue dans le tuto.</p>
            <button class="valid" id="valid" onclick="tuto()">Continuer</button>
    </div>
    </div>
            
    <div class="container">
        <div class="toggle-button" onclick="toggleMenu()">
            <div class="area">
                <div class="wire"></div>
                <div class="fixture">
                <div class="strip"></div>
                <div class="strip"></div>
                <div class="strip"></div>
                </div>
                <div class="bulb">
                <div class="zig"></div>
                <div class="zig"></div>
                <div class="zig"></div>
                </div>
            </div>
        </div>
        
        
        <div class="menu" id="menu">
            <h2 style="text-align: center;">Indices</h2>
            <ul>
                <li onclick="toggleInfo('print()', this)">
                    <span class="function-fonction">print</span><span class="parentheses">( )</span>
                    <div class="info-dropdown" id="infoDropdownPrint" onclick="preventDropdownClick(event)">
                        <p>La fonction print est utilisée pour afficher du texte à la console. Par exemple:
                            <code>print<span class="parentheses">(</span><span class="texte-code">"Bonjour, comment ça va?"</span><span class="parentheses">)</span></code>
                    </div>
                </li>

                <li onclick="toggleInfo('input()', this)">
                    <span class="function-fonction">input</span><span class="parentheses">( )</span>
                    <div class="info-dropdown" id="infoDropdownInput" onclick="preventDropdownClick(event)">
                        <p>Ceci est un exemple de <span class="function-fonction">définition de fonction</span> avec la fonction <code>input()</code>.</p>
                    </div>
                </li>

                <li onclick="toggleInfo('newFunction1()', this)">
                    <span class="function-fonction">len</span><span class="parentheses">( )</span>
                    <div class="info-dropdown" id="infoDropdownNew1" onclick="preventDropdownClick(event)">
                        <p>La fonction <span class="function-fonction">len</span>( ) renvoie la longueur d'un objet, comme une chaîne de caractères ou une liste. Par exemple :<br><code> mot = "Python" <br>longueur = <span class='function-fonction'>len</span><span class='parentheses'>(mot)</span><br><span class='function-fonction'>print</span><span class='parentheses'>(<span class='texte-code'>'La longueur du mot est :"</span>, longueur)</span></code></p>
                    </div>
                </li>
                <li onclick="toggleInfo('newFunction2()', this)">
                    <span class="function-fonction">range</span><span class="parentheses">( )</span>
                    <div class="info-dropdown" id="infoDropdownNew2" onclick="preventDropdownClick(event)">
                        <p>La fonction <span class="function-fonction">range</span>( ) génère une séquence d'entiers. Par exemple :<br><code> <span style="color : #003dd8">for</span> <span class='parentheses'>i</span> <span style="color : #003dd8">in</span> <span class='function-fonction'>range</span><span class='parentheses'>(<span style="color : #e90000;">5</span>):</span> print(i) <br>longueur = <span class='function-fonction'>len</span><span class='parentheses'>(mot)</span><br><span class='function-fonction'>print</span><span class='parentheses'>(<span class='texte-code'>'La longueur du mot est :"</span>, longueur)</span></code></p>
                    </div>
                </li>

                <li onclick="toggleInfo('newFunction3()', this)">
                    <span class="function-fonction">Les listes</span>
                    <div class="info-dropdown" id="infoDropdownNew3" onclick="preventDropdownClick(event)">
                        <p>Les listes sont des structures de données importantes. Voici un exemple de création et d'accès à une liste :<br><code><span class='parentheses'>ma_liste = [<span style="color : #ae81ff">1</span>, <span style="color : #ae81ff">2</span>, <span style="color : #ae81ff">3</span>, <span style="color : #ae81ff">4</span>, <span style="color : #ae81ff">5</span>]</span><br><span class='function-fonction'>range</span><span class='parentheses'>(<span style="color : #e90000;">5</span>):</span> print(i) <br>longueur = <span class='function-fonction'>len</span><span class='parentheses'>(mot)</span><br><span class='function-fonction'>print</span><span class='parentheses'>(<span class='texte-code'>'La longueur du mot est :"</span>, longueur)</span></code></p>
                    </div>
                </li>

                <li onclick="toggleInfo('newFunction4()', this)">
                    <span class="function-fonction">Condition If</span>
                    <div class="info-dropdown" id="infoDropdownNew4" onclick="preventDropdownClick(event)">
                        <p>La structure <span class="function-fonction">if</span> est utilisée pour prendre des décisions conditionnelles. Par exemple :<br><code><span class="parentheses">age = <span style="color : #ae81ff">18</span><br><span style="color : #003dd8">if</span> age</span> >= <span style="color : #ae81ff">18</span>: <br><span class="function-fonction">print</span><span class="parentheses">(</span><span class='texte-code'>'Vous êtes majeur.'</span><span class="parentheses">)</span><br><span style="color : #003dd8">else</span>:<br><span class="function-fonction">print</span><span class="parentheses">(</span><span class='texte-code'>'Vous êtes mineur.'</span><span class="parentheses">)</span></span></code><p>
                    </div>
                </li>

                <li onclick="toggleInfo('newFunction5()', this)">
                    <span class="function-fonction">Le for</span>
                    <div class="info-dropdown" id="infoDropdownNew5" onclick="preventDropdownClick(event)">
                        <p>Les boucles for sont utilisées pour répéter des blocs de code. Voici un exemple de boucle for :<br><code><span class="parentheses"><span style="color : #003dd8">for</span> i <span style="color : #003dd8">in</span> <span class="function-fonction">range</span>(<span style="color : #e90000">3</span>):<br>&emsp;&ensp;<span class="function-fonction">print</span>(<span class='texte-code'>"Répétition numéro"</span>, i+<span style="color : #ae81ff">1</span>)</span></code></p>
                    </div>
                </li>

                <li onclick="toggleInfo('newFunction6()', this)">
                    <span class="function-fonction">Le while</span>
                    <div class="info-dropdown" id="infoDropdownNew6" onclick="preventDropdownClick(event)">
                        <p>La boucle <span class='function-fonction'>while</span> permet d'exécuter un bloc de code tant qu'une condition est vraie. Voici une structure générale :<br><code><span class='parentheses'>compteur = 0<br><span style='color : #003dd8'>while</span> compteur < <span style='color : #ae81ff'>3</span>:<br>&emsp;&ensp;<span class='function-fonction'>print</span>(<span class='texte-code'>'Répétition numéro'</span>, compteur+<span style='color : #ae81ff'>1</span>)<br>&emsp;&ensp;compteur += <span style='color : #ae81ff'>1</span></span></code></p>
                    </div>
                </li>

            </ul>
        </div>
    </div>

    <div class="loading-bar">
        <div class="progress" id="progress"></div>
        <div class="time" id="time">0:00</div>
    </div>


    <div id="editor-container">
    <button id="restart" onclick="restart()"><svg xmlns="http://www.w3.org/2000/svg" class="bi bi-arrow-counterclockwise" viewBox="0 0 16 16"> <path fill-rule="evenodd" d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z"/> <path d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z"/> </svg></button>

        <div id="editor"># Demander à l'utilisateur de saisir un nombre
    nombre = int(input("Entrez un nombre : "))
    </div>
            <div id="tooltip">
                <p>Consignes :</p>
                <ul>
                    <li>Vérifiez si le nombre est pair ou impair.</li>
                    <li>Si le nombre est pair, affichez "pair", sinon affichez "impair".</li>
                </ul>
            </div>
        </div>
        <button id="runButton" onclick="verif()">Exécuter</button>
        <button id="validButton" onclick="redirect()">Valider</button>

        <div id="outputContainer">
            <div id="output"></div>
            <div id="verification">
                <span id="result1"><span id="svgun"><svg class="svgvalid" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span><span id="svgunno"><svg class="svgno" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 4.246094 2.902344 L 26.019531 2.902344 L 26.019531 26.855469 L 4.246094 26.855469 Z M 4.246094 2.902344 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 18.527344 14.878906 L 25.925781 3.785156 C 26.039062 3.617188 26.050781 3.40625 25.953125 3.226562 C 25.859375 3.050781 25.675781 2.941406 25.476562 2.941406 L 21.488281 2.941406 C 21.3125 2.941406 21.144531 3.027344 21.042969 3.175781 L 15.160156 11.625 L 9.273438 3.175781 C 9.171875 3.027344 9.003906 2.941406 8.828125 2.941406 L 4.839844 2.941406 C 4.640625 2.941406 4.457031 3.050781 4.363281 3.226562 C 4.269531 3.402344 4.277344 3.617188 4.390625 3.785156 L 11.792969 14.878906 L 4.390625 25.972656 C 4.277344 26.140625 4.269531 26.355469 4.363281 26.53125 C 4.457031 26.707031 4.640625 26.816406 4.839844 26.816406 L 8.828125 26.816406 C 9.003906 26.816406 9.171875 26.730469 9.273438 26.585938 L 15.160156 18.136719 L 21.042969 26.585938 C 21.144531 26.730469 21.3125 26.816406 21.488281 26.816406 L 25.476562 26.816406 C 25.675781 26.816406 25.859375 26.707031 25.953125 26.53125 C 26.050781 26.355469 26.039062 26.140625 25.925781 25.972656 Z M 18.527344 14.878906 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span>  Résultat 1 : 21</span>
                <span id="result2"><span id="svgdeux"><svg class="svgvalid" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span><span id="svgdeuxno"><svg class="svgno" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 4.246094 2.902344 L 26.019531 2.902344 L 26.019531 26.855469 L 4.246094 26.855469 Z M 4.246094 2.902344 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 18.527344 14.878906 L 25.925781 3.785156 C 26.039062 3.617188 26.050781 3.40625 25.953125 3.226562 C 25.859375 3.050781 25.675781 2.941406 25.476562 2.941406 L 21.488281 2.941406 C 21.3125 2.941406 21.144531 3.027344 21.042969 3.175781 L 15.160156 11.625 L 9.273438 3.175781 C 9.171875 3.027344 9.003906 2.941406 8.828125 2.941406 L 4.839844 2.941406 C 4.640625 2.941406 4.457031 3.050781 4.363281 3.226562 C 4.269531 3.402344 4.277344 3.617188 4.390625 3.785156 L 11.792969 14.878906 L 4.390625 25.972656 C 4.277344 26.140625 4.269531 26.355469 4.363281 26.53125 C 4.457031 26.707031 4.640625 26.816406 4.839844 26.816406 L 8.828125 26.816406 C 9.003906 26.816406 9.171875 26.730469 9.273438 26.585938 L 15.160156 18.136719 L 21.042969 26.585938 C 21.144531 26.730469 21.3125 26.816406 21.488281 26.816406 L 25.476562 26.816406 C 25.675781 26.816406 25.859375 26.707031 25.953125 26.53125 C 26.050781 26.355469 26.039062 26.140625 25.925781 25.972656 Z M 18.527344 14.878906 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span>  Résultat 2 : 19</span>
                <span id="result3"><span id="svgtrois"><svg class="svgvalid" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span><span id="svgtroisno"><svg class="svgno" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify" viewBox="0 0 30 30.000001" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 4.246094 2.902344 L 26.019531 2.902344 L 26.019531 26.855469 L 4.246094 26.855469 Z M 4.246094 2.902344 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 18.527344 14.878906 L 25.925781 3.785156 C 26.039062 3.617188 26.050781 3.40625 25.953125 3.226562 C 25.859375 3.050781 25.675781 2.941406 25.476562 2.941406 L 21.488281 2.941406 C 21.3125 2.941406 21.144531 3.027344 21.042969 3.175781 L 15.160156 11.625 L 9.273438 3.175781 C 9.171875 3.027344 9.003906 2.941406 8.828125 2.941406 L 4.839844 2.941406 C 4.640625 2.941406 4.457031 3.050781 4.363281 3.226562 C 4.269531 3.402344 4.277344 3.617188 4.390625 3.785156 L 11.792969 14.878906 L 4.390625 25.972656 C 4.277344 26.140625 4.269531 26.355469 4.363281 26.53125 C 4.457031 26.707031 4.640625 26.816406 4.839844 26.816406 L 8.828125 26.816406 C 9.003906 26.816406 9.171875 26.730469 9.273438 26.585938 L 15.160156 18.136719 L 21.042969 26.585938 C 21.144531 26.730469 21.3125 26.816406 21.488281 26.816406 L 25.476562 26.816406 C 25.675781 26.816406 25.859375 26.707031 25.953125 26.53125 C 26.050781 26.355469 26.039062 26.140625 25.925781 25.972656 Z M 18.527344 14.878906 " fill-opacity="1" fill-rule="nonzero"/></g></svg></span>  Résultat 3 : 3</span>
            </div>
        </div>
    </div>
    <script>
        nombre = 0
        function tuto(){
            if (nombre == 0){
                document.getElementById("textebox").innerHTML = "Cette partie est cruciale car elle contient l'éditeur de code, tu peux saisir et modifier ton code. ";
                document.getElementById("editor-container").style.zIndex = "1000001";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.getElementById("tooltip").style.background = "Transparent";
                document.getElementById("tooltip").style.color = "Transparent";
                document.getElementById("messagebox").style.top = "9%";
        } else if (nombre == 1){
                document.getElementById("textebox").innerHTML = "Ce bouton permet de tester ton code, ce qui est essentiel pour vérifier s'il fonctionne comme prévu.";
                document.getElementById("editor-container").style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.getElementById("runButton").style.zIndex = "1000001";
                document.getElementById("tooltip").style.background = "#2B2B2B";
                document.getElementById("tooltip").style.color = "#fff";
                document.getElementById("messagebox").style.top = "-7%";
        } else if (nombre == 2){
                document.getElementById("textebox").innerHTML = "Cette section explique les fonctions de programmation, idéale pour les débutants ou ceux qui découvrent de nouveaux concepts.";
                document.getElementById("runButton").style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.querySelector('.toggle-button').style.zIndex = "1000001";
                document.getElementById("messagebox").style.top = "-40%";
        } else if (nombre == 3){
                document.getElementById("textebox").innerHTML = "Cette partie affiche les résultats de l'exécution du code, ce qui est utile pour la phase de création et de test de votre code.";
                document.querySelector('.toggle-button').style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.getElementById("output").style.zIndex = "1000001";
                document.getElementById("messagebox").style.top = "1%";
        } else if (nombre == 4){
                document.getElementById("textebox").innerHTML = "Les indicateurs de validation affichent des symboles visuels pour signaler les erreurs ou les succès dans le code, offrant ainsi une indication rapide de sa validité.";
                document.getElementById("output").style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.getElementById("verification").style.zIndex = "1000001";
                document.getElementById("messagebox").style.top = "1%";
        } else if (nombre == 5){
                document.getElementById("textebox").innerHTML = "Cette barre de chargement affiche le temps écoulé, offrant ainsi une indication visuelle du temps passé.";
                document.getElementById("verification").style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.querySelector('.loading-bar').style.zIndex = "1000001";
                document.getElementById("messagebox").style.top = "-39%";
        } else if (nombre == 6){
                document.getElementById("textebox").innerHTML = "Le bouton Valider apparaît lorsque le code est correct et permet de passer à la page suivante où se trouve le score.";
                document.getElementById("valid").style.display = "none";
                document.querySelector('.loading-bar').style.zIndex = "1";
                document.getElementById("messagebox").style.zIndex = "1000001";
                document.getElementById("validButton").style.display = "block";
                document.getElementById("validButton").style.zIndex = "1000001";
                document.getElementById("messagebox").style.top = "32%";
        } else if (nombre == 7){
                window.location.href='starttime1'
            }
        nombre = nombre + 1;

    }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.12/ace.js"></script>
    <script>

        function redirect(){
            document.getElementById("textebox").innerHTML = "Êtes-vous sûr de vouloir quitter ? Vous allez passer à l'épreuve de programmation. Une fois commencée, vous ne pourrez plus revenir en arrière.";
            document.getElementById("valid").style.display = "initial";
            document.getElementById("validButton").style.display = "none";
            document.querySelector('.loading-bar').style.zIndex = "1";
            document.getElementById("messagebox").style.top = "0";
            document.getElementById("valid").innerHTML = "Terminer"
            document.getElementById("valid").style.border = "2px solid #019b33";
        }
        function restart(){
            editor.setValue(decodeURIComponent(`# Demander à l'utilisateur de saisir un nombre
    nombre = int(input("Entrez un nombre : "))
    `), 1);

        }
        document.getElementById("validButton").style.display = "none";

        document.getElementById("svgun").style.display = "none";
        document.getElementById("svgdeux").style.display = "none";
        document.getElementById("svgtrois").style.display = "none";

        document.getElementById("verification").style.color = "#a30000";

        document.getElementById("svgunno").style.display = "initial";
        document.getElementById("svgdeuxno").style.display = "initial";
        document.getElementById("svgtroisno").style.display = "initial";

        var editor = ace.edit("editor");
        editor.setTheme("ace/theme/monokai");
        editor.getSession().setMode("ace/mode/python");

        function openNav() {
            document.getElementById("sidePanel").style.width = "250px";
            document.getElementById("main-content").style.marginRight = "250px";
        }

        function closeNav() {
            document.getElementById("sidePanel").style.width = "0";
            document.getElementById("main-content").style.marginRight= "0";
        }




    </script>
    <script src="menu.js"></script>

    </body>
    </html>
    """
    return html_content


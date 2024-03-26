import os

def generate_page2_html():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, shrink-to-fit=no">
    <meta name="viewport" content="initial-scale=1.25"/>
    <meta name="viewport" content="user-scalable=no"/>
    <title>Ozanam CyberQuest Règles</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="bootstrap4-neon-glow.min.css">
    <link rel='stylesheet' href='//cdn.jsdelivr.net/font-hack/2.020/css/hack.min.css'>
    <link rel="stylesheet" href="main.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
        .fade-in {
            opacity: 0;
            transition: opacity 1s ease;
        }
        .fade-in.visible {
            opacity: 1;
        }
    </style>
</head>
<body class="imgloaded">
<div class="glitch">
    <div style="position: fixed;" class="glitch__img"></div>
    <div style="position: fixed;" class="glitch__img"></div>
    <div style="position: fixed;" class="glitch__img"></div>
    <div style="position: fixed;" class="glitch__img"></div>
    <div style="position: fixed;" class="glitch__img"></div>
</div>
<div class="navbar-dark text-white">
    <div class="container">
        <nav class="navbar px-0 navbar-expand-lg navbar-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a href="home" class="pl-md-0 p-3 text-decoration-none text-light">
                        <h3 class="bold"><span class="color_danger">Ozanam</span> <span class="color_white">CyberQuest</span></h3>
                    </a>
                </div>
                <div class="navbar-nav ml-auto">
                    <a href="home" class="p-3 text-decoration-none text-light bold">Accueil</a>
                    <a href="intro" class="p-3 text-decoration-none text-white bold">Commencer</a>
                </div>
            </div>
        </nav>
    </div>
</div>
<div class="jumbotron bg-transparent mb-0 pt-3 radius-0">
    <div class="container">
        <div class="row">
            <div class="col-xl-12">
                <h1 class="display-1 bold color_white content__title text-center"><span class="color_danger">INSTRUC</span>TIONS<span class="vim-caret">&nbsp;</span></h1>
                <br>
                <div class="row justify-content-center hackerFont">
                    <div class="col-md-10">
                        <h5 class="bold color_white pt-3">Règles générales et instructions</h5>
                        <ul id="instructionsList">
                            <li class="fade-in visible">Le CTF en solo est ouvert à tous les élèves d'Ozanam.</li>
                            <li class="fade-in">Chaque participant doit résoudre autant de défis que possible pour accumuler des points.</li>
                            <li class="fade-in">Les drapeaux sont placés dans les énigmes et doivent être soumis comme preuve de résolution.</li>
                            <li class="fade-in">Le CTF se déroule sur une plateforme en ligne sécurisée, avec des énigmes et des défis informatiques.</li>
                            <li class="fade-in">Toute tentative de piratage ou d'attaque contre le serveur ou les autres participants est strictement interdite.</li>
                            <li class="fade-in">Le CTF a une durée prédéfinie (3 jours), après quoi les participants doivent soumettre leurs réponses.</li>
                            <li class="fade-in">Les participants gagnent des points pour chaque énigme résolue et pour chaque drapeau capturé.</li>
                            <li class="fade-in">Le CTF en solo signifie que chaque participant travaille individuellement, sans aide extérieure.</li>
                            <li class="fade-in">Le respect des règles et de l'éthique en ligne est essentiel.</li>
                            <li class="fade-in">Les participants doivent garantir l'intégrité de leurs solutions. Les réponses doivent être obtenues de manière honnête sans tricher ni utiliser des ressources non autorisées.</li>
                            <li class="fade-in">Des points de pénalité peuvent être imposés en cas de comportement inapproprié, de triche ou de violation des règles.</li>
                            <li class="fade-in">Les participants ne doivent pas partager intentionnellement de réponses, d'indices ou de solutions avec d'autres participants pendant la compétition.</li>
                            <li class="fade-in">Tout plagiat de solutions ou de réponses provenant de sources en ligne ou d'autres participants est strictement interdit.</li>
                            <li class="fade-in">Les participants ont un certain délai après la fin du CTF pour contester les résultats s'ils estiment qu'il y a une erreur dans leur score.</li>
                            <br>
                            <li class="fade-in">Les participants sont encouragés à participer avec un esprit sportif, à s'amuser, à apprendre et à développer leurs compétences en programmation tout en respectant leurs camarades de classe.</li>
                        </ul>
                        <div class="row text-center pt-5">
                            <div class="col-xl-12">
                                <button class="btn btn-outline-danger btn-shadow px-3 my-2 ml-0 ml-sm-1 text-left typewriter" onclick="window.location.href='login';">
                                    <h4>QUE L'AVENTURE COMMENCE!</h4>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script>
    $(document).ready(function(){
        $(window).on('scroll', function() {
            var windowHeight = $(window).height();
            var windowScrollTop = $(window).scrollTop();
            var windowBottom = windowHeight + windowScrollTop - 200; 
            var windowTop = windowScrollTop + 125;
            $("#instructionsList li").each(function() {
                var elementTop = $(this).offset().top;
                if (elementTop < windowBottom && elementTop > windowTop) {
                    $(this).addClass('visible');
                } else {
                    $(this).removeClass('visible');
                }
            });
        });
    });
</script>
</body>
</html>

"""



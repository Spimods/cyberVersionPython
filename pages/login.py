def generate_login_html():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, shrink-to-fit=no">
    <meta name="viewport" content="initial-scale=1.25"/>
    <meta name="viewport" content="user-scalable=no"/>
    <title>Ozanam CyberQuest Login</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    <link rel="stylesheet" href="bootstrap4-neon-glow.min.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel='stylesheet' href='//cdn.jsdelivr.net/font-hack/2.020/css/hack.min.css'>
    <link rel="stylesheet" href="main.css">
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
                        <a href="home" class="pl-md-0 p-3 text-decoration-none text-light">
                            <h3 class="bold"><span class="color_danger">Ozanam</span><span class="color_white">CyberQuest</span></h3>
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
                <form action="loginpage" method="GET">
                <div class="col-xl-8">
                    <div class="container">
                        <div class="stack" style="--stacks: 3;">
                            <span style="--index: 0;">CyberQuest</span>
                            <span style="--index: 1;">CyberQuest</span>
                            <span style="--index: 2;">CyberQuest</span>
                        </div>
                    </div>
                    <p class="text-grey text-spacey hackerFont lead mb-5">
                        Tapez vos identifiants pour conquérir le monde
                    </p>
                    <div class="row hackerFont">
                        <div class="col-md-6">
                                <div class="form-group">
                                    <span id="timer"></span>
                                    <input type="text" required pattern="[a-zA-Z]*" class="form-control" name="nom" id="input" placeholder="Nom">
                                </div>
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-xl-8">
                            <button class="btn btn-outline-danger btn-shadow px-3 my-2 ml-0 ml-sm-1 text-left typewriter" id="btn" type="submit" value="Submit">
                                <h4>Confirmer</h4>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script>
        const dateCible = new Date(2023, 2, 30, 12, 0, 0); // Par exemple, le 30 novembre 2023 à midi

        const timerElement = document.getElementById('timer');

        const element1 = document.getElementById('input');
        const element2 = document.getElementById('btn');

        function mettreAJourTimer() {
            const differenceEnMillisecondes = dateCible - new Date();
            if (differenceEnMillisecondes > 0) {
                const secondes = Math.floor((differenceEnMillisecondes / 1000) % 60);
                const minutes = Math.floor((differenceEnMillisecondes / (1000 * 60)) % 60);
                const heures = Math.floor((differenceEnMillisecondes / (1000 * 60 * 60)) % 24);
                const jours = Math.floor(differenceEnMillisecondes / (1000 * 60 * 60 * 24));
                timerElement.textContent = `${jours}j ${heures}h ${minutes}m ${secondes}s`;

                element1.style.display = 'none';
                element2.style.display = 'none';
                setTimeout(mettreAJourTimer, 1000);
            } else {
                element1.style.display = 'initial';
                element2.style.display = 'initial';
            }
        }
        mettreAJourTimer();
    </script>
</body>

</html>

"""
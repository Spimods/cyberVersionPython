
<h1 align="center">
  <br>
  <a href="http://www.ozanam-cyberquest.fr/"><img src="https://spimods.github.io/falcon-IX/sources/images/no_image.png" alt="CyberQuest" width="200"></a>
  <br>
  Ozanam CyberQuest
  <br>
</h1>

<h4 align="center">Le premier CTF du <a href="https://ozanam-groupe.fr/" target="_blank">lycée Frédéric Ozanam</a>.</h4>


<p align="center">
  <a href="#principales-caractéristiques">Principales caractéristiques</a> •
  <a href="#comment-utiliser">Comment utiliser</a> •
  <a href="#crédits">Crédits</a> •
  <a href="#support">Support</a>
</p>

<h1 align="center">
	<a href="http://www.ozanam-cyberquest.fr/"><img src="https://spimods.github.io/falcon-IX/sources/images/gif/gif.gif" align="center" style="width: 900px; border-radius : 20px;"></a>
</h1>

## Principales caractéristiques 


* Diversité des Défis :
	- Il est essentiel d'offrir une diversité de défis, couvrant différents domaines tels que le python, le SQL, le développement WEB, les dangers des réseaux sociaux, etc.
* Difficulté progressive :
	- Il est important d'offrir des défis de difficulté progressive, en commençant par des niveaux plus simples et en augmentant progressivement la complexité.
* Infrastructure sécurisée
* Système de notation amélioré
* Suivi des progrès
* Accessibilité pour les débutants
* Responsabilité sociale
* Protection de la vie privée
* Éthique des défis

## Comment utiliser
<br>

### Étapes :

* Suivez ces étapes pour configurer et utiliser votre site web local :

	- Installer les bibliothèques : requests, pytz ainsi que urllib3.
    ```bash
    pip install requests
    pip install pytz
    pip install urllib3
    ```
    - Exécuter le fichier server.py, puis rendez-vous sur [http://localhost:8000/home](http://localhost:8000/home)

- Débogage et dépannage :

	- Vérifiez les journaux d'erreurs de votre serveur web en cas de problèmes.


> **Note :**
Si un problème de redirection vers la page de triche survient lors de la validation d'une étape, vous pouvez vous rendre dans le fichier ./pages/js.py à la ligne 16 418 et supprimer le code suivant :
```bash
window.addEventListener("blur", function () {
    var partie = window.location.pathname;
    console.log(partie)
    partie = partie.replace('/', '');
    partie.replace(',', '');
    console.log(partie)
    partie = partie.replace(new RegExp("(%20|_|-)", "g"), "");
    lien = 'triche?etape='+partie
    window.location.href = lien;
});
```


## Crédits

Ce logiciel utilise les paquets open source suivants :

- [ace.js](https://ace.c9.io/)
- [confetti.browser.min.js](https://github.com/catdad/canvas-confetti/)
- [Swinging Lightbulb](https://codepen.io/joebocock/pen/eYZKOjR)


## Support

<a href="https://discord.gg/K5gtCZMwvs" target="_blank"><img src="https://miro.medium.com/v2/resize:fit:800/1*_AsB_hCguMYC-wEG2Bidmw.png" alt="discord" style="height: 55px !important;width: 174px !important;" ></a>




---

> [ozanam-cyberquest.fr](http://www.ozanam-cyberquest.fr/) &nbsp;&middot;&nbsp;
> GitHub [@Spimods](https://github.com/Spimods) &nbsp;&middot;&nbsp;
> GitHub [@Aubin](https://github.com/au-bin)

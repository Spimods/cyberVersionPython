def generate_main_css():
    return """
:root {
--color-text: #fff;
--color-bg: #000;
--color-link: #f9d77e;
--color-link-hover: #fff;
--color-info: #efc453;
--glitch-width: 100vw;
--glitch-height: 100vh;
--gap-horizontal: 10px;
--gap-vertical: 5px;
--time-anim: 4s;
--time-anim-1: 4.5s;
--delay-anim: 3.5s;
--delay-anim-1: 7s;
--blend-mode-1: none;
--blend-mode-2: none;
--blend-mode-3: none;
--blend-mode-4: none;
--blend-mode-5: overlay;
--blend-color-1: transparent;
--blend-color-2: transparent;
--blend-color-3: transparent;
--blend-color-4: transparent;
--blend-color-5: #af4949;
--color: #FAFAFA;

}
body {
background-color: #000309;
}

@font-face {
font-family: "PhelixBoomgartner";
src: url("https://ozanam-cyberquest.fr/fonts/PhelixBoomgartner.otf") format("opentype")
}

@font-face {
font-family: "DoctorGlitch";
src: url("https://ozanam-cyberquest.fr/fonts/Doctor\ Glitch.otf") format("opentype")
}

* {
transition: all 0.3s ease;
letter-spacing: 0.125em;
}
*::-webkit-scrollbar {
width: 12px;
}

*::-webkit-scrollbar-thumb {
background-color: #888;
border-radius: 5px;
}

*::-webkit-scrollbar-track {
background-color: #333;
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
.collapsing {
position: relative;
height: 0;
overflow: hidden;
-webkit-transition-property: height, visibility;
transition-property: height, visibility;
-webkit-transition-duration: 0.25s;
transition-duration: 0.25s;
-webkit-transition-timing-function: ease;
transition-timing-function: ease;
}

#main {
background-image: url(https://ozanam-cyberquest.fr/images/bg.png); 
background-position: right;
background-size: cover;
background-repeat: no-repeat;
background-position-x: 350px;
background-color: #000309;
}

.solved .badge {
background-color: #17b06b94;
border: 1px solid #17b06b;
color: white;
}

.badge {
border: 1px solid #87c4f2;
}

.solved {
background-color: #FFFFFF14;
}

.solvers {
color: #36a2eb;
font-size: 1rem;
}

.solver_num {
color: white;
}

.machine .solvers {
font-size: 1rem!important;
}

.machine_page .solvers {
font-size: 1.25rem!important;
}

.ip {
padding-right: 20px;
}

.category_web {
border-top: 4px solid #ef121b94;
}

.category_reversing {
border-top: 4px solid #17b06b94;
}

.category_steg {
border-top: 4px solid #f9751594;
}

.category_pwning {
border-top: 4px solid #00a09994;
}

.category_machine {
border-top: 4px solid #0f329894;
}

.category_machine a:hover {
text-decoration: none;
color: inherit;
}

.category_misc {
border-top: 4px solid #ffce5694;
}

.category_crypt {
border-top: 4px solid #9966FF94;
}

.hackerFont {
font-family: Hack, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

.color_danger {
color: #ef121b;
}

.color_white {
color: white;
}

.bold {
font-weight: bold;
}

h1,
h2 {
font-family: 'PhelixBoomgartner'!important;
}

button.typewriter {
max-width: 0%;
overflow: hidden;
/* Ensures the content is not revealed until the animation */
white-space: nowrap;

/* Keeps the content on a single line */
/* margin: 0 auto; */
/* Gives that scrolling effect as the typing happens */
letter-spacing: .15em;
/* Adjust as needed */
animation: expand 1s steps(140, end), blink-caret .75s step-end infinite;
animation-delay: 1s;
animation-fill-mode: forwards;
}

.typewriter h4 {
width: 0%;
overflow: hidden;
/* Ensures the content is not revealed until the animation */
white-space: nowrap;
/* Keeps the content on a single line */
/* margin: 0 auto; */
/* Gives that scrolling effect as the typing happens */
letter-spacing: .15em;
/* Adjust as needed */
animation: typing 0.5s steps(140, end), blink-caret .75s step-end infinite;
animation-delay: 1.5s;
animation-fill-mode: forwards;
}

.toggle-yes { border-radius: 6px 0 0 6px !important; }
.toggle-no { border-radius: 0 6px 6px; }

input[type="radio"].toggle { display: none; }
input[type="radio"].toggle:checked + label {
background-color: #714cdf;
color: #fff;
}


/* The typing effect */

@keyframes expand {
0% {
max-width: 0%
}
10% {
max-width: 10%
}
15% {
max-width: 0%
}
20% {
max-width: 12%
}
30% {
max-width: 15%
}
40% {
max-width: 25%
}
50% {
max-width: 30%
}
60% {
max-width: 45%
}
70% {
max-width: 65%
}
80% {
max-width: 85%
}
100% {
max-width: 100%;
}
}


/* The typing effect */

@keyframes typing {
0% {
width: 0%
}
10% {
width: 10%
}
15% {
width: 0%
}
20% {
width: 0%
}
30% {
width: 15%
}
40% {
width: 25%
}
45% {
width: 15%
}
50% {
width: 30%
}
60% {
width: 45%
}
70% {
width: 65%
}
80% {
width: 85%
}
100% {
width: 100%;
}
}

.content__title {
animation-name: glitch-anim-text;
animation-duration: var(--time-anim);
animation-timing-function: linear;
animation-iteration-count: infinite;
animation-delay: calc(var(--delay-anim) + var(--time-anim) * 0.2);
}

.content__title2 {
animation-name: glitch-anim-text-2;
animation-duration: var(--time-anim-1);
animation-timing-function: linear;
animation-iteration-count: infinite;
animation-delay: calc(var(--delay-anim) + var(--time-anim) * 0.35);
}


/* glitch effect */

@keyframes glitch-anim-text {
0% {
/* transform: translate3d(calc(-1 * var(--gap-horizontal)), 0, 0) scale3d(-1, -1, 1); */
-webkit-clip-path: polygon(0 20%, 100% 20%, 100% 21%, 0 21%);
clip-path: polygon(0 20%, 100% 20%, 100% 21%, 0 21%);
}
2% {
-webkit-clip-path: polygon(0 33%, 100% 33%, 100% 33%, 0 33%);
clip-path: polygon(0 33%, 100% 33%, 100% 33%, 0 33%);
}
4% {
-webkit-clip-path: polygon(0 44%, 100% 44%, 100% 44%, 0 44%);
clip-path: polygon(0 44%, 100% 44%, 100% 44%, 0 44%);
}
5% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
}
6% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
}
7% {
-webkit-clip-path: polygon(0 80%, 100% 80%, 100% 80%, 0 80%);
clip-path: polygon(0 80%, 100% 80%, 100% 80%, 0 80%);
}
8% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
}
9% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 80%, 0 80%);
clip-path: polygon(0 70%, 100% 70%, 100% 80%, 0 80%);
}
9.9% {
/* transform: translate3d(calc(-1 * var(--gap-horizontal)), 0, 0) scale3d(-1, -1, 1); */
}
10%,
100% {
transform: translate3d(0, 0, 0) scale3d(1, 1, 1);
-webkit-clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
}
}

@keyframes glitch-anim-text-2 {
0% {
-webkit-clip-path: polygon(0 40%, 100% 20%, 100% 21%, 0 21%);
clip-path: polygon(0 40%, 100% 20%, 100% 21%, 0 21%);
}
2% {
-webkit-clip-path: polygon(0 33%, 100% 33%, 100% 73%, 0 33%);
clip-path: polygon(0 33%, 100% 33%, 100% 73%, 0 33%);
}
4% {
-webkit-clip-path: polygon(0 44%, 100% 82%, 100% 44%, 0 0%);
clip-path: polygon(0 44%, 100% 44%, 100% 82%, 0 0%);
}
5% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
}
6% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
}
7% {
-webkit-clip-path: polygon(0 11%, 100% 80%, 100% 80%, 0 80%);
clip-path: polygon(0 11%, 100% 80%, 100% 80%, 0 80%);
}
8% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
}
9% {
-webkit-clip-path: polygon(0 70%, 20% 70%, 100% 40%, 0 80%);
clip-path: polygon(0 70%, 100% 70%, 20% 40%, 0 80%);
}
9.9% {}
10%,
100% {
transform: translate3d(0, 0, 0) scale3d(1, 1, 1);
-webkit-clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
}
}

.glitch {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
overflow: hidden;
}

.glitch__img {
position: absolute;
top: calc(-1 * var(--gap-vertical));
left: calc(-1 * var(--gap-horizontal));
width: calc(100% + var(--gap-horizontal) * 2);
height: calc(100% + var(--gap-vertical) * 2);
background: url(https://ozanam-cyberquest.fr/images/bg.png);
transform: translate3d(0, 0, 0);
background-blend-mode: var(--blend-mode-1);
background-position: right;
background-size: cover;
background-repeat: no-repeat;
background-position-x: 350px;
}

.glitch__img_login {
background: url(https://ozanam-cyberquest.fr/images/bg--world.png)!important;
}

.glitch__img_404 {
background: url(https://ozanam-cyberquest.fr/images/404.gif)!important;
background-repeat: no-repeat!important;
background-size: contain!important;
background-position: center!important;
}

.glitch__img_leaderboard {
position: fixed!important;
background: url(https://ozanam-cyberquest.fr/images/bg--world.png)!important;
}

.glitch__img_register {
position: fixed!important;
}

.glitch__img:nth-child(n+2) {
opacity: 0;
}

.imgloaded .glitch__img:nth-child(n+2) {
animation-duration: var(--time-anim);
animation-delay: var(--delay-anim-1);
animation-timing-function: linear;
animation-iteration-count: infinite;
}

.imgloaded .glitch__img:nth-child(2) {
background-color: var(--blend-color-2);
background-blend-mode: var(--blend-mode-2);
animation-name: glitch-anim-1;
}

.imgloaded .glitch__img:nth-child(3) {
background-color: var(--blend-color-3);
background-blend-mode: var(--blend-mode-3);
animation-name: glitch-anim-2;
}

.imgloaded .glitch__img:nth-child(4) {
background-color: var(--blend-color-4);
background-blend-mode: var(--blend-mode-4);
animation-name: glitch-anim-3;
}

.imgloaded .glitch__img:nth-child(5) {
background-color: var(--blend-color-5);
background-blend-mode: var(--blend-mode-5);
animation-name: glitch-anim-flash;
}

@keyframes glitch-anim-1 {
0% {
opacity: 1;
transform: translate3d(var(--gap-horizontal), 0, 0);
-webkit-clip-path: polygon(0 2%, 100% 2%, 100% 5%, 0 5%);
clip-path: polygon(0 2%, 100% 2%, 100% 5%, 0 5%);
}
2% {
-webkit-clip-path: polygon(0 15%, 100% 15%, 100% 15%, 0 15%);
clip-path: polygon(0 15%, 100% 15%, 100% 15%, 0 15%);
}
4% {
-webkit-clip-path: polygon(0 10%, 100% 10%, 100% 20%, 0 20%);
clip-path: polygon(0 10%, 100% 10%, 100% 20%, 0 20%);
}
6% {
-webkit-clip-path: polygon(0 1%, 100% 1%, 100% 2%, 0 2%);
clip-path: polygon(0 1%, 100% 1%, 100% 2%, 0 2%);
}
8% {
-webkit-clip-path: polygon(0 33%, 100% 33%, 100% 33%, 0 33%);
clip-path: polygon(0 33%, 100% 33%, 100% 33%, 0 33%);
}
10% {
-webkit-clip-path: polygon(0 44%, 100% 44%, 100% 44%, 0 44%);
clip-path: polygon(0 44%, 100% 44%, 100% 44%, 0 44%);
}
12% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
clip-path: polygon(0 50%, 100% 50%, 100% 20%, 0 20%);
}
14% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
clip-path: polygon(0 70%, 100% 70%, 100% 70%, 0 70%);
}
16% {
-webkit-clip-path: polygon(0 80%, 100% 80%, 100% 80%, 0 80%);
clip-path: polygon(0 80%, 100% 80%, 100% 80%, 0 80%);
}
18% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
clip-path: polygon(0 50%, 100% 50%, 100% 55%, 0 55%);
}
20% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 80%, 0 80%);
clip-path: polygon(0 70%, 100% 70%, 100% 80%, 0 80%);
}
21.9% {
opacity: 1;
transform: translate3d(var(--gap-horizontal), 0, 0);
}
22%,
100% {
opacity: 0;
transform: translate3d(0, 0, 0);
-webkit-clip-path: polygon(0 0, 0 0, 0 0, 0 0);
clip-path: polygon(0 0, 0 0, 0 0, 0 0);
}
}

@keyframes glitch-anim-2 {
0% {
opacity: 1;
transform: translate3d(calc(-1 * var(--gap-horizontal)), 0, 0);
-webkit-clip-path: polygon(0 25%, 100% 25%, 100% 30%, 0 30%);
clip-path: polygon(0 25%, 100% 25%, 100% 30%, 0 30%);
}
3% {
-webkit-clip-path: polygon(0 3%, 100% 3%, 100% 3%, 0 3%);
clip-path: polygon(0 3%, 100% 3%, 100% 3%, 0 3%);
}
5% {
-webkit-clip-path: polygon(0 5%, 100% 5%, 100% 20%, 0 20%);
clip-path: polygon(0 5%, 100% 5%, 100% 20%, 0 20%);
}
7% {
-webkit-clip-path: polygon(0 20%, 100% 20%, 100% 20%, 0 20%);
clip-path: polygon(0 20%, 100% 20%, 100% 20%, 0 20%);
}
9% {
-webkit-clip-path: polygon(0 40%, 100% 40%, 100% 40%, 0 40%);
clip-path: polygon(0 40%, 100% 40%, 100% 40%, 0 40%);
}
11% {
-webkit-clip-path: polygon(0 52%, 100% 52%, 100% 59%, 0 59%);
clip-path: polygon(0 52%, 100% 52%, 100% 59%, 0 59%);
}
13% {
-webkit-clip-path: polygon(0 60%, 100% 60%, 100% 60%, 0 60%);
clip-path: polygon(0 60%, 100% 60%, 100% 60%, 0 60%);
}
15% {
-webkit-clip-path: polygon(0 75%, 100% 75%, 100% 75%, 0 75%);
clip-path: polygon(0 75%, 100% 75%, 100% 75%, 0 75%);
}
17% {
-webkit-clip-path: polygon(0 65%, 100% 65%, 100% 40%, 0 40%);
clip-path: polygon(0 65%, 100% 65%, 100% 40%, 0 40%);
}
19% {
-webkit-clip-path: polygon(0 45%, 100% 45%, 100% 50%, 0 50%);
clip-path: polygon(0 45%, 100% 45%, 100% 50%, 0 50%);
}
20% {
-webkit-clip-path: polygon(0 14%, 100% 14%, 100% 33%, 0 33%);
clip-path: polygon(0 14%, 100% 14%, 100% 33%, 0 33%);
}
21.9% {
opacity: 1;
transform: translate3d(calc(-1 * var(--gap-horizontal)), 0, 0);
}
22%,
100% {
opacity: 0;
transform: translate3d(0, 0, 0);
-webkit-clip-path: polygon(0 0, 0 0, 0 0, 0 0);
clip-path: polygon(0 0, 0 0, 0 0, 0 0);
}
}

@keyframes glitch-anim-3 {
0% {
opacity: 1;
transform: translate3d(0, calc(-1 * var(--gap-vertical)), 0) scale3d(-1, -1, 1);
-webkit-clip-path: polygon(0 1%, 100% 1%, 100% 3%, 0 3%);
clip-path: polygon(0 1%, 100% 1%, 100% 3%, 0 3%);
}
1.5% {
-webkit-clip-path: polygon(0 10%, 100% 10%, 100% 9%, 0 9%);
clip-path: polygon(0 10%, 100% 10%, 100% 9%, 0 9%);
}
2% {
-webkit-clip-path: polygon(0 5%, 100% 5%, 100% 6%, 0 6%);
clip-path: polygon(0 5%, 100% 5%, 100% 6%, 0 6%);
}
2.5% {
-webkit-clip-path: polygon(0 20%, 100% 20%, 100% 20%, 0 20%);
clip-path: polygon(0 20%, 100% 20%, 100% 20%, 0 20%);
}
3% {
-webkit-clip-path: polygon(0 10%, 100% 10%, 100% 10%, 0 10%);
clip-path: polygon(0 10%, 100% 10%, 100% 10%, 0 10%);
}
5% {
-webkit-clip-path: polygon(0 30%, 100% 30%, 100% 25%, 0 25%);
clip-path: polygon(0 30%, 100% 30%, 100% 25%, 0 25%);
}
5.5% {
-webkit-clip-path: polygon(0 15%, 100% 15%, 100% 16%, 0 16%);
clip-path: polygon(0 15%, 100% 15%, 100% 16%, 0 16%);
}
7% {
-webkit-clip-path: polygon(0 40%, 100% 40%, 100% 39%, 0 39%);
clip-path: polygon(0 40%, 100% 40%, 100% 39%, 0 39%);
}
8% {
-webkit-clip-path: polygon(0 20%, 100% 20%, 100% 21%, 0 21%);
clip-path: polygon(0 20%, 100% 20%, 100% 21%, 0 21%);
}
9% {
-webkit-clip-path: polygon(0 60%, 100% 60%, 100% 55%, 0 55%);
clip-path: polygon(0 60%, 100% 60%, 100% 55%, 0 55%);
}
10.5% {
-webkit-clip-path: polygon(0 30%, 100% 30%, 100% 31%, 0 31%);
clip-path: polygon(0 30%, 100% 30%, 100% 31%, 0 31%);
}
11% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 69%, 0 69%);
clip-path: polygon(0 70%, 100% 70%, 100% 69%, 0 69%);
}
13% {
-webkit-clip-path: polygon(0 40%, 100% 40%, 100% 41%, 0 41%);
clip-path: polygon(0 40%, 100% 40%, 100% 41%, 0 41%);
}
14% {
-webkit-clip-path: polygon(0 80%, 100% 80%, 100% 75%, 0 75%);
clip-path: polygon(0 80%, 100% 80%, 100% 75%, 0 75%);
}
14.5% {
-webkit-clip-path: polygon(0 50%, 100% 50%, 100% 51%, 0 51%);
clip-path: polygon(0 50%, 100% 50%, 100% 51%, 0 51%);
}
15% {
-webkit-clip-path: polygon(0 90%, 100% 90%, 100% 90%, 0 90%);
clip-path: polygon(0 90%, 100% 90%, 100% 90%, 0 90%);
}
16% {
-webkit-clip-path: polygon(0 60%, 100% 60%, 100% 60%, 0 60%);
clip-path: polygon(0 60%, 100% 60%, 100% 60%, 0 60%);
}
18% {
-webkit-clip-path: polygon(0 100%, 100% 100%, 100% 99%, 0 99%);
clip-path: polygon(0 100%, 100% 100%, 100% 99%, 0 99%);
}
20% {
-webkit-clip-path: polygon(0 70%, 100% 70%, 100% 71%, 0 71%);
clip-path: polygon(0 70%, 100% 70%, 100% 71%, 0 71%);
}
21.9% {
opacity: 1;
transform: translate3d(0, calc(-1 * var(--gap-vertical)), 0) scale3d(-1, -1, 1);
}
22%,
100% {
opacity: 0;
transform: translate3d(0, 0, 0);
-webkit-clip-path: polygon(0 0, 0 0, 0 0, 0 0);
clip-path: polygon(0 0, 0 0, 0 0, 0 0);
}
}

#preloader {
width: 100%;
height: 100%;
}

#preloader {
background: black;
color: #ddd;
padding: 5px;
box-sizing: border-box;
}

#preloader::-webkit-scrollbar {
display: none;
}

span.ok,
span.fail,
span.fail:before,
span.ok:before {
margin-right: 10px;
}

span.ok {
color: #1EC622;
}

span.fail {
color: red;
}

span.ok:before,
span.fail:before {
content: '[';
}

span.ok:after,
span.fail:after {
margin-left: 10px;
content: ']';
}

#main {
display: none;
}
.container {
color: var(--color);
font-size: 1.5rem;
display: flex;
flex-direction: column;
}

.right {
text-align: right;
width: 100%;
}

.stack {
display: grid;
grid-template-columns: 1fr;
margin-left: -0.7em;
min-width: 1100px !important ;
}

.stack span {
font-weight: bold;
grid-row-start: 1;
grid-column-start: 1;
font-size: 4rem;
--stack-height: calc(100% / var(--stacks) - 1px);
--inverse-index: calc(calc(var(--stacks) - 1) - var(--index));
--clip-top: calc(var(--stack-height) * var(--index));
--clip-bottom: calc(var(--stack-height) * var(--inverse-index));
clip-path: inset(var(--clip-top) 0 var(--clip-bottom) 0);
animation: stack 85ms cubic-bezier(.46,.29,0,1.24) 1 backwards calc(var(--index) * 30ms), glitch 2s ease infinite 2s alternate-reverse;
}

.stack span:nth-child(odd) { --glitch-translate: 8px; }
.stack span:nth-child(even) { --glitch-translate: -8px; }

@keyframes stack {
0% {
opacity: 0;
transform: translateX(-50%);
text-shadow: -2px 3px 0 red, 2px -3px 0 blue;
};
60% {
opacity: 0.5;
transform: translateX(50%);
}
80% {
transform: none;
opacity: 1;
text-shadow: 2px -3px 0 red, -2px 3px 0 blue;
}
100% {
text-shadow: none;
}
}

@keyframes glitch {
0% {
text-shadow: -2px 3px 0 red, 2px -3px 0 blue;
transform: translate(var(--glitch-translate));
}
2% {
text-shadow: 2px -3px 0 red, -2px 3px 0 blue;
}
4%, 100% {text-shadow: none; transform: none; }
}

.box1, .box1end, .box2, .box2end, .box3, .box3end{
height: 200px;
width: 200px;
position: absolute;
border-radius: 1em;
}
.box1{
text-align: center;
left: 10%;
background-image: url(https://ozanam-cyberquest.fr/images/python.png);
background-position: center;
background-size: cover;
filter: grayscale(50%);
cursor: pointer;
}
.box1end {
text-align: center;
left: 10%;
background-image: url(https://ozanam-cyberquest.fr/images/python.png);
background-position: center;
background-size: cover;
filter: grayscale(100%);

}
.box2{
text-align: center;
left: 40%;
background-image: url(https://ozanam-cyberquest.fr/images/progr.png);
background-position: center;
background-size: cover;
filter: grayscale(50%);
cursor: pointer;
}
.box2end {
text-align: center;
left: 40%;
background-image: url(https://ozanam-cyberquest.fr/images/progr.png);
background-position: center;
background-size: cover;
filter: grayscale(100%);

}
.box3{
text-align: center;
left: 70%;
background-image: url(https://ozanam-cyberquest.fr/images/question.png);
background-position: center;
background-size: cover;
filter: grayscale(50%);
cursor: pointer;
}
.box3end {
text-align: center;
left: 70%;
background-image: url(https://ozanam-cyberquest.fr/images/question.png);
background-position: center;
background-size: cover;
filter: grayscale(100%);

}
.text{
top: 42%;
position: relative; 
color: white;
}
.box1:hover, .box2:hover, .box3:hover{
scale: 1.2;
filter: grayscale(10%);

}
@media (min-width: 1200px){
.col-xl-8 {
max-width: 100% !important;
}
}
    """




def generate_bootstrap4_neon_glow_css():
    return """
:root {
  --blue: #007bff;
  --indigo: #6610f2;
  --purple: #6f42c1;
  --pink: #e83e8c;
  --red: #dc3545;
  --orange: #fd7e14;
  --yellow: #ffc107;
  --green: #28a745;
  --teal: #20c997;
  --cyan: #17a2b8;
  --white: #fff;
  --gray: #1d1e2f;
  --gray-dark: #11111d;
  --primary: #714cdf;
  --secondary: #16a4de;
  --success: #17b06b;
  --info: #2983fe;
  --warning: #f97515;
  --danger: #ff3c5c;
  --light: #dbebfb;
  --dark: #32334a;
  --breakpoint-xs: 0;
  --breakpoint-sm: 576px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 992px;
  --breakpoint-xl: 1200px;
  --font-family-sans-serif: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

*,
*::before,
*::after {
  -webkit-box-sizing: border-box;
          box-sizing: border-box; }

html {
  font-family: sans-serif;
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0); }

article, aside, figcaption, figure, footer, header, hgroup, main, nav, section {
  display: block; }

body {
  margin: 0;
  font-family: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #e4e2ff;
  text-align: left;
  background-color: #0c0d16; }

[tabindex="-1"]:focus {
  outline: 0 !important; }

hr {
  -webkit-box-sizing: content-box;
          box-sizing: content-box;
  height: 0;
  overflow: visible; }

h1, h2, h3, h4, h5, h6 {
  margin-top: 0;
  margin-bottom: 0.5rem; }

p {
  margin-top: 0;
  margin-bottom: 1rem; }

abbr[title],
abbr[data-original-title] {
  text-decoration: underline;
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
  cursor: help;
  border-bottom: 0;
  -webkit-text-decoration-skip-ink: none;
          text-decoration-skip-ink: none; }

address {
  margin-bottom: 1rem;
  font-style: normal;
  line-height: inherit; }

ol,
ul,
dl {
  margin-top: 0;
  margin-bottom: 1rem; }

ol ol,
ul ul,
ol ul,
ul ol {
  margin-bottom: 0; }

dt {
  font-weight: 700; }

dd {
  margin-bottom: .5rem;
  margin-left: 0; }

blockquote {
  margin: 0 0 1rem; }

b,
strong {
  font-weight: bolder; }

small {
  font-size: 80%; }

sub,
sup {
  position: relative;
  font-size: 75%;
  line-height: 0;
  vertical-align: baseline; }

sub {
  bottom: -.25em; }

sup {
  top: -.5em; }

a {
  color: #714cdf;
  text-decoration: none;
  background-color: transparent; }
  a:hover {
    color: #4922bd;
    text-decoration: underline; }

a:not([href]):not([tabindex]) {
  color: inherit;
  text-decoration: none; }
  a:not([href]):not([tabindex]):hover, a:not([href]):not([tabindex]):focus {
    color: inherit;
    text-decoration: none; }
  a:not([href]):not([tabindex]):focus {
    outline: 0; }

pre,
code,
kbd,
samp {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 1em; }

pre {
  margin-top: 0;
  margin-bottom: 1rem;
  overflow: auto; }

figure {
  margin: 0 0 1rem; }

img {
  vertical-align: middle;
  border-style: none; }

svg {
  overflow: hidden;
  vertical-align: middle; }

table {
  border-collapse: collapse; }

caption {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  color: #81839a;
  text-align: left;
  caption-side: bottom; }

th {
  text-align: inherit; }

label {
  display: inline-block;
  margin-bottom: 0.5rem; }

button {
  border-radius: 0; }

button:focus {
  outline: 1px dotted;
  outline: 5px auto -webkit-focus-ring-color; }

input,
button,
select,
optgroup,
textarea {
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit; }

button,
input {
  overflow: visible; }

button,
select {
  text-transform: none; }

select {
  word-wrap: normal; }

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button; }

button:not(:disabled),
[type="button"]:not(:disabled),
[type="reset"]:not(:disabled),
[type="submit"]:not(:disabled) {
  cursor: pointer; }

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  padding: 0;
  border-style: none; }

input[type="radio"],
input[type="checkbox"] {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  padding: 0; }

input[type="date"],
input[type="time"],
input[type="datetime-local"],
input[type="month"] {
  -webkit-appearance: listbox; }

textarea {
  overflow: auto;
  resize: vertical; }

fieldset {
  min-width: 0;
  padding: 0;
  margin: 0;
  border: 0; }

legend {
  display: block;
  width: 100%;
  max-width: 100%;
  padding: 0;
  margin-bottom: .5rem;
  font-size: 1.5rem;
  line-height: inherit;
  color: inherit;
  white-space: normal; }

progress {
  vertical-align: baseline; }

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto; }

[type="search"] {
  outline-offset: -2px;
  -webkit-appearance: none; }

[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none; }

::-webkit-file-upload-button {
  font: inherit;
  -webkit-appearance: button; }

output {
  display: inline-block; }

summary {
  display: list-item;
  cursor: pointer; }

template {
  display: none; }

[hidden] {
  display: none !important; }

h1, h2, h3, h4, h5, h6,
.h1, .h2, .h3, .h4, .h5, .h6 {
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2; }

h1, .h1 {
  font-size: 2.5rem; }

h2, .h2 {
  font-size: 2rem; }

h3, .h3 {
  font-size: 1.75rem; }

h4, .h4 {
  font-size: 1.5rem; }

h5, .h5 {
  font-size: 1.25rem; }

h6, .h6 {
  font-size: 1rem; }

.lead {
  font-size: 1.25rem;
  font-weight: 300; }

.display-1 {
  font-size: 4.5rem;
  font-weight: 300;
  line-height: 1.2; }

.display-2 {
  font-size: 3.5rem;
  font-weight: 300;
  line-height: 1.2; }

.display-3 {
  font-size: 2.5rem;
  font-weight: 300;
  line-height: 1.2; }

.display-4 {
  font-size: 2rem;
  font-weight: 300;
  line-height: 1.2; }

hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1); }

small,
.small {
  font-size: 80%;
  font-weight: 400; }

mark,
.mark {
  padding: 0.2em;
  background-color: #fcf8e3; }

.list-unstyled {
  padding-left: 0;
  list-style: none; }

.list-inline {
  padding-left: 0;
  list-style: none; }

.list-inline-item {
  display: inline-block; }
  .list-inline-item:not(:last-child) {
    margin-right: 0.5rem; }

.initialism {
  font-size: 90%;
  text-transform: uppercase; }

.blockquote {
  margin-bottom: 1rem;
  font-size: 1.25rem; }

.blockquote-footer {
  display: block;
  font-size: 80%;
  color: #81839a; }
  .blockquote-footer::before {
    content: "\2014\00A0"; }

.img-fluid {
  max-width: 100%;
  height: auto; }

.img-thumbnail {
  padding: 0.25rem;
  background-color: #0c0d16;
  border: 1px solid #151623;
  border-radius: 6px;
  max-width: 100%;
  height: auto; }

.figure {
  display: inline-block; }

.figure-img {
  margin-bottom: 0.5rem;
  line-height: 1; }

.figure-caption {
  font-size: 90%;
  color: #1d1e2f; }

code {
  font-size: 87.5%;
  color: #2983fe;
  word-break: break-word; }
  a > code {
    color: inherit; }

kbd {
  padding: 0.2rem 0.4rem;
  font-size: 87.5%;
  color: #32334a;
  background-color: #0a0b14;
  border-radius: 0.2rem; }
  kbd kbd {
    padding: 0;
    font-size: 100%;
    font-weight: 700; }

pre {
  display: block;
  font-size: 87.5%;
  color: #0a0b14; }
  pre code {
    font-size: inherit;
    color: inherit;
    word-break: normal; }

.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll; }

.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto; }
  @media (min-width: 576px) {
    .container {
      max-width: 540px; } }
  @media (min-width: 768px) {
    .container {
      max-width: 720px; } }
  @media (min-width: 992px) {
    .container {
      max-width: 960px; } }
  @media (min-width: 1200px) {
    .container {
      max-width: 1140px; } }

.container-fluid {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto; }

.row {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px; }

.no-gutters {
  margin-right: 0;
  margin-left: 0; }
  .no-gutters > .col,
  .no-gutters > [class*="col-"] {
    padding-right: 0;
    padding-left: 0; }

.col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col,
.col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm,
.col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md,
.col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg,
.col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl,
.col-xl-auto {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px; }

.col {
  -webkit-flex-basis: 0;
      -ms-flex-preferred-size: 0;
          flex-basis: 0;
  -webkit-box-flex: 1;
  -webkit-flex-grow: 1;
      -ms-flex-positive: 1;
          flex-grow: 1;
  max-width: 100%; }

.col-auto {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 auto;
      -ms-flex: 0 0 auto;
          flex: 0 0 auto;
  width: auto;
  max-width: 100%; }

.col-1 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 8.33333%;
      -ms-flex: 0 0 8.33333%;
          flex: 0 0 8.33333%;
  max-width: 8.33333%; }

.col-2 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 16.66667%;
      -ms-flex: 0 0 16.66667%;
          flex: 0 0 16.66667%;
  max-width: 16.66667%; }

.col-3 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 25%;
      -ms-flex: 0 0 25%;
          flex: 0 0 25%;
  max-width: 25%; }

.col-4 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 33.33333%;
      -ms-flex: 0 0 33.33333%;
          flex: 0 0 33.33333%;
  max-width: 33.33333%; }

.col-5 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 41.66667%;
      -ms-flex: 0 0 41.66667%;
          flex: 0 0 41.66667%;
  max-width: 41.66667%; }

.col-6 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 50%;
      -ms-flex: 0 0 50%;
          flex: 0 0 50%;
  max-width: 50%; }

.col-7 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 58.33333%;
      -ms-flex: 0 0 58.33333%;
          flex: 0 0 58.33333%;
  max-width: 58.33333%; }

.col-8 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 66.66667%;
      -ms-flex: 0 0 66.66667%;
          flex: 0 0 66.66667%;
  max-width: 66.66667%; }

.col-9 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 75%;
      -ms-flex: 0 0 75%;
          flex: 0 0 75%;
  max-width: 75%; }

.col-10 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 83.33333%;
      -ms-flex: 0 0 83.33333%;
          flex: 0 0 83.33333%;
  max-width: 83.33333%; }

.col-11 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 91.66667%;
      -ms-flex: 0 0 91.66667%;
          flex: 0 0 91.66667%;
  max-width: 91.66667%; }

.col-12 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 100%;
      -ms-flex: 0 0 100%;
          flex: 0 0 100%;
  max-width: 100%; }

.order-first {
  -webkit-box-ordinal-group: 0;
  -webkit-order: -1;
      -ms-flex-order: -1;
          order: -1; }

.order-last {
  -webkit-box-ordinal-group: 14;
  -webkit-order: 13;
      -ms-flex-order: 13;
          order: 13; }

.order-0 {
  -webkit-box-ordinal-group: 1;
  -webkit-order: 0;
      -ms-flex-order: 0;
          order: 0; }

.order-1 {
  -webkit-box-ordinal-group: 2;
  -webkit-order: 1;
      -ms-flex-order: 1;
          order: 1; }

.order-2 {
  -webkit-box-ordinal-group: 3;
  -webkit-order: 2;
      -ms-flex-order: 2;
          order: 2; }

.order-3 {
  -webkit-box-ordinal-group: 4;
  -webkit-order: 3;
      -ms-flex-order: 3;
          order: 3; }

.order-4 {
  -webkit-box-ordinal-group: 5;
  -webkit-order: 4;
      -ms-flex-order: 4;
          order: 4; }

.order-5 {
  -webkit-box-ordinal-group: 6;
  -webkit-order: 5;
      -ms-flex-order: 5;
          order: 5; }

.order-6 {
  -webkit-box-ordinal-group: 7;
  -webkit-order: 6;
      -ms-flex-order: 6;
          order: 6; }

.order-7 {
  -webkit-box-ordinal-group: 8;
  -webkit-order: 7;
      -ms-flex-order: 7;
          order: 7; }

.order-8 {
  -webkit-box-ordinal-group: 9;
  -webkit-order: 8;
      -ms-flex-order: 8;
          order: 8; }

.order-9 {
  -webkit-box-ordinal-group: 10;
  -webkit-order: 9;
      -ms-flex-order: 9;
          order: 9; }

.order-10 {
  -webkit-box-ordinal-group: 11;
  -webkit-order: 10;
      -ms-flex-order: 10;
          order: 10; }

.order-11 {
  -webkit-box-ordinal-group: 12;
  -webkit-order: 11;
      -ms-flex-order: 11;
          order: 11; }

.order-12 {
  -webkit-box-ordinal-group: 13;
  -webkit-order: 12;
      -ms-flex-order: 12;
          order: 12; }

.offset-1 {
  margin-left: 8.33333%; }

.offset-2 {
  margin-left: 16.66667%; }

.offset-3 {
  margin-left: 25%; }

.offset-4 {
  margin-left: 33.33333%; }

.offset-5 {
  margin-left: 41.66667%; }

.offset-6 {
  margin-left: 50%; }

.offset-7 {
  margin-left: 58.33333%; }

.offset-8 {
  margin-left: 66.66667%; }

.offset-9 {
  margin-left: 75%; }

.offset-10 {
  margin-left: 83.33333%; }

.offset-11 {
  margin-left: 91.66667%; }

@media (min-width: 576px) {
  .col-sm {
    -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
            flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    max-width: 100%; }
  .col-sm-auto {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
            flex: 0 0 auto;
    width: auto;
    max-width: 100%; }
  .col-sm-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
            flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-sm-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
            flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-sm-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
            flex: 0 0 25%;
    max-width: 25%; }
  .col-sm-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
            flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-sm-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
            flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-sm-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
            flex: 0 0 50%;
    max-width: 50%; }
  .col-sm-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
            flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-sm-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
            flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-sm-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
            flex: 0 0 75%;
    max-width: 75%; }
  .col-sm-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
            flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-sm-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
            flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-sm-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
            flex: 0 0 100%;
    max-width: 100%; }
  .order-sm-first {
    -webkit-box-ordinal-group: 0;
    -webkit-order: -1;
        -ms-flex-order: -1;
            order: -1; }
  .order-sm-last {
    -webkit-box-ordinal-group: 14;
    -webkit-order: 13;
        -ms-flex-order: 13;
            order: 13; }
  .order-sm-0 {
    -webkit-box-ordinal-group: 1;
    -webkit-order: 0;
        -ms-flex-order: 0;
            order: 0; }
  .order-sm-1 {
    -webkit-box-ordinal-group: 2;
    -webkit-order: 1;
        -ms-flex-order: 1;
            order: 1; }
  .order-sm-2 {
    -webkit-box-ordinal-group: 3;
    -webkit-order: 2;
        -ms-flex-order: 2;
            order: 2; }
  .order-sm-3 {
    -webkit-box-ordinal-group: 4;
    -webkit-order: 3;
        -ms-flex-order: 3;
            order: 3; }
  .order-sm-4 {
    -webkit-box-ordinal-group: 5;
    -webkit-order: 4;
        -ms-flex-order: 4;
            order: 4; }
  .order-sm-5 {
    -webkit-box-ordinal-group: 6;
    -webkit-order: 5;
        -ms-flex-order: 5;
            order: 5; }
  .order-sm-6 {
    -webkit-box-ordinal-group: 7;
    -webkit-order: 6;
        -ms-flex-order: 6;
            order: 6; }
  .order-sm-7 {
    -webkit-box-ordinal-group: 8;
    -webkit-order: 7;
        -ms-flex-order: 7;
            order: 7; }
  .order-sm-8 {
    -webkit-box-ordinal-group: 9;
    -webkit-order: 8;
        -ms-flex-order: 8;
            order: 8; }
  .order-sm-9 {
    -webkit-box-ordinal-group: 10;
    -webkit-order: 9;
        -ms-flex-order: 9;
            order: 9; }
  .order-sm-10 {
    -webkit-box-ordinal-group: 11;
    -webkit-order: 10;
        -ms-flex-order: 10;
            order: 10; }
  .order-sm-11 {
    -webkit-box-ordinal-group: 12;
    -webkit-order: 11;
        -ms-flex-order: 11;
            order: 11; }
  .order-sm-12 {
    -webkit-box-ordinal-group: 13;
    -webkit-order: 12;
        -ms-flex-order: 12;
            order: 12; }
  .offset-sm-0 {
    margin-left: 0; }
  .offset-sm-1 {
    margin-left: 8.33333%; }
  .offset-sm-2 {
    margin-left: 16.66667%; }
  .offset-sm-3 {
    margin-left: 25%; }
  .offset-sm-4 {
    margin-left: 33.33333%; }
  .offset-sm-5 {
    margin-left: 41.66667%; }
  .offset-sm-6 {
    margin-left: 50%; }
  .offset-sm-7 {
    margin-left: 58.33333%; }
  .offset-sm-8 {
    margin-left: 66.66667%; }
  .offset-sm-9 {
    margin-left: 75%; }
  .offset-sm-10 {
    margin-left: 83.33333%; }
  .offset-sm-11 {
    margin-left: 91.66667%; } }

@media (min-width: 768px) {
  .col-md {
    -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
            flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    max-width: 100%; }
  .col-md-auto {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
            flex: 0 0 auto;
    width: auto;
    max-width: 100%; }
  .col-md-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
            flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-md-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
            flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-md-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
            flex: 0 0 25%;
    max-width: 25%; }
  .col-md-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
            flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-md-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
            flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-md-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
            flex: 0 0 50%;
    max-width: 50%; }
  .col-md-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
            flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-md-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
            flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-md-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
            flex: 0 0 75%;
    max-width: 75%; }
  .col-md-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
            flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-md-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
            flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-md-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
            flex: 0 0 100%;
    max-width: 100%; }
  .order-md-first {
    -webkit-box-ordinal-group: 0;
    -webkit-order: -1;
        -ms-flex-order: -1;
            order: -1; }
  .order-md-last {
    -webkit-box-ordinal-group: 14;
    -webkit-order: 13;
        -ms-flex-order: 13;
            order: 13; }
  .order-md-0 {
    -webkit-box-ordinal-group: 1;
    -webkit-order: 0;
        -ms-flex-order: 0;
            order: 0; }
  .order-md-1 {
    -webkit-box-ordinal-group: 2;
    -webkit-order: 1;
        -ms-flex-order: 1;
            order: 1; }
  .order-md-2 {
    -webkit-box-ordinal-group: 3;
    -webkit-order: 2;
        -ms-flex-order: 2;
            order: 2; }
  .order-md-3 {
    -webkit-box-ordinal-group: 4;
    -webkit-order: 3;
        -ms-flex-order: 3;
            order: 3; }
  .order-md-4 {
    -webkit-box-ordinal-group: 5;
    -webkit-order: 4;
        -ms-flex-order: 4;
            order: 4; }
  .order-md-5 {
    -webkit-box-ordinal-group: 6;
    -webkit-order: 5;
        -ms-flex-order: 5;
            order: 5; }
  .order-md-6 {
    -webkit-box-ordinal-group: 7;
    -webkit-order: 6;
        -ms-flex-order: 6;
            order: 6; }
  .order-md-7 {
    -webkit-box-ordinal-group: 8;
    -webkit-order: 7;
        -ms-flex-order: 7;
            order: 7; }
  .order-md-8 {
    -webkit-box-ordinal-group: 9;
    -webkit-order: 8;
        -ms-flex-order: 8;
            order: 8; }
  .order-md-9 {
    -webkit-box-ordinal-group: 10;
    -webkit-order: 9;
        -ms-flex-order: 9;
            order: 9; }
  .order-md-10 {
    -webkit-box-ordinal-group: 11;
    -webkit-order: 10;
        -ms-flex-order: 10;
            order: 10; }
  .order-md-11 {
    -webkit-box-ordinal-group: 12;
    -webkit-order: 11;
        -ms-flex-order: 11;
            order: 11; }
  .order-md-12 {
    -webkit-box-ordinal-group: 13;
    -webkit-order: 12;
        -ms-flex-order: 12;
            order: 12; }
  .offset-md-0 {
    margin-left: 0; }
  .offset-md-1 {
    margin-left: 8.33333%; }
  .offset-md-2 {
    margin-left: 16.66667%; }
  .offset-md-3 {
    margin-left: 25%; }
  .offset-md-4 {
    margin-left: 33.33333%; }
  .offset-md-5 {
    margin-left: 41.66667%; }
  .offset-md-6 {
    margin-left: 50%; }
  .offset-md-7 {
    margin-left: 58.33333%; }
  .offset-md-8 {
    margin-left: 66.66667%; }
  .offset-md-9 {
    margin-left: 75%; }
  .offset-md-10 {
    margin-left: 83.33333%; }
  .offset-md-11 {
    margin-left: 91.66667%; } }

@media (min-width: 992px) {
  .col-lg {
    -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
            flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    max-width: 100%; }
  .col-lg-auto {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
            flex: 0 0 auto;
    width: auto;
    max-width: 100%; }
  .col-lg-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
            flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-lg-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
            flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-lg-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
            flex: 0 0 25%;
    max-width: 25%; }
  .col-lg-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
            flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-lg-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
            flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-lg-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
            flex: 0 0 50%;
    max-width: 50%; }
  .col-lg-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
            flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-lg-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
            flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-lg-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
            flex: 0 0 75%;
    max-width: 75%; }
  .col-lg-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
            flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-lg-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
            flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-lg-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
            flex: 0 0 100%;
    max-width: 100%; }
  .order-lg-first {
    -webkit-box-ordinal-group: 0;
    -webkit-order: -1;
        -ms-flex-order: -1;
            order: -1; }
  .order-lg-last {
    -webkit-box-ordinal-group: 14;
    -webkit-order: 13;
        -ms-flex-order: 13;
            order: 13; }
  .order-lg-0 {
    -webkit-box-ordinal-group: 1;
    -webkit-order: 0;
        -ms-flex-order: 0;
            order: 0; }
  .order-lg-1 {
    -webkit-box-ordinal-group: 2;
    -webkit-order: 1;
        -ms-flex-order: 1;
            order: 1; }
  .order-lg-2 {
    -webkit-box-ordinal-group: 3;
    -webkit-order: 2;
        -ms-flex-order: 2;
            order: 2; }
  .order-lg-3 {
    -webkit-box-ordinal-group: 4;
    -webkit-order: 3;
        -ms-flex-order: 3;
            order: 3; }
  .order-lg-4 {
    -webkit-box-ordinal-group: 5;
    -webkit-order: 4;
        -ms-flex-order: 4;
            order: 4; }
  .order-lg-5 {
    -webkit-box-ordinal-group: 6;
    -webkit-order: 5;
        -ms-flex-order: 5;
            order: 5; }
  .order-lg-6 {
    -webkit-box-ordinal-group: 7;
    -webkit-order: 6;
        -ms-flex-order: 6;
            order: 6; }
  .order-lg-7 {
    -webkit-box-ordinal-group: 8;
    -webkit-order: 7;
        -ms-flex-order: 7;
            order: 7; }
  .order-lg-8 {
    -webkit-box-ordinal-group: 9;
    -webkit-order: 8;
        -ms-flex-order: 8;
            order: 8; }
  .order-lg-9 {
    -webkit-box-ordinal-group: 10;
    -webkit-order: 9;
        -ms-flex-order: 9;
            order: 9; }
  .order-lg-10 {
    -webkit-box-ordinal-group: 11;
    -webkit-order: 10;
        -ms-flex-order: 10;
            order: 10; }
  .order-lg-11 {
    -webkit-box-ordinal-group: 12;
    -webkit-order: 11;
        -ms-flex-order: 11;
            order: 11; }
  .order-lg-12 {
    -webkit-box-ordinal-group: 13;
    -webkit-order: 12;
        -ms-flex-order: 12;
            order: 12; }
  .offset-lg-0 {
    margin-left: 0; }
  .offset-lg-1 {
    margin-left: 8.33333%; }
  .offset-lg-2 {
    margin-left: 16.66667%; }
  .offset-lg-3 {
    margin-left: 25%; }
  .offset-lg-4 {
    margin-left: 33.33333%; }
  .offset-lg-5 {
    margin-left: 41.66667%; }
  .offset-lg-6 {
    margin-left: 50%; }
  .offset-lg-7 {
    margin-left: 58.33333%; }
  .offset-lg-8 {
    margin-left: 66.66667%; }
  .offset-lg-9 {
    margin-left: 75%; }
  .offset-lg-10 {
    margin-left: 83.33333%; }
  .offset-lg-11 {
    margin-left: 91.66667%; } }

@media (min-width: 1200px) {
  .col-xl {
    -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
            flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
            flex-grow: 1;
    max-width: 100%; }
  .col-xl-auto {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
            flex: 0 0 auto;
    width: auto;
    max-width: 100%; }
  .col-xl-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
            flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-xl-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
            flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-xl-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
            flex: 0 0 25%;
    max-width: 25%; }
  .col-xl-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
            flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-xl-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
            flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-xl-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
            flex: 0 0 50%;
    max-width: 50%; }
  .col-xl-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
            flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-xl-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
            flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-xl-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
            flex: 0 0 75%;
    max-width: 75%; }
  .col-xl-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
            flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-xl-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
            flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-xl-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
            flex: 0 0 100%;
    max-width: 100%; }
  .order-xl-first {
    -webkit-box-ordinal-group: 0;
    -webkit-order: -1;
        -ms-flex-order: -1;
            order: -1; }
  .order-xl-last {
    -webkit-box-ordinal-group: 14;
    -webkit-order: 13;
        -ms-flex-order: 13;
            order: 13; }
  .order-xl-0 {
    -webkit-box-ordinal-group: 1;
    -webkit-order: 0;
        -ms-flex-order: 0;
            order: 0; }
  .order-xl-1 {
    -webkit-box-ordinal-group: 2;
    -webkit-order: 1;
        -ms-flex-order: 1;
            order: 1; }
  .order-xl-2 {
    -webkit-box-ordinal-group: 3;
    -webkit-order: 2;
        -ms-flex-order: 2;
            order: 2; }
  .order-xl-3 {
    -webkit-box-ordinal-group: 4;
    -webkit-order: 3;
        -ms-flex-order: 3;
            order: 3; }
  .order-xl-4 {
    -webkit-box-ordinal-group: 5;
    -webkit-order: 4;
        -ms-flex-order: 4;
            order: 4; }
  .order-xl-5 {
    -webkit-box-ordinal-group: 6;
    -webkit-order: 5;
        -ms-flex-order: 5;
            order: 5; }
  .order-xl-6 {
    -webkit-box-ordinal-group: 7;
    -webkit-order: 6;
        -ms-flex-order: 6;
            order: 6; }
  .order-xl-7 {
    -webkit-box-ordinal-group: 8;
    -webkit-order: 7;
        -ms-flex-order: 7;
            order: 7; }
  .order-xl-8 {
    -webkit-box-ordinal-group: 9;
    -webkit-order: 8;
        -ms-flex-order: 8;
            order: 8; }
  .order-xl-9 {
    -webkit-box-ordinal-group: 10;
    -webkit-order: 9;
        -ms-flex-order: 9;
            order: 9; }
  .order-xl-10 {
    -webkit-box-ordinal-group: 11;
    -webkit-order: 10;
        -ms-flex-order: 10;
            order: 10; }
  .order-xl-11 {
    -webkit-box-ordinal-group: 12;
    -webkit-order: 11;
        -ms-flex-order: 11;
            order: 11; }
  .order-xl-12 {
    -webkit-box-ordinal-group: 13;
    -webkit-order: 12;
        -ms-flex-order: 12;
            order: 12; }
  .offset-xl-0 {
    margin-left: 0; }
  .offset-xl-1 {
    margin-left: 8.33333%; }
  .offset-xl-2 {
    margin-left: 16.66667%; }
  .offset-xl-3 {
    margin-left: 25%; }
  .offset-xl-4 {
    margin-left: 33.33333%; }
  .offset-xl-5 {
    margin-left: 41.66667%; }
  .offset-xl-6 {
    margin-left: 50%; }
  .offset-xl-7 {
    margin-left: 58.33333%; }
  .offset-xl-8 {
    margin-left: 66.66667%; }
  .offset-xl-9 {
    margin-left: 75%; }
  .offset-xl-10 {
    margin-left: 83.33333%; }
  .offset-xl-11 {
    margin-left: 91.66667%; } }

.table {
  width: 100%;
  margin-bottom: 1rem;
  color: #e4e2ff; }
  .table th,
  .table td {
    padding: 0.75rem;
    vertical-align: top;
    border-top: 1px solid #28293e; }
  .table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #28293e; }
  .table tbody + tbody {
    border-top: 2px solid #28293e; }

.table-sm th,
.table-sm td {
  padding: 0.3rem; }

.table-bordered {
  border: 1px solid #28293e; }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #28293e; }
  .table-bordered thead th,
  .table-bordered thead td {
    border-bottom-width: 2px; }

.table-borderless th,
.table-borderless td,
.table-borderless thead th,
.table-borderless tbody + tbody {
  border: 0; }

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05); }

.table-hover tbody tr:hover {
  color: #e4e2ff;
  background-color: rgba(0, 0, 0, 0.075); }

.table-primary,
.table-primary > th,
.table-primary > td {
  background-color: #d7cdf6; }

.table-primary th,
.table-primary td,
.table-primary thead th,
.table-primary tbody + tbody {
  border-color: #b5a2ee; }

.table-hover .table-primary:hover {
  background-color: #c6b7f2; }
  .table-hover .table-primary:hover > td,
  .table-hover .table-primary:hover > th {
    background-color: #c6b7f2; }

.table-secondary,
.table-secondary > th,
.table-secondary > td {
  background-color: #bee6f6; }

.table-secondary th,
.table-secondary td,
.table-secondary thead th,
.table-secondary tbody + tbody {
  border-color: #86d0ee; }

.table-hover .table-secondary:hover {
  background-color: #a8ddf3; }
  .table-hover .table-secondary:hover > td,
  .table-hover .table-secondary:hover > th {
    background-color: #a8ddf3; }

.table-success,
.table-success > th,
.table-success > td {
  background-color: #bee9d6; }

.table-success th,
.table-success td,
.table-success thead th,
.table-success tbody + tbody {
  border-color: #86d6b2; }

.table-hover .table-success:hover {
  background-color: #abe3ca; }
  .table-hover .table-success:hover > td,
  .table-hover .table-success:hover > th {
    background-color: #abe3ca; }

.table-info,
.table-info > th,
.table-info > td {
  background-color: #c3dcff; }

.table-info th,
.table-info td,
.table-info thead th,
.table-info tbody + tbody {
  border-color: #90bffe; }

.table-hover .table-info:hover {
  background-color: #aacdff; }
  .table-hover .table-info:hover > td,
  .table-hover .table-info:hover > th {
    background-color: #aacdff; }

.table-warning,
.table-warning > th,
.table-warning > td {
  background-color: #fdd8bd; }

.table-warning th,
.table-warning td,
.table-warning thead th,
.table-warning tbody + tbody {
  border-color: #fcb785; }

.table-hover .table-warning:hover {
  background-color: #fcc9a4; }
  .table-hover .table-warning:hover > td,
  .table-hover .table-warning:hover > th {
    background-color: #fcc9a4; }

.table-danger,
.table-danger > th,
.table-danger > td {
  background-color: #ffc8d1; }

.table-danger th,
.table-danger td,
.table-danger thead th,
.table-danger tbody + tbody {
  border-color: #ff9aaa; }

.table-hover .table-danger:hover {
  background-color: #ffafbc; }
  .table-hover .table-danger:hover > td,
  .table-hover .table-danger:hover > th {
    background-color: #ffafbc; }

.table-light,
.table-light > th,
.table-light > td {
  background-color: #f5f9fe; }

.table-light th,
.table-light td,
.table-light thead th,
.table-light tbody + tbody {
  border-color: #ecf5fd; }

.table-hover .table-light:hover {
  background-color: #deebfc; }
  .table-hover .table-light:hover > td,
  .table-hover .table-light:hover > th {
    background-color: #deebfc; }

.table-dark,
.table-dark > th,
.table-dark > td {
  background-color: #c6c6cc; }

.table-dark th,
.table-dark td,
.table-dark thead th,
.table-dark tbody + tbody {
  border-color: #9495a1; }

.table-hover .table-dark:hover {
  background-color: #b9b9c0; }
  .table-hover .table-dark:hover > td,
  .table-hover .table-dark:hover > th {
    background-color: #b9b9c0; }

.table-active,
.table-active > th,
.table-active > td {
  background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover {
  background-color: rgba(0, 0, 0, 0.075); }
  .table-hover .table-active:hover > td,
  .table-hover .table-active:hover > th {
    background-color: rgba(0, 0, 0, 0.075); }

.table .thead-dark th {
  color: #e4e2ff;
  background-color: #11111d;
  border-color: #1f1f35; }

.table .thead-light th {
  color: #151623;
  background-color: #282a38;
  border-color: #28293e; }

.table-dark {
  color: #e4e2ff;
  background-color: #11111d; }
  .table-dark th,
  .table-dark td,
  .table-dark thead th {
    border-color: #1f1f35; }
  .table-dark.table-bordered {
    border: 0; }
  .table-dark.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(50, 51, 74, 0.05); }
  .table-dark.table-hover tbody tr:hover {
    color: #e4e2ff;
    background-color: rgba(50, 51, 74, 0.075); }

@media (max-width: 575.98px) {
  .table-responsive-sm {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; }
    .table-responsive-sm > .table-bordered {
      border: 0; } }

@media (max-width: 767.98px) {
  .table-responsive-md {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; }
    .table-responsive-md > .table-bordered {
      border: 0; } }

@media (max-width: 991.98px) {
  .table-responsive-lg {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; }
    .table-responsive-lg > .table-bordered {
      border: 0; } }

@media (max-width: 1199.98px) {
  .table-responsive-xl {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; }
    .table-responsive-xl > .table-bordered {
      border: 0; } }

.table-responsive {
  display: block;
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch; }
  .table-responsive > .table-bordered {
    border: 0; }

.form-control {
  display: block;
  width: 100%;
  height: calc(1.5em + 0.75rem + 2px);
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #adabc6;
  background-color: #28293e;
  background-clip: padding-box;
  border: 1px solid #11111d;
  border-radius: 6px;
  -webkit-transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  -o-transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
  @media (prefers-reduced-motion: reduce) {
    .form-control {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }
  .form-control::-ms-expand {
    background-color: transparent;
    border: 0; }
  .form-control:focus {
    color: #adabc6;
    background-color: #28293e;
    border-color: #c7b8f2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
  .form-control::-webkit-input-placeholder {
    color: #a19fb9;
    opacity: 1; }
  .form-control::-moz-placeholder {
    color: #a19fb9;
    opacity: 1; }
  .form-control:-ms-input-placeholder {
    color: #a19fb9;
    opacity: 1; }
  .form-control::-ms-input-placeholder {
    color: #a19fb9;
    opacity: 1; }
  .form-control::placeholder {
    color: #a19fb9;
    opacity: 1; }
  .form-control:disabled, .form-control[readonly] {
    background-color: #282a38;
    opacity: 1; }

select.form-control:focus::-ms-value {
  color: #adabc6;
  background-color: #28293e; }

.form-control-file,
.form-control-range {
  display: block;
  width: 100%; }

.col-form-label {
  padding-top: calc(0.375rem + 1px);
  padding-bottom: calc(0.375rem + 1px);
  margin-bottom: 0;
  font-size: inherit;
  line-height: 1.5; }

.col-form-label-lg {
  padding-top: calc(0.5rem + 1px);
  padding-bottom: calc(0.5rem + 1px);
  font-size: 1.25rem;
  line-height: 1.5; }

.col-form-label-sm {
  padding-top: calc(0.25rem + 1px);
  padding-bottom: calc(0.25rem + 1px);
  font-size: 0.875rem;
  line-height: 1.5; }

.form-control-plaintext {
  display: block;
  width: 100%;
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
  margin-bottom: 0;
  line-height: 1.5;
  color: #e4e2ff;
  background-color: transparent;
  border: solid transparent;
  border-width: 1px 0; }
  .form-control-plaintext.form-control-sm, .form-control-plaintext.form-control-lg {
    padding-right: 0;
    padding-left: 0; }

.form-control-sm {
  height: calc(1.5em + 0.5rem + 2px);
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.form-control-lg {
  height: calc(1.5em + 1rem + 2px);
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 6px; }

select.form-control[size], select.form-control[multiple] {
  height: auto; }

textarea.form-control {
  height: auto; }

.form-group {
  margin-bottom: 1rem; }

.form-text {
  display: block;
  margin-top: 0.25rem; }

.form-row {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  margin-right: -5px;
  margin-left: -5px; }
  .form-row > .col,
  .form-row > [class*="col-"] {
    padding-right: 5px;
    padding-left: 5px; }

.form-check {
  position: relative;
  display: block;
  padding-left: 1.25rem; }

.form-check-input {
  position: absolute;
  margin-top: 0.3rem;
  margin-left: -1.25rem; }
  .form-check-input:disabled ~ .form-check-label {
    color: #81839a; }

.form-check-label {
  margin-bottom: 0; }

.form-check-inline {
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  padding-left: 0;
  margin-right: 0.75rem; }
  .form-check-inline .form-check-input {
    position: static;
    margin-top: 0;
    margin-right: 0.3125rem;
    margin-left: 0; }

.valid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 80%;
  color: #17b06b; }

.valid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: #fff;
  background-color: rgba(23, 176, 107, 0.9);
  border-radius: 6px; }

.was-validated .form-control:valid, .form-control.is-valid {
  border-color: #17b06b;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2317b06b' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: center right calc(0.375em + 0.1875rem);
  -webkit-background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
          background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem); }
  .was-validated .form-control:valid:focus, .form-control.is-valid:focus {
    border-color: #17b06b;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25); }
  .was-validated .form-control:valid ~ .valid-feedback,
  .was-validated .form-control:valid ~ .valid-tooltip, .form-control.is-valid ~ .valid-feedback,
  .form-control.is-valid ~ .valid-tooltip {
    display: block; }

.was-validated textarea.form-control:valid, textarea.form-control.is-valid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem); }

.was-validated .custom-select:valid, .custom-select.is-valid {
  border-color: #17b06b;
  padding-right: calc((1em + 0.75rem) * 3 / 4 + 1.75rem);
  background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2317b06b' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e") #32334a no-repeat center right 1.75rem/calc(0.75em + 0.375rem) calc(0.75em + 0.375rem); }
  .was-validated .custom-select:valid:focus, .custom-select.is-valid:focus {
    border-color: #17b06b;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25); }
  .was-validated .custom-select:valid ~ .valid-feedback,
  .was-validated .custom-select:valid ~ .valid-tooltip, .custom-select.is-valid ~ .valid-feedback,
  .custom-select.is-valid ~ .valid-tooltip {
    display: block; }

.was-validated .form-control-file:valid ~ .valid-feedback,
.was-validated .form-control-file:valid ~ .valid-tooltip, .form-control-file.is-valid ~ .valid-feedback,
.form-control-file.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .form-check-input:valid ~ .form-check-label, .form-check-input.is-valid ~ .form-check-label {
  color: #17b06b; }

.was-validated .form-check-input:valid ~ .valid-feedback,
.was-validated .form-check-input:valid ~ .valid-tooltip, .form-check-input.is-valid ~ .valid-feedback,
.form-check-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-control-input:valid ~ .custom-control-label, .custom-control-input.is-valid ~ .custom-control-label {
  color: #17b06b; }
  .was-validated .custom-control-input:valid ~ .custom-control-label::before, .custom-control-input.is-valid ~ .custom-control-label::before {
    border-color: #17b06b; }

.was-validated .custom-control-input:valid ~ .valid-feedback,
.was-validated .custom-control-input:valid ~ .valid-tooltip, .custom-control-input.is-valid ~ .valid-feedback,
.custom-control-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-control-input:valid:checked ~ .custom-control-label::before, .custom-control-input.is-valid:checked ~ .custom-control-label::before {
  border-color: #1ddd86;
  background-color: #1ddd86; }

.was-validated .custom-control-input:valid:focus ~ .custom-control-label::before, .custom-control-input.is-valid:focus ~ .custom-control-label::before {
  -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25);
          box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25); }

.was-validated .custom-control-input:valid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-valid:focus:not(:checked) ~ .custom-control-label::before {
  border-color: #17b06b; }

.was-validated .custom-file-input:valid ~ .custom-file-label, .custom-file-input.is-valid ~ .custom-file-label {
  border-color: #17b06b; }

.was-validated .custom-file-input:valid ~ .valid-feedback,
.was-validated .custom-file-input:valid ~ .valid-tooltip, .custom-file-input.is-valid ~ .valid-feedback,
.custom-file-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-file-input:valid:focus ~ .custom-file-label, .custom-file-input.is-valid:focus ~ .custom-file-label {
  border-color: #17b06b;
  -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25);
          box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.25); }

.invalid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 80%;
  color: #ff3c5c; }

.invalid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: #fff;
  background-color: rgba(255, 60, 92, 0.9);
  border-radius: 6px; }

.was-validated .form-control:invalid, .form-control.is-invalid {
  border-color: #ff3c5c;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff3c5c' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23ff3c5c' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E");
  background-repeat: no-repeat;
  background-position: center right calc(0.375em + 0.1875rem);
  -webkit-background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
          background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem); }
  .was-validated .form-control:invalid:focus, .form-control.is-invalid:focus {
    border-color: #ff3c5c;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25); }
  .was-validated .form-control:invalid ~ .invalid-feedback,
  .was-validated .form-control:invalid ~ .invalid-tooltip, .form-control.is-invalid ~ .invalid-feedback,
  .form-control.is-invalid ~ .invalid-tooltip {
    display: block; }

.was-validated textarea.form-control:invalid, textarea.form-control.is-invalid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem); }

.was-validated .custom-select:invalid, .custom-select.is-invalid {
  border-color: #ff3c5c;
  padding-right: calc((1em + 0.75rem) * 3 / 4 + 1.75rem);
  background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ff3c5c' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23ff3c5c' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E") #32334a no-repeat center right 1.75rem/calc(0.75em + 0.375rem) calc(0.75em + 0.375rem); }
  .was-validated .custom-select:invalid:focus, .custom-select.is-invalid:focus {
    border-color: #ff3c5c;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25); }
  .was-validated .custom-select:invalid ~ .invalid-feedback,
  .was-validated .custom-select:invalid ~ .invalid-tooltip, .custom-select.is-invalid ~ .invalid-feedback,
  .custom-select.is-invalid ~ .invalid-tooltip {
    display: block; }

.was-validated .form-control-file:invalid ~ .invalid-feedback,
.was-validated .form-control-file:invalid ~ .invalid-tooltip, .form-control-file.is-invalid ~ .invalid-feedback,
.form-control-file.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .form-check-input:invalid ~ .form-check-label, .form-check-input.is-invalid ~ .form-check-label {
  color: #ff3c5c; }

.was-validated .form-check-input:invalid ~ .invalid-feedback,
.was-validated .form-check-input:invalid ~ .invalid-tooltip, .form-check-input.is-invalid ~ .invalid-feedback,
.form-check-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-control-input:invalid ~ .custom-control-label, .custom-control-input.is-invalid ~ .custom-control-label {
  color: #ff3c5c; }
  .was-validated .custom-control-input:invalid ~ .custom-control-label::before, .custom-control-input.is-invalid ~ .custom-control-label::before {
    border-color: #ff3c5c; }

.was-validated .custom-control-input:invalid ~ .invalid-feedback,
.was-validated .custom-control-input:invalid ~ .invalid-tooltip, .custom-control-input.is-invalid ~ .invalid-feedback,
.custom-control-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-control-input:invalid:checked ~ .custom-control-label::before, .custom-control-input.is-invalid:checked ~ .custom-control-label::before {
  border-color: #ff6f87;
  background-color: #ff6f87; }

.was-validated .custom-control-input:invalid:focus ~ .custom-control-label::before, .custom-control-input.is-invalid:focus ~ .custom-control-label::before {
  -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25);
          box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25); }

.was-validated .custom-control-input:invalid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-invalid:focus:not(:checked) ~ .custom-control-label::before {
  border-color: #ff3c5c; }

.was-validated .custom-file-input:invalid ~ .custom-file-label, .custom-file-input.is-invalid ~ .custom-file-label {
  border-color: #ff3c5c; }

.was-validated .custom-file-input:invalid ~ .invalid-feedback,
.was-validated .custom-file-input:invalid ~ .invalid-tooltip, .custom-file-input.is-invalid ~ .invalid-feedback,
.custom-file-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-file-input:invalid:focus ~ .custom-file-label, .custom-file-input.is-invalid:focus ~ .custom-file-label {
  border-color: #ff3c5c;
  -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25);
          box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.25); }

.form-inline {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -webkit-flex-flow: row wrap;
      -ms-flex-flow: row wrap;
          flex-flow: row wrap;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center; }
  .form-inline .form-check {
    width: 100%; }
  @media (min-width: 576px) {
    .form-inline label {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-align: center;
      -webkit-align-items: center;
          -ms-flex-align: center;
              align-items: center;
      -webkit-box-pack: center;
      -webkit-justify-content: center;
          -ms-flex-pack: center;
              justify-content: center;
      margin-bottom: 0; }
    .form-inline .form-group {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-flex: 0;
      -webkit-flex: 0 0 auto;
          -ms-flex: 0 0 auto;
              flex: 0 0 auto;
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-flow: row wrap;
          -ms-flex-flow: row wrap;
              flex-flow: row wrap;
      -webkit-box-align: center;
      -webkit-align-items: center;
          -ms-flex-align: center;
              align-items: center;
      margin-bottom: 0; }
    .form-inline .form-control {
      display: inline-block;
      width: auto;
      vertical-align: middle; }
    .form-inline .form-control-plaintext {
      display: inline-block; }
    .form-inline .input-group,
    .form-inline .custom-select {
      width: auto; }
    .form-inline .form-check {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-align: center;
      -webkit-align-items: center;
          -ms-flex-align: center;
              align-items: center;
      -webkit-box-pack: center;
      -webkit-justify-content: center;
          -ms-flex-pack: center;
              justify-content: center;
      width: auto;
      padding-left: 0; }
    .form-inline .form-check-input {
      position: relative;
      -webkit-flex-shrink: 0;
          -ms-flex-negative: 0;
              flex-shrink: 0;
      margin-top: 0;
      margin-right: 0.25rem;
      margin-left: 0; }
    .form-inline .custom-control {
      -webkit-box-align: center;
      -webkit-align-items: center;
          -ms-flex-align: center;
              align-items: center;
      -webkit-box-pack: center;
      -webkit-justify-content: center;
          -ms-flex-pack: center;
              justify-content: center; }
    .form-inline .custom-control-label {
      margin-bottom: 0; } }

.btn {
  display: inline-block;
  font-weight: 400;
  color: #e4e2ff;
  text-align: center;
  vertical-align: middle;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  background-color: transparent;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 6px;
  -webkit-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  -o-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
  @media (prefers-reduced-motion: reduce) {
    .btn {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }
  .btn:hover {
    color: #e4e2ff;
    text-decoration: none; }
  .btn:focus, .btn.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
  .btn.disabled, .btn:disabled {
    opacity: 0.65; }

a.btn.disabled,
fieldset:disabled a.btn {
  pointer-events: none; }

.btn-primary {
  color: #fff;
  background-color: #714cdf;
  border-color: #714cdf; }
  .btn-primary:hover {
    color: #fff;
    background-color: #572cd9;
    border-color: #5126d2; }
  .btn-primary:focus, .btn-primary.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(134, 103, 228, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(134, 103, 228, 0.5); }
  .btn-primary.disabled, .btn-primary:disabled {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf; }
  .btn-primary:not(:disabled):not(.disabled):active, .btn-primary:not(:disabled):not(.disabled).active,
  .show > .btn-primary.dropdown-toggle {
    color: #fff;
    background-color: #5126d2;
    border-color: #4d24c8; }
    .btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-primary.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(134, 103, 228, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(134, 103, 228, 0.5); }

.btn-secondary {
  color: #fff;
  background-color: #16a4de;
  border-color: #16a4de; }
  .btn-secondary:hover {
    color: #fff;
    background-color: #138abb;
    border-color: #1182b0; }
  .btn-secondary:focus, .btn-secondary.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(57, 178, 227, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(57, 178, 227, 0.5); }
  .btn-secondary.disabled, .btn-secondary:disabled {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de; }
  .btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-secondary.dropdown-toggle {
    color: #fff;
    background-color: #1182b0;
    border-color: #1079a4; }
    .btn-secondary:not(:disabled):not(.disabled):active:focus, .btn-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-secondary.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(57, 178, 227, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(57, 178, 227, 0.5); }

.btn-success {
  color: #fff;
  background-color: #17b06b;
  border-color: #17b06b; }
  .btn-success:hover {
    color: #fff;
    background-color: #138e56;
    border-color: #118350; }
  .btn-success:focus, .btn-success.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(58, 188, 129, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(58, 188, 129, 0.5); }
  .btn-success.disabled, .btn-success:disabled {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b; }
  .btn-success:not(:disabled):not(.disabled):active, .btn-success:not(:disabled):not(.disabled).active,
  .show > .btn-success.dropdown-toggle {
    color: #fff;
    background-color: #118350;
    border-color: #107849; }
    .btn-success:not(:disabled):not(.disabled):active:focus, .btn-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-success.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(58, 188, 129, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(58, 188, 129, 0.5); }

.btn-info {
  color: #fff;
  background-color: #2983fe;
  border-color: #2983fe; }
  .btn-info:hover {
    color: #fff;
    background-color: #036dfe;
    border-color: #0167f3; }
  .btn-info:focus, .btn-info.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(73, 150, 254, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(73, 150, 254, 0.5); }
  .btn-info.disabled, .btn-info:disabled {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe; }
  .btn-info:not(:disabled):not(.disabled):active, .btn-info:not(:disabled):not(.disabled).active,
  .show > .btn-info.dropdown-toggle {
    color: #fff;
    background-color: #0167f3;
    border-color: #0162e6; }
    .btn-info:not(:disabled):not(.disabled):active:focus, .btn-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-info.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(73, 150, 254, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(73, 150, 254, 0.5); }

.btn-warning {
  color: #fff;
  background-color: #f97515;
  border-color: #f97515; }
  .btn-warning:hover {
    color: #fff;
    background-color: #e26206;
    border-color: #d65d05; }
  .btn-warning:focus, .btn-warning.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(250, 138, 56, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(250, 138, 56, 0.5); }
  .btn-warning.disabled, .btn-warning:disabled {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515; }
  .btn-warning:not(:disabled):not(.disabled):active, .btn-warning:not(:disabled):not(.disabled).active,
  .show > .btn-warning.dropdown-toggle {
    color: #fff;
    background-color: #d65d05;
    border-color: #c95805; }
    .btn-warning:not(:disabled):not(.disabled):active:focus, .btn-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-warning.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(250, 138, 56, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(250, 138, 56, 0.5); }

.btn-danger {
  color: #fff;
  background-color: #ff3c5c;
  border-color: #ff3c5c; }
  .btn-danger:hover {
    color: #fff;
    background-color: #ff163c;
    border-color: #ff0931; }
  .btn-danger:focus, .btn-danger.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 89, 116, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(255, 89, 116, 0.5); }
  .btn-danger.disabled, .btn-danger:disabled {
    color: #fff;
    background-color: #ff3c5c;
    border-color: #ff3c5c; }
  .btn-danger:not(:disabled):not(.disabled):active, .btn-danger:not(:disabled):not(.disabled).active,
  .show > .btn-danger.dropdown-toggle {
    color: #fff;
    background-color: #ff0931;
    border-color: #fb0029; }
    .btn-danger:not(:disabled):not(.disabled):active:focus, .btn-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-danger.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 89, 116, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(255, 89, 116, 0.5); }

.btn-light {
  color: #0a0b14;
  background-color: #dbebfb;
  border-color: #dbebfb; }
  .btn-light:hover {
    color: #0a0b14;
    background-color: #b9d8f7;
    border-color: #add2f6; }
  .btn-light:focus, .btn-light.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(188, 201, 216, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(188, 201, 216, 0.5); }
  .btn-light.disabled, .btn-light:disabled {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb; }
  .btn-light:not(:disabled):not(.disabled):active, .btn-light:not(:disabled):not(.disabled).active,
  .show > .btn-light.dropdown-toggle {
    color: #0a0b14;
    background-color: #add2f6;
    border-color: #a2cbf5; }
    .btn-light:not(:disabled):not(.disabled):active:focus, .btn-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-light.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(188, 201, 216, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(188, 201, 216, 0.5); }

.btn-dark {
  color: #fff;
  background-color: #32334a;
  border-color: #32334a; }
  .btn-dark:hover {
    color: #fff;
    background-color: #232333;
    border-color: #1d1e2c; }
  .btn-dark:focus, .btn-dark.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(81, 82, 101, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(81, 82, 101, 0.5); }
  .btn-dark.disabled, .btn-dark:disabled {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a; }
  .btn-dark:not(:disabled):not(.disabled):active, .btn-dark:not(:disabled):not(.disabled).active,
  .show > .btn-dark.dropdown-toggle {
    color: #fff;
    background-color: #1d1e2c;
    border-color: #181924; }
    .btn-dark:not(:disabled):not(.disabled):active:focus, .btn-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dark.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(81, 82, 101, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(81, 82, 101, 0.5); }

.btn-outline-primary {
  color: #714cdf;
  border-color: #714cdf; }
  .btn-outline-primary:hover {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf; }
  .btn-outline-primary:focus, .btn-outline-primary.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5); }
  .btn-outline-primary.disabled, .btn-outline-primary:disabled {
    color: #714cdf;
    background-color: transparent; }
  .btn-outline-primary:not(:disabled):not(.disabled):active, .btn-outline-primary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-primary.dropdown-toggle {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf; }
    .btn-outline-primary:not(:disabled):not(.disabled):active:focus, .btn-outline-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-primary.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5); }

.btn-outline-secondary {
  color: #16a4de;
  border-color: #16a4de; }
  .btn-outline-secondary:hover {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de; }
  .btn-outline-secondary:focus, .btn-outline-secondary.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5); }
  .btn-outline-secondary.disabled, .btn-outline-secondary:disabled {
    color: #16a4de;
    background-color: transparent; }
  .btn-outline-secondary:not(:disabled):not(.disabled):active, .btn-outline-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-secondary.dropdown-toggle {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de; }
    .btn-outline-secondary:not(:disabled):not(.disabled):active:focus, .btn-outline-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-secondary.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5); }

.btn-outline-success {
  color: #17b06b;
  border-color: #17b06b; }
  .btn-outline-success:hover {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b; }
  .btn-outline-success:focus, .btn-outline-success.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5); }
  .btn-outline-success.disabled, .btn-outline-success:disabled {
    color: #17b06b;
    background-color: transparent; }
  .btn-outline-success:not(:disabled):not(.disabled):active, .btn-outline-success:not(:disabled):not(.disabled).active,
  .show > .btn-outline-success.dropdown-toggle {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b; }
    .btn-outline-success:not(:disabled):not(.disabled):active:focus, .btn-outline-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-success.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5); }

.btn-outline-info {
  color: #2983fe;
  border-color: #2983fe; }
  .btn-outline-info:hover {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe; }
  .btn-outline-info:focus, .btn-outline-info.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5); }
  .btn-outline-info.disabled, .btn-outline-info:disabled {
    color: #2983fe;
    background-color: transparent; }
  .btn-outline-info:not(:disabled):not(.disabled):active, .btn-outline-info:not(:disabled):not(.disabled).active,
  .show > .btn-outline-info.dropdown-toggle {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe; }
    .btn-outline-info:not(:disabled):not(.disabled):active:focus, .btn-outline-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-info.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5); }

.btn-outline-warning {
  color: #f97515;
  border-color: #f97515; }
  .btn-outline-warning:hover {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515; }
  .btn-outline-warning:focus, .btn-outline-warning.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5); }
  .btn-outline-warning.disabled, .btn-outline-warning:disabled {
    color: #f97515;
    background-color: transparent; }
  .btn-outline-warning:not(:disabled):not(.disabled):active, .btn-outline-warning:not(:disabled):not(.disabled).active,
  .show > .btn-outline-warning.dropdown-toggle {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515; }
    .btn-outline-warning:not(:disabled):not(.disabled):active:focus, .btn-outline-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-warning.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5); }

.btn-outline-danger {
  color: #ff3c5c;
  border-color: #ff3c5c; }
  .btn-outline-danger:hover {
    color: #fff;
    background-color: #ff3c5c;
    border-color: #ff3c5c; }
  .btn-outline-danger:focus, .btn-outline-danger.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5); }
  .btn-outline-danger.disabled, .btn-outline-danger:disabled {
    color: #ff3c5c;
    background-color: transparent; }
  .btn-outline-danger:not(:disabled):not(.disabled):active, .btn-outline-danger:not(:disabled):not(.disabled).active,
  .show > .btn-outline-danger.dropdown-toggle {
    color: #fff;
    background-color: #ff3c5c;
    border-color: #ff3c5c; }
    .btn-outline-danger:not(:disabled):not(.disabled):active:focus, .btn-outline-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-danger.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5); }

.btn-outline-light {
  color: #dbebfb;
  border-color: #dbebfb; }
  .btn-outline-light:hover {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb; }
  .btn-outline-light:focus, .btn-outline-light.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5); }
  .btn-outline-light.disabled, .btn-outline-light:disabled {
    color: #dbebfb;
    background-color: transparent; }
  .btn-outline-light:not(:disabled):not(.disabled):active, .btn-outline-light:not(:disabled):not(.disabled).active,
  .show > .btn-outline-light.dropdown-toggle {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb; }
    .btn-outline-light:not(:disabled):not(.disabled):active:focus, .btn-outline-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-light.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5); }

.btn-outline-dark {
  color: #32334a;
  border-color: #32334a; }
  .btn-outline-dark:hover {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a; }
  .btn-outline-dark:focus, .btn-outline-dark.focus {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5); }
  .btn-outline-dark.disabled, .btn-outline-dark:disabled {
    color: #32334a;
    background-color: transparent; }
  .btn-outline-dark:not(:disabled):not(.disabled):active, .btn-outline-dark:not(:disabled):not(.disabled).active,
  .show > .btn-outline-dark.dropdown-toggle {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a; }
    .btn-outline-dark:not(:disabled):not(.disabled):active:focus, .btn-outline-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-dark.dropdown-toggle:focus {
      -webkit-box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5);
              box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5); }

.btn-link {
  font-weight: 400;
  color: #714cdf;
  text-decoration: none; }
  .btn-link:hover {
    color: #4922bd;
    text-decoration: underline; }
  .btn-link:focus, .btn-link.focus {
    text-decoration: underline;
    -webkit-box-shadow: none;
            box-shadow: none; }
  .btn-link:disabled, .btn-link.disabled {
    color: #1d1e2f;
    pointer-events: none; }

.btn-lg, .btn-group-lg > .btn {
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 6px; }

.btn-sm, .btn-group-sm > .btn {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.btn-block {
  display: block;
  width: 100%; }
  .btn-block + .btn-block {
    margin-top: 0.5rem; }

input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%; }

.fade {
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear; }
  @media (prefers-reduced-motion: reduce) {
    .fade {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }
  .fade:not(.show) {
    opacity: 0; }

.collapse:not(.show) {
  display: none; }

.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition: height 0.35s ease;
  -o-transition: height 0.35s ease;
  transition: height 0.35s ease; }
  @media (prefers-reduced-motion: reduce) {
    .collapsing {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }

.dropup,
.dropright,
.dropdown,
.dropleft {
  position: relative; }

.dropdown-toggle {
  white-space: nowrap; }
  .dropdown-toggle::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: "";
    border-top: 0.3em solid;
    border-right: 0.3em solid transparent;
    border-bottom: 0;
    border-left: 0.3em solid transparent; }
  .dropdown-toggle:empty::after {
    margin-left: 0; }

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0.125rem 0 0;
  font-size: 1rem;
  color: #e4e2ff;
  text-align: left;
  list-style: none;
  background-color: #32334a;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 6px; }

.dropdown-menu-left {
  right: auto;
  left: 0; }

.dropdown-menu-right {
  right: 0;
  left: auto; }

@media (min-width: 576px) {
  .dropdown-menu-sm-left {
    right: auto;
    left: 0; }
  .dropdown-menu-sm-right {
    right: 0;
    left: auto; } }

@media (min-width: 768px) {
  .dropdown-menu-md-left {
    right: auto;
    left: 0; }
  .dropdown-menu-md-right {
    right: 0;
    left: auto; } }

@media (min-width: 992px) {
  .dropdown-menu-lg-left {
    right: auto;
    left: 0; }
  .dropdown-menu-lg-right {
    right: 0;
    left: auto; } }

@media (min-width: 1200px) {
  .dropdown-menu-xl-left {
    right: auto;
    left: 0; }
  .dropdown-menu-xl-right {
    right: 0;
    left: auto; } }

.dropup .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-top: 0;
  margin-bottom: 0.125rem; }

.dropup .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0;
  border-right: 0.3em solid transparent;
  border-bottom: 0.3em solid;
  border-left: 0.3em solid transparent; }

.dropup .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropright .dropdown-menu {
  top: 0;
  right: auto;
  left: 100%;
  margin-top: 0;
  margin-left: 0.125rem; }

.dropright .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0;
  border-bottom: 0.3em solid transparent;
  border-left: 0.3em solid; }

.dropright .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropright .dropdown-toggle::after {
  vertical-align: 0; }

.dropleft .dropdown-menu {
  top: 0;
  right: 100%;
  left: auto;
  margin-top: 0;
  margin-right: 0.125rem; }

.dropleft .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: ""; }

.dropleft .dropdown-toggle::after {
  display: none; }

.dropleft .dropdown-toggle::before {
  display: inline-block;
  margin-right: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0.3em solid;
  border-bottom: 0.3em solid transparent; }

.dropleft .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropleft .dropdown-toggle::before {
  vertical-align: 0; }

.dropdown-menu[x-placement^="top"], .dropdown-menu[x-placement^="right"], .dropdown-menu[x-placement^="bottom"], .dropdown-menu[x-placement^="left"] {
  right: auto;
  bottom: auto; }

.dropdown-divider {
  height: 0;
  margin: 0.5rem 0;
  overflow: hidden;
  border-top: 1px solid #282a38; }

.dropdown-item {
  display: block;
  width: 100%;
  padding: 0.25rem 1.5rem;
  clear: both;
  font-weight: 400;
  color: #0a0b14;
  text-align: inherit;
  white-space: nowrap;
  background-color: transparent;
  border: 0; }
  .dropdown-item:hover, .dropdown-item:focus {
    color: #020203;
    text-decoration: none;
    background-color: #2d2e3f; }
  .dropdown-item.active, .dropdown-item:active {
    color: #32334a;
    text-decoration: none;
    background-color: #714cdf; }
  .dropdown-item.disabled, .dropdown-item:disabled {
    color: #1d1e2f;
    pointer-events: none;
    background-color: transparent; }

.dropdown-menu.show {
  display: block; }

.dropdown-header {
  display: block;
  padding: 0.5rem 1.5rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  color: #1d1e2f;
  white-space: nowrap; }

.dropdown-item-text {
  display: block;
  padding: 0.25rem 1.5rem;
  color: #0a0b14; }

.btn-group,
.btn-group-vertical {
  position: relative;
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  vertical-align: middle; }
  .btn-group > .btn,
  .btn-group-vertical > .btn {
    position: relative;
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
        -ms-flex: 1 1 auto;
            flex: 1 1 auto; }
    .btn-group > .btn:hover,
    .btn-group-vertical > .btn:hover {
      z-index: 1; }
    .btn-group > .btn:focus, .btn-group > .btn:active, .btn-group > .btn.active,
    .btn-group-vertical > .btn:focus,
    .btn-group-vertical > .btn:active,
    .btn-group-vertical > .btn.active {
      z-index: 1; }

.btn-toolbar {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  -webkit-box-pack: start;
  -webkit-justify-content: flex-start;
      -ms-flex-pack: start;
          justify-content: flex-start; }
  .btn-toolbar .input-group {
    width: auto; }

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) {
  margin-left: -1px; }

.btn-group > .btn:not(:last-child):not(.dropdown-toggle),
.btn-group > .btn-group:not(:last-child) > .btn {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0; }

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) > .btn {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0; }

.dropdown-toggle-split {
  padding-right: 0.5625rem;
  padding-left: 0.5625rem; }
  .dropdown-toggle-split::after,
  .dropup .dropdown-toggle-split::after,
  .dropright .dropdown-toggle-split::after {
    margin-left: 0; }
  .dropleft .dropdown-toggle-split::before {
    margin-right: 0; }

.btn-sm + .dropdown-toggle-split, .btn-group-sm > .btn + .dropdown-toggle-split {
  padding-right: 0.375rem;
  padding-left: 0.375rem; }

.btn-lg + .dropdown-toggle-split, .btn-group-lg > .btn + .dropdown-toggle-split {
  padding-right: 0.75rem;
  padding-left: 0.75rem; }

.btn-group-vertical {
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-align: start;
  -webkit-align-items: flex-start;
      -ms-flex-align: start;
          align-items: flex-start;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
      -ms-flex-pack: center;
          justify-content: center; }
  .btn-group-vertical > .btn,
  .btn-group-vertical > .btn-group {
    width: 100%; }
  .btn-group-vertical > .btn:not(:first-child),
  .btn-group-vertical > .btn-group:not(:first-child) {
    margin-top: -1px; }
  .btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle),
  .btn-group-vertical > .btn-group:not(:last-child) > .btn {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0; }
  .btn-group-vertical > .btn:not(:first-child),
  .btn-group-vertical > .btn-group:not(:first-child) > .btn {
    border-top-left-radius: 0;
    border-top-right-radius: 0; }

.btn-group-toggle > .btn,
.btn-group-toggle > .btn-group > .btn {
  margin-bottom: 0; }
  .btn-group-toggle > .btn input[type="radio"],
  .btn-group-toggle > .btn input[type="checkbox"],
  .btn-group-toggle > .btn-group > .btn input[type="radio"],
  .btn-group-toggle > .btn-group > .btn input[type="checkbox"] {
    position: absolute;
    clip: rect(0, 0, 0, 0);
    pointer-events: none; }

.input-group {
  position: relative;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  -webkit-box-align: stretch;
  -webkit-align-items: stretch;
      -ms-flex-align: stretch;
          align-items: stretch;
  width: 100%; }
  .input-group > .form-control,
  .input-group > .form-control-plaintext,
  .input-group > .custom-select,
  .input-group > .custom-file {
    position: relative;
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
        -ms-flex: 1 1 auto;
            flex: 1 1 auto;
    width: 1%;
    margin-bottom: 0; }
    .input-group > .form-control + .form-control,
    .input-group > .form-control + .custom-select,
    .input-group > .form-control + .custom-file,
    .input-group > .form-control-plaintext + .form-control,
    .input-group > .form-control-plaintext + .custom-select,
    .input-group > .form-control-plaintext + .custom-file,
    .input-group > .custom-select + .form-control,
    .input-group > .custom-select + .custom-select,
    .input-group > .custom-select + .custom-file,
    .input-group > .custom-file + .form-control,
    .input-group > .custom-file + .custom-select,
    .input-group > .custom-file + .custom-file {
      margin-left: -1px; }
  .input-group > .form-control:focus,
  .input-group > .custom-select:focus,
  .input-group > .custom-file .custom-file-input:focus ~ .custom-file-label {
    z-index: 3; }
  .input-group > .custom-file .custom-file-input:focus {
    z-index: 4; }
  .input-group > .form-control:not(:last-child),
  .input-group > .custom-select:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0; }
  .input-group > .form-control:not(:first-child),
  .input-group > .custom-select:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0; }
  .input-group > .custom-file {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
        -ms-flex-align: center;
            align-items: center; }
    .input-group > .custom-file:not(:last-child) .custom-file-label,
    .input-group > .custom-file:not(:last-child) .custom-file-label::after {
      border-top-right-radius: 0;
      border-bottom-right-radius: 0; }
    .input-group > .custom-file:not(:first-child) .custom-file-label {
      border-top-left-radius: 0;
      border-bottom-left-radius: 0; }

.input-group-prepend,
.input-group-append {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex; }
  .input-group-prepend .btn,
  .input-group-append .btn {
    position: relative;
    z-index: 2; }
    .input-group-prepend .btn:focus,
    .input-group-append .btn:focus {
      z-index: 3; }
  .input-group-prepend .btn + .btn,
  .input-group-prepend .btn + .input-group-text,
  .input-group-prepend .input-group-text + .input-group-text,
  .input-group-prepend .input-group-text + .btn,
  .input-group-append .btn + .btn,
  .input-group-append .btn + .input-group-text,
  .input-group-append .input-group-text + .input-group-text,
  .input-group-append .input-group-text + .btn {
    margin-left: -1px; }

.input-group-prepend {
  margin-right: -1px; }

.input-group-append {
  margin-left: -1px; }

.input-group-text {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  padding: 0.375rem 0.75rem;
  margin-bottom: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #adabc6;
  text-align: center;
  white-space: nowrap;
  background-color: #282a38;
  border: 1px solid #11111d;
  border-radius: 6px; }
  .input-group-text input[type="radio"],
  .input-group-text input[type="checkbox"] {
    margin-top: 0; }

.input-group-lg > .form-control:not(textarea),
.input-group-lg > .custom-select {
  height: calc(1.5em + 1rem + 2px); }

.input-group-lg > .form-control,
.input-group-lg > .custom-select,
.input-group-lg > .input-group-prepend > .input-group-text,
.input-group-lg > .input-group-append > .input-group-text,
.input-group-lg > .input-group-prepend > .btn,
.input-group-lg > .input-group-append > .btn {
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 6px; }

.input-group-sm > .form-control:not(textarea),
.input-group-sm > .custom-select {
  height: calc(1.5em + 0.5rem + 2px); }

.input-group-sm > .form-control,
.input-group-sm > .custom-select,
.input-group-sm > .input-group-prepend > .input-group-text,
.input-group-sm > .input-group-append > .input-group-text,
.input-group-sm > .input-group-prepend > .btn,
.input-group-sm > .input-group-append > .btn {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.input-group-lg > .custom-select,
.input-group-sm > .custom-select {
  padding-right: 1.75rem; }

.input-group > .input-group-prepend > .btn,
.input-group > .input-group-prepend > .input-group-text,
.input-group > .input-group-append:not(:last-child) > .btn,
.input-group > .input-group-append:not(:last-child) > .input-group-text,
.input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group > .input-group-append:last-child > .input-group-text:not(:last-child) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0; }

.input-group > .input-group-append > .btn,
.input-group > .input-group-append > .input-group-text,
.input-group > .input-group-prepend:not(:first-child) > .btn,
.input-group > .input-group-prepend:not(:first-child) > .input-group-text,
.input-group > .input-group-prepend:first-child > .btn:not(:first-child),
.input-group > .input-group-prepend:first-child > .input-group-text:not(:first-child) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0; }

.custom-control {
  position: relative;
  display: block;
  min-height: 1.5rem;
  padding-left: 1.5rem; }

.custom-control-inline {
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  margin-right: 1rem; }

.custom-control-input {
  position: absolute;
  z-index: -1;
  opacity: 0; }
  .custom-control-input:checked ~ .custom-control-label::before {
    color: #32334a;
    border-color: #714cdf;
    background-color: #714cdf; }
  .custom-control-input:focus ~ .custom-control-label::before {
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
  .custom-control-input:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #c7b8f2; }
  .custom-control-input:not(:disabled):active ~ .custom-control-label::before {
    color: #32334a;
    background-color: #e9e3fa;
    border-color: #e9e3fa; }
  .custom-control-input:disabled ~ .custom-control-label {
    color: #1d1e2f; }
    .custom-control-input:disabled ~ .custom-control-label::before {
      background-color: #282a38; }

.custom-control-label {
  position: relative;
  margin-bottom: 0;
  vertical-align: top; }
  .custom-control-label::before {
    position: absolute;
    top: 0.25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    pointer-events: none;
    content: "";
    background-color: #151623;
    border: #1c1d2c solid 1px; }
  .custom-control-label::after {
    position: absolute;
    top: 0.25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    content: "";
    background: no-repeat 50% / 50% 50%; }

.custom-checkbox .custom-control-label::before {
  border-radius: 6px; }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2332334a' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e"); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::before {
  border-color: #714cdf;
  background-color: #714cdf; }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3e%3cpath stroke='%2332334a' d='M0 2h4'/%3e%3c/svg%3e"); }

.custom-checkbox .custom-control-input:disabled:checked ~ .custom-control-label::before {
  background-color: rgba(113, 76, 223, 0.5); }

.custom-checkbox .custom-control-input:disabled:indeterminate ~ .custom-control-label::before {
  background-color: rgba(113, 76, 223, 0.5); }

.custom-radio .custom-control-label::before {
  border-radius: 50%; }

.custom-radio .custom-control-input:checked ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%2332334a'/%3e%3c/svg%3e"); }

.custom-radio .custom-control-input:disabled:checked ~ .custom-control-label::before {
  background-color: rgba(113, 76, 223, 0.5); }

.custom-switch {
  padding-left: 2.25rem; }
  .custom-switch .custom-control-label::before {
    left: -2.25rem;
    width: 1.75rem;
    pointer-events: all;
    border-radius: 0.5rem; }
  .custom-switch .custom-control-label::after {
    top: calc(0.25rem + 2px);
    left: calc(-2.25rem + 2px);
    width: calc(1rem - 4px);
    height: calc(1rem - 4px);
    background-color: #1c1d2c;
    border-radius: 0.5rem;
    -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-transform 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-transform 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -o-transform 0.15s ease-in-out;
    transition: transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-transform 0.15s ease-in-out, -o-transform 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
    @media (prefers-reduced-motion: reduce) {
      .custom-switch .custom-control-label::after {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
  .custom-switch .custom-control-input:checked ~ .custom-control-label::after {
    background-color: #151623;
    -webkit-transform: translateX(0.75rem);
         -o-transform: translateX(0.75rem);
            transform: translateX(0.75rem); }
  .custom-switch .custom-control-input:disabled:checked ~ .custom-control-label::before {
    background-color: rgba(113, 76, 223, 0.5); }

.custom-select {
  display: inline-block;
  width: 100%;
  height: calc(1.5em + 0.75rem + 2px);
  padding: 0.375rem 1.75rem 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #adabc6;
  vertical-align: middle;
  background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px;
  background-color: #32334a;
  border: 1px solid #11111d;
  border-radius: 6px;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none; }
  .custom-select:focus {
    border-color: #c7b8f2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
    .custom-select:focus::-ms-value {
      color: #adabc6;
      background-color: #28293e; }
  .custom-select[multiple], .custom-select[size]:not([size="1"]) {
    height: auto;
    padding-right: 0.75rem;
    background-image: none; }
  .custom-select:disabled {
    color: #1d1e2f;
    background-color: #282a38; }
  .custom-select::-ms-expand {
    display: none; }

.custom-select-sm {
  height: calc(1.5em + 0.5rem + 2px);
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  padding-left: 0.5rem;
  font-size: 0.875rem; }

.custom-select-lg {
  height: calc(1.5em + 1rem + 2px);
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1rem;
  font-size: 1.25rem; }

.custom-file {
  position: relative;
  display: inline-block;
  width: 100%;
  height: calc(1.5em + 0.75rem + 2px);
  margin-bottom: 0; }

.custom-file-input {
  position: relative;
  z-index: 2;
  width: 100%;
  height: calc(1.5em + 0.75rem + 2px);
  margin: 0;
  opacity: 0; }
  .custom-file-input:focus ~ .custom-file-label {
    border-color: #c7b8f2;
    -webkit-box-shadow: 0 0 0 0.075rem #32334a, 0 0 0 0.2rem theme-color("primary");
            box-shadow: 0 0 0 0.075rem #32334a, 0 0 0 0.2rem theme-color("primary"); }
  .custom-file-input:disabled ~ .custom-file-label {
    background-color: #282a38; }
  .custom-file-input:lang(en) ~ .custom-file-label::after {
    content: "Browse"; }
  .custom-file-input ~ .custom-file-label[data-browse]::after {
    content: attr(data-browse); }

.custom-file-label {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1;
  height: calc(1.5em + 0.75rem + 2px);
  padding: 0.375rem 0.75rem;
  font-weight: 400;
  line-height: 1.5;
  color: #adabc6;
  background-color: #28293e;
  border: 1px solid #11111d;
  border-radius: 6px; }
  .custom-file-label::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;
    display: block;
    height: calc(1.5em + 0.75rem);
    padding: 0.375rem 0.75rem;
    line-height: 1.5;
    color: #adabc6;
    content: "Browse";
    background-color: #282a38;
    border-left: inherit;
    border-radius: 0 6px 6px 0; }

.custom-range {
  width: 100%;
  height: calc(1rem + 0.4rem);
  padding: 0;
  background-color: transparent;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none; }
  .custom-range:focus {
    outline: none; }
    .custom-range:focus::-webkit-slider-thumb {
      -webkit-box-shadow: 0 0 0 1px #0c0d16, 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
              box-shadow: 0 0 0 1px #0c0d16, 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
    .custom-range:focus::-moz-range-thumb {
      box-shadow: 0 0 0 1px #0c0d16, 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
    .custom-range:focus::-ms-thumb {
      box-shadow: 0 0 0 1px #0c0d16, 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }
  .custom-range::-moz-focus-outer {
    border: 0; }
  .custom-range::-webkit-slider-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: -0.25rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -webkit-appearance: none;
            appearance: none; }
    @media (prefers-reduced-motion: reduce) {
      .custom-range::-webkit-slider-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
    .custom-range::-webkit-slider-thumb:active {
      background-color: #e9e3fa; }
  .custom-range::-webkit-slider-runnable-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #28293e;
    border-color: transparent;
    border-radius: 1rem; }
  .custom-range::-moz-range-thumb {
    width: 1rem;
    height: 1rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -moz-appearance: none;
         appearance: none; }
    @media (prefers-reduced-motion: reduce) {
      .custom-range::-moz-range-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
    .custom-range::-moz-range-thumb:active {
      background-color: #e9e3fa; }
  .custom-range::-moz-range-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #28293e;
    border-color: transparent;
    border-radius: 1rem; }
  .custom-range::-ms-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: 0;
    margin-right: 0.2rem;
    margin-left: 0.2rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    appearance: none; }
    @media (prefers-reduced-motion: reduce) {
      .custom-range::-ms-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
    .custom-range::-ms-thumb:active {
      background-color: #e9e3fa; }
  .custom-range::-ms-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: transparent;
    border-color: transparent;
    border-width: 0.5rem; }
  .custom-range::-ms-fill-lower {
    background-color: #28293e;
    border-radius: 1rem; }
  .custom-range::-ms-fill-upper {
    margin-right: 15px;
    background-color: #28293e;
    border-radius: 1rem; }
  .custom-range:disabled::-webkit-slider-thumb {
    background-color: #1c1d2c; }
  .custom-range:disabled::-webkit-slider-runnable-track {
    cursor: default; }
  .custom-range:disabled::-moz-range-thumb {
    background-color: #1c1d2c; }
  .custom-range:disabled::-moz-range-track {
    cursor: default; }
  .custom-range:disabled::-ms-thumb {
    background-color: #1c1d2c; }

.custom-control-label::before,
.custom-file-label,
.custom-select {
  -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  -o-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
  @media (prefers-reduced-motion: reduce) {
    .custom-control-label::before,
    .custom-file-label,
    .custom-select {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }

.nav {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none; }

.nav-link {
  display: block;
  padding: 0.5rem 1rem; }
  .nav-link:hover, .nav-link:focus {
    text-decoration: none; }
  .nav-link.disabled {
    color: #1d1e2f;
    pointer-events: none;
    cursor: default; }

.nav-tabs {
  border-bottom: 1px solid #151623; }
  .nav-tabs .nav-item {
    margin-bottom: -1px; }
  .nav-tabs .nav-link {
    border: 1px solid transparent;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px; }
    .nav-tabs .nav-link:hover, .nav-tabs .nav-link:focus {
      border-color: #282a38 #282a38 #151623; }
    .nav-tabs .nav-link.disabled {
      color: #1d1e2f;
      background-color: transparent;
      border-color: transparent; }
  .nav-tabs .nav-link.active,
  .nav-tabs .nav-item.show .nav-link {
    color: #e4e2ff;
    background-color: #0c0d16;
    border-color: #151623; }
  .nav-tabs .dropdown-menu {
    margin-top: -1px;
    border-top-left-radius: 0;
    border-top-right-radius: 0; }

.nav-pills .nav-link {
  border-radius: 6px; }

.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
  color: #32334a;
  background-color: #714cdf; }

.nav-fill .nav-item {
  -webkit-box-flex: 1;
  -webkit-flex: 1 1 auto;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  text-align: center; }

.nav-justified .nav-item {
  -webkit-flex-basis: 0;
      -ms-flex-preferred-size: 0;
          flex-basis: 0;
  -webkit-box-flex: 1;
  -webkit-flex-grow: 1;
      -ms-flex-positive: 1;
          flex-grow: 1;
  text-align: center; }

.tab-content > .tab-pane {
  display: none; }

.tab-content > .active {
  display: block; }

.navbar {
  position: relative;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: justify;
  -webkit-justify-content: space-between;
      -ms-flex-pack: justify;
          justify-content: space-between;
  padding: 0.5rem 1rem; }
  .navbar > .container,
  .navbar > .container-fluid {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
        -ms-flex-wrap: wrap;
            flex-wrap: wrap;
    -webkit-box-align: center;
    -webkit-align-items: center;
        -ms-flex-align: center;
            align-items: center;
    -webkit-box-pack: justify;
    -webkit-justify-content: space-between;
        -ms-flex-pack: justify;
            justify-content: space-between; }

.navbar-brand {
  display: inline-block;
  padding-top: 0.3125rem;
  padding-bottom: 0.3125rem;
  margin-right: 1rem;
  font-size: 1.25rem;
  line-height: inherit;
  white-space: nowrap; }
  .navbar-brand:hover, .navbar-brand:focus {
    text-decoration: none; }

.navbar-nav {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none; }
  .navbar-nav .nav-link {
    padding-right: 0;
    padding-left: 0; }
  .navbar-nav .dropdown-menu {
    position: static;
    float: none; }

.navbar-text {
  display: inline-block;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem; }

.navbar-collapse {
  -webkit-flex-basis: 100%;
      -ms-flex-preferred-size: 100%;
          flex-basis: 100%;
  -webkit-box-flex: 1;
  -webkit-flex-grow: 1;
      -ms-flex-positive: 1;
          flex-grow: 1;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center; }

.navbar-toggler {
  padding: 0.25rem 0.75rem;
  font-size: 1.25rem;
  line-height: 1;
  background-color: transparent;
  border: 1px solid transparent;
  border-radius: 6px; }
  .navbar-toggler:hover, .navbar-toggler:focus {
    text-decoration: none; }

.navbar-toggler-icon {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  content: "";
  background: no-repeat center center;
  -webkit-background-size: 100% 100%;
          background-size: 100% 100%; }

@media (max-width: 575.98px) {
  .navbar-expand-sm > .container,
  .navbar-expand-sm > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 576px) {
  .navbar-expand-sm {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
            flex-flow: row nowrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
            justify-content: flex-start; }
    .navbar-expand-sm .navbar-nav {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-direction: row;
          -ms-flex-direction: row;
              flex-direction: row; }
      .navbar-expand-sm .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-sm .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-sm > .container,
    .navbar-expand-sm > .container-fluid {
      -webkit-flex-wrap: nowrap;
          -ms-flex-wrap: nowrap;
              flex-wrap: nowrap; }
    .navbar-expand-sm .navbar-collapse {
      display: -webkit-box !important;
      display: -webkit-flex !important;
      display: -ms-flexbox !important;
      display: flex !important;
      -webkit-flex-basis: auto;
          -ms-flex-preferred-size: auto;
              flex-basis: auto; }
    .navbar-expand-sm .navbar-toggler {
      display: none; } }

@media (max-width: 767.98px) {
  .navbar-expand-md > .container,
  .navbar-expand-md > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 768px) {
  .navbar-expand-md {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
            flex-flow: row nowrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
            justify-content: flex-start; }
    .navbar-expand-md .navbar-nav {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-direction: row;
          -ms-flex-direction: row;
              flex-direction: row; }
      .navbar-expand-md .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-md .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-md > .container,
    .navbar-expand-md > .container-fluid {
      -webkit-flex-wrap: nowrap;
          -ms-flex-wrap: nowrap;
              flex-wrap: nowrap; }
    .navbar-expand-md .navbar-collapse {
      display: -webkit-box !important;
      display: -webkit-flex !important;
      display: -ms-flexbox !important;
      display: flex !important;
      -webkit-flex-basis: auto;
          -ms-flex-preferred-size: auto;
              flex-basis: auto; }
    .navbar-expand-md .navbar-toggler {
      display: none; } }

@media (max-width: 991.98px) {
  .navbar-expand-lg > .container,
  .navbar-expand-lg > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 992px) {
  .navbar-expand-lg {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
            flex-flow: row nowrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
            justify-content: flex-start; }
    .navbar-expand-lg .navbar-nav {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-direction: row;
          -ms-flex-direction: row;
              flex-direction: row; }
      .navbar-expand-lg .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-lg .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-lg > .container,
    .navbar-expand-lg > .container-fluid {
      -webkit-flex-wrap: nowrap;
          -ms-flex-wrap: nowrap;
              flex-wrap: nowrap; }
    .navbar-expand-lg .navbar-collapse {
      display: -webkit-box !important;
      display: -webkit-flex !important;
      display: -ms-flexbox !important;
      display: flex !important;
      -webkit-flex-basis: auto;
          -ms-flex-preferred-size: auto;
              flex-basis: auto; }
    .navbar-expand-lg .navbar-toggler {
      display: none; } }

@media (max-width: 1199.98px) {
  .navbar-expand-xl > .container,
  .navbar-expand-xl > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 1200px) {
  .navbar-expand-xl {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
            flex-flow: row nowrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
            justify-content: flex-start; }
    .navbar-expand-xl .navbar-nav {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-direction: row;
          -ms-flex-direction: row;
              flex-direction: row; }
      .navbar-expand-xl .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-xl .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-xl > .container,
    .navbar-expand-xl > .container-fluid {
      -webkit-flex-wrap: nowrap;
          -ms-flex-wrap: nowrap;
              flex-wrap: nowrap; }
    .navbar-expand-xl .navbar-collapse {
      display: -webkit-box !important;
      display: -webkit-flex !important;
      display: -ms-flexbox !important;
      display: flex !important;
      -webkit-flex-basis: auto;
          -ms-flex-preferred-size: auto;
              flex-basis: auto; }
    .navbar-expand-xl .navbar-toggler {
      display: none; } }

.navbar-expand {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -webkit-flex-flow: row nowrap;
      -ms-flex-flow: row nowrap;
          flex-flow: row nowrap;
  -webkit-box-pack: start;
  -webkit-justify-content: flex-start;
      -ms-flex-pack: start;
          justify-content: flex-start; }
  .navbar-expand > .container,
  .navbar-expand > .container-fluid {
    padding-right: 0;
    padding-left: 0; }
  .navbar-expand .navbar-nav {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
        -ms-flex-direction: row;
            flex-direction: row; }
    .navbar-expand .navbar-nav .dropdown-menu {
      position: absolute; }
    .navbar-expand .navbar-nav .nav-link {
      padding-right: 0.5rem;
      padding-left: 0.5rem; }
  .navbar-expand > .container,
  .navbar-expand > .container-fluid {
    -webkit-flex-wrap: nowrap;
        -ms-flex-wrap: nowrap;
            flex-wrap: nowrap; }
  .navbar-expand .navbar-collapse {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important;
    -webkit-flex-basis: auto;
        -ms-flex-preferred-size: auto;
            flex-basis: auto; }
  .navbar-expand .navbar-toggler {
    display: none; }

.navbar-light .navbar-brand {
  color: rgba(0, 0, 0, 0.9); }
  .navbar-light .navbar-brand:hover, .navbar-light .navbar-brand:focus {
    color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 0.5); }
  .navbar-light .navbar-nav .nav-link:hover, .navbar-light .navbar-nav .nav-link:focus {
    color: rgba(0, 0, 0, 0.7); }
  .navbar-light .navbar-nav .nav-link.disabled {
    color: rgba(0, 0, 0, 0.3); }

.navbar-light .navbar-nav .show > .nav-link,
.navbar-light .navbar-nav .active > .nav-link,
.navbar-light .navbar-nav .nav-link.show,
.navbar-light .navbar-nav .nav-link.active {
  color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-toggler {
  color: rgba(0, 0, 0, 0.5);
  border-color: rgba(0, 0, 0, 0.1); }

.navbar-light .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e"); }

.navbar-light .navbar-text {
  color: rgba(0, 0, 0, 0.5); }
  .navbar-light .navbar-text a {
    color: rgba(0, 0, 0, 0.9); }
    .navbar-light .navbar-text a:hover, .navbar-light .navbar-text a:focus {
      color: rgba(0, 0, 0, 0.9); }

.navbar-dark .navbar-brand {
  color: #32334a; }
  .navbar-dark .navbar-brand:hover, .navbar-dark .navbar-brand:focus {
    color: #32334a; }

.navbar-dark .navbar-nav .nav-link {
  color: rgba(50, 51, 74, 0.5); }
  .navbar-dark .navbar-nav .nav-link:hover, .navbar-dark .navbar-nav .nav-link:focus {
    color: rgba(50, 51, 74, 0.75); }
  .navbar-dark .navbar-nav .nav-link.disabled {
    color: rgba(50, 51, 74, 0.25); }

.navbar-dark .navbar-nav .show > .nav-link,
.navbar-dark .navbar-nav .active > .nav-link,
.navbar-dark .navbar-nav .nav-link.show,
.navbar-dark .navbar-nav .nav-link.active {
  color: #32334a; }

.navbar-dark .navbar-toggler {
  color: rgba(50, 51, 74, 0.5);
  border-color: rgba(50, 51, 74, 0.1); }

.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(50, 51, 74, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e"); }

.navbar-dark .navbar-text {
  color: rgba(50, 51, 74, 0.5); }
  .navbar-dark .navbar-text a {
    color: #32334a; }
    .navbar-dark .navbar-text a:hover, .navbar-dark .navbar-text a:focus {
      color: #32334a; }

.card {
  position: relative;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #32334a;
  background-clip: border-box;
  border: 1px solid #151623;
  border-radius: 6px; }
  .card > hr {
    margin-right: 0;
    margin-left: 0; }
  .card > .list-group:first-child .list-group-item:first-child {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px; }
  .card > .list-group:last-child .list-group-item:last-child {
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 6px; }

.card-body {
  -webkit-box-flex: 1;
  -webkit-flex: 1 1 auto;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  padding: 1.25rem; }

.card-title {
  margin-bottom: 0.75rem; }

.card-subtitle {
  margin-top: -0.375rem;
  margin-bottom: 0; }

.card-text:last-child {
  margin-bottom: 0; }

.card-link:hover {
  text-decoration: none; }

.card-link + .card-link {
  margin-left: 1.25rem; }

.card-header {
  padding: 0.75rem 1.25rem;
  margin-bottom: 0;
  background-color: #1e2037;
  border-bottom: 1px solid #151623; }
  .card-header:first-child {
    border-radius: calc(6px - 1px) calc(6px - 1px) 0 0; }
  .card-header + .list-group .list-group-item:first-child {
    border-top: 0; }

.card-footer {
  padding: 0.75rem 1.25rem;
  background-color: #1e2037;
  border-top: 1px solid #151623; }
  .card-footer:last-child {
    border-radius: 0 0 calc(6px - 1px) calc(6px - 1px); }

.card-header-tabs {
  margin-right: -0.625rem;
  margin-bottom: -0.75rem;
  margin-left: -0.625rem;
  border-bottom: 0; }

.card-header-pills {
  margin-right: -0.625rem;
  margin-left: -0.625rem; }

.card-img-overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 1.25rem; }

.card-img {
  width: 100%;
  border-radius: calc(6px - 1px); }

.card-img-top {
  width: 100%;
  border-top-left-radius: calc(6px - 1px);
  border-top-right-radius: calc(6px - 1px); }

.card-img-bottom {
  width: 100%;
  border-bottom-right-radius: calc(6px - 1px);
  border-bottom-left-radius: calc(6px - 1px); }

.card-deck {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column; }
  .card-deck .card {
    margin-bottom: 15px; }
  @media (min-width: 576px) {
    .card-deck {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-flow: row wrap;
          -ms-flex-flow: row wrap;
              flex-flow: row wrap;
      margin-right: -15px;
      margin-left: -15px; }
      .card-deck .card {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-flex: 1;
        -webkit-flex: 1 0 0%;
            -ms-flex: 1 0 0%;
                flex: 1 0 0%;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -webkit-flex-direction: column;
            -ms-flex-direction: column;
                flex-direction: column;
        margin-right: 15px;
        margin-bottom: 0;
        margin-left: 15px; } }

.card-group {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column; }
  .card-group > .card {
    margin-bottom: 15px; }
  @media (min-width: 576px) {
    .card-group {
      -webkit-box-orient: horizontal;
      -webkit-box-direction: normal;
      -webkit-flex-flow: row wrap;
          -ms-flex-flow: row wrap;
              flex-flow: row wrap; }
      .card-group > .card {
        -webkit-box-flex: 1;
        -webkit-flex: 1 0 0%;
            -ms-flex: 1 0 0%;
                flex: 1 0 0%;
        margin-bottom: 0; }
        .card-group > .card + .card {
          margin-left: 0;
          border-left: 0; }
        .card-group > .card:not(:last-child) {
          border-top-right-radius: 0;
          border-bottom-right-radius: 0; }
          .card-group > .card:not(:last-child) .card-img-top,
          .card-group > .card:not(:last-child) .card-header {
            border-top-right-radius: 0; }
          .card-group > .card:not(:last-child) .card-img-bottom,
          .card-group > .card:not(:last-child) .card-footer {
            border-bottom-right-radius: 0; }
        .card-group > .card:not(:first-child) {
          border-top-left-radius: 0;
          border-bottom-left-radius: 0; }
          .card-group > .card:not(:first-child) .card-img-top,
          .card-group > .card:not(:first-child) .card-header {
            border-top-left-radius: 0; }
          .card-group > .card:not(:first-child) .card-img-bottom,
          .card-group > .card:not(:first-child) .card-footer {
            border-bottom-left-radius: 0; } }

.card-columns .card {
  margin-bottom: 0.75rem; }

@media (min-width: 576px) {
  .card-columns {
    -webkit-column-count: 3;
       -moz-column-count: 3;
            column-count: 3;
    -webkit-column-gap: 1.25rem;
       -moz-column-gap: 1.25rem;
            column-gap: 1.25rem;
    orphans: 1;
    widows: 1; }
    .card-columns .card {
      display: inline-block;
      width: 100%; } }

.accordion > .card {
  overflow: hidden; }
  .accordion > .card:not(:first-of-type) .card-header:first-child {
    border-radius: 0; }
  .accordion > .card:not(:first-of-type):not(:last-of-type) {
    border-bottom: 0;
    border-radius: 0; }
  .accordion > .card:first-of-type {
    border-bottom: 0;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0; }
  .accordion > .card:last-of-type {
    border-top-left-radius: 0;
    border-top-right-radius: 0; }
  .accordion > .card .card-header {
    margin-bottom: -1px; }

.breadcrumb {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
  list-style: none;
  background-color: #282a38;
  border-radius: 6px; }

.breadcrumb-item + .breadcrumb-item {
  padding-left: 0.5rem; }
  .breadcrumb-item + .breadcrumb-item::before {
    display: inline-block;
    padding-right: 0.5rem;
    color: #1d1e2f;
    content: "/"; }

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: underline; }

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: none; }

.breadcrumb-item.active {
  color: #1d1e2f; }

.pagination {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  padding-left: 0;
  list-style: none;
  border-radius: 6px; }

.page-link {
  position: relative;
  display: block;
  padding: 0.5rem 0.75rem;
  margin-left: -1px;
  line-height: 1.25;
  color: #714cdf;
  background-color: #32334a;
  border: 1px solid #151623; }
  .page-link:hover {
    z-index: 2;
    color: #4922bd;
    text-decoration: none;
    background-color: #282a38;
    border-color: #151623; }
  .page-link:focus {
    z-index: 2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.25); }

.page-item:first-child .page-link {
  margin-left: 0;
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px; }

.page-item:last-child .page-link {
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px; }

.page-item.active .page-link {
  z-index: 1;
  color: #fff;
  background-color: #714cdf;
  border-color: #714cdf; }

.page-item.disabled .page-link {
  color: #11111d;
  pointer-events: none;
  cursor: auto;
  background-color: #32334a;
  border-color: #151623; }

.pagination-lg .page-link {
  padding: 0.75rem 1.5rem;
  font-size: 1.25rem;
  line-height: 1.5; }

.pagination-lg .page-item:first-child .page-link {
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px; }

.pagination-lg .page-item:last-child .page-link {
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px; }

.pagination-sm .page-link {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5; }

.pagination-sm .page-item:first-child .page-link {
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem; }

.pagination-sm .page-item:last-child .page-link {
  border-top-right-radius: 0.2rem;
  border-bottom-right-radius: 0.2rem; }

.badge {
  display: inline-block;
  padding: 0.25em 0.4em;
  font-size: 75%;
  font-weight: 700;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 6px;
  -webkit-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
  -o-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
  @media (prefers-reduced-motion: reduce) {
    .badge {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }
  a.badge:hover, a.badge:focus {
    text-decoration: none; }
  .badge:empty {
    display: none; }

.btn .badge {
  position: relative;
  top: -1px; }

.badge-pill {
  padding-right: 0.6em;
  padding-left: 0.6em;
  border-radius: 10rem; }

.badge-primary {
  color: #fff;
  background-color: #714cdf; }
  a.badge-primary:hover, a.badge-primary:focus {
    color: #fff;
    background-color: #5126d2; }
  a.badge-primary:focus, a.badge-primary.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(113, 76, 223, 0.5); }

.badge-secondary {
  color: #fff;
  background-color: #16a4de; }
  a.badge-secondary:hover, a.badge-secondary:focus {
    color: #fff;
    background-color: #1182b0; }
  a.badge-secondary:focus, a.badge-secondary.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(22, 164, 222, 0.5); }

.badge-success {
  color: #fff;
  background-color: #17b06b; }
  a.badge-success:hover, a.badge-success:focus {
    color: #fff;
    background-color: #118350; }
  a.badge-success:focus, a.badge-success.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(23, 176, 107, 0.5); }

.badge-info {
  color: #fff;
  background-color: #2983fe; }
  a.badge-info:hover, a.badge-info:focus {
    color: #fff;
    background-color: #0167f3; }
  a.badge-info:focus, a.badge-info.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(41, 131, 254, 0.5); }

.badge-warning {
  color: #fff;
  background-color: #f97515; }
  a.badge-warning:hover, a.badge-warning:focus {
    color: #fff;
    background-color: #d65d05; }
  a.badge-warning:focus, a.badge-warning.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(249, 117, 21, 0.5); }

.badge-danger {
  color: #fff;
  background-color: #ff3c5c; }
  a.badge-danger:hover, a.badge-danger:focus {
    color: #fff;
    background-color: #ff0931; }
  a.badge-danger:focus, a.badge-danger.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(255, 60, 92, 0.5); }

.badge-light {
  color: #0a0b14;
  background-color: #dbebfb; }
  a.badge-light:hover, a.badge-light:focus {
    color: #0a0b14;
    background-color: #add2f6; }
  a.badge-light:focus, a.badge-light.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(219, 235, 251, 0.5); }

.badge-dark {
  color: #fff;
  background-color: #32334a; }
  a.badge-dark:hover, a.badge-dark:focus {
    color: #fff;
    background-color: #1d1e2c; }
  a.badge-dark:focus, a.badge-dark.focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5);
            box-shadow: 0 0 0 0.2rem rgba(50, 51, 74, 0.5); }

.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  background-color: #282a38;
  border-radius: 6px; }
  @media (min-width: 576px) {
    .jumbotron {
      padding: 4rem 2rem; } }

.jumbotron-fluid {
  padding-right: 0;
  padding-left: 0;
  border-radius: 0; }

.alert {
  position: relative;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: 6px; }

.alert-heading {
  color: inherit; }

.alert-link {
  font-weight: 700; }

.alert-dismissible {
  padding-right: 4rem; }
  .alert-dismissible .close {
    position: absolute;
    top: 0;
    right: 0;
    padding: 0.75rem 1.25rem;
    color: inherit; }

.alert-primary {
  color: #3b2874;
  background-color: #e3dbf9;
  border-color: #d7cdf6; }
  .alert-primary hr {
    border-top-color: #c6b7f2; }
  .alert-primary .alert-link {
    color: #281b4e; }

.alert-secondary {
  color: #0b5573;
  background-color: #d0edf8;
  border-color: #bee6f6; }
  .alert-secondary hr {
    border-top-color: #a8ddf3; }
  .alert-secondary .alert-link {
    color: #073344; }

.alert-success {
  color: #0c5c38;
  background-color: #d1efe1;
  border-color: #bee9d6; }
  .alert-success hr {
    border-top-color: #abe3ca; }
  .alert-success .alert-link {
    color: #062f1d; }

.alert-info {
  color: #154484;
  background-color: #d4e6ff;
  border-color: #c3dcff; }
  .alert-info hr {
    border-top-color: #aacdff; }
  .alert-info .alert-link {
    color: #0e2d58; }

.alert-warning {
  color: #813d0b;
  background-color: #fee3d0;
  border-color: #fdd8bd; }
  .alert-warning hr {
    border-top-color: #fcc9a4; }
  .alert-warning .alert-link {
    color: #522707; }

.alert-danger {
  color: #851f30;
  background-color: #ffd8de;
  border-color: #ffc8d1; }
  .alert-danger hr {
    border-top-color: #ffafbc; }
  .alert-danger .alert-link {
    color: #5c1521; }

.alert-light {
  color: #727a83;
  background-color: #f8fbfe;
  border-color: #f5f9fe; }
  .alert-light hr {
    border-top-color: #deebfc; }
  .alert-light .alert-link {
    color: #5a6168; }

.alert-dark {
  color: #1a1b26;
  background-color: #d6d6db;
  border-color: #c6c6cc; }
  .alert-dark hr {
    border-top-color: #b9b9c0; }
  .alert-dark .alert-link {
    color: #050508; }

@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 1rem 0; }
  to {
    background-position: 0 0; } }

@-o-keyframes progress-bar-stripes {
  from {
    background-position: 1rem 0; }
  to {
    background-position: 0 0; } }

@keyframes progress-bar-stripes {
  from {
    background-position: 1rem 0; }
  to {
    background-position: 0 0; } }

.progress {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  height: 1rem;
  overflow: hidden;
  font-size: 0.75rem;
  background-color: #282a38;
  border-radius: 6px; }

.progress-bar {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
      -ms-flex-pack: center;
          justify-content: center;
  color: #32334a;
  text-align: center;
  white-space: nowrap;
  background-color: #714cdf;
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease; }
  @media (prefers-reduced-motion: reduce) {
    .progress-bar {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }

.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  -webkit-background-size: 1rem 1rem;
          background-size: 1rem 1rem; }

.progress-bar-animated {
  -webkit-animation: progress-bar-stripes 1s linear infinite;
       -o-animation: progress-bar-stripes 1s linear infinite;
          animation: progress-bar-stripes 1s linear infinite; }
  @media (prefers-reduced-motion: reduce) {
    .progress-bar-animated {
      -webkit-animation: none;
           -o-animation: none;
              animation: none; } }

.media {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -webkit-align-items: flex-start;
      -ms-flex-align: start;
          align-items: flex-start; }

.media-body {
  -webkit-box-flex: 1;
  -webkit-flex: 1;
      -ms-flex: 1;
          flex: 1; }

.list-group {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  padding-left: 0;
  margin-bottom: 0; }

.list-group-item-action {
  width: 100%;
  color: #e4e2ff;
  text-align: inherit; }
  .list-group-item-action:hover, .list-group-item-action:focus {
    z-index: 1;
    color: #e4e2ff;
    text-decoration: none;
    background-color: #2d2e3f; }
  .list-group-item-action:active {
    color: #e4e2ff;
    background-color: #282a38; }

.list-group-item {
  position: relative;
  display: block;
  padding: 0.75rem 1.25rem;
  margin-bottom: -1px;
  background-color: #32334a;
  border: 1px solid rgba(0, 0, 0, 0.125); }
  .list-group-item:first-child {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px; }
  .list-group-item:last-child {
    margin-bottom: 0;
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 6px; }
  .list-group-item.disabled, .list-group-item:disabled {
    color: #1d1e2f;
    pointer-events: none;
    background-color: #32334a; }
  .list-group-item.active {
    z-index: 2;
    color: #32334a;
    background-color: #714cdf;
    border-color: #714cdf; }

.list-group-horizontal {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -webkit-flex-direction: row;
      -ms-flex-direction: row;
          flex-direction: row; }
  .list-group-horizontal .list-group-item {
    margin-right: -1px;
    margin-bottom: 0; }
    .list-group-horizontal .list-group-item:first-child {
      border-top-left-radius: 6px;
      border-bottom-left-radius: 6px;
      border-top-right-radius: 0; }
    .list-group-horizontal .list-group-item:last-child {
      margin-right: 0;
      border-top-right-radius: 6px;
      border-bottom-right-radius: 6px;
      border-bottom-left-radius: 0; }

@media (min-width: 576px) {
  .list-group-horizontal-sm {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
        -ms-flex-direction: row;
            flex-direction: row; }
    .list-group-horizontal-sm .list-group-item {
      margin-right: -1px;
      margin-bottom: 0; }
      .list-group-horizontal-sm .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0; }
      .list-group-horizontal-sm .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0; } }

@media (min-width: 768px) {
  .list-group-horizontal-md {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
        -ms-flex-direction: row;
            flex-direction: row; }
    .list-group-horizontal-md .list-group-item {
      margin-right: -1px;
      margin-bottom: 0; }
      .list-group-horizontal-md .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0; }
      .list-group-horizontal-md .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0; } }

@media (min-width: 992px) {
  .list-group-horizontal-lg {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
        -ms-flex-direction: row;
            flex-direction: row; }
    .list-group-horizontal-lg .list-group-item {
      margin-right: -1px;
      margin-bottom: 0; }
      .list-group-horizontal-lg .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0; }
      .list-group-horizontal-lg .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0; } }

@media (min-width: 1200px) {
  .list-group-horizontal-xl {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
        -ms-flex-direction: row;
            flex-direction: row; }
    .list-group-horizontal-xl .list-group-item {
      margin-right: -1px;
      margin-bottom: 0; }
      .list-group-horizontal-xl .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0; }
      .list-group-horizontal-xl .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0; } }

.list-group-flush .list-group-item {
  border-right: 0;
  border-left: 0;
  border-radius: 0; }
  .list-group-flush .list-group-item:last-child {
    margin-bottom: -1px; }

.list-group-flush:first-child .list-group-item:first-child {
  border-top: 0; }

.list-group-flush:last-child .list-group-item:last-child {
  margin-bottom: 0;
  border-bottom: 0; }

.list-group-item-primary {
  color: #3b2874;
  background-color: #d7cdf6; }
  .list-group-item-primary.list-group-item-action:hover, .list-group-item-primary.list-group-item-action:focus {
    color: #3b2874;
    background-color: #c6b7f2; }
  .list-group-item-primary.list-group-item-action.active {
    color: #fff;
    background-color: #3b2874;
    border-color: #3b2874; }

.list-group-item-secondary {
  color: #0b5573;
  background-color: #bee6f6; }
  .list-group-item-secondary.list-group-item-action:hover, .list-group-item-secondary.list-group-item-action:focus {
    color: #0b5573;
    background-color: #a8ddf3; }
  .list-group-item-secondary.list-group-item-action.active {
    color: #fff;
    background-color: #0b5573;
    border-color: #0b5573; }

.list-group-item-success {
  color: #0c5c38;
  background-color: #bee9d6; }
  .list-group-item-success.list-group-item-action:hover, .list-group-item-success.list-group-item-action:focus {
    color: #0c5c38;
    background-color: #abe3ca; }
  .list-group-item-success.list-group-item-action.active {
    color: #fff;
    background-color: #0c5c38;
    border-color: #0c5c38; }

.list-group-item-info {
  color: #154484;
  background-color: #c3dcff; }
  .list-group-item-info.list-group-item-action:hover, .list-group-item-info.list-group-item-action:focus {
    color: #154484;
    background-color: #aacdff; }
  .list-group-item-info.list-group-item-action.active {
    color: #fff;
    background-color: #154484;
    border-color: #154484; }

.list-group-item-warning {
  color: #813d0b;
  background-color: #fdd8bd; }
  .list-group-item-warning.list-group-item-action:hover, .list-group-item-warning.list-group-item-action:focus {
    color: #813d0b;
    background-color: #fcc9a4; }
  .list-group-item-warning.list-group-item-action.active {
    color: #fff;
    background-color: #813d0b;
    border-color: #813d0b; }

.list-group-item-danger {
  color: #851f30;
  background-color: #ffc8d1; }
  .list-group-item-danger.list-group-item-action:hover, .list-group-item-danger.list-group-item-action:focus {
    color: #851f30;
    background-color: #ffafbc; }
  .list-group-item-danger.list-group-item-action.active {
    color: #fff;
    background-color: #851f30;
    border-color: #851f30; }

.list-group-item-light {
  color: #727a83;
  background-color: #f5f9fe; }
  .list-group-item-light.list-group-item-action:hover, .list-group-item-light.list-group-item-action:focus {
    color: #727a83;
    background-color: #deebfc; }
  .list-group-item-light.list-group-item-action.active {
    color: #fff;
    background-color: #727a83;
    border-color: #727a83; }

.list-group-item-dark {
  color: #1a1b26;
  background-color: #c6c6cc; }
  .list-group-item-dark.list-group-item-action:hover, .list-group-item-dark.list-group-item-action:focus {
    color: #1a1b26;
    background-color: #b9b9c0; }
  .list-group-item-dark.list-group-item-action.active {
    color: #fff;
    background-color: #1a1b26;
    border-color: #1a1b26; }

.close {
  float: right;
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #32334a;
  opacity: .5; }
  .close:hover {
    color: #000;
    text-decoration: none; }
  .close:not(:disabled):not(.disabled):hover, .close:not(:disabled):not(.disabled):focus {
    opacity: .75; }

button.close {
  padding: 0;
  background-color: transparent;
  border: 0;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none; }

a.close.disabled {
  pointer-events: none; }

.toast {
  max-width: 350px;
  overflow: hidden;
  font-size: 0.875rem;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.1);
  -webkit-box-shadow: 0 0.25rem 0.75rem rgba(0, 0, 0, 0.1);
          box-shadow: 0 0.25rem 0.75rem rgba(0, 0, 0, 0.1);
  -webkit-backdrop-filter: blur(10px);
          backdrop-filter: blur(10px);
  opacity: 0;
  border-radius: 0.25rem; }
  .toast:not(:last-child) {
    margin-bottom: 0.75rem; }
  .toast.showing {
    opacity: 1; }
  .toast.show {
    display: block;
    opacity: 1; }
  .toast.hide {
    display: none; }

.toast-header {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  padding: 0.25rem 0.75rem;
  color: #1d1e2f;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05); }

.toast-body {
  padding: 0.75rem; }

.modal-open {
  overflow: hidden; }
  .modal-open .modal {
    overflow-x: hidden;
    overflow-y: auto; }

.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  display: none;
  width: 100%;
  height: 100%;
  overflow: hidden;
  outline: 0; }

.modal-dialog {
  position: relative;
  width: auto;
  margin: 0.5rem;
  pointer-events: none; }
  .modal.fade .modal-dialog {
    -webkit-transition: -webkit-transform 0.3s ease-out;
    transition: -webkit-transform 0.3s ease-out;
    -o-transition: -o-transform 0.3s ease-out;
    transition: transform 0.3s ease-out;
    transition: transform 0.3s ease-out, -webkit-transform 0.3s ease-out, -o-transform 0.3s ease-out;
    -webkit-transform: translate(0, -50px);
         -o-transform: translate(0, -50px);
            transform: translate(0, -50px); }
    @media (prefers-reduced-motion: reduce) {
      .modal.fade .modal-dialog {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
  .modal.show .modal-dialog {
    -webkit-transform: none;
         -o-transform: none;
            transform: none; }

.modal-dialog-scrollable {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  max-height: calc(100% - 1rem); }
  .modal-dialog-scrollable .modal-content {
    max-height: calc(100vh - 1rem);
    overflow: hidden; }
  .modal-dialog-scrollable .modal-header,
  .modal-dialog-scrollable .modal-footer {
    -webkit-flex-shrink: 0;
        -ms-flex-negative: 0;
            flex-shrink: 0; }
  .modal-dialog-scrollable .modal-body {
    overflow-y: auto; }

.modal-dialog-centered {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  min-height: calc(100% - 1rem); }
  .modal-dialog-centered::before {
    display: block;
    height: calc(100vh - 1rem);
    content: ""; }
  .modal-dialog-centered.modal-dialog-scrollable {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
        -ms-flex-direction: column;
            flex-direction: column;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
        -ms-flex-pack: center;
            justify-content: center;
    height: 100%; }
    .modal-dialog-centered.modal-dialog-scrollable .modal-content {
      max-height: none; }
    .modal-dialog-centered.modal-dialog-scrollable::before {
      content: none; }

.modal-content {
  position: relative;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #32334a;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 6px;
  outline: 0; }

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1040;
  width: 100vw;
  height: 100vh;
  background-color: #000; }
  .modal-backdrop.fade {
    opacity: 0; }
  .modal-backdrop.show {
    opacity: 0.5; }

.modal-header {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -webkit-align-items: flex-start;
      -ms-flex-align: start;
          align-items: flex-start;
  -webkit-box-pack: justify;
  -webkit-justify-content: space-between;
      -ms-flex-pack: justify;
          justify-content: space-between;
  padding: 1rem 1rem;
  border-bottom: 1px solid #28293e;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px; }
  .modal-header .close {
    padding: 1rem 1rem;
    margin: -1rem -1rem -1rem auto; }

.modal-title {
  margin-bottom: 0;
  line-height: 1.5; }

.modal-body {
  position: relative;
  -webkit-box-flex: 1;
  -webkit-flex: 1 1 auto;
      -ms-flex: 1 1 auto;
          flex: 1 1 auto;
  padding: 1rem; }

.modal-footer {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: end;
  -webkit-justify-content: flex-end;
      -ms-flex-pack: end;
          justify-content: flex-end;
  padding: 1rem;
  border-top: 1px solid #28293e;
  border-bottom-right-radius: 6px;
  border-bottom-left-radius: 6px; }
  .modal-footer > :not(:first-child) {
    margin-left: .25rem; }
  .modal-footer > :not(:last-child) {
    margin-right: .25rem; }

.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll; }

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 500px;
    margin: 1.75rem auto; }
  .modal-dialog-scrollable {
    max-height: calc(100% - 3.5rem); }
    .modal-dialog-scrollable .modal-content {
      max-height: calc(100vh - 3.5rem); }
  .modal-dialog-centered {
    min-height: calc(100% - 3.5rem); }
    .modal-dialog-centered::before {
      height: calc(100vh - 3.5rem); }
  .modal-sm {
    max-width: 300px; } }

@media (min-width: 992px) {
  .modal-lg,
  .modal-xl {
    max-width: 800px; } }

@media (min-width: 1200px) {
  .modal-xl {
    max-width: 1140px; } }

.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  margin: 0;
  font-family: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-style: normal;
  font-weight: 400;
  line-height: 1.5;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  opacity: 0; }
  .tooltip.show {
    opacity: 0.9; }
  .tooltip .arrow {
    position: absolute;
    display: block;
    width: 0.8rem;
    height: 0.4rem; }
    .tooltip .arrow::before {
      position: absolute;
      content: "";
      border-color: transparent;
      border-style: solid; }

.bs-tooltip-top, .bs-tooltip-auto[x-placement^="top"] {
  padding: 0.4rem 0; }
  .bs-tooltip-top .arrow, .bs-tooltip-auto[x-placement^="top"] .arrow {
    bottom: 0; }
    .bs-tooltip-top .arrow::before, .bs-tooltip-auto[x-placement^="top"] .arrow::before {
      top: 0;
      border-width: 0.4rem 0.4rem 0;
      border-top-color: #000; }

.bs-tooltip-right, .bs-tooltip-auto[x-placement^="right"] {
  padding: 0 0.4rem; }
  .bs-tooltip-right .arrow, .bs-tooltip-auto[x-placement^="right"] .arrow {
    left: 0;
    width: 0.4rem;
    height: 0.8rem; }
    .bs-tooltip-right .arrow::before, .bs-tooltip-auto[x-placement^="right"] .arrow::before {
      right: 0;
      border-width: 0.4rem 0.4rem 0.4rem 0;
      border-right-color: #000; }

.bs-tooltip-bottom, .bs-tooltip-auto[x-placement^="bottom"] {
  padding: 0.4rem 0; }
  .bs-tooltip-bottom .arrow, .bs-tooltip-auto[x-placement^="bottom"] .arrow {
    top: 0; }
    .bs-tooltip-bottom .arrow::before, .bs-tooltip-auto[x-placement^="bottom"] .arrow::before {
      bottom: 0;
      border-width: 0 0.4rem 0.4rem;
      border-bottom-color: #000; }

.bs-tooltip-left, .bs-tooltip-auto[x-placement^="left"] {
  padding: 0 0.4rem; }
  .bs-tooltip-left .arrow, .bs-tooltip-auto[x-placement^="left"] .arrow {
    right: 0;
    width: 0.4rem;
    height: 0.8rem; }
    .bs-tooltip-left .arrow::before, .bs-tooltip-auto[x-placement^="left"] .arrow::before {
      left: 0;
      border-width: 0.4rem 0 0.4rem 0.4rem;
      border-left-color: #000; }

.tooltip-inner {
  max-width: 200px;
  padding: 0.25rem 0.5rem;
  color: #e4e2ff;
  text-align: center;
  background-color: #000;
  border-radius: 6px; }

.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: block;
  max-width: 276px;
  font-family: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-style: normal;
  font-weight: 400;
  line-height: 1.5;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  background-color: #32334a;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 6px; }
  .popover .arrow {
    position: absolute;
    display: block;
    width: 1rem;
    height: 0.5rem;
    margin: 0 6px; }
    .popover .arrow::before, .popover .arrow::after {
      position: absolute;
      display: block;
      content: "";
      border-color: transparent;
      border-style: solid; }

.bs-popover-top, .bs-popover-auto[x-placement^="top"] {
  margin-bottom: 0.5rem; }
  .bs-popover-top > .arrow, .bs-popover-auto[x-placement^="top"] > .arrow {
    bottom: calc((0.5rem + 1px) * -1); }
    .bs-popover-top > .arrow::before, .bs-popover-auto[x-placement^="top"] > .arrow::before {
      bottom: 0;
      border-width: 0.5rem 0.5rem 0;
      border-top-color: rgba(0, 0, 0, 0.25); }
    .bs-popover-top > .arrow::after, .bs-popover-auto[x-placement^="top"] > .arrow::after {
      bottom: 1px;
      border-width: 0.5rem 0.5rem 0;
      border-top-color: #32334a; }

.bs-popover-right, .bs-popover-auto[x-placement^="right"] {
  margin-left: 0.5rem; }
  .bs-popover-right > .arrow, .bs-popover-auto[x-placement^="right"] > .arrow {
    left: calc((0.5rem + 1px) * -1);
    width: 0.5rem;
    height: 1rem;
    margin: 6px 0; }
    .bs-popover-right > .arrow::before, .bs-popover-auto[x-placement^="right"] > .arrow::before {
      left: 0;
      border-width: 0.5rem 0.5rem 0.5rem 0;
      border-right-color: rgba(0, 0, 0, 0.25); }
    .bs-popover-right > .arrow::after, .bs-popover-auto[x-placement^="right"] > .arrow::after {
      left: 1px;
      border-width: 0.5rem 0.5rem 0.5rem 0;
      border-right-color: #32334a; }

.bs-popover-bottom, .bs-popover-auto[x-placement^="bottom"] {
  margin-top: 0.5rem; }
  .bs-popover-bottom > .arrow, .bs-popover-auto[x-placement^="bottom"] > .arrow {
    top: calc((0.5rem + 1px) * -1); }
    .bs-popover-bottom > .arrow::before, .bs-popover-auto[x-placement^="bottom"] > .arrow::before {
      top: 0;
      border-width: 0 0.5rem 0.5rem 0.5rem;
      border-bottom-color: rgba(0, 0, 0, 0.25); }
    .bs-popover-bottom > .arrow::after, .bs-popover-auto[x-placement^="bottom"] > .arrow::after {
      top: 1px;
      border-width: 0 0.5rem 0.5rem 0.5rem;
      border-bottom-color: #32334a; }
  .bs-popover-bottom .popover-header::before, .bs-popover-auto[x-placement^="bottom"] .popover-header::before {
    position: absolute;
    top: 0;
    left: 50%;
    display: block;
    width: 1rem;
    margin-left: -0.5rem;
    content: "";
    border-bottom: 1px solid #2c2d41; }

.bs-popover-left, .bs-popover-auto[x-placement^="left"] {
  margin-right: 0.5rem; }
  .bs-popover-left > .arrow, .bs-popover-auto[x-placement^="left"] > .arrow {
    right: calc((0.5rem + 1px) * -1);
    width: 0.5rem;
    height: 1rem;
    margin: 6px 0; }
    .bs-popover-left > .arrow::before, .bs-popover-auto[x-placement^="left"] > .arrow::before {
      right: 0;
      border-width: 0.5rem 0 0.5rem 0.5rem;
      border-left-color: rgba(0, 0, 0, 0.25); }
    .bs-popover-left > .arrow::after, .bs-popover-auto[x-placement^="left"] > .arrow::after {
      right: 1px;
      border-width: 0.5rem 0 0.5rem 0.5rem;
      border-left-color: #32334a; }

.popover-header {
  padding: 0.5rem 0.75rem;
  margin-bottom: 0;
  font-size: 1rem;
  background-color: #2c2d41;
  border-bottom: 1px solid #222232;
  border-top-left-radius: calc(6px - 1px);
  border-top-right-radius: calc(6px - 1px); }
  .popover-header:empty {
    display: none; }

.popover-body {
  padding: 0.5rem 0.75rem;
  color: #e4e2ff; }

.carousel {
  position: relative; }

.carousel.pointer-event {
  -ms-touch-action: pan-y;
      touch-action: pan-y; }

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden; }
  .carousel-inner::after {
    display: block;
    clear: both;
    content: ""; }

.carousel-item {
  position: relative;
  display: none;
  float: left;
  width: 100%;
  margin-right: -100%;
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
  -webkit-transition: -webkit-transform 0.6s ease-in-out;
  transition: -webkit-transform 0.6s ease-in-out;
  -o-transition: -o-transform 0.6s ease-in-out;
  transition: transform 0.6s ease-in-out;
  transition: transform 0.6s ease-in-out, -webkit-transform 0.6s ease-in-out, -o-transform 0.6s ease-in-out; }
  @media (prefers-reduced-motion: reduce) {
    .carousel-item {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }

.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
  display: block; }

.carousel-item-next:not(.carousel-item-left),
.active.carousel-item-right {
  -webkit-transform: translateX(100%);
       -o-transform: translateX(100%);
          transform: translateX(100%); }

.carousel-item-prev:not(.carousel-item-right),
.active.carousel-item-left {
  -webkit-transform: translateX(-100%);
       -o-transform: translateX(-100%);
          transform: translateX(-100%); }

.carousel-fade .carousel-item {
  opacity: 0;
  -webkit-transition-property: opacity;
  -o-transition-property: opacity;
  transition-property: opacity;
  -webkit-transform: none;
       -o-transform: none;
          transform: none; }

.carousel-fade .carousel-item.active,
.carousel-fade .carousel-item-next.carousel-item-left,
.carousel-fade .carousel-item-prev.carousel-item-right {
  z-index: 1;
  opacity: 1; }

.carousel-fade .active.carousel-item-left,
.carousel-fade .active.carousel-item-right {
  z-index: 0;
  opacity: 0;
  -webkit-transition: 0s 0.6s opacity;
  -o-transition: 0s 0.6s opacity;
  transition: 0s 0.6s opacity; }
  @media (prefers-reduced-motion: reduce) {
    .carousel-fade .active.carousel-item-left,
    .carousel-fade .active.carousel-item-right {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 1;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
      -ms-flex-pack: center;
          justify-content: center;
  width: 15%;
  color: #32334a;
  text-align: center;
  opacity: 0.5;
  -webkit-transition: opacity 0.15s ease;
  -o-transition: opacity 0.15s ease;
  transition: opacity 0.15s ease; }
  @media (prefers-reduced-motion: reduce) {
    .carousel-control-prev,
    .carousel-control-next {
      -webkit-transition: none;
      -o-transition: none;
      transition: none; } }
  .carousel-control-prev:hover, .carousel-control-prev:focus,
  .carousel-control-next:hover,
  .carousel-control-next:focus {
    color: #32334a;
    text-decoration: none;
    outline: 0;
    opacity: 0.9; }

.carousel-control-prev {
  left: 0; }

.carousel-control-next {
  right: 0; }

.carousel-control-prev-icon,
.carousel-control-next-icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  background: no-repeat 50% / 100% 100%; }

.carousel-control-prev-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%2332334a' viewBox='0 0 8 8'%3e%3cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3e%3c/svg%3e"); }

.carousel-control-next-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%2332334a' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3e%3c/svg%3e"); }

.carousel-indicators {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 15;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
      -ms-flex-pack: center;
          justify-content: center;
  padding-left: 0;
  margin-right: 15%;
  margin-left: 15%;
  list-style: none; }
  .carousel-indicators li {
    -webkit-box-sizing: content-box;
            box-sizing: content-box;
    -webkit-box-flex: 0;
    -webkit-flex: 0 1 auto;
        -ms-flex: 0 1 auto;
            flex: 0 1 auto;
    width: 30px;
    height: 3px;
    margin-right: 3px;
    margin-left: 3px;
    text-indent: -999px;
    cursor: pointer;
    background-color: #32334a;
    background-clip: padding-box;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    opacity: .5;
    -webkit-transition: opacity 0.6s ease;
    -o-transition: opacity 0.6s ease;
    transition: opacity 0.6s ease; }
    @media (prefers-reduced-motion: reduce) {
      .carousel-indicators li {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
  .carousel-indicators .active {
    opacity: 1; }

.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 15%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #32334a;
  text-align: center; }

@-webkit-keyframes spinner-border {
  to {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg); } }

@-o-keyframes spinner-border {
  to {
    -o-transform: rotate(360deg);
       transform: rotate(360deg); } }

@keyframes spinner-border {
  to {
    -webkit-transform: rotate(360deg);
         -o-transform: rotate(360deg);
            transform: rotate(360deg); } }

.spinner-border {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  border: 0.25em solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  -webkit-animation: spinner-border .75s linear infinite;
       -o-animation: spinner-border .75s linear infinite;
          animation: spinner-border .75s linear infinite; }

.spinner-border-sm {
  width: 1rem;
  height: 1rem;
  border-width: 0.2em; }

@-webkit-keyframes spinner-grow {
  0% {
    -webkit-transform: scale(0);
            transform: scale(0); }
  50% {
    opacity: 1; } }

@-o-keyframes spinner-grow {
  0% {
    -o-transform: scale(0);
       transform: scale(0); }
  50% {
    opacity: 1; } }

@keyframes spinner-grow {
  0% {
    -webkit-transform: scale(0);
         -o-transform: scale(0);
            transform: scale(0); }
  50% {
    opacity: 1; } }

.spinner-grow {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  background-color: currentColor;
  border-radius: 50%;
  opacity: 0;
  -webkit-animation: spinner-grow .75s linear infinite;
       -o-animation: spinner-grow .75s linear infinite;
          animation: spinner-grow .75s linear infinite; }

.spinner-grow-sm {
  width: 1rem;
  height: 1rem; }

.align-baseline {
  vertical-align: baseline !important; }

.align-top {
  vertical-align: top !important; }

.align-middle {
  vertical-align: middle !important; }

.align-bottom {
  vertical-align: bottom !important; }

.align-text-bottom {
  vertical-align: text-bottom !important; }

.align-text-top {
  vertical-align: text-top !important; }

.bg-primary {
  background-color: #714cdf !important; }

a.bg-primary:hover, a.bg-primary:focus,
button.bg-primary:hover,
button.bg-primary:focus {
  background-color: #5126d2 !important; }

.bg-secondary {
  background-color: #16a4de !important; }

a.bg-secondary:hover, a.bg-secondary:focus,
button.bg-secondary:hover,
button.bg-secondary:focus {
  background-color: #1182b0 !important; }

.bg-success {
  background-color: #17b06b !important; }

a.bg-success:hover, a.bg-success:focus,
button.bg-success:hover,
button.bg-success:focus {
  background-color: #118350 !important; }

.bg-info {
  background-color: #2983fe !important; }

a.bg-info:hover, a.bg-info:focus,
button.bg-info:hover,
button.bg-info:focus {
  background-color: #0167f3 !important; }

.bg-warning {
  background-color: #f97515 !important; }

a.bg-warning:hover, a.bg-warning:focus,
button.bg-warning:hover,
button.bg-warning:focus {
  background-color: #d65d05 !important; }

.bg-danger {
  background-color: #ff3c5c !important; }

a.bg-danger:hover, a.bg-danger:focus,
button.bg-danger:hover,
button.bg-danger:focus {
  background-color: #ff0931 !important; }

.bg-light {
  background-color: #dbebfb !important; }

a.bg-light:hover, a.bg-light:focus,
button.bg-light:hover,
button.bg-light:focus {
  background-color: #add2f6 !important; }

.bg-dark {
  background-color: #32334a !important; }

a.bg-dark:hover, a.bg-dark:focus,
button.bg-dark:hover,
button.bg-dark:focus {
  background-color: #1d1e2c !important; }

.bg-white {
  background-color: #fff !important; }

.bg-transparent {
  background-color: transparent !important; }

.border {
  border: 1px solid #28293e !important; }

.border-top {
  border-top: 1px solid #28293e !important; }

.border-right {
  border-right: 1px solid #28293e !important; }

.border-bottom {
  border-bottom: 1px solid #28293e !important; }

.border-left {
  border-left: 1px solid #28293e !important; }

.border-0 {
  border: 0 !important; }

.border-top-0 {
  border-top: 0 !important; }

.border-right-0 {
  border-right: 0 !important; }

.border-bottom-0 {
  border-bottom: 0 !important; }

.border-left-0 {
  border-left: 0 !important; }

.border-primary {
  border-color: #714cdf !important; }

.border-secondary {
  border-color: #16a4de !important; }

.border-success {
  border-color: #17b06b !important; }

.border-info {
  border-color: #2983fe !important; }

.border-warning {
  border-color: #f97515 !important; }

.border-danger {
  border-color: #ff3c5c !important; }

.border-light {
  border-color: #dbebfb !important; }

.border-dark {
  border-color: #32334a !important; }

.border-white {
  border-color: #fff !important; }

.rounded-sm {
  border-radius: 0.2rem !important; }

.rounded {
  border-radius: 6px !important; }

.rounded-top {
  border-top-left-radius: 6px !important;
  border-top-right-radius: 6px !important; }

.rounded-right {
  border-top-right-radius: 6px !important;
  border-bottom-right-radius: 6px !important; }

.rounded-bottom {
  border-bottom-right-radius: 6px !important;
  border-bottom-left-radius: 6px !important; }

.rounded-left {
  border-top-left-radius: 6px !important;
  border-bottom-left-radius: 6px !important; }

.rounded-lg {
  border-radius: 6px !important; }

.rounded-circle {
  border-radius: 50% !important; }

.rounded-pill {
  border-radius: 50rem !important; }

.rounded-0 {
  border-radius: 0 !important; }

.clearfix::after {
  display: block;
  clear: both;
  content: ""; }

.d-none {
  display: none !important; }

.d-inline {
  display: inline !important; }

.d-inline-block {
  display: inline-block !important; }

.d-block {
  display: block !important; }

.d-table {
  display: table !important; }

.d-table-row {
  display: table-row !important; }

.d-table-cell {
  display: table-cell !important; }

.d-flex {
  display: -webkit-box !important;
  display: -webkit-flex !important;
  display: -ms-flexbox !important;
  display: flex !important; }

.d-inline-flex {
  display: -webkit-inline-box !important;
  display: -webkit-inline-flex !important;
  display: -ms-inline-flexbox !important;
  display: inline-flex !important; }

@media (min-width: 576px) {
  .d-sm-none {
    display: none !important; }
  .d-sm-inline {
    display: inline !important; }
  .d-sm-inline-block {
    display: inline-block !important; }
  .d-sm-block {
    display: block !important; }
  .d-sm-table {
    display: table !important; }
  .d-sm-table-row {
    display: table-row !important; }
  .d-sm-table-cell {
    display: table-cell !important; }
  .d-sm-flex {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  .d-sm-inline-flex {
    display: -webkit-inline-box !important;
    display: -webkit-inline-flex !important;
    display: -ms-inline-flexbox !important;
    display: inline-flex !important; } }

@media (min-width: 768px) {
  .d-md-none {
    display: none !important; }
  .d-md-inline {
    display: inline !important; }
  .d-md-inline-block {
    display: inline-block !important; }
  .d-md-block {
    display: block !important; }
  .d-md-table {
    display: table !important; }
  .d-md-table-row {
    display: table-row !important; }
  .d-md-table-cell {
    display: table-cell !important; }
  .d-md-flex {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  .d-md-inline-flex {
    display: -webkit-inline-box !important;
    display: -webkit-inline-flex !important;
    display: -ms-inline-flexbox !important;
    display: inline-flex !important; } }

@media (min-width: 992px) {
  .d-lg-none {
    display: none !important; }
  .d-lg-inline {
    display: inline !important; }
  .d-lg-inline-block {
    display: inline-block !important; }
  .d-lg-block {
    display: block !important; }
  .d-lg-table {
    display: table !important; }
  .d-lg-table-row {
    display: table-row !important; }
  .d-lg-table-cell {
    display: table-cell !important; }
  .d-lg-flex {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  .d-lg-inline-flex {
    display: -webkit-inline-box !important;
    display: -webkit-inline-flex !important;
    display: -ms-inline-flexbox !important;
    display: inline-flex !important; } }

@media (min-width: 1200px) {
  .d-xl-none {
    display: none !important; }
  .d-xl-inline {
    display: inline !important; }
  .d-xl-inline-block {
    display: inline-block !important; }
  .d-xl-block {
    display: block !important; }
  .d-xl-table {
    display: table !important; }
  .d-xl-table-row {
    display: table-row !important; }
  .d-xl-table-cell {
    display: table-cell !important; }
  .d-xl-flex {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  .d-xl-inline-flex {
    display: -webkit-inline-box !important;
    display: -webkit-inline-flex !important;
    display: -ms-inline-flexbox !important;
    display: inline-flex !important; } }

@media print {
  .d-print-none {
    display: none !important; }
  .d-print-inline {
    display: inline !important; }
  .d-print-inline-block {
    display: inline-block !important; }
  .d-print-block {
    display: block !important; }
  .d-print-table {
    display: table !important; }
  .d-print-table-row {
    display: table-row !important; }
  .d-print-table-cell {
    display: table-cell !important; }
  .d-print-flex {
    display: -webkit-box !important;
    display: -webkit-flex !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  .d-print-inline-flex {
    display: -webkit-inline-box !important;
    display: -webkit-inline-flex !important;
    display: -ms-inline-flexbox !important;
    display: inline-flex !important; } }

.embed-responsive {
  position: relative;
  display: block;
  width: 100%;
  padding: 0;
  overflow: hidden; }
  .embed-responsive::before {
    display: block;
    content: ""; }
  .embed-responsive .embed-responsive-item,
  .embed-responsive iframe,
  .embed-responsive embed,
  .embed-responsive object,
  .embed-responsive video {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0; }

.embed-responsive-21by9::before {
  padding-top: 42.85714%; }

.embed-responsive-16by9::before {
  padding-top: 56.25%; }

.embed-responsive-4by3::before {
  padding-top: 75%; }

.embed-responsive-1by1::before {
  padding-top: 100%; }

.flex-row {
  -webkit-box-orient: horizontal !important;
  -webkit-box-direction: normal !important;
  -webkit-flex-direction: row !important;
      -ms-flex-direction: row !important;
          flex-direction: row !important; }

.flex-column {
  -webkit-box-orient: vertical !important;
  -webkit-box-direction: normal !important;
  -webkit-flex-direction: column !important;
      -ms-flex-direction: column !important;
          flex-direction: column !important; }

.flex-row-reverse {
  -webkit-box-orient: horizontal !important;
  -webkit-box-direction: reverse !important;
  -webkit-flex-direction: row-reverse !important;
      -ms-flex-direction: row-reverse !important;
          flex-direction: row-reverse !important; }

.flex-column-reverse {
  -webkit-box-orient: vertical !important;
  -webkit-box-direction: reverse !important;
  -webkit-flex-direction: column-reverse !important;
      -ms-flex-direction: column-reverse !important;
          flex-direction: column-reverse !important; }

.flex-wrap {
  -webkit-flex-wrap: wrap !important;
      -ms-flex-wrap: wrap !important;
          flex-wrap: wrap !important; }

.flex-nowrap {
  -webkit-flex-wrap: nowrap !important;
      -ms-flex-wrap: nowrap !important;
          flex-wrap: nowrap !important; }

.flex-wrap-reverse {
  -webkit-flex-wrap: wrap-reverse !important;
      -ms-flex-wrap: wrap-reverse !important;
          flex-wrap: wrap-reverse !important; }

.flex-fill {
  -webkit-box-flex: 1 !important;
  -webkit-flex: 1 1 auto !important;
      -ms-flex: 1 1 auto !important;
          flex: 1 1 auto !important; }

.flex-grow-0 {
  -webkit-box-flex: 0 !important;
  -webkit-flex-grow: 0 !important;
      -ms-flex-positive: 0 !important;
          flex-grow: 0 !important; }

.flex-grow-1 {
  -webkit-box-flex: 1 !important;
  -webkit-flex-grow: 1 !important;
      -ms-flex-positive: 1 !important;
          flex-grow: 1 !important; }

.flex-shrink-0 {
  -webkit-flex-shrink: 0 !important;
      -ms-flex-negative: 0 !important;
          flex-shrink: 0 !important; }

.flex-shrink-1 {
  -webkit-flex-shrink: 1 !important;
      -ms-flex-negative: 1 !important;
          flex-shrink: 1 !important; }

.justify-content-start {
  -webkit-box-pack: start !important;
  -webkit-justify-content: flex-start !important;
      -ms-flex-pack: start !important;
          justify-content: flex-start !important; }

.justify-content-end {
  -webkit-box-pack: end !important;
  -webkit-justify-content: flex-end !important;
      -ms-flex-pack: end !important;
          justify-content: flex-end !important; }

.justify-content-center {
  -webkit-box-pack: center !important;
  -webkit-justify-content: center !important;
      -ms-flex-pack: center !important;
          justify-content: center !important; }

.justify-content-between {
  -webkit-box-pack: justify !important;
  -webkit-justify-content: space-between !important;
      -ms-flex-pack: justify !important;
          justify-content: space-between !important; }

.justify-content-around {
  -webkit-justify-content: space-around !important;
      -ms-flex-pack: distribute !important;
          justify-content: space-around !important; }

.align-items-start {
  -webkit-box-align: start !important;
  -webkit-align-items: flex-start !important;
      -ms-flex-align: start !important;
          align-items: flex-start !important; }

.align-items-end {
  -webkit-box-align: end !important;
  -webkit-align-items: flex-end !important;
      -ms-flex-align: end !important;
          align-items: flex-end !important; }

.align-items-center {
  -webkit-box-align: center !important;
  -webkit-align-items: center !important;
      -ms-flex-align: center !important;
          align-items: center !important; }

.align-items-baseline {
  -webkit-box-align: baseline !important;
  -webkit-align-items: baseline !important;
      -ms-flex-align: baseline !important;
          align-items: baseline !important; }

.align-items-stretch {
  -webkit-box-align: stretch !important;
  -webkit-align-items: stretch !important;
      -ms-flex-align: stretch !important;
          align-items: stretch !important; }

.align-content-start {
  -webkit-align-content: flex-start !important;
      -ms-flex-line-pack: start !important;
          align-content: flex-start !important; }

.align-content-end {
  -webkit-align-content: flex-end !important;
      -ms-flex-line-pack: end !important;
          align-content: flex-end !important; }

.align-content-center {
  -webkit-align-content: center !important;
      -ms-flex-line-pack: center !important;
          align-content: center !important; }

.align-content-between {
  -webkit-align-content: space-between !important;
      -ms-flex-line-pack: justify !important;
          align-content: space-between !important; }

.align-content-around {
  -webkit-align-content: space-around !important;
      -ms-flex-line-pack: distribute !important;
          align-content: space-around !important; }

.align-content-stretch {
  -webkit-align-content: stretch !important;
      -ms-flex-line-pack: stretch !important;
          align-content: stretch !important; }

.align-self-auto {
  -webkit-align-self: auto !important;
      -ms-flex-item-align: auto !important;
          align-self: auto !important; }

.align-self-start {
  -webkit-align-self: flex-start !important;
      -ms-flex-item-align: start !important;
          align-self: flex-start !important; }

.align-self-end {
  -webkit-align-self: flex-end !important;
      -ms-flex-item-align: end !important;
          align-self: flex-end !important; }

.align-self-center {
  -webkit-align-self: center !important;
      -ms-flex-item-align: center !important;
          align-self: center !important; }

.align-self-baseline {
  -webkit-align-self: baseline !important;
      -ms-flex-item-align: baseline !important;
          align-self: baseline !important; }

.align-self-stretch {
  -webkit-align-self: stretch !important;
      -ms-flex-item-align: stretch !important;
          align-self: stretch !important; }

@media (min-width: 576px) {
  .flex-sm-row {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: row !important;
        -ms-flex-direction: row !important;
            flex-direction: row !important; }
  .flex-sm-column {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: column !important;
        -ms-flex-direction: column !important;
            flex-direction: column !important; }
  .flex-sm-row-reverse {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: row-reverse !important;
        -ms-flex-direction: row-reverse !important;
            flex-direction: row-reverse !important; }
  .flex-sm-column-reverse {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: column-reverse !important;
        -ms-flex-direction: column-reverse !important;
            flex-direction: column-reverse !important; }
  .flex-sm-wrap {
    -webkit-flex-wrap: wrap !important;
        -ms-flex-wrap: wrap !important;
            flex-wrap: wrap !important; }
  .flex-sm-nowrap {
    -webkit-flex-wrap: nowrap !important;
        -ms-flex-wrap: nowrap !important;
            flex-wrap: nowrap !important; }
  .flex-sm-wrap-reverse {
    -webkit-flex-wrap: wrap-reverse !important;
        -ms-flex-wrap: wrap-reverse !important;
            flex-wrap: wrap-reverse !important; }
  .flex-sm-fill {
    -webkit-box-flex: 1 !important;
    -webkit-flex: 1 1 auto !important;
        -ms-flex: 1 1 auto !important;
            flex: 1 1 auto !important; }
  .flex-sm-grow-0 {
    -webkit-box-flex: 0 !important;
    -webkit-flex-grow: 0 !important;
        -ms-flex-positive: 0 !important;
            flex-grow: 0 !important; }
  .flex-sm-grow-1 {
    -webkit-box-flex: 1 !important;
    -webkit-flex-grow: 1 !important;
        -ms-flex-positive: 1 !important;
            flex-grow: 1 !important; }
  .flex-sm-shrink-0 {
    -webkit-flex-shrink: 0 !important;
        -ms-flex-negative: 0 !important;
            flex-shrink: 0 !important; }
  .flex-sm-shrink-1 {
    -webkit-flex-shrink: 1 !important;
        -ms-flex-negative: 1 !important;
            flex-shrink: 1 !important; }
  .justify-content-sm-start {
    -webkit-box-pack: start !important;
    -webkit-justify-content: flex-start !important;
        -ms-flex-pack: start !important;
            justify-content: flex-start !important; }
  .justify-content-sm-end {
    -webkit-box-pack: end !important;
    -webkit-justify-content: flex-end !important;
        -ms-flex-pack: end !important;
            justify-content: flex-end !important; }
  .justify-content-sm-center {
    -webkit-box-pack: center !important;
    -webkit-justify-content: center !important;
        -ms-flex-pack: center !important;
            justify-content: center !important; }
  .justify-content-sm-between {
    -webkit-box-pack: justify !important;
    -webkit-justify-content: space-between !important;
        -ms-flex-pack: justify !important;
            justify-content: space-between !important; }
  .justify-content-sm-around {
    -webkit-justify-content: space-around !important;
        -ms-flex-pack: distribute !important;
            justify-content: space-around !important; }
  .align-items-sm-start {
    -webkit-box-align: start !important;
    -webkit-align-items: flex-start !important;
        -ms-flex-align: start !important;
            align-items: flex-start !important; }
  .align-items-sm-end {
    -webkit-box-align: end !important;
    -webkit-align-items: flex-end !important;
        -ms-flex-align: end !important;
            align-items: flex-end !important; }
  .align-items-sm-center {
    -webkit-box-align: center !important;
    -webkit-align-items: center !important;
        -ms-flex-align: center !important;
            align-items: center !important; }
  .align-items-sm-baseline {
    -webkit-box-align: baseline !important;
    -webkit-align-items: baseline !important;
        -ms-flex-align: baseline !important;
            align-items: baseline !important; }
  .align-items-sm-stretch {
    -webkit-box-align: stretch !important;
    -webkit-align-items: stretch !important;
        -ms-flex-align: stretch !important;
            align-items: stretch !important; }
  .align-content-sm-start {
    -webkit-align-content: flex-start !important;
        -ms-flex-line-pack: start !important;
            align-content: flex-start !important; }
  .align-content-sm-end {
    -webkit-align-content: flex-end !important;
        -ms-flex-line-pack: end !important;
            align-content: flex-end !important; }
  .align-content-sm-center {
    -webkit-align-content: center !important;
        -ms-flex-line-pack: center !important;
            align-content: center !important; }
  .align-content-sm-between {
    -webkit-align-content: space-between !important;
        -ms-flex-line-pack: justify !important;
            align-content: space-between !important; }
  .align-content-sm-around {
    -webkit-align-content: space-around !important;
        -ms-flex-line-pack: distribute !important;
            align-content: space-around !important; }
  .align-content-sm-stretch {
    -webkit-align-content: stretch !important;
        -ms-flex-line-pack: stretch !important;
            align-content: stretch !important; }
  .align-self-sm-auto {
    -webkit-align-self: auto !important;
        -ms-flex-item-align: auto !important;
            align-self: auto !important; }
  .align-self-sm-start {
    -webkit-align-self: flex-start !important;
        -ms-flex-item-align: start !important;
            align-self: flex-start !important; }
  .align-self-sm-end {
    -webkit-align-self: flex-end !important;
        -ms-flex-item-align: end !important;
            align-self: flex-end !important; }
  .align-self-sm-center {
    -webkit-align-self: center !important;
        -ms-flex-item-align: center !important;
            align-self: center !important; }
  .align-self-sm-baseline {
    -webkit-align-self: baseline !important;
        -ms-flex-item-align: baseline !important;
            align-self: baseline !important; }
  .align-self-sm-stretch {
    -webkit-align-self: stretch !important;
        -ms-flex-item-align: stretch !important;
            align-self: stretch !important; } }

@media (min-width: 768px) {
  .flex-md-row {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: row !important;
        -ms-flex-direction: row !important;
            flex-direction: row !important; }
  .flex-md-column {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: column !important;
        -ms-flex-direction: column !important;
            flex-direction: column !important; }
  .flex-md-row-reverse {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: row-reverse !important;
        -ms-flex-direction: row-reverse !important;
            flex-direction: row-reverse !important; }
  .flex-md-column-reverse {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: column-reverse !important;
        -ms-flex-direction: column-reverse !important;
            flex-direction: column-reverse !important; }
  .flex-md-wrap {
    -webkit-flex-wrap: wrap !important;
        -ms-flex-wrap: wrap !important;
            flex-wrap: wrap !important; }
  .flex-md-nowrap {
    -webkit-flex-wrap: nowrap !important;
        -ms-flex-wrap: nowrap !important;
            flex-wrap: nowrap !important; }
  .flex-md-wrap-reverse {
    -webkit-flex-wrap: wrap-reverse !important;
        -ms-flex-wrap: wrap-reverse !important;
            flex-wrap: wrap-reverse !important; }
  .flex-md-fill {
    -webkit-box-flex: 1 !important;
    -webkit-flex: 1 1 auto !important;
        -ms-flex: 1 1 auto !important;
            flex: 1 1 auto !important; }
  .flex-md-grow-0 {
    -webkit-box-flex: 0 !important;
    -webkit-flex-grow: 0 !important;
        -ms-flex-positive: 0 !important;
            flex-grow: 0 !important; }
  .flex-md-grow-1 {
    -webkit-box-flex: 1 !important;
    -webkit-flex-grow: 1 !important;
        -ms-flex-positive: 1 !important;
            flex-grow: 1 !important; }
  .flex-md-shrink-0 {
    -webkit-flex-shrink: 0 !important;
        -ms-flex-negative: 0 !important;
            flex-shrink: 0 !important; }
  .flex-md-shrink-1 {
    -webkit-flex-shrink: 1 !important;
        -ms-flex-negative: 1 !important;
            flex-shrink: 1 !important; }
  .justify-content-md-start {
    -webkit-box-pack: start !important;
    -webkit-justify-content: flex-start !important;
        -ms-flex-pack: start !important;
            justify-content: flex-start !important; }
  .justify-content-md-end {
    -webkit-box-pack: end !important;
    -webkit-justify-content: flex-end !important;
        -ms-flex-pack: end !important;
            justify-content: flex-end !important; }
  .justify-content-md-center {
    -webkit-box-pack: center !important;
    -webkit-justify-content: center !important;
        -ms-flex-pack: center !important;
            justify-content: center !important; }
  .justify-content-md-between {
    -webkit-box-pack: justify !important;
    -webkit-justify-content: space-between !important;
        -ms-flex-pack: justify !important;
            justify-content: space-between !important; }
  .justify-content-md-around {
    -webkit-justify-content: space-around !important;
        -ms-flex-pack: distribute !important;
            justify-content: space-around !important; }
  .align-items-md-start {
    -webkit-box-align: start !important;
    -webkit-align-items: flex-start !important;
        -ms-flex-align: start !important;
            align-items: flex-start !important; }
  .align-items-md-end {
    -webkit-box-align: end !important;
    -webkit-align-items: flex-end !important;
        -ms-flex-align: end !important;
            align-items: flex-end !important; }
  .align-items-md-center {
    -webkit-box-align: center !important;
    -webkit-align-items: center !important;
        -ms-flex-align: center !important;
            align-items: center !important; }
  .align-items-md-baseline {
    -webkit-box-align: baseline !important;
    -webkit-align-items: baseline !important;
        -ms-flex-align: baseline !important;
            align-items: baseline !important; }
  .align-items-md-stretch {
    -webkit-box-align: stretch !important;
    -webkit-align-items: stretch !important;
        -ms-flex-align: stretch !important;
            align-items: stretch !important; }
  .align-content-md-start {
    -webkit-align-content: flex-start !important;
        -ms-flex-line-pack: start !important;
            align-content: flex-start !important; }
  .align-content-md-end {
    -webkit-align-content: flex-end !important;
        -ms-flex-line-pack: end !important;
            align-content: flex-end !important; }
  .align-content-md-center {
    -webkit-align-content: center !important;
        -ms-flex-line-pack: center !important;
            align-content: center !important; }
  .align-content-md-between {
    -webkit-align-content: space-between !important;
        -ms-flex-line-pack: justify !important;
            align-content: space-between !important; }
  .align-content-md-around {
    -webkit-align-content: space-around !important;
        -ms-flex-line-pack: distribute !important;
            align-content: space-around !important; }
  .align-content-md-stretch {
    -webkit-align-content: stretch !important;
        -ms-flex-line-pack: stretch !important;
            align-content: stretch !important; }
  .align-self-md-auto {
    -webkit-align-self: auto !important;
        -ms-flex-item-align: auto !important;
            align-self: auto !important; }
  .align-self-md-start {
    -webkit-align-self: flex-start !important;
        -ms-flex-item-align: start !important;
            align-self: flex-start !important; }
  .align-self-md-end {
    -webkit-align-self: flex-end !important;
        -ms-flex-item-align: end !important;
            align-self: flex-end !important; }
  .align-self-md-center {
    -webkit-align-self: center !important;
        -ms-flex-item-align: center !important;
            align-self: center !important; }
  .align-self-md-baseline {
    -webkit-align-self: baseline !important;
        -ms-flex-item-align: baseline !important;
            align-self: baseline !important; }
  .align-self-md-stretch {
    -webkit-align-self: stretch !important;
        -ms-flex-item-align: stretch !important;
            align-self: stretch !important; } }

@media (min-width: 992px) {
  .flex-lg-row {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: row !important;
        -ms-flex-direction: row !important;
            flex-direction: row !important; }
  .flex-lg-column {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: column !important;
        -ms-flex-direction: column !important;
            flex-direction: column !important; }
  .flex-lg-row-reverse {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: row-reverse !important;
        -ms-flex-direction: row-reverse !important;
            flex-direction: row-reverse !important; }
  .flex-lg-column-reverse {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: column-reverse !important;
        -ms-flex-direction: column-reverse !important;
            flex-direction: column-reverse !important; }
  .flex-lg-wrap {
    -webkit-flex-wrap: wrap !important;
        -ms-flex-wrap: wrap !important;
            flex-wrap: wrap !important; }
  .flex-lg-nowrap {
    -webkit-flex-wrap: nowrap !important;
        -ms-flex-wrap: nowrap !important;
            flex-wrap: nowrap !important; }
  .flex-lg-wrap-reverse {
    -webkit-flex-wrap: wrap-reverse !important;
        -ms-flex-wrap: wrap-reverse !important;
            flex-wrap: wrap-reverse !important; }
  .flex-lg-fill {
    -webkit-box-flex: 1 !important;
    -webkit-flex: 1 1 auto !important;
        -ms-flex: 1 1 auto !important;
            flex: 1 1 auto !important; }
  .flex-lg-grow-0 {
    -webkit-box-flex: 0 !important;
    -webkit-flex-grow: 0 !important;
        -ms-flex-positive: 0 !important;
            flex-grow: 0 !important; }
  .flex-lg-grow-1 {
    -webkit-box-flex: 1 !important;
    -webkit-flex-grow: 1 !important;
        -ms-flex-positive: 1 !important;
            flex-grow: 1 !important; }
  .flex-lg-shrink-0 {
    -webkit-flex-shrink: 0 !important;
        -ms-flex-negative: 0 !important;
            flex-shrink: 0 !important; }
  .flex-lg-shrink-1 {
    -webkit-flex-shrink: 1 !important;
        -ms-flex-negative: 1 !important;
            flex-shrink: 1 !important; }
  .justify-content-lg-start {
    -webkit-box-pack: start !important;
    -webkit-justify-content: flex-start !important;
        -ms-flex-pack: start !important;
            justify-content: flex-start !important; }
  .justify-content-lg-end {
    -webkit-box-pack: end !important;
    -webkit-justify-content: flex-end !important;
        -ms-flex-pack: end !important;
            justify-content: flex-end !important; }
  .justify-content-lg-center {
    -webkit-box-pack: center !important;
    -webkit-justify-content: center !important;
        -ms-flex-pack: center !important;
            justify-content: center !important; }
  .justify-content-lg-between {
    -webkit-box-pack: justify !important;
    -webkit-justify-content: space-between !important;
        -ms-flex-pack: justify !important;
            justify-content: space-between !important; }
  .justify-content-lg-around {
    -webkit-justify-content: space-around !important;
        -ms-flex-pack: distribute !important;
            justify-content: space-around !important; }
  .align-items-lg-start {
    -webkit-box-align: start !important;
    -webkit-align-items: flex-start !important;
        -ms-flex-align: start !important;
            align-items: flex-start !important; }
  .align-items-lg-end {
    -webkit-box-align: end !important;
    -webkit-align-items: flex-end !important;
        -ms-flex-align: end !important;
            align-items: flex-end !important; }
  .align-items-lg-center {
    -webkit-box-align: center !important;
    -webkit-align-items: center !important;
        -ms-flex-align: center !important;
            align-items: center !important; }
  .align-items-lg-baseline {
    -webkit-box-align: baseline !important;
    -webkit-align-items: baseline !important;
        -ms-flex-align: baseline !important;
            align-items: baseline !important; }
  .align-items-lg-stretch {
    -webkit-box-align: stretch !important;
    -webkit-align-items: stretch !important;
        -ms-flex-align: stretch !important;
            align-items: stretch !important; }
  .align-content-lg-start {
    -webkit-align-content: flex-start !important;
        -ms-flex-line-pack: start !important;
            align-content: flex-start !important; }
  .align-content-lg-end {
    -webkit-align-content: flex-end !important;
        -ms-flex-line-pack: end !important;
            align-content: flex-end !important; }
  .align-content-lg-center {
    -webkit-align-content: center !important;
        -ms-flex-line-pack: center !important;
            align-content: center !important; }
  .align-content-lg-between {
    -webkit-align-content: space-between !important;
        -ms-flex-line-pack: justify !important;
            align-content: space-between !important; }
  .align-content-lg-around {
    -webkit-align-content: space-around !important;
        -ms-flex-line-pack: distribute !important;
            align-content: space-around !important; }
  .align-content-lg-stretch {
    -webkit-align-content: stretch !important;
        -ms-flex-line-pack: stretch !important;
            align-content: stretch !important; }
  .align-self-lg-auto {
    -webkit-align-self: auto !important;
        -ms-flex-item-align: auto !important;
            align-self: auto !important; }
  .align-self-lg-start {
    -webkit-align-self: flex-start !important;
        -ms-flex-item-align: start !important;
            align-self: flex-start !important; }
  .align-self-lg-end {
    -webkit-align-self: flex-end !important;
        -ms-flex-item-align: end !important;
            align-self: flex-end !important; }
  .align-self-lg-center {
    -webkit-align-self: center !important;
        -ms-flex-item-align: center !important;
            align-self: center !important; }
  .align-self-lg-baseline {
    -webkit-align-self: baseline !important;
        -ms-flex-item-align: baseline !important;
            align-self: baseline !important; }
  .align-self-lg-stretch {
    -webkit-align-self: stretch !important;
        -ms-flex-item-align: stretch !important;
            align-self: stretch !important; } }

@media (min-width: 1200px) {
  .flex-xl-row {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: row !important;
        -ms-flex-direction: row !important;
            flex-direction: row !important; }
  .flex-xl-column {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: normal !important;
    -webkit-flex-direction: column !important;
        -ms-flex-direction: column !important;
            flex-direction: column !important; }
  .flex-xl-row-reverse {
    -webkit-box-orient: horizontal !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: row-reverse !important;
        -ms-flex-direction: row-reverse !important;
            flex-direction: row-reverse !important; }
  .flex-xl-column-reverse {
    -webkit-box-orient: vertical !important;
    -webkit-box-direction: reverse !important;
    -webkit-flex-direction: column-reverse !important;
        -ms-flex-direction: column-reverse !important;
            flex-direction: column-reverse !important; }
  .flex-xl-wrap {
    -webkit-flex-wrap: wrap !important;
        -ms-flex-wrap: wrap !important;
            flex-wrap: wrap !important; }
  .flex-xl-nowrap {
    -webkit-flex-wrap: nowrap !important;
        -ms-flex-wrap: nowrap !important;
            flex-wrap: nowrap !important; }
  .flex-xl-wrap-reverse {
    -webkit-flex-wrap: wrap-reverse !important;
        -ms-flex-wrap: wrap-reverse !important;
            flex-wrap: wrap-reverse !important; }
  .flex-xl-fill {
    -webkit-box-flex: 1 !important;
    -webkit-flex: 1 1 auto !important;
        -ms-flex: 1 1 auto !important;
            flex: 1 1 auto !important; }
  .flex-xl-grow-0 {
    -webkit-box-flex: 0 !important;
    -webkit-flex-grow: 0 !important;
        -ms-flex-positive: 0 !important;
            flex-grow: 0 !important; }
  .flex-xl-grow-1 {
    -webkit-box-flex: 1 !important;
    -webkit-flex-grow: 1 !important;
        -ms-flex-positive: 1 !important;
            flex-grow: 1 !important; }
  .flex-xl-shrink-0 {
    -webkit-flex-shrink: 0 !important;
        -ms-flex-negative: 0 !important;
            flex-shrink: 0 !important; }
  .flex-xl-shrink-1 {
    -webkit-flex-shrink: 1 !important;
        -ms-flex-negative: 1 !important;
            flex-shrink: 1 !important; }
  .justify-content-xl-start {
    -webkit-box-pack: start !important;
    -webkit-justify-content: flex-start !important;
        -ms-flex-pack: start !important;
            justify-content: flex-start !important; }
  .justify-content-xl-end {
    -webkit-box-pack: end !important;
    -webkit-justify-content: flex-end !important;
        -ms-flex-pack: end !important;
            justify-content: flex-end !important; }
  .justify-content-xl-center {
    -webkit-box-pack: center !important;
    -webkit-justify-content: center !important;
        -ms-flex-pack: center !important;
            justify-content: center !important; }
  .justify-content-xl-between {
    -webkit-box-pack: justify !important;
    -webkit-justify-content: space-between !important;
        -ms-flex-pack: justify !important;
            justify-content: space-between !important; }
  .justify-content-xl-around {
    -webkit-justify-content: space-around !important;
        -ms-flex-pack: distribute !important;
            justify-content: space-around !important; }
  .align-items-xl-start {
    -webkit-box-align: start !important;
    -webkit-align-items: flex-start !important;
        -ms-flex-align: start !important;
            align-items: flex-start !important; }
  .align-items-xl-end {
    -webkit-box-align: end !important;
    -webkit-align-items: flex-end !important;
        -ms-flex-align: end !important;
            align-items: flex-end !important; }
  .align-items-xl-center {
    -webkit-box-align: center !important;
    -webkit-align-items: center !important;
        -ms-flex-align: center !important;
            align-items: center !important; }
  .align-items-xl-baseline {
    -webkit-box-align: baseline !important;
    -webkit-align-items: baseline !important;
        -ms-flex-align: baseline !important;
            align-items: baseline !important; }
  .align-items-xl-stretch {
    -webkit-box-align: stretch !important;
    -webkit-align-items: stretch !important;
        -ms-flex-align: stretch !important;
            align-items: stretch !important; }
  .align-content-xl-start {
    -webkit-align-content: flex-start !important;
        -ms-flex-line-pack: start !important;
            align-content: flex-start !important; }
  .align-content-xl-end {
    -webkit-align-content: flex-end !important;
        -ms-flex-line-pack: end !important;
            align-content: flex-end !important; }
  .align-content-xl-center {
    -webkit-align-content: center !important;
        -ms-flex-line-pack: center !important;
            align-content: center !important; }
  .align-content-xl-between {
    -webkit-align-content: space-between !important;
        -ms-flex-line-pack: justify !important;
            align-content: space-between !important; }
  .align-content-xl-around {
    -webkit-align-content: space-around !important;
        -ms-flex-line-pack: distribute !important;
            align-content: space-around !important; }
  .align-content-xl-stretch {
    -webkit-align-content: stretch !important;
        -ms-flex-line-pack: stretch !important;
            align-content: stretch !important; }
  .align-self-xl-auto {
    -webkit-align-self: auto !important;
        -ms-flex-item-align: auto !important;
            align-self: auto !important; }
  .align-self-xl-start {
    -webkit-align-self: flex-start !important;
        -ms-flex-item-align: start !important;
            align-self: flex-start !important; }
  .align-self-xl-end {
    -webkit-align-self: flex-end !important;
        -ms-flex-item-align: end !important;
            align-self: flex-end !important; }
  .align-self-xl-center {
    -webkit-align-self: center !important;
        -ms-flex-item-align: center !important;
            align-self: center !important; }
  .align-self-xl-baseline {
    -webkit-align-self: baseline !important;
        -ms-flex-item-align: baseline !important;
            align-self: baseline !important; }
  .align-self-xl-stretch {
    -webkit-align-self: stretch !important;
        -ms-flex-item-align: stretch !important;
            align-self: stretch !important; } }

.float-left {
  float: left !important; }

.float-right {
  float: right !important; }

.float-none {
  float: none !important; }

@media (min-width: 576px) {
  .float-sm-left {
    float: left !important; }
  .float-sm-right {
    float: right !important; }
  .float-sm-none {
    float: none !important; } }

@media (min-width: 768px) {
  .float-md-left {
    float: left !important; }
  .float-md-right {
    float: right !important; }
  .float-md-none {
    float: none !important; } }

@media (min-width: 992px) {
  .float-lg-left {
    float: left !important; }
  .float-lg-right {
    float: right !important; }
  .float-lg-none {
    float: none !important; } }

@media (min-width: 1200px) {
  .float-xl-left {
    float: left !important; }
  .float-xl-right {
    float: right !important; }
  .float-xl-none {
    float: none !important; } }

.overflow-auto {
  overflow: auto !important; }

.overflow-hidden {
  overflow: hidden !important; }

.position-static {
  position: static !important; }

.position-relative {
  position: relative !important; }

.position-absolute {
  position: absolute !important; }

.position-fixed {
  position: fixed !important; }

.position-sticky {
  position: -webkit-sticky !important;
  position: sticky !important; }

.fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030; }

.fixed-bottom {
  position: fixed;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1030; }

@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sticky-top {
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    z-index: 1020; } }

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0; }

.sr-only-focusable:active, .sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  overflow: visible;
  clip: auto;
  white-space: normal; }

.shadow-sm {
  -webkit-box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
          box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important; }

.shadow {
  -webkit-box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
          box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important; }

.shadow-lg {
  -webkit-box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important;
          box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important; }

.shadow-none {
  -webkit-box-shadow: none !important;
          box-shadow: none !important; }

.w-25 {
  width: 25% !important; }

.w-50 {
  width: 50% !important; }

.w-75 {
  width: 75% !important; }

.w-100 {
  width: 100% !important; }

.w-auto {
  width: auto !important; }

.h-25 {
  height: 25% !important; }

.h-50 {
  height: 50% !important; }

.h-75 {
  height: 75% !important; }

.h-100 {
  height: 100% !important; }

.h-auto {
  height: auto !important; }

.mw-100 {
  max-width: 100% !important; }

.mh-100 {
  max-height: 100% !important; }

.min-vw-100 {
  min-width: 100vw !important; }

.min-vh-100 {
  min-height: 100vh !important; }

.vw-100 {
  width: 100vw !important; }

.vh-100 {
  height: 100vh !important; }

.stretched-link::after {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  pointer-events: auto;
  content: "";
  background-color: rgba(0, 0, 0, 0); }

.m-0 {
  margin: 0 !important; }

.mt-0,
.my-0 {
  margin-top: 0 !important; }

.mr-0,
.mx-0 {
  margin-right: 0 !important; }

.mb-0,
.my-0 {
  margin-bottom: 0 !important; }

.ml-0,
.mx-0 {
  margin-left: 0 !important; }

.m-1 {
  margin: 0.25rem !important; }

.mt-1,
.my-1 {
  margin-top: 0.25rem !important; }

.mr-1,
.mx-1 {
  margin-right: 0.25rem !important; }

.mb-1,
.my-1 {
  margin-bottom: 0.25rem !important; }

.ml-1,
.mx-1 {
  margin-left: 0.25rem !important; }

.m-2 {
  margin: 0.5rem !important; }

.mt-2,
.my-2 {
  margin-top: 0.5rem !important; }

.mr-2,
.mx-2 {
  margin-right: 0.5rem !important; }

.mb-2,
.my-2 {
  margin-bottom: 0.5rem !important; }

.ml-2,
.mx-2 {
  margin-left: 0.5rem !important; }

.m-3 {
  margin: 1rem !important; }

.mt-3,
.my-3 {
  margin-top: 1rem !important; }

.mr-3,
.mx-3 {
  margin-right: 1rem !important; }

.mb-3,
.my-3 {
  margin-bottom: 1rem !important; }

.ml-3,
.mx-3 {
  margin-left: 1rem !important; }

.m-4 {
  margin: 1.5rem !important; }

.mt-4,
.my-4 {
  margin-top: 1.5rem !important; }

.mr-4,
.mx-4 {
  margin-right: 1.5rem !important; }

.mb-4,
.my-4 {
  margin-bottom: 1.5rem !important; }

.ml-4,
.mx-4 {
  margin-left: 1.5rem !important; }

.m-5 {
  margin: 3rem !important; }

.mt-5,
.my-5 {
  margin-top: 3rem !important; }

.mr-5,
.mx-5 {
  margin-right: 3rem !important; }

.mb-5,
.my-5 {
  margin-bottom: 3rem !important; }

.ml-5,
.mx-5 {
  margin-left: 3rem !important; }

.p-0 {
  padding: 0 !important; }

.pt-0,
.py-0 {
  padding-top: 0 !important; }

.pr-0,
.px-0 {
  padding-right: 0 !important; }

.pb-0,
.py-0 {
  padding-bottom: 0 !important; }

.pl-0,
.px-0 {
  padding-left: 0 !important; }

.p-1 {
  padding: 0.25rem !important; }

.pt-1,
.py-1 {
  padding-top: 0.25rem !important; }

.pr-1,
.px-1 {
  padding-right: 0.25rem !important; }

.pb-1,
.py-1 {
  padding-bottom: 0.25rem !important; }

.pl-1,
.px-1 {
  padding-left: 0.25rem !important; }

.p-2 {
  padding: 0.5rem !important; }

.pt-2,
.py-2 {
  padding-top: 0.5rem !important; }

.pr-2,
.px-2 {
  padding-right: 0.5rem !important; }

.pb-2,
.py-2 {
  padding-bottom: 0.5rem !important; }

.pl-2,
.px-2 {
  padding-left: 0.5rem !important; }

.p-3 {
  padding: 1rem !important; }

.pt-3,
.py-3 {
  padding-top: 1rem !important; }

.pr-3,
.px-3 {
  padding-right: 1rem !important; }

.pb-3,
.py-3 {
  padding-bottom: 1rem !important; }

.pl-3,
.px-3 {
  padding-left: 1rem !important; }

.p-4 {
  padding: 1.5rem !important; }

.pt-4,
.py-4 {
  padding-top: 1.5rem !important; }

.pr-4,
.px-4 {
  padding-right: 1.5rem !important; }

.pb-4,
.py-4 {
  padding-bottom: 1.5rem !important; }

.pl-4,
.px-4 {
  padding-left: 1.5rem !important; }

.p-5 {
  padding: 3rem !important; }

.pt-5,
.py-5 {
  padding-top: 3rem !important; }

.pr-5,
.px-5 {
  padding-right: 3rem !important; }

.pb-5,
.py-5 {
  padding-bottom: 3rem !important; }

.pl-5,
.px-5 {
  padding-left: 3rem !important; }

.m-n1 {
  margin: -0.25rem !important; }

.mt-n1,
.my-n1 {
  margin-top: -0.25rem !important; }

.mr-n1,
.mx-n1 {
  margin-right: -0.25rem !important; }

.mb-n1,
.my-n1 {
  margin-bottom: -0.25rem !important; }

.ml-n1,
.mx-n1 {
  margin-left: -0.25rem !important; }

.m-n2 {
  margin: -0.5rem !important; }

.mt-n2,
.my-n2 {
  margin-top: -0.5rem !important; }

.mr-n2,
.mx-n2 {
  margin-right: -0.5rem !important; }

.mb-n2,
.my-n2 {
  margin-bottom: -0.5rem !important; }

.ml-n2,
.mx-n2 {
  margin-left: -0.5rem !important; }

.m-n3 {
  margin: -1rem !important; }

.mt-n3,
.my-n3 {
  margin-top: -1rem !important; }

.mr-n3,
.mx-n3 {
  margin-right: -1rem !important; }

.mb-n3,
.my-n3 {
  margin-bottom: -1rem !important; }

.ml-n3,
.mx-n3 {
  margin-left: -1rem !important; }

.m-n4 {
  margin: -1.5rem !important; }

.mt-n4,
.my-n4 {
  margin-top: -1.5rem !important; }

.mr-n4,
.mx-n4 {
  margin-right: -1.5rem !important; }

.mb-n4,
.my-n4 {
  margin-bottom: -1.5rem !important; }

.ml-n4,
.mx-n4 {
  margin-left: -1.5rem !important; }

.m-n5 {
  margin: -3rem !important; }

.mt-n5,
.my-n5 {
  margin-top: -3rem !important; }

.mr-n5,
.mx-n5 {
  margin-right: -3rem !important; }

.mb-n5,
.my-n5 {
  margin-bottom: -3rem !important; }

.ml-n5,
.mx-n5 {
  margin-left: -3rem !important; }

.m-auto {
  margin: auto !important; }

.mt-auto,
.my-auto {
  margin-top: auto !important; }

.mr-auto,
.mx-auto {
  margin-right: auto !important; }

.mb-auto,
.my-auto {
  margin-bottom: auto !important; }

.ml-auto,
.mx-auto {
  margin-left: auto !important; }

@media (min-width: 576px) {
  .m-sm-0 {
    margin: 0 !important; }
  .mt-sm-0,
  .my-sm-0 {
    margin-top: 0 !important; }
  .mr-sm-0,
  .mx-sm-0 {
    margin-right: 0 !important; }
  .mb-sm-0,
  .my-sm-0 {
    margin-bottom: 0 !important; }
  .ml-sm-0,
  .mx-sm-0 {
    margin-left: 0 !important; }
  .m-sm-1 {
    margin: 0.25rem !important; }
  .mt-sm-1,
  .my-sm-1 {
    margin-top: 0.25rem !important; }
  .mr-sm-1,
  .mx-sm-1 {
    margin-right: 0.25rem !important; }
  .mb-sm-1,
  .my-sm-1 {
    margin-bottom: 0.25rem !important; }
  .ml-sm-1,
  .mx-sm-1 {
    margin-left: 0.25rem !important; }
  .m-sm-2 {
    margin: 0.5rem !important; }
  .mt-sm-2,
  .my-sm-2 {
    margin-top: 0.5rem !important; }
  .mr-sm-2,
  .mx-sm-2 {
    margin-right: 0.5rem !important; }
  .mb-sm-2,
  .my-sm-2 {
    margin-bottom: 0.5rem !important; }
  .ml-sm-2,
  .mx-sm-2 {
    margin-left: 0.5rem !important; }
  .m-sm-3 {
    margin: 1rem !important; }
  .mt-sm-3,
  .my-sm-3 {
    margin-top: 1rem !important; }
  .mr-sm-3,
  .mx-sm-3 {
    margin-right: 1rem !important; }
  .mb-sm-3,
  .my-sm-3 {
    margin-bottom: 1rem !important; }
  .ml-sm-3,
  .mx-sm-3 {
    margin-left: 1rem !important; }
  .m-sm-4 {
    margin: 1.5rem !important; }
  .mt-sm-4,
  .my-sm-4 {
    margin-top: 1.5rem !important; }
  .mr-sm-4,
  .mx-sm-4 {
    margin-right: 1.5rem !important; }
  .mb-sm-4,
  .my-sm-4 {
    margin-bottom: 1.5rem !important; }
  .ml-sm-4,
  .mx-sm-4 {
    margin-left: 1.5rem !important; }
  .m-sm-5 {
    margin: 3rem !important; }
  .mt-sm-5,
  .my-sm-5 {
    margin-top: 3rem !important; }
  .mr-sm-5,
  .mx-sm-5 {
    margin-right: 3rem !important; }
  .mb-sm-5,
  .my-sm-5 {
    margin-bottom: 3rem !important; }
  .ml-sm-5,
  .mx-sm-5 {
    margin-left: 3rem !important; }
  .p-sm-0 {
    padding: 0 !important; }
  .pt-sm-0,
  .py-sm-0 {
    padding-top: 0 !important; }
  .pr-sm-0,
  .px-sm-0 {
    padding-right: 0 !important; }
  .pb-sm-0,
  .py-sm-0 {
    padding-bottom: 0 !important; }
  .pl-sm-0,
  .px-sm-0 {
    padding-left: 0 !important; }
  .p-sm-1 {
    padding: 0.25rem !important; }
  .pt-sm-1,
  .py-sm-1 {
    padding-top: 0.25rem !important; }
  .pr-sm-1,
  .px-sm-1 {
    padding-right: 0.25rem !important; }
  .pb-sm-1,
  .py-sm-1 {
    padding-bottom: 0.25rem !important; }
  .pl-sm-1,
  .px-sm-1 {
    padding-left: 0.25rem !important; }
  .p-sm-2 {
    padding: 0.5rem !important; }
  .pt-sm-2,
  .py-sm-2 {
    padding-top: 0.5rem !important; }
  .pr-sm-2,
  .px-sm-2 {
    padding-right: 0.5rem !important; }
  .pb-sm-2,
  .py-sm-2 {
    padding-bottom: 0.5rem !important; }
  .pl-sm-2,
  .px-sm-2 {
    padding-left: 0.5rem !important; }
  .p-sm-3 {
    padding: 1rem !important; }
  .pt-sm-3,
  .py-sm-3 {
    padding-top: 1rem !important; }
  .pr-sm-3,
  .px-sm-3 {
    padding-right: 1rem !important; }
  .pb-sm-3,
  .py-sm-3 {
    padding-bottom: 1rem !important; }
  .pl-sm-3,
  .px-sm-3 {
    padding-left: 1rem !important; }
  .p-sm-4 {
    padding: 1.5rem !important; }
  .pt-sm-4,
  .py-sm-4 {
    padding-top: 1.5rem !important; }
  .pr-sm-4,
  .px-sm-4 {
    padding-right: 1.5rem !important; }
  .pb-sm-4,
  .py-sm-4 {
    padding-bottom: 1.5rem !important; }
  .pl-sm-4,
  .px-sm-4 {
    padding-left: 1.5rem !important; }
  .p-sm-5 {
    padding: 3rem !important; }
  .pt-sm-5,
  .py-sm-5 {
    padding-top: 3rem !important; }
  .pr-sm-5,
  .px-sm-5 {
    padding-right: 3rem !important; }
  .pb-sm-5,
  .py-sm-5 {
    padding-bottom: 3rem !important; }
  .pl-sm-5,
  .px-sm-5 {
    padding-left: 3rem !important; }
  .m-sm-n1 {
    margin: -0.25rem !important; }
  .mt-sm-n1,
  .my-sm-n1 {
    margin-top: -0.25rem !important; }
  .mr-sm-n1,
  .mx-sm-n1 {
    margin-right: -0.25rem !important; }
  .mb-sm-n1,
  .my-sm-n1 {
    margin-bottom: -0.25rem !important; }
  .ml-sm-n1,
  .mx-sm-n1 {
    margin-left: -0.25rem !important; }
  .m-sm-n2 {
    margin: -0.5rem !important; }
  .mt-sm-n2,
  .my-sm-n2 {
    margin-top: -0.5rem !important; }
  .mr-sm-n2,
  .mx-sm-n2 {
    margin-right: -0.5rem !important; }
  .mb-sm-n2,
  .my-sm-n2 {
    margin-bottom: -0.5rem !important; }
  .ml-sm-n2,
  .mx-sm-n2 {
    margin-left: -0.5rem !important; }
  .m-sm-n3 {
    margin: -1rem !important; }
  .mt-sm-n3,
  .my-sm-n3 {
    margin-top: -1rem !important; }
  .mr-sm-n3,
  .mx-sm-n3 {
    margin-right: -1rem !important; }
  .mb-sm-n3,
  .my-sm-n3 {
    margin-bottom: -1rem !important; }
  .ml-sm-n3,
  .mx-sm-n3 {
    margin-left: -1rem !important; }
  .m-sm-n4 {
    margin: -1.5rem !important; }
  .mt-sm-n4,
  .my-sm-n4 {
    margin-top: -1.5rem !important; }
  .mr-sm-n4,
  .mx-sm-n4 {
    margin-right: -1.5rem !important; }
  .mb-sm-n4,
  .my-sm-n4 {
    margin-bottom: -1.5rem !important; }
  .ml-sm-n4,
  .mx-sm-n4 {
    margin-left: -1.5rem !important; }
  .m-sm-n5 {
    margin: -3rem !important; }
  .mt-sm-n5,
  .my-sm-n5 {
    margin-top: -3rem !important; }
  .mr-sm-n5,
  .mx-sm-n5 {
    margin-right: -3rem !important; }
  .mb-sm-n5,
  .my-sm-n5 {
    margin-bottom: -3rem !important; }
  .ml-sm-n5,
  .mx-sm-n5 {
    margin-left: -3rem !important; }
  .m-sm-auto {
    margin: auto !important; }
  .mt-sm-auto,
  .my-sm-auto {
    margin-top: auto !important; }
  .mr-sm-auto,
  .mx-sm-auto {
    margin-right: auto !important; }
  .mb-sm-auto,
  .my-sm-auto {
    margin-bottom: auto !important; }
  .ml-sm-auto,
  .mx-sm-auto {
    margin-left: auto !important; } }

@media (min-width: 768px) {
  .m-md-0 {
    margin: 0 !important; }
  .mt-md-0,
  .my-md-0 {
    margin-top: 0 !important; }
  .mr-md-0,
  .mx-md-0 {
    margin-right: 0 !important; }
  .mb-md-0,
  .my-md-0 {
    margin-bottom: 0 !important; }
  .ml-md-0,
  .mx-md-0 {
    margin-left: 0 !important; }
  .m-md-1 {
    margin: 0.25rem !important; }
  .mt-md-1,
  .my-md-1 {
    margin-top: 0.25rem !important; }
  .mr-md-1,
  .mx-md-1 {
    margin-right: 0.25rem !important; }
  .mb-md-1,
  .my-md-1 {
    margin-bottom: 0.25rem !important; }
  .ml-md-1,
  .mx-md-1 {
    margin-left: 0.25rem !important; }
  .m-md-2 {
    margin: 0.5rem !important; }
  .mt-md-2,
  .my-md-2 {
    margin-top: 0.5rem !important; }
  .mr-md-2,
  .mx-md-2 {
    margin-right: 0.5rem !important; }
  .mb-md-2,
  .my-md-2 {
    margin-bottom: 0.5rem !important; }
  .ml-md-2,
  .mx-md-2 {
    margin-left: 0.5rem !important; }
  .m-md-3 {
    margin: 1rem !important; }
  .mt-md-3,
  .my-md-3 {
    margin-top: 1rem !important; }
  .mr-md-3,
  .mx-md-3 {
    margin-right: 1rem !important; }
  .mb-md-3,
  .my-md-3 {
    margin-bottom: 1rem !important; }
  .ml-md-3,
  .mx-md-3 {
    margin-left: 1rem !important; }
  .m-md-4 {
    margin: 1.5rem !important; }
  .mt-md-4,
  .my-md-4 {
    margin-top: 1.5rem !important; }
  .mr-md-4,
  .mx-md-4 {
    margin-right: 1.5rem !important; }
  .mb-md-4,
  .my-md-4 {
    margin-bottom: 1.5rem !important; }
  .ml-md-4,
  .mx-md-4 {
    margin-left: 1.5rem !important; }
  .m-md-5 {
    margin: 3rem !important; }
  .mt-md-5,
  .my-md-5 {
    margin-top: 3rem !important; }
  .mr-md-5,
  .mx-md-5 {
    margin-right: 3rem !important; }
  .mb-md-5,
  .my-md-5 {
    margin-bottom: 3rem !important; }
  .ml-md-5,
  .mx-md-5 {
    margin-left: 3rem !important; }
  .p-md-0 {
    padding: 0 !important; }
  .pt-md-0,
  .py-md-0 {
    padding-top: 0 !important; }
  .pr-md-0,
  .px-md-0 {
    padding-right: 0 !important; }
  .pb-md-0,
  .py-md-0 {
    padding-bottom: 0 !important; }
  .pl-md-0,
  .px-md-0 {
    padding-left: 0 !important; }
  .p-md-1 {
    padding: 0.25rem !important; }
  .pt-md-1,
  .py-md-1 {
    padding-top: 0.25rem !important; }
  .pr-md-1,
  .px-md-1 {
    padding-right: 0.25rem !important; }
  .pb-md-1,
  .py-md-1 {
    padding-bottom: 0.25rem !important; }
  .pl-md-1,
  .px-md-1 {
    padding-left: 0.25rem !important; }
  .p-md-2 {
    padding: 0.5rem !important; }
  .pt-md-2,
  .py-md-2 {
    padding-top: 0.5rem !important; }
  .pr-md-2,
  .px-md-2 {
    padding-right: 0.5rem !important; }
  .pb-md-2,
  .py-md-2 {
    padding-bottom: 0.5rem !important; }
  .pl-md-2,
  .px-md-2 {
    padding-left: 0.5rem !important; }
  .p-md-3 {
    padding: 1rem !important; }
  .pt-md-3,
  .py-md-3 {
    padding-top: 1rem !important; }
  .pr-md-3,
  .px-md-3 {
    padding-right: 1rem !important; }
  .pb-md-3,
  .py-md-3 {
    padding-bottom: 1rem !important; }
  .pl-md-3,
  .px-md-3 {
    padding-left: 1rem !important; }
  .p-md-4 {
    padding: 1.5rem !important; }
  .pt-md-4,
  .py-md-4 {
    padding-top: 1.5rem !important; }
  .pr-md-4,
  .px-md-4 {
    padding-right: 1.5rem !important; }
  .pb-md-4,
  .py-md-4 {
    padding-bottom: 1.5rem !important; }
  .pl-md-4,
  .px-md-4 {
    padding-left: 1.5rem !important; }
  .p-md-5 {
    padding: 3rem !important; }
  .pt-md-5,
  .py-md-5 {
    padding-top: 3rem !important; }
  .pr-md-5,
  .px-md-5 {
    padding-right: 3rem !important; }
  .pb-md-5,
  .py-md-5 {
    padding-bottom: 3rem !important; }
  .pl-md-5,
  .px-md-5 {
    padding-left: 3rem !important; }
  .m-md-n1 {
    margin: -0.25rem !important; }
  .mt-md-n1,
  .my-md-n1 {
    margin-top: -0.25rem !important; }
  .mr-md-n1,
  .mx-md-n1 {
    margin-right: -0.25rem !important; }
  .mb-md-n1,
  .my-md-n1 {
    margin-bottom: -0.25rem !important; }
  .ml-md-n1,
  .mx-md-n1 {
    margin-left: -0.25rem !important; }
  .m-md-n2 {
    margin: -0.5rem !important; }
  .mt-md-n2,
  .my-md-n2 {
    margin-top: -0.5rem !important; }
  .mr-md-n2,
  .mx-md-n2 {
    margin-right: -0.5rem !important; }
  .mb-md-n2,
  .my-md-n2 {
    margin-bottom: -0.5rem !important; }
  .ml-md-n2,
  .mx-md-n2 {
    margin-left: -0.5rem !important; }
  .m-md-n3 {
    margin: -1rem !important; }
  .mt-md-n3,
  .my-md-n3 {
    margin-top: -1rem !important; }
  .mr-md-n3,
  .mx-md-n3 {
    margin-right: -1rem !important; }
  .mb-md-n3,
  .my-md-n3 {
    margin-bottom: -1rem !important; }
  .ml-md-n3,
  .mx-md-n3 {
    margin-left: -1rem !important; }
  .m-md-n4 {
    margin: -1.5rem !important; }
  .mt-md-n4,
  .my-md-n4 {
    margin-top: -1.5rem !important; }
  .mr-md-n4,
  .mx-md-n4 {
    margin-right: -1.5rem !important; }
  .mb-md-n4,
  .my-md-n4 {
    margin-bottom: -1.5rem !important; }
  .ml-md-n4,
  .mx-md-n4 {
    margin-left: -1.5rem !important; }
  .m-md-n5 {
    margin: -3rem !important; }
  .mt-md-n5,
  .my-md-n5 {
    margin-top: -3rem !important; }
  .mr-md-n5,
  .mx-md-n5 {
    margin-right: -3rem !important; }
  .mb-md-n5,
  .my-md-n5 {
    margin-bottom: -3rem !important; }
  .ml-md-n5,
  .mx-md-n5 {
    margin-left: -3rem !important; }
  .m-md-auto {
    margin: auto !important; }
  .mt-md-auto,
  .my-md-auto {
    margin-top: auto !important; }
  .mr-md-auto,
  .mx-md-auto {
    margin-right: auto !important; }
  .mb-md-auto,
  .my-md-auto {
    margin-bottom: auto !important; }
  .ml-md-auto,
  .mx-md-auto {
    margin-left: auto !important; } }

@media (min-width: 992px) {
  .m-lg-0 {
    margin: 0 !important; }
  .mt-lg-0,
  .my-lg-0 {
    margin-top: 0 !important; }
  .mr-lg-0,
  .mx-lg-0 {
    margin-right: 0 !important; }
  .mb-lg-0,
  .my-lg-0 {
    margin-bottom: 0 !important; }
  .ml-lg-0,
  .mx-lg-0 {
    margin-left: 0 !important; }
  .m-lg-1 {
    margin: 0.25rem !important; }
  .mt-lg-1,
  .my-lg-1 {
    margin-top: 0.25rem !important; }
  .mr-lg-1,
  .mx-lg-1 {
    margin-right: 0.25rem !important; }
  .mb-lg-1,
  .my-lg-1 {
    margin-bottom: 0.25rem !important; }
  .ml-lg-1,
  .mx-lg-1 {
    margin-left: 0.25rem !important; }
  .m-lg-2 {
    margin: 0.5rem !important; }
  .mt-lg-2,
  .my-lg-2 {
    margin-top: 0.5rem !important; }
  .mr-lg-2,
  .mx-lg-2 {
    margin-right: 0.5rem !important; }
  .mb-lg-2,
  .my-lg-2 {
    margin-bottom: 0.5rem !important; }
  .ml-lg-2,
  .mx-lg-2 {
    margin-left: 0.5rem !important; }
  .m-lg-3 {
    margin: 1rem !important; }
  .mt-lg-3,
  .my-lg-3 {
    margin-top: 1rem !important; }
  .mr-lg-3,
  .mx-lg-3 {
    margin-right: 1rem !important; }
  .mb-lg-3,
  .my-lg-3 {
    margin-bottom: 1rem !important; }
  .ml-lg-3,
  .mx-lg-3 {
    margin-left: 1rem !important; }
  .m-lg-4 {
    margin: 1.5rem !important; }
  .mt-lg-4,
  .my-lg-4 {
    margin-top: 1.5rem !important; }
  .mr-lg-4,
  .mx-lg-4 {
    margin-right: 1.5rem !important; }
  .mb-lg-4,
  .my-lg-4 {
    margin-bottom: 1.5rem !important; }
  .ml-lg-4,
  .mx-lg-4 {
    margin-left: 1.5rem !important; }
  .m-lg-5 {
    margin: 3rem !important; }
  .mt-lg-5,
  .my-lg-5 {
    margin-top: 3rem !important; }
  .mr-lg-5,
  .mx-lg-5 {
    margin-right: 3rem !important; }
  .mb-lg-5,
  .my-lg-5 {
    margin-bottom: 3rem !important; }
  .ml-lg-5,
  .mx-lg-5 {
    margin-left: 3rem !important; }
  .p-lg-0 {
    padding: 0 !important; }
  .pt-lg-0,
  .py-lg-0 {
    padding-top: 0 !important; }
  .pr-lg-0,
  .px-lg-0 {
    padding-right: 0 !important; }
  .pb-lg-0,
  .py-lg-0 {
    padding-bottom: 0 !important; }
  .pl-lg-0,
  .px-lg-0 {
    padding-left: 0 !important; }
  .p-lg-1 {
    padding: 0.25rem !important; }
  .pt-lg-1,
  .py-lg-1 {
    padding-top: 0.25rem !important; }
  .pr-lg-1,
  .px-lg-1 {
    padding-right: 0.25rem !important; }
  .pb-lg-1,
  .py-lg-1 {
    padding-bottom: 0.25rem !important; }
  .pl-lg-1,
  .px-lg-1 {
    padding-left: 0.25rem !important; }
  .p-lg-2 {
    padding: 0.5rem !important; }
  .pt-lg-2,
  .py-lg-2 {
    padding-top: 0.5rem !important; }
  .pr-lg-2,
  .px-lg-2 {
    padding-right: 0.5rem !important; }
  .pb-lg-2,
  .py-lg-2 {
    padding-bottom: 0.5rem !important; }
  .pl-lg-2,
  .px-lg-2 {
    padding-left: 0.5rem !important; }
  .p-lg-3 {
    padding: 1rem !important; }
  .pt-lg-3,
  .py-lg-3 {
    padding-top: 1rem !important; }
  .pr-lg-3,
  .px-lg-3 {
    padding-right: 1rem !important; }
  .pb-lg-3,
  .py-lg-3 {
    padding-bottom: 1rem !important; }
  .pl-lg-3,
  .px-lg-3 {
    padding-left: 1rem !important; }
  .p-lg-4 {
    padding: 1.5rem !important; }
  .pt-lg-4,
  .py-lg-4 {
    padding-top: 1.5rem !important; }
  .pr-lg-4,
  .px-lg-4 {
    padding-right: 1.5rem !important; }
  .pb-lg-4,
  .py-lg-4 {
    padding-bottom: 1.5rem !important; }
  .pl-lg-4,
  .px-lg-4 {
    padding-left: 1.5rem !important; }
  .p-lg-5 {
    padding: 3rem !important; }
  .pt-lg-5,
  .py-lg-5 {
    padding-top: 3rem !important; }
  .pr-lg-5,
  .px-lg-5 {
    padding-right: 3rem !important; }
  .pb-lg-5,
  .py-lg-5 {
    padding-bottom: 3rem !important; }
  .pl-lg-5,
  .px-lg-5 {
    padding-left: 3rem !important; }
  .m-lg-n1 {
    margin: -0.25rem !important; }
  .mt-lg-n1,
  .my-lg-n1 {
    margin-top: -0.25rem !important; }
  .mr-lg-n1,
  .mx-lg-n1 {
    margin-right: -0.25rem !important; }
  .mb-lg-n1,
  .my-lg-n1 {
    margin-bottom: -0.25rem !important; }
  .ml-lg-n1,
  .mx-lg-n1 {
    margin-left: -0.25rem !important; }
  .m-lg-n2 {
    margin: -0.5rem !important; }
  .mt-lg-n2,
  .my-lg-n2 {
    margin-top: -0.5rem !important; }
  .mr-lg-n2,
  .mx-lg-n2 {
    margin-right: -0.5rem !important; }
  .mb-lg-n2,
  .my-lg-n2 {
    margin-bottom: -0.5rem !important; }
  .ml-lg-n2,
  .mx-lg-n2 {
    margin-left: -0.5rem !important; }
  .m-lg-n3 {
    margin: -1rem !important; }
  .mt-lg-n3,
  .my-lg-n3 {
    margin-top: -1rem !important; }
  .mr-lg-n3,
  .mx-lg-n3 {
    margin-right: -1rem !important; }
  .mb-lg-n3,
  .my-lg-n3 {
    margin-bottom: -1rem !important; }
  .ml-lg-n3,
  .mx-lg-n3 {
    margin-left: -1rem !important; }
  .m-lg-n4 {
    margin: -1.5rem !important; }
  .mt-lg-n4,
  .my-lg-n4 {
    margin-top: -1.5rem !important; }
  .mr-lg-n4,
  .mx-lg-n4 {
    margin-right: -1.5rem !important; }
  .mb-lg-n4,
  .my-lg-n4 {
    margin-bottom: -1.5rem !important; }
  .ml-lg-n4,
  .mx-lg-n4 {
    margin-left: -1.5rem !important; }
  .m-lg-n5 {
    margin: -3rem !important; }
  .mt-lg-n5,
  .my-lg-n5 {
    margin-top: -3rem !important; }
  .mr-lg-n5,
  .mx-lg-n5 {
    margin-right: -3rem !important; }
  .mb-lg-n5,
  .my-lg-n5 {
    margin-bottom: -3rem !important; }
  .ml-lg-n5,
  .mx-lg-n5 {
    margin-left: -3rem !important; }
  .m-lg-auto {
    margin: auto !important; }
  .mt-lg-auto,
  .my-lg-auto {
    margin-top: auto !important; }
  .mr-lg-auto,
  .mx-lg-auto {
    margin-right: auto !important; }
  .mb-lg-auto,
  .my-lg-auto {
    margin-bottom: auto !important; }
  .ml-lg-auto,
  .mx-lg-auto {
    margin-left: auto !important; } }

@media (min-width: 1200px) {
  .m-xl-0 {
    margin: 0 !important; }
  .mt-xl-0,
  .my-xl-0 {
    margin-top: 0 !important; }
  .mr-xl-0,
  .mx-xl-0 {
    margin-right: 0 !important; }
  .mb-xl-0,
  .my-xl-0 {
    margin-bottom: 0 !important; }
  .ml-xl-0,
  .mx-xl-0 {
    margin-left: 0 !important; }
  .m-xl-1 {
    margin: 0.25rem !important; }
  .mt-xl-1,
  .my-xl-1 {
    margin-top: 0.25rem !important; }
  .mr-xl-1,
  .mx-xl-1 {
    margin-right: 0.25rem !important; }
  .mb-xl-1,
  .my-xl-1 {
    margin-bottom: 0.25rem !important; }
  .ml-xl-1,
  .mx-xl-1 {
    margin-left: 0.25rem !important; }
  .m-xl-2 {
    margin: 0.5rem !important; }
  .mt-xl-2,
  .my-xl-2 {
    margin-top: 0.5rem !important; }
  .mr-xl-2,
  .mx-xl-2 {
    margin-right: 0.5rem !important; }
  .mb-xl-2,
  .my-xl-2 {
    margin-bottom: 0.5rem !important; }
  .ml-xl-2,
  .mx-xl-2 {
    margin-left: 0.5rem !important; }
  .m-xl-3 {
    margin: 1rem !important; }
  .mt-xl-3,
  .my-xl-3 {
    margin-top: 1rem !important; }
  .mr-xl-3,
  .mx-xl-3 {
    margin-right: 1rem !important; }
  .mb-xl-3,
  .my-xl-3 {
    margin-bottom: 1rem !important; }
  .ml-xl-3,
  .mx-xl-3 {
    margin-left: 1rem !important; }
  .m-xl-4 {
    margin: 1.5rem !important; }
  .mt-xl-4,
  .my-xl-4 {
    margin-top: 1.5rem !important; }
  .mr-xl-4,
  .mx-xl-4 {
    margin-right: 1.5rem !important; }
  .mb-xl-4,
  .my-xl-4 {
    margin-bottom: 1.5rem !important; }
  .ml-xl-4,
  .mx-xl-4 {
    margin-left: 1.5rem !important; }
  .m-xl-5 {
    margin: 3rem !important; }
  .mt-xl-5,
  .my-xl-5 {
    margin-top: 3rem !important; }
  .mr-xl-5,
  .mx-xl-5 {
    margin-right: 3rem !important; }
  .mb-xl-5,
  .my-xl-5 {
    margin-bottom: 3rem !important; }
  .ml-xl-5,
  .mx-xl-5 {
    margin-left: 3rem !important; }
  .p-xl-0 {
    padding: 0 !important; }
  .pt-xl-0,
  .py-xl-0 {
    padding-top: 0 !important; }
  .pr-xl-0,
  .px-xl-0 {
    padding-right: 0 !important; }
  .pb-xl-0,
  .py-xl-0 {
    padding-bottom: 0 !important; }
  .pl-xl-0,
  .px-xl-0 {
    padding-left: 0 !important; }
  .p-xl-1 {
    padding: 0.25rem !important; }
  .pt-xl-1,
  .py-xl-1 {
    padding-top: 0.25rem !important; }
  .pr-xl-1,
  .px-xl-1 {
    padding-right: 0.25rem !important; }
  .pb-xl-1,
  .py-xl-1 {
    padding-bottom: 0.25rem !important; }
  .pl-xl-1,
  .px-xl-1 {
    padding-left: 0.25rem !important; }
  .p-xl-2 {
    padding: 0.5rem !important; }
  .pt-xl-2,
  .py-xl-2 {
    padding-top: 0.5rem !important; }
  .pr-xl-2,
  .px-xl-2 {
    padding-right: 0.5rem !important; }
  .pb-xl-2,
  .py-xl-2 {
    padding-bottom: 0.5rem !important; }
  .pl-xl-2,
  .px-xl-2 {
    padding-left: 0.5rem !important; }
  .p-xl-3 {
    padding: 1rem !important; }
  .pt-xl-3,
  .py-xl-3 {
    padding-top: 1rem !important; }
  .pr-xl-3,
  .px-xl-3 {
    padding-right: 1rem !important; }
  .pb-xl-3,
  .py-xl-3 {
    padding-bottom: 1rem !important; }
  .pl-xl-3,
  .px-xl-3 {
    padding-left: 1rem !important; }
  .p-xl-4 {
    padding: 1.5rem !important; }
  .pt-xl-4,
  .py-xl-4 {
    padding-top: 1.5rem !important; }
  .pr-xl-4,
  .px-xl-4 {
    padding-right: 1.5rem !important; }
  .pb-xl-4,
  .py-xl-4 {
    padding-bottom: 1.5rem !important; }
  .pl-xl-4,
  .px-xl-4 {
    padding-left: 1.5rem !important; }
  .p-xl-5 {
    padding: 3rem !important; }
  .pt-xl-5,
  .py-xl-5 {
    padding-top: 3rem !important; }
  .pr-xl-5,
  .px-xl-5 {
    padding-right: 3rem !important; }
  .pb-xl-5,
  .py-xl-5 {
    padding-bottom: 3rem !important; }
  .pl-xl-5,
  .px-xl-5 {
    padding-left: 3rem !important; }
  .m-xl-n1 {
    margin: -0.25rem !important; }
  .mt-xl-n1,
  .my-xl-n1 {
    margin-top: -0.25rem !important; }
  .mr-xl-n1,
  .mx-xl-n1 {
    margin-right: -0.25rem !important; }
  .mb-xl-n1,
  .my-xl-n1 {
    margin-bottom: -0.25rem !important; }
  .ml-xl-n1,
  .mx-xl-n1 {
    margin-left: -0.25rem !important; }
  .m-xl-n2 {
    margin: -0.5rem !important; }
  .mt-xl-n2,
  .my-xl-n2 {
    margin-top: -0.5rem !important; }
  .mr-xl-n2,
  .mx-xl-n2 {
    margin-right: -0.5rem !important; }
  .mb-xl-n2,
  .my-xl-n2 {
    margin-bottom: -0.5rem !important; }
  .ml-xl-n2,
  .mx-xl-n2 {
    margin-left: -0.5rem !important; }
  .m-xl-n3 {
    margin: -1rem !important; }
  .mt-xl-n3,
  .my-xl-n3 {
    margin-top: -1rem !important; }
  .mr-xl-n3,
  .mx-xl-n3 {
    margin-right: -1rem !important; }
  .mb-xl-n3,
  .my-xl-n3 {
    margin-bottom: -1rem !important; }
  .ml-xl-n3,
  .mx-xl-n3 {
    margin-left: -1rem !important; }
  .m-xl-n4 {
    margin: -1.5rem !important; }
  .mt-xl-n4,
  .my-xl-n4 {
    margin-top: -1.5rem !important; }
  .mr-xl-n4,
  .mx-xl-n4 {
    margin-right: -1.5rem !important; }
  .mb-xl-n4,
  .my-xl-n4 {
    margin-bottom: -1.5rem !important; }
  .ml-xl-n4,
  .mx-xl-n4 {
    margin-left: -1.5rem !important; }
  .m-xl-n5 {
    margin: -3rem !important; }
  .mt-xl-n5,
  .my-xl-n5 {
    margin-top: -3rem !important; }
  .mr-xl-n5,
  .mx-xl-n5 {
    margin-right: -3rem !important; }
  .mb-xl-n5,
  .my-xl-n5 {
    margin-bottom: -3rem !important; }
  .ml-xl-n5,
  .mx-xl-n5 {
    margin-left: -3rem !important; }
  .m-xl-auto {
    margin: auto !important; }
  .mt-xl-auto,
  .my-xl-auto {
    margin-top: auto !important; }
  .mr-xl-auto,
  .mx-xl-auto {
    margin-right: auto !important; }
  .mb-xl-auto,
  .my-xl-auto {
    margin-bottom: auto !important; }
  .ml-xl-auto,
  .mx-xl-auto {
    margin-left: auto !important; } }

.text-monospace {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace !important; }

.text-justify {
  text-align: justify !important; }

.text-wrap {
  white-space: normal !important; }

.text-nowrap {
  white-space: nowrap !important; }

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap; }

.text-left {
  text-align: left !important; }

.text-right {
  text-align: right !important; }

.text-center {
  text-align: center !important; }

@media (min-width: 576px) {
  .text-sm-left {
    text-align: left !important; }
  .text-sm-right {
    text-align: right !important; }
  .text-sm-center {
    text-align: center !important; } }

@media (min-width: 768px) {
  .text-md-left {
    text-align: left !important; }
  .text-md-right {
    text-align: right !important; }
  .text-md-center {
    text-align: center !important; } }

@media (min-width: 992px) {
  .text-lg-left {
    text-align: left !important; }
  .text-lg-right {
    text-align: right !important; }
  .text-lg-center {
    text-align: center !important; } }

@media (min-width: 1200px) {
  .text-xl-left {
    text-align: left !important; }
  .text-xl-right {
    text-align: right !important; }
  .text-xl-center {
    text-align: center !important; } }

.text-lowercase {
  text-transform: lowercase !important; }

.text-uppercase {
  text-transform: uppercase !important; }

.text-capitalize {
  text-transform: capitalize !important; }

.font-weight-light {
  font-weight: 300 !important; }

.font-weight-lighter {
  font-weight: lighter !important; }

.font-weight-normal {
  font-weight: 400 !important; }

.font-weight-bold {
  font-weight: 700 !important; }

.font-weight-bolder {
  font-weight: bolder !important; }

.font-italic {
  font-style: italic !important; }

.text-white {
  color: #fff !important; }

.text-primary {
  color: #714cdf !important; }

a.text-primary:hover, a.text-primary:focus {
  color: #4922bd !important; }

.text-secondary {
  color: #16a4de !important; }

a.text-secondary:hover, a.text-secondary:focus {
  color: #0f7198 !important; }

.text-success {
  color: #17b06b !important; }

a.text-success:hover, a.text-success:focus {
  color: #0e6c42 !important; }

.text-info {
  color: #2983fe !important; }

a.text-info:hover, a.text-info:focus {
  color: #015cd9 !important; }

.text-warning {
  color: #f97515 !important; }

a.text-warning:hover, a.text-warning:focus {
  color: #bd5205 !important; }

.text-danger {
  color: #ff3c5c !important; }

a.text-danger:hover, a.text-danger:focus {
  color: #ef0027 !important; }

.text-light {
  color: #dbebfb !important; }

a.text-light:hover, a.text-light:focus {
  color: #96c5f3 !important; }

.text-dark {
  color: #32334a !important; }

a.text-dark:hover, a.text-dark:focus {
  color: #13141c !important; }

.text-body {
  color: #e4e2ff !important; }

.text-muted {
  color: #81839a !important; }

.text-black-50 {
  color: rgba(0, 0, 0, 0.5) !important; }

.text-white-50 {
  color: rgba(255, 255, 255, 0.5) !important; }

.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0; }

.text-decoration-none {
  text-decoration: none !important; }

.text-break {
  word-break: break-word !important;
  overflow-wrap: break-word !important; }

.text-reset {
  color: inherit !important; }

.visible {
  visibility: visible !important; }

.invisible {
  visibility: hidden !important; }

@media print {
  *,
  *::before,
  *::after {
    text-shadow: none !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important; }
  a:not(.btn) {
    text-decoration: underline; }
  abbr[title]::after {
    content: " (" attr(title) ")"; }
  pre {
    white-space: pre-wrap !important; }
  pre,
  blockquote {
    border: 1px solid #1c1d2c;
    page-break-inside: avoid; }
  thead {
    display: table-header-group; }
  tr,
  img {
    page-break-inside: avoid; }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3; }
  h2,
  h3 {
    page-break-after: avoid; }
  @page {
    size: a3; }
  body {
    min-width: 992px !important; }
  .container {
    min-width: 992px !important; }
  .navbar {
    display: none; }
  .badge {
    border: 1px solid #000; }
  .table {
    border-collapse: collapse !important; }
    .table td,
    .table th {
      background-color: #fff !important; }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #28293e !important; }
  .table-dark {
    color: inherit; }
    .table-dark th,
    .table-dark td,
    .table-dark thead th,
    .table-dark tbody + tbody {
      border-color: #28293e; }
  .table .thead-dark th {
    color: inherit;
    border-color: #28293e; } }

.btn-hover-text-primary:hover, .btn-hover-text-primary:active {
  color: #714cdf !important; }

.btn-hover-text-secondary:hover, .btn-hover-text-secondary:active {
  color: #16a4de !important; }

.btn-hover-text-success:hover, .btn-hover-text-success:active {
  color: #17b06b !important; }

.btn-hover-text-info:hover, .btn-hover-text-info:active {
  color: #2983fe !important; }

.btn-hover-text-warning:hover, .btn-hover-text-warning:active {
  color: #f97515 !important; }

.btn-hover-text-danger:hover, .btn-hover-text-danger:active {
  color: #ff3c5c !important; }

.btn-hover-text-light:hover, .btn-hover-text-light:active {
  color: #dbebfb !important; }

.btn-hover-text-dark:hover, .btn-hover-text-dark:active {
  color: #32334a !important; }

.btn-wide {
  padding-left: 50px;
  padding-right: 50px; }

.display-fix {
  margin-left: -4px; }

.btn-pill {
  border-radius: 100px; }

.lead-lg {
  font-size: 35px; }

.radius-0 {
  border-radius: 0; }

.text-spacey {
  line-height: 28px; }

@media (max-width: 767.98px) {
  .display-1 {
    font-size: 4rem; } }

@media (max-width: 767.98px) {
  .display-2 {
    font-size: 3.5rem; } }

body {
  background-image: url("https://ozanam-cyberquest.fr/images/ng-background-dot.png"); }

.btn-shadow {
  margin-left: 8px; }
  .btn-shadow.btn-primary, .btn-shadow.btn-outline-primary {
    border-color: #986edf;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-primary, .btn-shadow.btn-primary.focus, .btn-shadow.btn-primary:focus, .btn-shadow.btn-outline-primary, .btn-shadow.btn-outline-primary.focus, .btn-shadow.btn-outline-primary:focus {
      -webkit-box-shadow: 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
              box-shadow: 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf; }
    .btn-shadow.btn-primary:hover, .btn-shadow.btn-outline-primary:hover {
      -webkit-box-shadow: 5px 5px 0 #986edf, 4px 4px 0 #986edf, 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
              box-shadow: 5px 5px 0 #986edf, 4px 4px 0 #986edf, 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-primary:active, .btn-shadow.btn-outline-primary:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-secondary, .btn-shadow.btn-outline-secondary {
    border-color: #87c4f2;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-secondary, .btn-shadow.btn-secondary.focus, .btn-shadow.btn-secondary:focus, .btn-shadow.btn-outline-secondary, .btn-shadow.btn-outline-secondary.focus, .btn-shadow.btn-outline-secondary:focus {
      -webkit-box-shadow: 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
              box-shadow: 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2; }
    .btn-shadow.btn-secondary:hover, .btn-shadow.btn-outline-secondary:hover {
      -webkit-box-shadow: 5px 5px 0 #87c4f2, 4px 4px 0 #87c4f2, 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
              box-shadow: 5px 5px 0 #87c4f2, 4px 4px 0 #87c4f2, 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-secondary:active, .btn-shadow.btn-outline-secondary:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-success, .btn-shadow.btn-outline-success {
    border-color: #43cb8e;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-success, .btn-shadow.btn-success.focus, .btn-shadow.btn-success:focus, .btn-shadow.btn-outline-success, .btn-shadow.btn-outline-success.focus, .btn-shadow.btn-outline-success:focus {
      -webkit-box-shadow: 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
              box-shadow: 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e; }
    .btn-shadow.btn-success:hover, .btn-shadow.btn-outline-success:hover {
      -webkit-box-shadow: 5px 5px 0 #43cb8e, 4px 4px 0 #43cb8e, 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
              box-shadow: 5px 5px 0 #43cb8e, 4px 4px 0 #43cb8e, 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-success:active, .btn-shadow.btn-outline-success:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-info, .btn-shadow.btn-outline-info {
    border-color: #25a8eb;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-info, .btn-shadow.btn-info.focus, .btn-shadow.btn-info:focus, .btn-shadow.btn-outline-info, .btn-shadow.btn-outline-info.focus, .btn-shadow.btn-outline-info:focus {
      -webkit-box-shadow: 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
              box-shadow: 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb; }
    .btn-shadow.btn-info:hover, .btn-shadow.btn-outline-info:hover {
      -webkit-box-shadow: 5px 5px 0 #25a8eb, 4px 4px 0 #25a8eb, 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
              box-shadow: 5px 5px 0 #25a8eb, 4px 4px 0 #25a8eb, 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-info:active, .btn-shadow.btn-outline-info:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-warning, .btn-shadow.btn-outline-warning {
    border-color: #f99511;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-warning, .btn-shadow.btn-warning.focus, .btn-shadow.btn-warning:focus, .btn-shadow.btn-outline-warning, .btn-shadow.btn-outline-warning.focus, .btn-shadow.btn-outline-warning:focus {
      -webkit-box-shadow: 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
              box-shadow: 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511; }
    .btn-shadow.btn-warning:hover, .btn-shadow.btn-outline-warning:hover {
      -webkit-box-shadow: 5px 5px 0 #f99511, 4px 4px 0 #f99511, 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
              box-shadow: 5px 5px 0 #f99511, 4px 4px 0 #f99511, 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-warning:active, .btn-shadow.btn-outline-warning:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-danger, .btn-shadow.btn-outline-danger {
    border-color: #ff707f;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-danger, .btn-shadow.btn-danger.focus, .btn-shadow.btn-danger:focus, .btn-shadow.btn-outline-danger, .btn-shadow.btn-outline-danger.focus, .btn-shadow.btn-outline-danger:focus {
      -webkit-box-shadow: 3px 3px 0 #ff707f, 2px 2px 0 #ff707f, 1px 1px 0 #ff707f;
              box-shadow: 3px 3px 0 #ff707f, 2px 2px 0 #ff707f, 1px 1px 0 #ff707f; }
    .btn-shadow.btn-danger:hover, .btn-shadow.btn-outline-danger:hover {
      -webkit-box-shadow: 5px 5px 0 #ff707f, 4px 4px 0 #ff707f, 3px 3px 0 #ff707f, 2px 2px 0 #ff707f, 1px 1px 0 #ff707f;
              box-shadow: 5px 5px 0 #ff707f, 4px 4px 0 #ff707f, 3px 3px 0 #ff707f, 2px 2px 0 #ff707f, 1px 1px 0 #ff707f;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-danger:active, .btn-shadow.btn-outline-danger:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-light, .btn-shadow.btn-outline-light {
    border-color: #9ea9b6;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-light, .btn-shadow.btn-light.focus, .btn-shadow.btn-light:focus, .btn-shadow.btn-outline-light, .btn-shadow.btn-outline-light.focus, .btn-shadow.btn-outline-light:focus {
      -webkit-box-shadow: 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
              box-shadow: 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6; }
    .btn-shadow.btn-light:hover, .btn-shadow.btn-outline-light:hover {
      -webkit-box-shadow: 5px 5px 0 #9ea9b6, 4px 4px 0 #9ea9b6, 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
              box-shadow: 5px 5px 0 #9ea9b6, 4px 4px 0 #9ea9b6, 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-light:active, .btn-shadow.btn-outline-light:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-dark, .btn-shadow.btn-outline-dark {
    border-color: #191a2d;
    -webkit-transition: none;
    -o-transition: none;
    transition: none; }
    .btn-shadow.btn-dark, .btn-shadow.btn-dark.focus, .btn-shadow.btn-dark:focus, .btn-shadow.btn-outline-dark, .btn-shadow.btn-outline-dark.focus, .btn-shadow.btn-outline-dark:focus {
      -webkit-box-shadow: 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
              box-shadow: 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d; }
    .btn-shadow.btn-dark:hover, .btn-shadow.btn-outline-dark:hover {
      -webkit-box-shadow: 5px 5px 0 #191a2d, 4px 4px 0 #191a2d, 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
              box-shadow: 5px 5px 0 #191a2d, 4px 4px 0 #191a2d, 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
      -webkit-transform: translate(-2px, -2px);
           -o-transform: translate(-2px, -2px);
              transform: translate(-2px, -2px);
      -webkit-transition: all .3s ease;
      -o-transition: all .3s ease;
      transition: all .3s ease; }
    .btn-shadow.btn-dark:active, .btn-shadow.btn-outline-dark:active {
      -webkit-box-shadow: none;
              box-shadow: none;
      -webkit-transform: translate(4px, 4px) !important;
           -o-transform: translate(4px, 4px) !important;
              transform: translate(4px, 4px) !important;
      -webkit-transition: all .1s ease;
      -o-transition: all .1s ease;
      transition: all .1s ease; }
  .btn-shadow.btn-primary:hover, .btn-shadow.btn-outline-primary:hover {
    background-color: #714cdf; }
  .btn-shadow.btn-secondary:hover, .btn-shadow.btn-outline-secondary:hover {
    background-color: #16a4de; }
  .btn-shadow.btn-success:hover, .btn-shadow.btn-outline-success:hover {
    background-color: #17b06b; }
  .btn-shadow.btn-info:hover, .btn-shadow.btn-outline-info:hover {
    background-color: #2983fe; }
  .btn-shadow.btn-warning:hover, .btn-shadow.btn-outline-warning:hover {
    background-color: #f97515; }
  .btn-shadow.btn-danger:hover, .btn-shadow.btn-outline-danger:hover {
    background-color: #ff3c5c; }
  .btn-shadow.btn-light:hover, .btn-shadow.btn-outline-light:hover {
    background-color: #dbebfb; }
  .btn-shadow.btn-dark:hover, .btn-shadow.btn-outline-dark:hover {
    background-color: #32334a; }

.display-1,
.display-2,
.display-3,
.display-4 {
  font-family: "Hack", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; }
  .text-white .display-1, .display-1.text-white, .text-white
  .display-2,
  .display-2.text-white, .text-white
  .display-3,
  .display-3.text-white, .text-white
  .display-4,
  .display-4.text-white {
    text-shadow: -1px -1px rgba(255, 255, 255, 0.2); }

.text-reduced-opacity {
  opacity: .5; }

.text-grey {
  color: #a0a0a0; }

.text-darkblue {
  color: #4d4d74; }

.text-darkgrey {
  color: #6f6974; }

.text-mono {
  font-family: "Hack", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; }

.btn-success, .btn-success:hover, .btn-success:focus, .btn-success:active {
  color: #c1f8c2; }

.vim-caret {
  -webkit-animation: vimCaret 1s linear infinite;
       -o-animation: vimCaret 1s linear infinite;
          animation: vimCaret 1s linear infinite; }

@-webkit-keyframes vimCaret {
  0% {
    background-color: transparent; }
  49% {
    background-color: transparent; }
  50% {
    background-color: rgba(255, 255, 255, 0.2); }
  100% {
    background-color: rgba(255, 255, 255, 0.2); } }

@-o-keyframes vimCaret {
  0% {
    background-color: transparent; }
  49% {
    background-color: transparent; }
  50% {
    background-color: rgba(255, 255, 255, 0.2); }
  100% {
    background-color: rgba(255, 255, 255, 0.2); } }

@keyframes vimCaret {
  0% {
    background-color: transparent; }
  49% {
    background-color: transparent; }
  50% {
    background-color: rgba(255, 255, 255, 0.2); }
  100% {
    background-color: rgba(255, 255, 255, 0.2); } }

.list-group-item-primary {
  color: #3b2874;
  background-color: #8869e4; }
  .list-group-item-primary.list-group-item-action:hover, .list-group-item-primary.list-group-item-action:focus {
    color: #3b2874;
    background-color: #7753e0; }
  .list-group-item-primary.list-group-item-action.active {
    color: #fff;
    background-color: #3b2874;
    border-color: #3b2874; }

.list-group-item-secondary {
  color: #0b5573;
  background-color: #3bb3e3; }
  .list-group-item-secondary.list-group-item-action:hover, .list-group-item-secondary.list-group-item-action:focus {
    color: #0b5573;
    background-color: #25aae0; }
  .list-group-item-secondary.list-group-item-action.active {
    color: #fff;
    background-color: #0b5573;
    border-color: #0b5573; }

.list-group-item-success {
  color: #0c5c38;
  background-color: #3cbd83; }
  .list-group-item-success.list-group-item-action:hover, .list-group-item-success.list-group-item-action:focus {
    color: #0c5c38;
    background-color: #36aa76; }
  .list-group-item-success.list-group-item-action.active {
    color: #fff;
    background-color: #0c5c38;
    border-color: #0c5c38; }

.list-group-item-info {
  color: #154484;
  background-color: #4b97fe; }
  .list-group-item-info.list-group-item-action:hover, .list-group-item-info.list-group-item-action:focus {
    color: #154484;
    background-color: #3288fe; }
  .list-group-item-info.list-group-item-action.active {
    color: #fff;
    background-color: #154484;
    border-color: #154484; }

.list-group-item-warning {
  color: #813d0b;
  background-color: #fa8b3a; }
  .list-group-item-warning.list-group-item-action:hover, .list-group-item-warning.list-group-item-action:focus {
    color: #813d0b;
    background-color: #f97c21; }
  .list-group-item-warning.list-group-item-action.active {
    color: #fff;
    background-color: #813d0b;
    border-color: #813d0b; }

.list-group-item-danger {
  color: #851f30;
  background-color: #ff5b76; }
  .list-group-item-danger.list-group-item-action:hover, .list-group-item-danger.list-group-item-action:focus {
    color: #851f30;
    background-color: #ff4261; }
  .list-group-item-danger.list-group-item-action.active {
    color: #fff;
    background-color: #851f30;
    border-color: #851f30; }

.list-group-item-light {
  color: #727a83;
  background-color: #e1eefc; }
  .list-group-item-light.list-group-item-action:hover, .list-group-item-light.list-group-item-action:focus {
    color: #727a83;
    background-color: #cae1fa; }
  .list-group-item-light.list-group-item-action.active {
    color: #fff;
    background-color: #727a83;
    border-color: #727a83; }

.list-group-item-dark {
  color: #1a1b26;
  background-color: #535467; }
  .list-group-item-dark.list-group-item-action:hover, .list-group-item-dark.list-group-item-action:focus {
    color: #1a1b26;
    background-color: #484859; }
  .list-group-item-dark.list-group-item-action.active {
    color: #fff;
    background-color: #1a1b26;
    border-color: #1a1b26; }

.alert-primary {
  color: #322162;
  background-color: #aa94ec;
  border-color: #8869e4; }
  .alert-primary hr {
    border-top-color: #7753e0; }
  .alert-primary .alert-link {
    color: #1f143c; }

.alert-secondary {
  color: #0a4862;
  background-color: #73c8eb;
  border-color: #3bb3e3; }
  .alert-secondary hr {
    border-top-color: #25aae0; }
  .alert-secondary .alert-link {
    color: #052634; }

.alert-success {
  color: #0a4d2f;
  background-color: #74d0a6;
  border-color: #3cbd83; }
  .alert-success hr {
    border-top-color: #36aa76; }
  .alert-success .alert-link {
    color: #042013; }

.alert-info {
  color: #123a70;
  background-color: #7fb5fe;
  border-color: #4b97fe; }
  .alert-info hr {
    border-top-color: #3288fe; }
  .alert-info .alert-link {
    color: #0b2344; }

.alert-warning {
  color: #6e3309;
  background-color: #fbac73;
  border-color: #fa8b3a; }
  .alert-warning hr {
    border-top-color: #f97c21; }
  .alert-warning .alert-link {
    color: #3f1d05; }

.alert-danger {
  color: #701a28;
  background-color: #ff8a9d;
  border-color: #ff5b76; }
  .alert-danger hr {
    border-top-color: #ff4261; }
  .alert-danger .alert-link {
    color: #471019; }

.alert-light {
  color: #60676e;
  background-color: #e9f3fd;
  border-color: #e1eefc; }
  .alert-light hr {
    border-top-color: #cae1fa; }
  .alert-light .alert-link {
    color: #484e53; }

.alert-dark {
  color: #161621;
  background-color: #848592;
  border-color: #535467; }
  .alert-dark hr {
    border-top-color: #484859; }
  .alert-dark .alert-link {
    color: #020202; }

.table-primary,
.table-primary > th,
.table-primary > td {
  background-color: #8869e4; }

.table-hover .table-primary:hover {
  background-color: #7753e0; }
  .table-hover .table-primary:hover > td,
  .table-hover .table-primary:hover > th {
    background-color: #7753e0; }

.table-secondary,
.table-secondary > th,
.table-secondary > td {
  background-color: #3bb3e3; }

.table-hover .table-secondary:hover {
  background-color: #25aae0; }
  .table-hover .table-secondary:hover > td,
  .table-hover .table-secondary:hover > th {
    background-color: #25aae0; }

.table-success,
.table-success > th,
.table-success > td {
  background-color: #3cbd83; }

.table-hover .table-success:hover {
  background-color: #36aa76; }
  .table-hover .table-success:hover > td,
  .table-hover .table-success:hover > th {
    background-color: #36aa76; }

.table-info,
.table-info > th,
.table-info > td {
  background-color: #4b97fe; }

.table-hover .table-info:hover {
  background-color: #3288fe; }
  .table-hover .table-info:hover > td,
  .table-hover .table-info:hover > th {
    background-color: #3288fe; }

.table-warning,
.table-warning > th,
.table-warning > td {
  background-color: #fa8b3a; }

.table-hover .table-warning:hover {
  background-color: #f97c21; }
  .table-hover .table-warning:hover > td,
  .table-hover .table-warning:hover > th {
    background-color: #f97c21; }

.table-danger,
.table-danger > th,
.table-danger > td {
  background-color: #ff5b76; }

.table-hover .table-danger:hover {
  background-color: #ff4261; }
  .table-hover .table-danger:hover > td,
  .table-hover .table-danger:hover > th {
    background-color: #ff4261; }

.table-light,
.table-light > th,
.table-light > td {
  background-color: #e1eefc; }

.table-hover .table-light:hover {
  background-color: #cae1fa; }
  .table-hover .table-light:hover > td,
  .table-hover .table-light:hover > th {
    background-color: #cae1fa; }

.table-dark,
.table-dark > th,
.table-dark > td {
  background-color: #535467; }

.table-hover .table-dark:hover {
  background-color: #484859; }
  .table-hover .table-dark:hover > td,
  .table-hover .table-dark:hover > th {
    background-color: #484859; }

.hal-9000 {
  background: #f9d080;
  border: 12px #ff3c5c solid;
  border-radius: 90px;
  -webkit-box-shadow: 0 0 40px #ff3c5c;
          box-shadow: 0 0 40px #ff3c5c;
  display: inline-block;
  height: 40px;
  width: 40px; }
"""

def generate_bootstrap4_neon_glow_min_css():
    return """

:root {
    --blue: #007bff;
    --indigo: #6610f2;
    --purple: #6f42c1;
    --pink: #e83e8c;
    --red: #dc3545;
    --orange: #fd7e14;
    --yellow: #ffc107;
    --green: #28a745;
    --teal: #20c997;
    --cyan: #17a2b8;
    --white: #fff;
    --gray: #1d1e2f;
    --gray-dark: #11111d;
    --primary: #714cdf;
    --secondary: #16a4de;
    --success: #17b06b;
    --info: #2983fe;
    --warning: #f97515;
    --danger: #ef121b;
    --light: #dbebfb;
    --dark: #32334a;
    --breakpoint-xs: 0;
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
    --font-family-sans-serif: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace
}

*,
::after,
::before {
    -webkit-box-sizing: border-box;
    box-sizing: border-box
}

html {
    font-family: sans-serif;
    line-height: 1.15;
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: transparent
}

article,
aside,
figcaption,
figure,
footer,
header,
hgroup,
main,
nav,
section {
    display: block
}

body {
    margin: 0;
    font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #e4e2ff;
    text-align: left;
    background-color: #000e20
}

[tabindex="-1"]:focus {
    outline: 0!important
}

hr {
    -webkit-box-sizing: content-box;
    box-sizing: content-box;
    height: 0;
    overflow: visible
}

h1,
h2,
h3,
h4,
h5,
h6 {
    margin-top: 0;
    margin-bottom: .5rem
}

p {
    margin-top: 0;
    margin-bottom: 1rem
}

abbr[data-original-title],
abbr[title] {
    text-decoration: underline;
    -webkit-text-decoration: underline dotted;
    text-decoration: underline dotted;
    cursor: help;
    border-bottom: 0;
    -webkit-text-decoration-skip-ink: none;
    text-decoration-skip-ink: none
}

address {
    margin-bottom: 1rem;
    font-style: normal;
    line-height: inherit
}

dl,
ol,
ul {
    margin-top: 0;
    margin-bottom: 1rem
}

ol ol,
ol ul,
ul ol,
ul ul {
    margin-bottom: 0
}

dt {
    font-weight: 700
}

dd {
    margin-bottom: .5rem;
    margin-left: 0
}

blockquote {
    margin: 0 0 1rem
}

b,
strong {
    font-weight: bolder
}

small {
    font-size: 80%
}

sub,
sup {
    position: relative;
    font-size: 75%;
    line-height: 0;
    vertical-align: baseline
}

sub {
    bottom: -.25em
}

sup {
    top: -.5em
}

a {
    color: #714cdf;
    text-decoration: none;
    background-color: transparent
}

a:hover {
    color: #4922bd;
    text-decoration: underline
}

a:not([href]):not([tabindex]) {
    color: inherit;
    text-decoration: none
}

a:not([href]):not([tabindex]):focus,
a:not([href]):not([tabindex]):hover {
    color: inherit;
    text-decoration: none
}

a:not([href]):not([tabindex]):focus {
    outline: 0
}

code,
kbd,
pre,
samp {
    font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 1em
}

pre {
    margin-top: 0;
    margin-bottom: 1rem;
    overflow: auto
}

figure {
    margin: 0 0 1rem
}

img {
    vertical-align: middle;
    border-style: none
}

svg {
    overflow: hidden;
    vertical-align: middle
}

table {
    border-collapse: collapse
}

caption {
    padding-top: .75rem;
    padding-bottom: .75rem;
    color: #81839a;
    text-align: left;
    caption-side: bottom
}

th {
    text-align: inherit
}

label {
    display: inline-block;
    margin-bottom: .5rem
}

button {
    border-radius: 0
}

button:focus {
    outline: 1px dotted;
    outline: 5px auto -webkit-focus-ring-color
}

button,
input,
optgroup,
select,
textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit
}

button,
input {
    overflow: visible
}

button,
select {
    text-transform: none
}

select {
    word-wrap: normal
}

[type=button],
[type=reset],
[type=submit],
button {
    -webkit-appearance: button
}

[type=button]:not(:disabled),
[type=reset]:not(:disabled),
[type=submit]:not(:disabled),
button:not(:disabled) {
    cursor: pointer
}

[type=button]::-moz-focus-inner,
[type=reset]::-moz-focus-inner,
[type=submit]::-moz-focus-inner,
button::-moz-focus-inner {
    padding: 0;
    border-style: none
}

input[type=checkbox],
input[type=radio] {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    padding: 0
}

input[type=date],
input[type=datetime-local],
input[type=month],
input[type=time] {
    -webkit-appearance: listbox
}

textarea {
    overflow: auto;
    resize: vertical
}

fieldset {
    min-width: 0;
    padding: 0;
    margin: 0;
    border: 0
}

legend {
    display: block;
    width: 100%;
    max-width: 100%;
    padding: 0;
    margin-bottom: .5rem;
    font-size: 1.5rem;
    line-height: inherit;
    color: inherit;
    white-space: normal
}

progress {
    vertical-align: baseline
}

[type=number]::-webkit-inner-spin-button,
[type=number]::-webkit-outer-spin-button {
    height: auto
}

[type=search] {
    outline-offset: -2px;
    -webkit-appearance: none
}

[type=search]::-webkit-search-decoration {
    -webkit-appearance: none
}

::-webkit-file-upload-button {
    font: inherit;
    -webkit-appearance: button
}

output {
    display: inline-block
}

summary {
    display: list-item;
    cursor: pointer
}

template {
    display: none
}

[hidden] {
    display: none!important
}

.h1,
.h2,
.h3,
.h4,
.h5,
.h6,
h1,
h2,
h3,
h4,
h5,
h6 {
    margin-bottom: .5rem;
    font-weight: 500;
    line-height: 1.2
}

.h1,
h1 {
    font-size: 2.5rem
}

.h2,
h2 {
    font-size: 2rem
}

.h3,
h3 {
    font-size: 1.75rem
}

.h4,
h4 {
    font-size: 1.5rem
}

.h5,
h5 {
    font-size: 1.25rem
}

.h6,
h6 {
    font-size: 1rem
}

.lead {
    font-size: 1.25rem;
    font-weight: 300
}

.display-1 {
    font-size: 4.5rem;
    font-weight: 300;
    line-height: 1.2
}

.display-2 {
    font-size: 3.5rem;
    font-weight: 300;
    line-height: 1.2
}

.display-3 {
    font-size: 2.5rem;
    font-weight: 300;
    line-height: 1.2
}

.display-4 {
    font-size: 2rem;
    font-weight: 300;
    line-height: 1.2
}

hr {
    margin-top: 1rem;
    margin-bottom: 1rem;
    border: 0;
    border-top: 1px solid rgba(0, 0, 0, .1)
}

.small,
small {
    font-size: 80%;
    font-weight: 400
}

.mark,
mark {
    padding: .2em;
    background-color: #fcf8e3
}

.list-unstyled {
    padding-left: 0;
    list-style: none
}

.list-inline {
    padding-left: 0;
    list-style: none
}

.list-inline-item {
    display: inline-block
}

.list-inline-item:not(:last-child) {
    margin-right: .5rem
}

.initialism {
    font-size: 90%;
    text-transform: uppercase
}

.blockquote {
    margin-bottom: 1rem;
    font-size: 1.25rem
}

.blockquote-footer {
    display: block;
    font-size: 80%;
    color: #81839a
}

.blockquote-footer::before {
    content: "\2014\00A0"
}

.img-fluid {
    max-width: 100%;
    height: auto
}

.img-thumbnail {
    padding: .25rem;
    background-color: #000e20;
    border: 1px solid #151623;
    border-radius: 6px;
    max-width: 100%;
    height: auto
}

.figure {
    display: inline-block
}

.figure-img {
    margin-bottom: .5rem;
    line-height: 1
}

.figure-caption {
    font-size: 90%;
    color: #1d1e2f
}

code {
    font-size: 87.5%;
    color: #2983fe;
    word-break: break-word
}

a>code {
    color: inherit
}

kbd {
    padding: .2rem .4rem;
    font-size: 87.5%;
    color: #32334a;
    background-color: #0a0b14;
    border-radius: .2rem
}

kbd kbd {
    padding: 0;
    font-size: 100%;
    font-weight: 700
}

pre {
    display: block;
    font-size: 87.5%;
    color: #0a0b14
}

pre code {
    font-size: inherit;
    color: inherit;
    word-break: normal
}

.pre-scrollable {
    max-height: 340px;
    overflow-y: scroll
}

.container {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto
}

@media (min-width:576px) {
    .container {
        max-width: 540px
    }
}

@media (min-width:768px) {
    .container {
        max-width: 720px
    }
}

@media (min-width:992px) {
    .container {
        max-width: 960px
    }
}

@media (min-width:1200px) {
    .container {
        max-width: 1140px
    }
}

.container-fluid {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto
}

.row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px
}

.no-gutters {
    margin-right: 0;
    margin-left: 0
}

.no-gutters>.col,
.no-gutters>[class*=col-] {
    padding-right: 0;
    padding-left: 0
}

.col,
.col-1,
.col-10,
.col-11,
.col-12,
.col-2,
.col-3,
.col-4,
.col-5,
.col-6,
.col-7,
.col-8,
.col-9,
.col-auto,
.col-lg,
.col-lg-1,
.col-lg-10,
.col-lg-11,
.col-lg-12,
.col-lg-2,
.col-lg-3,
.col-lg-4,
.col-lg-5,
.col-lg-6,
.col-lg-7,
.col-lg-8,
.col-lg-9,
.col-lg-auto,
.col-md,
.col-md-1,
.col-md-10,
.col-md-11,
.col-md-12,
.col-md-2,
.col-md-3,
.col-md-4,
.col-md-5,
.col-md-6,
.col-md-7,
.col-md-8,
.col-md-9,
.col-md-auto,
.col-sm,
.col-sm-1,
.col-sm-10,
.col-sm-11,
.col-sm-12,
.col-sm-2,
.col-sm-3,
.col-sm-4,
.col-sm-5,
.col-sm-6,
.col-sm-7,
.col-sm-8,
.col-sm-9,
.col-sm-auto,
.col-xl,
.col-xl-1,
.col-xl-10,
.col-xl-11,
.col-xl-12,
.col-xl-2,
.col-xl-3,
.col-xl-4,
.col-xl-5,
.col-xl-6,
.col-xl-7,
.col-xl-8,
.col-xl-9,
.col-xl-auto {
    position: relative;
    width: 100%;
    padding-right: 15px;
    padding-left: 15px
}

.col {
    -webkit-flex-basis: 0;
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
    -ms-flex-positive: 1;
    flex-grow: 1;
    max-width: 100%
}

.col-auto {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
    -ms-flex: 0 0 auto;
    flex: 0 0 auto;
    width: auto;
    max-width: 100%
}

.col-1 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 8.33333%;
    -ms-flex: 0 0 8.33333%;
    flex: 0 0 8.33333%;
    max-width: 8.33333%
}

.col-2 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 16.66667%;
    -ms-flex: 0 0 16.66667%;
    flex: 0 0 16.66667%;
    max-width: 16.66667%
}

.col-3 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 25%;
    -ms-flex: 0 0 25%;
    flex: 0 0 25%;
    max-width: 25%
}

.col-4 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 33.33333%;
    -ms-flex: 0 0 33.33333%;
    flex: 0 0 33.33333%;
    max-width: 33.33333%
}

.col-5 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 41.66667%;
    -ms-flex: 0 0 41.66667%;
    flex: 0 0 41.66667%;
    max-width: 41.66667%
}

.col-6 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 50%;
    -ms-flex: 0 0 50%;
    flex: 0 0 50%;
    max-width: 50%
}

.col-7 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 58.33333%;
    -ms-flex: 0 0 58.33333%;
    flex: 0 0 58.33333%;
    max-width: 58.33333%
}

.col-8 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 66.66667%;
    -ms-flex: 0 0 66.66667%;
    flex: 0 0 66.66667%;
    max-width: 66.66667%
}

.col-9 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 75%;
    -ms-flex: 0 0 75%;
    flex: 0 0 75%;
    max-width: 75%
}

.col-10 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 83.33333%;
    -ms-flex: 0 0 83.33333%;
    flex: 0 0 83.33333%;
    max-width: 83.33333%
}

.col-11 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 91.66667%;
    -ms-flex: 0 0 91.66667%;
    flex: 0 0 91.66667%;
    max-width: 91.66667%
}

.col-12 {
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 100%;
    -ms-flex: 0 0 100%;
    flex: 0 0 100%;
    max-width: 100%
}

.order-first {
    -webkit-box-ordinal-group: 0;
    -webkit-order: -1;
    -ms-flex-order: -1;
    order: -1
}

.order-last {
    -webkit-box-ordinal-group: 14;
    -webkit-order: 13;
    -ms-flex-order: 13;
    order: 13
}

.order-0 {
    -webkit-box-ordinal-group: 1;
    -webkit-order: 0;
    -ms-flex-order: 0;
    order: 0
}

.order-1 {
    -webkit-box-ordinal-group: 2;
    -webkit-order: 1;
    -ms-flex-order: 1;
    order: 1
}

.order-2 {
    -webkit-box-ordinal-group: 3;
    -webkit-order: 2;
    -ms-flex-order: 2;
    order: 2
}

.order-3 {
    -webkit-box-ordinal-group: 4;
    -webkit-order: 3;
    -ms-flex-order: 3;
    order: 3
}

.order-4 {
    -webkit-box-ordinal-group: 5;
    -webkit-order: 4;
    -ms-flex-order: 4;
    order: 4
}

.order-5 {
    -webkit-box-ordinal-group: 6;
    -webkit-order: 5;
    -ms-flex-order: 5;
    order: 5
}

.order-6 {
    -webkit-box-ordinal-group: 7;
    -webkit-order: 6;
    -ms-flex-order: 6;
    order: 6
}

.order-7 {
    -webkit-box-ordinal-group: 8;
    -webkit-order: 7;
    -ms-flex-order: 7;
    order: 7
}

.order-8 {
    -webkit-box-ordinal-group: 9;
    -webkit-order: 8;
    -ms-flex-order: 8;
    order: 8
}

.order-9 {
    -webkit-box-ordinal-group: 10;
    -webkit-order: 9;
    -ms-flex-order: 9;
    order: 9
}

.order-10 {
    -webkit-box-ordinal-group: 11;
    -webkit-order: 10;
    -ms-flex-order: 10;
    order: 10
}

.order-11 {
    -webkit-box-ordinal-group: 12;
    -webkit-order: 11;
    -ms-flex-order: 11;
    order: 11
}

.order-12 {
    -webkit-box-ordinal-group: 13;
    -webkit-order: 12;
    -ms-flex-order: 12;
    order: 12
}

.offset-1 {
    margin-left: 8.33333%
}

.offset-2 {
    margin-left: 16.66667%
}

.offset-3 {
    margin-left: 25%
}

.offset-4 {
    margin-left: 33.33333%
}

.offset-5 {
    margin-left: 41.66667%
}

.offset-6 {
    margin-left: 50%
}

.offset-7 {
    margin-left: 58.33333%
}

.offset-8 {
    margin-left: 66.66667%
}

.offset-9 {
    margin-left: 75%
}

.offset-10 {
    margin-left: 83.33333%
}

.offset-11 {
    margin-left: 91.66667%
}

@media (min-width:576px) {
    .col-sm {
        -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
        flex-basis: 0;
        -webkit-box-flex: 1;
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        flex-grow: 1;
        max-width: 100%
    }
    .col-sm-auto {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        width: auto;
        max-width: 100%
    }
    .col-sm-1 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
        flex: 0 0 8.33333%;
        max-width: 8.33333%
    }
    .col-sm-2 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
        flex: 0 0 16.66667%;
        max-width: 16.66667%
    }
    .col-sm-3 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
        flex: 0 0 25%;
        max-width: 25%
    }
    .col-sm-4 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
        flex: 0 0 33.33333%;
        max-width: 33.33333%
    }
    .col-sm-5 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
        flex: 0 0 41.66667%;
        max-width: 41.66667%
    }
    .col-sm-6 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
        flex: 0 0 50%;
        max-width: 50%
    }
    .col-sm-7 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
        flex: 0 0 58.33333%;
        max-width: 58.33333%
    }
    .col-sm-8 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
        flex: 0 0 66.66667%;
        max-width: 66.66667%
    }
    .col-sm-9 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
        flex: 0 0 75%;
        max-width: 75%
    }
    .col-sm-10 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
        flex: 0 0 83.33333%;
        max-width: 83.33333%
    }
    .col-sm-11 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
        flex: 0 0 91.66667%;
        max-width: 91.66667%
    }
    .col-sm-12 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
        flex: 0 0 100%;
        max-width: 100%
    }
    .order-sm-first {
        -webkit-box-ordinal-group: 0;
        -webkit-order: -1;
        -ms-flex-order: -1;
        order: -1
    }
    .order-sm-last {
        -webkit-box-ordinal-group: 14;
        -webkit-order: 13;
        -ms-flex-order: 13;
        order: 13
    }
    .order-sm-0 {
        -webkit-box-ordinal-group: 1;
        -webkit-order: 0;
        -ms-flex-order: 0;
        order: 0
    }
    .order-sm-1 {
        -webkit-box-ordinal-group: 2;
        -webkit-order: 1;
        -ms-flex-order: 1;
        order: 1
    }
    .order-sm-2 {
        -webkit-box-ordinal-group: 3;
        -webkit-order: 2;
        -ms-flex-order: 2;
        order: 2
    }
    .order-sm-3 {
        -webkit-box-ordinal-group: 4;
        -webkit-order: 3;
        -ms-flex-order: 3;
        order: 3
    }
    .order-sm-4 {
        -webkit-box-ordinal-group: 5;
        -webkit-order: 4;
        -ms-flex-order: 4;
        order: 4
    }
    .order-sm-5 {
        -webkit-box-ordinal-group: 6;
        -webkit-order: 5;
        -ms-flex-order: 5;
        order: 5
    }
    .order-sm-6 {
        -webkit-box-ordinal-group: 7;
        -webkit-order: 6;
        -ms-flex-order: 6;
        order: 6
    }
    .order-sm-7 {
        -webkit-box-ordinal-group: 8;
        -webkit-order: 7;
        -ms-flex-order: 7;
        order: 7
    }
    .order-sm-8 {
        -webkit-box-ordinal-group: 9;
        -webkit-order: 8;
        -ms-flex-order: 8;
        order: 8
    }
    .order-sm-9 {
        -webkit-box-ordinal-group: 10;
        -webkit-order: 9;
        -ms-flex-order: 9;
        order: 9
    }
    .order-sm-10 {
        -webkit-box-ordinal-group: 11;
        -webkit-order: 10;
        -ms-flex-order: 10;
        order: 10
    }
    .order-sm-11 {
        -webkit-box-ordinal-group: 12;
        -webkit-order: 11;
        -ms-flex-order: 11;
        order: 11
    }
    .order-sm-12 {
        -webkit-box-ordinal-group: 13;
        -webkit-order: 12;
        -ms-flex-order: 12;
        order: 12
    }
    .offset-sm-0 {
        margin-left: 0
    }
    .offset-sm-1 {
        margin-left: 8.33333%
    }
    .offset-sm-2 {
        margin-left: 16.66667%
    }
    .offset-sm-3 {
        margin-left: 25%
    }
    .offset-sm-4 {
        margin-left: 33.33333%
    }
    .offset-sm-5 {
        margin-left: 41.66667%
    }
    .offset-sm-6 {
        margin-left: 50%
    }
    .offset-sm-7 {
        margin-left: 58.33333%
    }
    .offset-sm-8 {
        margin-left: 66.66667%
    }
    .offset-sm-9 {
        margin-left: 75%
    }
    .offset-sm-10 {
        margin-left: 83.33333%
    }
    .offset-sm-11 {
        margin-left: 91.66667%
    }
}

@media (min-width:768px) {
    .col-md {
        -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
        flex-basis: 0;
        -webkit-box-flex: 1;
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        flex-grow: 1;
        max-width: 100%
    }
    .col-md-auto {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        width: auto;
        max-width: 100%
    }
    .col-md-1 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
        flex: 0 0 8.33333%;
        max-width: 8.33333%
    }
    .col-md-2 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
        flex: 0 0 16.66667%;
        max-width: 16.66667%
    }
    .col-md-3 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
        flex: 0 0 25%;
        max-width: 25%
    }
    .col-md-4 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
        flex: 0 0 33.33333%;
        max-width: 33.33333%
    }
    .col-md-5 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
        flex: 0 0 41.66667%;
        max-width: 41.66667%
    }
    .col-md-6 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
        flex: 0 0 50%;
        max-width: 50%
    }
    .col-md-7 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
        flex: 0 0 58.33333%;
        max-width: 58.33333%
    }
    .col-md-8 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
        flex: 0 0 66.66667%;
        max-width: 66.66667%
    }
    .col-md-9 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
        flex: 0 0 75%;
        max-width: 75%
    }
    .col-md-10 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
        flex: 0 0 83.33333%;
        max-width: 83.33333%
    }
    .col-md-11 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
        flex: 0 0 91.66667%;
        max-width: 91.66667%
    }
    .col-md-12 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
        flex: 0 0 100%;
        max-width: 100%
    }
    .order-md-first {
        -webkit-box-ordinal-group: 0;
        -webkit-order: -1;
        -ms-flex-order: -1;
        order: -1
    }
    .order-md-last {
        -webkit-box-ordinal-group: 14;
        -webkit-order: 13;
        -ms-flex-order: 13;
        order: 13
    }
    .order-md-0 {
        -webkit-box-ordinal-group: 1;
        -webkit-order: 0;
        -ms-flex-order: 0;
        order: 0
    }
    .order-md-1 {
        -webkit-box-ordinal-group: 2;
        -webkit-order: 1;
        -ms-flex-order: 1;
        order: 1
    }
    .order-md-2 {
        -webkit-box-ordinal-group: 3;
        -webkit-order: 2;
        -ms-flex-order: 2;
        order: 2
    }
    .order-md-3 {
        -webkit-box-ordinal-group: 4;
        -webkit-order: 3;
        -ms-flex-order: 3;
        order: 3
    }
    .order-md-4 {
        -webkit-box-ordinal-group: 5;
        -webkit-order: 4;
        -ms-flex-order: 4;
        order: 4
    }
    .order-md-5 {
        -webkit-box-ordinal-group: 6;
        -webkit-order: 5;
        -ms-flex-order: 5;
        order: 5
    }
    .order-md-6 {
        -webkit-box-ordinal-group: 7;
        -webkit-order: 6;
        -ms-flex-order: 6;
        order: 6
    }
    .order-md-7 {
        -webkit-box-ordinal-group: 8;
        -webkit-order: 7;
        -ms-flex-order: 7;
        order: 7
    }
    .order-md-8 {
        -webkit-box-ordinal-group: 9;
        -webkit-order: 8;
        -ms-flex-order: 8;
        order: 8
    }
    .order-md-9 {
        -webkit-box-ordinal-group: 10;
        -webkit-order: 9;
        -ms-flex-order: 9;
        order: 9
    }
    .order-md-10 {
        -webkit-box-ordinal-group: 11;
        -webkit-order: 10;
        -ms-flex-order: 10;
        order: 10
    }
    .order-md-11 {
        -webkit-box-ordinal-group: 12;
        -webkit-order: 11;
        -ms-flex-order: 11;
        order: 11
    }
    .order-md-12 {
        -webkit-box-ordinal-group: 13;
        -webkit-order: 12;
        -ms-flex-order: 12;
        order: 12
    }
    .offset-md-0 {
        margin-left: 0
    }
    .offset-md-1 {
        margin-left: 8.33333%
    }
    .offset-md-2 {
        margin-left: 16.66667%
    }
    .offset-md-3 {
        margin-left: 25%
    }
    .offset-md-4 {
        margin-left: 33.33333%
    }
    .offset-md-5 {
        margin-left: 41.66667%
    }
    .offset-md-6 {
        margin-left: 50%
    }
    .offset-md-7 {
        margin-left: 58.33333%
    }
    .offset-md-8 {
        margin-left: 66.66667%
    }
    .offset-md-9 {
        margin-left: 75%
    }
    .offset-md-10 {
        margin-left: 83.33333%
    }
    .offset-md-11 {
        margin-left: 91.66667%
    }
}

@media (min-width:992px) {
    .col-lg {
        -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
        flex-basis: 0;
        -webkit-box-flex: 1;
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        flex-grow: 1;
        max-width: 100%
    }
    .col-lg-auto {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        width: auto;
        max-width: 100%
    }
    .col-lg-1 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
        flex: 0 0 8.33333%;
        max-width: 8.33333%
    }
    .col-lg-2 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
        flex: 0 0 16.66667%;
        max-width: 16.66667%
    }
    .col-lg-3 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
        flex: 0 0 25%;
        max-width: 25%
    }
    .col-lg-4 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
        flex: 0 0 33.33333%;
        max-width: 33.33333%
    }
    .col-lg-5 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
        flex: 0 0 41.66667%;
        max-width: 41.66667%
    }
    .col-lg-6 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
        flex: 0 0 50%;
        max-width: 50%
    }
    .col-lg-7 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
        flex: 0 0 58.33333%;
        max-width: 58.33333%
    }
    .col-lg-8 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
        flex: 0 0 66.66667%;
        max-width: 66.66667%
    }
    .col-lg-9 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
        flex: 0 0 75%;
        max-width: 75%
    }
    .col-lg-10 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
        flex: 0 0 83.33333%;
        max-width: 83.33333%
    }
    .col-lg-11 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
        flex: 0 0 91.66667%;
        max-width: 91.66667%
    }
    .col-lg-12 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
        flex: 0 0 100%;
        max-width: 100%
    }
    .order-lg-first {
        -webkit-box-ordinal-group: 0;
        -webkit-order: -1;
        -ms-flex-order: -1;
        order: -1
    }
    .order-lg-last {
        -webkit-box-ordinal-group: 14;
        -webkit-order: 13;
        -ms-flex-order: 13;
        order: 13
    }
    .order-lg-0 {
        -webkit-box-ordinal-group: 1;
        -webkit-order: 0;
        -ms-flex-order: 0;
        order: 0
    }
    .order-lg-1 {
        -webkit-box-ordinal-group: 2;
        -webkit-order: 1;
        -ms-flex-order: 1;
        order: 1
    }
    .order-lg-2 {
        -webkit-box-ordinal-group: 3;
        -webkit-order: 2;
        -ms-flex-order: 2;
        order: 2
    }
    .order-lg-3 {
        -webkit-box-ordinal-group: 4;
        -webkit-order: 3;
        -ms-flex-order: 3;
        order: 3
    }
    .order-lg-4 {
        -webkit-box-ordinal-group: 5;
        -webkit-order: 4;
        -ms-flex-order: 4;
        order: 4
    }
    .order-lg-5 {
        -webkit-box-ordinal-group: 6;
        -webkit-order: 5;
        -ms-flex-order: 5;
        order: 5
    }
    .order-lg-6 {
        -webkit-box-ordinal-group: 7;
        -webkit-order: 6;
        -ms-flex-order: 6;
        order: 6
    }
    .order-lg-7 {
        -webkit-box-ordinal-group: 8;
        -webkit-order: 7;
        -ms-flex-order: 7;
        order: 7
    }
    .order-lg-8 {
        -webkit-box-ordinal-group: 9;
        -webkit-order: 8;
        -ms-flex-order: 8;
        order: 8
    }
    .order-lg-9 {
        -webkit-box-ordinal-group: 10;
        -webkit-order: 9;
        -ms-flex-order: 9;
        order: 9
    }
    .order-lg-10 {
        -webkit-box-ordinal-group: 11;
        -webkit-order: 10;
        -ms-flex-order: 10;
        order: 10
    }
    .order-lg-11 {
        -webkit-box-ordinal-group: 12;
        -webkit-order: 11;
        -ms-flex-order: 11;
        order: 11
    }
    .order-lg-12 {
        -webkit-box-ordinal-group: 13;
        -webkit-order: 12;
        -ms-flex-order: 12;
        order: 12
    }
    .offset-lg-0 {
        margin-left: 0
    }
    .offset-lg-1 {
        margin-left: 8.33333%
    }
    .offset-lg-2 {
        margin-left: 16.66667%
    }
    .offset-lg-3 {
        margin-left: 25%
    }
    .offset-lg-4 {
        margin-left: 33.33333%
    }
    .offset-lg-5 {
        margin-left: 41.66667%
    }
    .offset-lg-6 {
        margin-left: 50%
    }
    .offset-lg-7 {
        margin-left: 58.33333%
    }
    .offset-lg-8 {
        margin-left: 66.66667%
    }
    .offset-lg-9 {
        margin-left: 75%
    }
    .offset-lg-10 {
        margin-left: 83.33333%
    }
    .offset-lg-11 {
        margin-left: 91.66667%
    }
}

@media (min-width:1200px) {
    .col-xl {
        -webkit-flex-basis: 0;
        -ms-flex-preferred-size: 0;
        flex-basis: 0;
        -webkit-box-flex: 1;
        -webkit-flex-grow: 1;
        -ms-flex-positive: 1;
        flex-grow: 1;
        max-width: 100%
    }
    .col-xl-auto {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        width: auto;
        max-width: 100%
    }
    .col-xl-1 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 8.33333%;
        -ms-flex: 0 0 8.33333%;
        flex: 0 0 8.33333%;
        max-width: 8.33333%
    }
    .col-xl-2 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 16.66667%;
        -ms-flex: 0 0 16.66667%;
        flex: 0 0 16.66667%;
        max-width: 16.66667%
    }
    .col-xl-3 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 25%;
        -ms-flex: 0 0 25%;
        flex: 0 0 25%;
        max-width: 25%
    }
    .col-xl-4 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 33.33333%;
        -ms-flex: 0 0 33.33333%;
        flex: 0 0 33.33333%;
        max-width: 33.33333%
    }
    .col-xl-5 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 41.66667%;
        -ms-flex: 0 0 41.66667%;
        flex: 0 0 41.66667%;
        max-width: 41.66667%
    }
    .col-xl-6 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 50%;
        -ms-flex: 0 0 50%;
        flex: 0 0 50%;
        max-width: 50%
    }
    .col-xl-7 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 58.33333%;
        -ms-flex: 0 0 58.33333%;
        flex: 0 0 58.33333%;
        max-width: 58.33333%
    }
    .col-xl-8 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 66.66667%;
        -ms-flex: 0 0 66.66667%;
        flex: 0 0 66.66667%;
        max-width: 66.66667%
    }
    .col-xl-9 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 75%;
        -ms-flex: 0 0 75%;
        flex: 0 0 75%;
        max-width: 75%
    }
    .col-xl-10 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 83.33333%;
        -ms-flex: 0 0 83.33333%;
        flex: 0 0 83.33333%;
        max-width: 83.33333%
    }
    .col-xl-11 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 91.66667%;
        -ms-flex: 0 0 91.66667%;
        flex: 0 0 91.66667%;
        max-width: 91.66667%
    }
    .col-xl-12 {
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 100%;
        -ms-flex: 0 0 100%;
        flex: 0 0 100%;
        max-width: 100%
    }
    .order-xl-first {
        -webkit-box-ordinal-group: 0;
        -webkit-order: -1;
        -ms-flex-order: -1;
        order: -1
    }
    .order-xl-last {
        -webkit-box-ordinal-group: 14;
        -webkit-order: 13;
        -ms-flex-order: 13;
        order: 13
    }
    .order-xl-0 {
        -webkit-box-ordinal-group: 1;
        -webkit-order: 0;
        -ms-flex-order: 0;
        order: 0
    }
    .order-xl-1 {
        -webkit-box-ordinal-group: 2;
        -webkit-order: 1;
        -ms-flex-order: 1;
        order: 1
    }
    .order-xl-2 {
        -webkit-box-ordinal-group: 3;
        -webkit-order: 2;
        -ms-flex-order: 2;
        order: 2
    }
    .order-xl-3 {
        -webkit-box-ordinal-group: 4;
        -webkit-order: 3;
        -ms-flex-order: 3;
        order: 3
    }
    .order-xl-4 {
        -webkit-box-ordinal-group: 5;
        -webkit-order: 4;
        -ms-flex-order: 4;
        order: 4
    }
    .order-xl-5 {
        -webkit-box-ordinal-group: 6;
        -webkit-order: 5;
        -ms-flex-order: 5;
        order: 5
    }
    .order-xl-6 {
        -webkit-box-ordinal-group: 7;
        -webkit-order: 6;
        -ms-flex-order: 6;
        order: 6
    }
    .order-xl-7 {
        -webkit-box-ordinal-group: 8;
        -webkit-order: 7;
        -ms-flex-order: 7;
        order: 7
    }
    .order-xl-8 {
        -webkit-box-ordinal-group: 9;
        -webkit-order: 8;
        -ms-flex-order: 8;
        order: 8
    }
    .order-xl-9 {
        -webkit-box-ordinal-group: 10;
        -webkit-order: 9;
        -ms-flex-order: 9;
        order: 9
    }
    .order-xl-10 {
        -webkit-box-ordinal-group: 11;
        -webkit-order: 10;
        -ms-flex-order: 10;
        order: 10
    }
    .order-xl-11 {
        -webkit-box-ordinal-group: 12;
        -webkit-order: 11;
        -ms-flex-order: 11;
        order: 11
    }
    .order-xl-12 {
        -webkit-box-ordinal-group: 13;
        -webkit-order: 12;
        -ms-flex-order: 12;
        order: 12
    }
    .offset-xl-0 {
        margin-left: 0
    }
    .offset-xl-1 {
        margin-left: 8.33333%
    }
    .offset-xl-2 {
        margin-left: 16.66667%
    }
    .offset-xl-3 {
        margin-left: 25%
    }
    .offset-xl-4 {
        margin-left: 33.33333%
    }
    .offset-xl-5 {
        margin-left: 41.66667%
    }
    .offset-xl-6 {
        margin-left: 50%
    }
    .offset-xl-7 {
        margin-left: 58.33333%
    }
    .offset-xl-8 {
        margin-left: 66.66667%
    }
    .offset-xl-9 {
        margin-left: 75%
    }
    .offset-xl-10 {
        margin-left: 83.33333%
    }
    .offset-xl-11 {
        margin-left: 91.66667%
    }
}

.table {
    width: 100%;
    margin-bottom: 1rem;
    color: #e4e2ff
}

.table td,
.table th {
    padding: .75rem;
    vertical-align: top;
    border-top: 1px solid #28293e
}

.table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #28293e
}

.table tbody+tbody {
    border-top: 2px solid #28293e
}

.table-sm td,
.table-sm th {
    padding: .3rem
}

.table-bordered {
    border: 1px solid #28293e
}

.table-bordered td,
.table-bordered th {
    border: 1px solid #28293e
}

.table-bordered thead td,
.table-bordered thead th {
    border-bottom-width: 2px
}

.table-borderless tbody+tbody,
.table-borderless td,
.table-borderless th,
.table-borderless thead th {
    border: 0
}

.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(0, 0, 0, .05)
}

.table-hover tbody tr:hover {
    color: #e4e2ff;
    background-color: rgba(0, 0, 0, .075)
}

.table-primary,
.table-primary>td,
.table-primary>th {
    background-color: #d7cdf6
}

.table-primary tbody+tbody,
.table-primary td,
.table-primary th,
.table-primary thead th {
    border-color: #b5a2ee
}

.table-hover .table-primary:hover {
    background-color: #c6b7f2
}

.table-hover .table-primary:hover>td,
.table-hover .table-primary:hover>th {
    background-color: #c6b7f2
}

.table-secondary,
.table-secondary>td,
.table-secondary>th {
    background-color: #bee6f6
}

.table-secondary tbody+tbody,
.table-secondary td,
.table-secondary th,
.table-secondary thead th {
    border-color: #86d0ee
}

.table-hover .table-secondary:hover {
    background-color: #a8ddf3
}

.table-hover .table-secondary:hover>td,
.table-hover .table-secondary:hover>th {
    background-color: #a8ddf3
}

.table-success,
.table-success>td,
.table-success>th {
    background-color: #bee9d6
}

.table-success tbody+tbody,
.table-success td,
.table-success th,
.table-success thead th {
    border-color: #86d6b2
}

.table-hover .table-success:hover {
    background-color: #abe3ca
}

.table-hover .table-success:hover>td,
.table-hover .table-success:hover>th {
    background-color: #abe3ca
}

.table-info,
.table-info>td,
.table-info>th {
    background-color: #c3dcff
}

.table-info tbody+tbody,
.table-info td,
.table-info th,
.table-info thead th {
    border-color: #90bffe
}

.table-hover .table-info:hover {
    background-color: #aacdff
}

.table-hover .table-info:hover>td,
.table-hover .table-info:hover>th {
    background-color: #aacdff
}

.table-warning,
.table-warning>td,
.table-warning>th {
    background-color: #fdd8bd
}

.table-warning tbody+tbody,
.table-warning td,
.table-warning th,
.table-warning thead th {
    border-color: #fcb785
}

.table-hover .table-warning:hover {
    background-color: #fcc9a4
}

.table-hover .table-warning:hover>td,
.table-hover .table-warning:hover>th {
    background-color: #fcc9a4
}

.table-danger,
.table-danger>td,
.table-danger>th {
    background-color: #ffc8d1
}

.table-danger tbody+tbody,
.table-danger td,
.table-danger th,
.table-danger thead th {
    border-color: #ff9aaa
}

.table-hover .table-danger:hover {
    background-color: #ffafbc
}

.table-hover .table-danger:hover>td,
.table-hover .table-danger:hover>th {
    background-color: #ffafbc
}

.table-light,
.table-light>td,
.table-light>th {
    background-color: #f5f9fe
}

.table-light tbody+tbody,
.table-light td,
.table-light th,
.table-light thead th {
    border-color: #ecf5fd
}

.table-hover .table-light:hover {
    background-color: #deebfc
}

.table-hover .table-light:hover>td,
.table-hover .table-light:hover>th {
    background-color: #deebfc
}

.table-dark,
.table-dark>td,
.table-dark>th {
    background-color: #c6c6cc
}

.table-dark tbody+tbody,
.table-dark td,
.table-dark th,
.table-dark thead th {
    border-color: #9495a1
}

.table-hover .table-dark:hover {
    background-color: #b9b9c0
}

.table-hover .table-dark:hover>td,
.table-hover .table-dark:hover>th {
    background-color: #b9b9c0
}

.table-active,
.table-active>td,
.table-active>th {
    background-color: rgba(0, 0, 0, .075)
}

.table-hover .table-active:hover {
    background-color: rgba(0, 0, 0, .075)
}

.table-hover .table-active:hover>td,
.table-hover .table-active:hover>th {
    background-color: rgba(0, 0, 0, .075)
}

.table .thead-dark th {
    color: #e4e2ff;
    background-color: #11111d;
    border-color: #1f1f35
}

.table .thead-light th {
    color: #151623;
    background-color: #282a38;
    border-color: #28293e
}

.table-dark {
    color: #e4e2ff;
    background-color: #11111d
}

.table-dark td,
.table-dark th,
.table-dark thead th {
    border-color: #1f1f35
}

.table-dark.table-bordered {
    border: 0
}

.table-dark.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(50, 51, 74, .05)
}

.table-dark.table-hover tbody tr:hover {
    color: #e4e2ff;
    background-color: rgba(50, 51, 74, .075)
}

@media (max-width:575.98px) {
    .table-responsive-sm {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch
    }
    .table-responsive-sm>.table-bordered {
        border: 0
    }
}

@media (max-width:767.98px) {
    .table-responsive-md {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch
    }
    .table-responsive-md>.table-bordered {
        border: 0
    }
}

@media (max-width:991.98px) {
    .table-responsive-lg {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch
    }
    .table-responsive-lg>.table-bordered {
        border: 0
    }
}

@media (max-width:1199.98px) {
    .table-responsive-xl {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch
    }
    .table-responsive-xl>.table-bordered {
        border: 0
    }
}

.table-responsive {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch
}

.table-responsive>.table-bordered {
    border: 0
}

.form-control {
    display: block;
    width: 100%;
    height: calc(1.5em + .75rem + 2px);
    padding: .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #adabc6;
    background-color: #28293e;
    background-clip: padding-box;
    border: 1px solid #11111d;
    border-radius: 6px;
    -webkit-transition: border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .form-control {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.form-control::-ms-expand {
    background-color: transparent;
    border: 0
}

.form-control:focus {
    color: #adabc6;
    background-color: #28293e;
    border-color: #c7b8f2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.form-control::-webkit-input-placeholder {
    color: #a19fb9;
    opacity: 1
}

.form-control::-moz-placeholder {
    color: #a19fb9;
    opacity: 1
}

.form-control:-ms-input-placeholder {
    color: #a19fb9;
    opacity: 1
}

.form-control::-ms-input-placeholder {
    color: #a19fb9;
    opacity: 1
}

.form-control::placeholder {
    color: #a19fb9;
    opacity: 1
}

.form-control:disabled,
.form-control[readonly] {
    background-color: #282a38;
    opacity: 1
}

select.form-control:focus::-ms-value {
    color: #adabc6;
    background-color: #28293e
}

.form-control-file,
.form-control-range {
    display: block;
    width: 100%
}

.col-form-label {
    padding-top: calc(.375rem + 1px);
    padding-bottom: calc(.375rem + 1px);
    margin-bottom: 0;
    font-size: inherit;
    line-height: 1.5
}

.col-form-label-lg {
    padding-top: calc(.5rem + 1px);
    padding-bottom: calc(.5rem + 1px);
    font-size: 1.25rem;
    line-height: 1.5
}

.col-form-label-sm {
    padding-top: calc(.25rem + 1px);
    padding-bottom: calc(.25rem + 1px);
    font-size: .875rem;
    line-height: 1.5
}

.form-control-plaintext {
    display: block;
    width: 100%;
    padding-top: .375rem;
    padding-bottom: .375rem;
    margin-bottom: 0;
    line-height: 1.5;
    color: #e4e2ff;
    background-color: transparent;
    border: solid transparent;
    border-width: 1px 0
}

.form-control-plaintext.form-control-lg,
.form-control-plaintext.form-control-sm {
    padding-right: 0;
    padding-left: 0
}

.form-control-sm {
    height: calc(1.5em + .5rem + 2px);
    padding: .25rem .5rem;
    font-size: .875rem;
    line-height: 1.5;
    border-radius: .2rem
}

.form-control-lg {
    height: calc(1.5em + 1rem + 2px);
    padding: .5rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 6px
}

select.form-control[multiple],
select.form-control[size] {
    height: auto
}

textarea.form-control {
    height: auto
}

.form-group {
    margin-bottom: 1rem
}

.form-text {
    display: block;
    margin-top: .25rem
}

.form-row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    margin-right: -5px;
    margin-left: -5px
}

.form-row>.col,
.form-row>[class*=col-] {
    padding-right: 5px;
    padding-left: 5px
}

.form-check {
    position: relative;
    display: block;
    padding-left: 1.25rem
}

.form-check-input {
    position: absolute;
    margin-top: .3rem;
    margin-left: -1.25rem
}

.form-check-input:disabled~.form-check-label {
    color: #81839a
}

.form-check-label {
    margin-bottom: 0
}

.form-check-inline {
    display: -webkit-inline-box;
    display: -webkit-inline-flex;
    display: -ms-inline-flexbox;
    display: inline-flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    padding-left: 0;
    margin-right: .75rem
}

.form-check-inline .form-check-input {
    position: static;
    margin-top: 0;
    margin-right: .3125rem;
    margin-left: 0
}

.valid-feedback {
    display: none;
    width: 100%;
    margin-top: .25rem;
    font-size: 80%;
    color: #17b06b
}

.valid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: .25rem .5rem;
    margin-top: .1rem;
    font-size: .875rem;
    line-height: 1.5;
    color: #fff;
    background-color: rgba(23, 176, 107, .9);
    border-radius: 6px
}

.form-control.is-valid,
.was-validated .form-control:valid {
    border-color: #17b06b;
    padding-right: calc(1.5em + .75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2317b06b' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: center right calc(.375em + .1875rem);
    -webkit-background-size: calc(.75em + .375rem) calc(.75em + .375rem);
    background-size: calc(.75em + .375rem) calc(.75em + .375rem)
}

.form-control.is-valid:focus,
.was-validated .form-control:valid:focus {
    border-color: #17b06b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25)
}

.form-control.is-valid~.valid-feedback,
.form-control.is-valid~.valid-tooltip,
.was-validated .form-control:valid~.valid-feedback,
.was-validated .form-control:valid~.valid-tooltip {
    display: block
}

.was-validated textarea.form-control:valid,
textarea.form-control.is-valid {
    padding-right: calc(1.5em + .75rem);
    background-position: top calc(.375em + .1875rem) right calc(.375em + .1875rem)
}

.custom-select.is-valid,
.was-validated .custom-select:valid {
    border-color: #17b06b;
    padding-right: calc((1em + .75rem) * 3 / 4 + 1.75rem);
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right .75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2317b06b' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e") #32334a no-repeat center right 1.75rem/calc(.75em + .375rem) calc(.75em + .375rem)
}

.custom-select.is-valid:focus,
.was-validated .custom-select:valid:focus {
    border-color: #17b06b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25)
}

.custom-select.is-valid~.valid-feedback,
.custom-select.is-valid~.valid-tooltip,
.was-validated .custom-select:valid~.valid-feedback,
.was-validated .custom-select:valid~.valid-tooltip {
    display: block
}

.form-control-file.is-valid~.valid-feedback,
.form-control-file.is-valid~.valid-tooltip,
.was-validated .form-control-file:valid~.valid-feedback,
.was-validated .form-control-file:valid~.valid-tooltip {
    display: block
}

.form-check-input.is-valid~.form-check-label,
.was-validated .form-check-input:valid~.form-check-label {
    color: #17b06b
}

.form-check-input.is-valid~.valid-feedback,
.form-check-input.is-valid~.valid-tooltip,
.was-validated .form-check-input:valid~.valid-feedback,
.was-validated .form-check-input:valid~.valid-tooltip {
    display: block
}

.custom-control-input.is-valid~.custom-control-label,
.was-validated .custom-control-input:valid~.custom-control-label {
    color: #17b06b
}

.custom-control-input.is-valid~.custom-control-label::before,
.was-validated .custom-control-input:valid~.custom-control-label::before {
    border-color: #17b06b
}

.custom-control-input.is-valid~.valid-feedback,
.custom-control-input.is-valid~.valid-tooltip,
.was-validated .custom-control-input:valid~.valid-feedback,
.was-validated .custom-control-input:valid~.valid-tooltip {
    display: block
}

.custom-control-input.is-valid:checked~.custom-control-label::before,
.was-validated .custom-control-input:valid:checked~.custom-control-label::before {
    border-color: #1ddd86;
    background-color: #1ddd86
}

.custom-control-input.is-valid:focus~.custom-control-label::before,
.was-validated .custom-control-input:valid:focus~.custom-control-label::before {
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25)
}

.custom-control-input.is-valid:focus:not(:checked)~.custom-control-label::before,
.was-validated .custom-control-input:valid:focus:not(:checked)~.custom-control-label::before {
    border-color: #17b06b
}

.custom-file-input.is-valid~.custom-file-label,
.was-validated .custom-file-input:valid~.custom-file-label {
    border-color: #17b06b
}

.custom-file-input.is-valid~.valid-feedback,
.custom-file-input.is-valid~.valid-tooltip,
.was-validated .custom-file-input:valid~.valid-feedback,
.was-validated .custom-file-input:valid~.valid-tooltip {
    display: block
}

.custom-file-input.is-valid:focus~.custom-file-label,
.was-validated .custom-file-input:valid:focus~.custom-file-label {
    border-color: #17b06b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .25)
}

.invalid-feedback {
    display: none;
    width: 100%;
    margin-top: .25rem;
    font-size: 80%;
    color: #ef121b
}

.invalid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: .25rem .5rem;
    margin-top: .1rem;
    font-size: .875rem;
    line-height: 1.5;
    color: #fff;
    background-color: rgba(255, 60, 92, .9);
    border-radius: 6px
}

.form-control.is-invalid,
.was-validated .form-control:invalid {
    border-color: #ef121b;
    padding-right: calc(1.5em + .75rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ef121b' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23ef121b' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E");
    background-repeat: no-repeat;
    background-position: center right calc(.375em + .1875rem);
    -webkit-background-size: calc(.75em + .375rem) calc(.75em + .375rem);
    background-size: calc(.75em + .375rem) calc(.75em + .375rem)
}

.form-control.is-invalid:focus,
.was-validated .form-control:invalid:focus {
    border-color: #ef121b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25)
}

.form-control.is-invalid~.invalid-feedback,
.form-control.is-invalid~.invalid-tooltip,
.was-validated .form-control:invalid~.invalid-feedback,
.was-validated .form-control:invalid~.invalid-tooltip {
    display: block
}

.was-validated textarea.form-control:invalid,
textarea.form-control.is-invalid {
    padding-right: calc(1.5em + .75rem);
    background-position: top calc(.375em + .1875rem) right calc(.375em + .1875rem)
}

.custom-select.is-invalid,
.was-validated .custom-select:invalid {
    border-color: #ef121b;
    padding-right: calc((1em + .75rem) * 3 / 4 + 1.75rem);
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right .75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ef121b' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23ef121b' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E") #32334a no-repeat center right 1.75rem/calc(.75em + .375rem) calc(.75em + .375rem)
}

.custom-select.is-invalid:focus,
.was-validated .custom-select:invalid:focus {
    border-color: #ef121b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25)
}

.custom-select.is-invalid~.invalid-feedback,
.custom-select.is-invalid~.invalid-tooltip,
.was-validated .custom-select:invalid~.invalid-feedback,
.was-validated .custom-select:invalid~.invalid-tooltip {
    display: block
}

.form-control-file.is-invalid~.invalid-feedback,
.form-control-file.is-invalid~.invalid-tooltip,
.was-validated .form-control-file:invalid~.invalid-feedback,
.was-validated .form-control-file:invalid~.invalid-tooltip {
    display: block
}

.form-check-input.is-invalid~.form-check-label,
.was-validated .form-check-input:invalid~.form-check-label {
    color: #ef121b
}

.form-check-input.is-invalid~.invalid-feedback,
.form-check-input.is-invalid~.invalid-tooltip,
.was-validated .form-check-input:invalid~.invalid-feedback,
.was-validated .form-check-input:invalid~.invalid-tooltip {
    display: block
}

.custom-control-input.is-invalid~.custom-control-label,
.was-validated .custom-control-input:invalid~.custom-control-label {
    color: #ef121b
}

.custom-control-input.is-invalid~.custom-control-label::before,
.was-validated .custom-control-input:invalid~.custom-control-label::before {
    border-color: #ef121b
}

.custom-control-input.is-invalid~.invalid-feedback,
.custom-control-input.is-invalid~.invalid-tooltip,
.was-validated .custom-control-input:invalid~.invalid-feedback,
.was-validated .custom-control-input:invalid~.invalid-tooltip {
    display: block
}

.custom-control-input.is-invalid:checked~.custom-control-label::before,
.was-validated .custom-control-input:invalid:checked~.custom-control-label::before {
    border-color: #ff6f87;
    background-color: #ff6f87
}

.custom-control-input.is-invalid:focus~.custom-control-label::before,
.was-validated .custom-control-input:invalid:focus~.custom-control-label::before {
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25)
}

.custom-control-input.is-invalid:focus:not(:checked)~.custom-control-label::before,
.was-validated .custom-control-input:invalid:focus:not(:checked)~.custom-control-label::before {
    border-color: #ef121b
}

.custom-file-input.is-invalid~.custom-file-label,
.was-validated .custom-file-input:invalid~.custom-file-label {
    border-color: #ef121b
}

.custom-file-input.is-invalid~.invalid-feedback,
.custom-file-input.is-invalid~.invalid-tooltip,
.was-validated .custom-file-input:invalid~.invalid-feedback,
.was-validated .custom-file-input:invalid~.invalid-tooltip {
    display: block
}

.custom-file-input.is-invalid:focus~.custom-file-label,
.was-validated .custom-file-input:invalid:focus~.custom-file-label {
    border-color: #ef121b;
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .25)
}

.form-inline {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row wrap;
    -ms-flex-flow: row wrap;
    flex-flow: row wrap;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center
}

.form-inline .form-check {
    width: 100%
}

@media (min-width:576px) {
    .form-inline label {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -webkit-justify-content: center;
        -ms-flex-pack: center;
        justify-content: center;
        margin-bottom: 0
    }
    .form-inline .form-group {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-flex: 0;
        -webkit-flex: 0 0 auto;
        -ms-flex: 0 0 auto;
        flex: 0 0 auto;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row wrap;
        -ms-flex-flow: row wrap;
        flex-flow: row wrap;
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        margin-bottom: 0
    }
    .form-inline .form-control {
        display: inline-block;
        width: auto;
        vertical-align: middle
    }
    .form-inline .form-control-plaintext {
        display: inline-block
    }
    .form-inline .custom-select,
    .form-inline .input-group {
        width: auto
    }
    .form-inline .form-check {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -webkit-justify-content: center;
        -ms-flex-pack: center;
        justify-content: center;
        width: auto;
        padding-left: 0
    }
    .form-inline .form-check-input {
        position: relative;
        -webkit-flex-shrink: 0;
        -ms-flex-negative: 0;
        flex-shrink: 0;
        margin-top: 0;
        margin-right: .25rem;
        margin-left: 0
    }
    .form-inline .custom-control {
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -webkit-justify-content: center;
        -ms-flex-pack: center;
        justify-content: center
    }
    .form-inline .custom-control-label {
        margin-bottom: 0
    }
}

.btn {
    display: inline-block;
    font-weight: 400;
    color: #e4e2ff;
    text-align: center;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: transparent;
    border: 1px solid transparent;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 6px;
    -webkit-transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .btn {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.btn:hover {
    color: #e4e2ff;
    text-decoration: none
}

.btn.focus,
.btn:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.btn.disabled,
.btn:disabled {
    opacity: .65
}

a.btn.disabled,
fieldset:disabled a.btn {
    pointer-events: none
}

.btn-primary {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf
}

.btn-primary:hover {
    color: #fff;
    background-color: #572cd9;
    border-color: #5126d2
}

.btn-primary.focus,
.btn-primary:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(134, 103, 228, .5);
    box-shadow: 0 0 0 .2rem rgba(134, 103, 228, .5)
}

.btn-primary.disabled,
.btn-primary:disabled {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf
}

.btn-primary:not(:disabled):not(.disabled).active,
.btn-primary:not(:disabled):not(.disabled):active,
.show>.btn-primary.dropdown-toggle {
    color: #fff;
    background-color: #5126d2;
    border-color: #4d24c8
}

.btn-primary:not(:disabled):not(.disabled).active:focus,
.btn-primary:not(:disabled):not(.disabled):active:focus,
.show>.btn-primary.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(134, 103, 228, .5);
    box-shadow: 0 0 0 .2rem rgba(134, 103, 228, .5)
}

.btn-secondary {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de
}

.btn-secondary:hover {
    color: #fff;
    background-color: #138abb;
    border-color: #1182b0
}

.btn-secondary.focus,
.btn-secondary:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(57, 178, 227, .5);
    box-shadow: 0 0 0 .2rem rgba(57, 178, 227, .5)
}

.btn-secondary.disabled,
.btn-secondary:disabled {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de
}

.btn-secondary:not(:disabled):not(.disabled).active,
.btn-secondary:not(:disabled):not(.disabled):active,
.show>.btn-secondary.dropdown-toggle {
    color: #fff;
    background-color: #1182b0;
    border-color: #1079a4
}

.btn-secondary:not(:disabled):not(.disabled).active:focus,
.btn-secondary:not(:disabled):not(.disabled):active:focus,
.show>.btn-secondary.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(57, 178, 227, .5);
    box-shadow: 0 0 0 .2rem rgba(57, 178, 227, .5)
}

.btn-success {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b
}

.btn-success:hover {
    color: #fff;
    background-color: #138e56;
    border-color: #118350
}

.btn-success.focus,
.btn-success:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(58, 188, 129, .5);
    box-shadow: 0 0 0 .2rem rgba(58, 188, 129, .5)
}

.btn-success.disabled,
.btn-success:disabled {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b
}

.btn-success:not(:disabled):not(.disabled).active,
.btn-success:not(:disabled):not(.disabled):active,
.show>.btn-success.dropdown-toggle {
    color: #fff;
    background-color: #118350;
    border-color: #107849
}

.btn-success:not(:disabled):not(.disabled).active:focus,
.btn-success:not(:disabled):not(.disabled):active:focus,
.show>.btn-success.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(58, 188, 129, .5);
    box-shadow: 0 0 0 .2rem rgba(58, 188, 129, .5)
}

.btn-info {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe
}

.btn-info:hover {
    color: #fff;
    background-color: #036dfe;
    border-color: #0167f3
}

.btn-info.focus,
.btn-info:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(73, 150, 254, .5);
    box-shadow: 0 0 0 .2rem rgba(73, 150, 254, .5)
}

.btn-info.disabled,
.btn-info:disabled {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe
}

.btn-info:not(:disabled):not(.disabled).active,
.btn-info:not(:disabled):not(.disabled):active,
.show>.btn-info.dropdown-toggle {
    color: #fff;
    background-color: #0167f3;
    border-color: #0162e6
}

.btn-info:not(:disabled):not(.disabled).active:focus,
.btn-info:not(:disabled):not(.disabled):active:focus,
.show>.btn-info.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(73, 150, 254, .5);
    box-shadow: 0 0 0 .2rem rgba(73, 150, 254, .5)
}

.btn-warning {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515
}

.btn-warning:hover {
    color: #fff;
    background-color: #e26206;
    border-color: #d65d05
}

.btn-warning.focus,
.btn-warning:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(250, 138, 56, .5);
    box-shadow: 0 0 0 .2rem rgba(250, 138, 56, .5)
}

.btn-warning.disabled,
.btn-warning:disabled {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515
}

.btn-warning:not(:disabled):not(.disabled).active,
.btn-warning:not(:disabled):not(.disabled):active,
.show>.btn-warning.dropdown-toggle {
    color: #fff;
    background-color: #d65d05;
    border-color: #c95805
}

.btn-warning:not(:disabled):not(.disabled).active:focus,
.btn-warning:not(:disabled):not(.disabled):active:focus,
.show>.btn-warning.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(250, 138, 56, .5);
    box-shadow: 0 0 0 .2rem rgba(250, 138, 56, .5)
}

.btn-danger {
    color: #fff;
    background-color: #ef121b;
    border-color: #ef121b
}

.btn-danger:hover {
    color: #fff;
    background-color: #ff163c;
    border-color: #ff0931
}

.btn-danger.focus,
.btn-danger:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 89, 116, .5);
    box-shadow: 0 0 0 .2rem rgba(255, 89, 116, .5)
}

.btn-danger.disabled,
.btn-danger:disabled {
    color: #fff;
    background-color: #ef121b;
    border-color: #ef121b
}

.btn-danger:not(:disabled):not(.disabled).active,
.btn-danger:not(:disabled):not(.disabled):active,
.show>.btn-danger.dropdown-toggle {
    color: #fff;
    background-color: #ff0931;
    border-color: #fb0029
}

.btn-danger:not(:disabled):not(.disabled).active:focus,
.btn-danger:not(:disabled):not(.disabled):active:focus,
.show>.btn-danger.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 89, 116, .5);
    box-shadow: 0 0 0 .2rem rgba(255, 89, 116, .5)
}

.btn-light {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb
}

.btn-light:hover {
    color: #0a0b14;
    background-color: #b9d8f7;
    border-color: #add2f6
}

.btn-light.focus,
.btn-light:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(188, 201, 216, .5);
    box-shadow: 0 0 0 .2rem rgba(188, 201, 216, .5)
}

.btn-light.disabled,
.btn-light:disabled {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb
}

.btn-light:not(:disabled):not(.disabled).active,
.btn-light:not(:disabled):not(.disabled):active,
.show>.btn-light.dropdown-toggle {
    color: #0a0b14;
    background-color: #add2f6;
    border-color: #a2cbf5
}

.btn-light:not(:disabled):not(.disabled).active:focus,
.btn-light:not(:disabled):not(.disabled):active:focus,
.show>.btn-light.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(188, 201, 216, .5);
    box-shadow: 0 0 0 .2rem rgba(188, 201, 216, .5)
}

.btn-dark {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a
}

.btn-dark:hover {
    color: #fff;
    background-color: #232333;
    border-color: #1d1e2c
}

.btn-dark.focus,
.btn-dark:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(81, 82, 101, .5);
    box-shadow: 0 0 0 .2rem rgba(81, 82, 101, .5)
}

.btn-dark.disabled,
.btn-dark:disabled {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a
}

.btn-dark:not(:disabled):not(.disabled).active,
.btn-dark:not(:disabled):not(.disabled):active,
.show>.btn-dark.dropdown-toggle {
    color: #fff;
    background-color: #1d1e2c;
    border-color: #181924
}

.btn-dark:not(:disabled):not(.disabled).active:focus,
.btn-dark:not(:disabled):not(.disabled):active:focus,
.show>.btn-dark.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(81, 82, 101, .5);
    box-shadow: 0 0 0 .2rem rgba(81, 82, 101, .5)
}

.btn-outline-primary {
    color: #714cdf;
    border-color: #714cdf
}

.btn-outline-primary:hover {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf
}

.btn-outline-primary.focus,
.btn-outline-primary:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5)
}

.btn-outline-primary.disabled,
.btn-outline-primary:disabled {
    color: #714cdf;
    background-color: transparent
}

.btn-outline-primary:not(:disabled):not(.disabled).active,
.btn-outline-primary:not(:disabled):not(.disabled):active,
.show>.btn-outline-primary.dropdown-toggle {
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf
}

.btn-outline-primary:not(:disabled):not(.disabled).active:focus,
.btn-outline-primary:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-primary.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5)
}

.btn-outline-secondary {
    color: #16a4de;
    border-color: #16a4de
}

.btn-outline-secondary:hover {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de
}

.btn-outline-secondary.focus,
.btn-outline-secondary:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5);
    box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5)
}

.btn-outline-secondary.disabled,
.btn-outline-secondary:disabled {
    color: #16a4de;
    background-color: transparent
}

.btn-outline-secondary:not(:disabled):not(.disabled).active,
.btn-outline-secondary:not(:disabled):not(.disabled):active,
.show>.btn-outline-secondary.dropdown-toggle {
    color: #fff;
    background-color: #16a4de;
    border-color: #16a4de
}

.btn-outline-secondary:not(:disabled):not(.disabled).active:focus,
.btn-outline-secondary:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-secondary.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5);
    box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5)
}

.btn-outline-success {
    color: #17b06b;
    border-color: #17b06b
}

.btn-outline-success:hover {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b
}

.btn-outline-success.focus,
.btn-outline-success:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5)
}

.btn-outline-success.disabled,
.btn-outline-success:disabled {
    color: #17b06b;
    background-color: transparent
}

.btn-outline-success:not(:disabled):not(.disabled).active,
.btn-outline-success:not(:disabled):not(.disabled):active,
.show>.btn-outline-success.dropdown-toggle {
    color: #fff;
    background-color: #17b06b;
    border-color: #17b06b
}

.btn-outline-success:not(:disabled):not(.disabled).active:focus,
.btn-outline-success:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-success.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5)
}

.btn-outline-info {
    color: #2983fe;
    border-color: #2983fe
}

.btn-outline-info:hover {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe
}

.btn-outline-info.focus,
.btn-outline-info:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5);
    box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5)
}

.btn-outline-info.disabled,
.btn-outline-info:disabled {
    color: #2983fe;
    background-color: transparent
}

.btn-outline-info:not(:disabled):not(.disabled).active,
.btn-outline-info:not(:disabled):not(.disabled):active,
.show>.btn-outline-info.dropdown-toggle {
    color: #fff;
    background-color: #2983fe;
    border-color: #2983fe
}

.btn-outline-info:not(:disabled):not(.disabled).active:focus,
.btn-outline-info:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-info.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5);
    box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5)
}

.btn-outline-warning {
    color: #f97515;
    border-color: #f97515
}

.btn-outline-warning:hover {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515
}

.btn-outline-warning.focus,
.btn-outline-warning:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5);
    box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5)
}

.btn-outline-warning.disabled,
.btn-outline-warning:disabled {
    color: #f97515;
    background-color: transparent
}

.btn-outline-warning:not(:disabled):not(.disabled).active,
.btn-outline-warning:not(:disabled):not(.disabled):active,
.show>.btn-outline-warning.dropdown-toggle {
    color: #fff;
    background-color: #f97515;
    border-color: #f97515
}

.btn-outline-warning:not(:disabled):not(.disabled).active:focus,
.btn-outline-warning:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-warning.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5);
    box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5)
}

.btn-outline-danger {
    color: #ef121b;
    border-color: #ef121b
}

.btn-outline-danger:hover {
    color: #fff;
    background-color: #ef121b;
    border-color: #ef121b
}

.btn-outline-danger.focus,
.btn-outline-danger:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5)
}

.btn-outline-danger.disabled,
.btn-outline-danger:disabled {
    color: #ef121b;
    background-color: transparent
}

.btn-outline-danger:not(:disabled):not(.disabled).active,
.btn-outline-danger:not(:disabled):not(.disabled):active,
.show>.btn-outline-danger.dropdown-toggle {
    color: #fff;
    background-color: #ef121b;
    border-color: #ef121b
}

.btn-outline-danger:not(:disabled):not(.disabled).active:focus,
.btn-outline-danger:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-danger.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5)
}

.btn-outline-light {
    color: #dbebfb;
    border-color: #dbebfb
}

.btn-outline-light:hover {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb
}

.btn-outline-light.focus,
.btn-outline-light:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5);
    box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5)
}

.btn-outline-light.disabled,
.btn-outline-light:disabled {
    color: #dbebfb;
    background-color: transparent
}

.btn-outline-light:not(:disabled):not(.disabled).active,
.btn-outline-light:not(:disabled):not(.disabled):active,
.show>.btn-outline-light.dropdown-toggle {
    color: #0a0b14;
    background-color: #dbebfb;
    border-color: #dbebfb
}

.btn-outline-light:not(:disabled):not(.disabled).active:focus,
.btn-outline-light:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-light.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5);
    box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5)
}

.btn-outline-dark {
    color: #32334a;
    border-color: #32334a
}

.btn-outline-dark:hover {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a
}

.btn-outline-dark.focus,
.btn-outline-dark:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5);
    box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5)
}

.btn-outline-dark.disabled,
.btn-outline-dark:disabled {
    color: #32334a;
    background-color: transparent
}

.btn-outline-dark:not(:disabled):not(.disabled).active,
.btn-outline-dark:not(:disabled):not(.disabled):active,
.show>.btn-outline-dark.dropdown-toggle {
    color: #fff;
    background-color: #32334a;
    border-color: #32334a
}

.btn-outline-dark:not(:disabled):not(.disabled).active:focus,
.btn-outline-dark:not(:disabled):not(.disabled):active:focus,
.show>.btn-outline-dark.dropdown-toggle:focus {
    -webkit-box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5);
    box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5)
}

.btn-link {
    font-weight: 400;
    color: #714cdf;
    text-decoration: none
}

.btn-link:hover {
    color: #4922bd;
    text-decoration: underline
}

.btn-link.focus,
.btn-link:focus {
    text-decoration: underline;
    -webkit-box-shadow: none;
    box-shadow: none
}

.btn-link.disabled,
.btn-link:disabled {
    color: #1d1e2f;
    pointer-events: none
}

.btn-group-lg>.btn,
.btn-lg {
    padding: .5rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 6px
}

.btn-group-sm>.btn,
.btn-sm {
    padding: .25rem .5rem;
    font-size: .875rem;
    line-height: 1.5;
    border-radius: .2rem
}

.btn-block {
    display: block;
    width: 100%
}

.btn-block+.btn-block {
    margin-top: .5rem
}

input[type=button].btn-block,
input[type=reset].btn-block,
input[type=submit].btn-block {
    width: 100%
}

.fade {
    -webkit-transition: opacity .15s linear;
    -o-transition: opacity .15s linear;
    transition: opacity .15s linear
}

@media (prefers-reduced-motion:reduce) {
    .fade {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.fade:not(.show) {
    opacity: 0
}

.collapse:not(.show) {
    display: none
}

.collapsing {
    position: relative;
    height: 0;
    overflow: hidden;
    -webkit-transition: height .35s ease;
    -o-transition: height .35s ease;
    transition: height .35s ease
}

@media (prefers-reduced-motion:reduce) {
    .collapsing {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.dropdown,
.dropleft,
.dropright,
.dropup {
    position: relative
}

.dropdown-toggle {
    white-space: nowrap
}

.dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid;
    border-right: .3em solid transparent;
    border-bottom: 0;
    border-left: .3em solid transparent
}

.dropdown-toggle:empty::after {
    margin-left: 0
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    z-index: 1000;
    display: none;
    float: left;
    min-width: 10rem;
    padding: .5rem 0;
    margin: .125rem 0 0;
    font-size: 1rem;
    color: #e4e2ff;
    text-align: left;
    list-style: none;
    background-color: #32334a;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .15);
    border-radius: 6px
}

.dropdown-menu-left {
    right: auto;
    left: 0
}

.dropdown-menu-right {
    right: 0;
    left: auto
}

@media (min-width:576px) {
    .dropdown-menu-sm-left {
        right: auto;
        left: 0
    }
    .dropdown-menu-sm-right {
        right: 0;
        left: auto
    }
}

@media (min-width:768px) {
    .dropdown-menu-md-left {
        right: auto;
        left: 0
    }
    .dropdown-menu-md-right {
        right: 0;
        left: auto
    }
}

@media (min-width:992px) {
    .dropdown-menu-lg-left {
        right: auto;
        left: 0
    }
    .dropdown-menu-lg-right {
        right: 0;
        left: auto
    }
}

@media (min-width:1200px) {
    .dropdown-menu-xl-left {
        right: auto;
        left: 0
    }
    .dropdown-menu-xl-right {
        right: 0;
        left: auto
    }
}

.dropup .dropdown-menu {
    top: auto;
    bottom: 100%;
    margin-top: 0;
    margin-bottom: .125rem
}

.dropup .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: 0;
    border-right: .3em solid transparent;
    border-bottom: .3em solid;
    border-left: .3em solid transparent
}

.dropup .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropright .dropdown-menu {
    top: 0;
    right: auto;
    left: 100%;
    margin-top: 0;
    margin-left: .125rem
}

.dropright .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid transparent;
    border-right: 0;
    border-bottom: .3em solid transparent;
    border-left: .3em solid
}

.dropright .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropright .dropdown-toggle::after {
    vertical-align: 0
}

.dropleft .dropdown-menu {
    top: 0;
    right: 100%;
    left: auto;
    margin-top: 0;
    margin-right: .125rem
}

.dropleft .dropdown-toggle::after {
    display: inline-block;
    margin-left: .255em;
    vertical-align: .255em;
    content: ""
}

.dropleft .dropdown-toggle::after {
    display: none
}

.dropleft .dropdown-toggle::before {
    display: inline-block;
    margin-right: .255em;
    vertical-align: .255em;
    content: "";
    border-top: .3em solid transparent;
    border-right: .3em solid;
    border-bottom: .3em solid transparent
}

.dropleft .dropdown-toggle:empty::after {
    margin-left: 0
}

.dropleft .dropdown-toggle::before {
    vertical-align: 0
}

.dropdown-menu[x-placement^=bottom],
.dropdown-menu[x-placement^=left],
.dropdown-menu[x-placement^=right],
.dropdown-menu[x-placement^=top] {
    right: auto;
    bottom: auto
}

.dropdown-divider {
    height: 0;
    margin: .5rem 0;
    overflow: hidden;
    border-top: 1px solid #282a38
}

.dropdown-item {
    display: block;
    width: 100%;
    padding: .25rem 1.5rem;
    clear: both;
    font-weight: 400;
    color: #0a0b14;
    text-align: inherit;
    white-space: nowrap;
    background-color: transparent;
    border: 0
}

.dropdown-item:focus,
.dropdown-item:hover {
    color: #020203;
    text-decoration: none;
    background-color: #2d2e3f
}

.dropdown-item.active,
.dropdown-item:active {
    color: #32334a;
    text-decoration: none;
    background-color: #714cdf
}

.dropdown-item.disabled,
.dropdown-item:disabled {
    color: #1d1e2f;
    pointer-events: none;
    background-color: transparent
}

.dropdown-menu.show {
    display: block
}

.dropdown-header {
    display: block;
    padding: .5rem 1.5rem;
    margin-bottom: 0;
    font-size: .875rem;
    color: #1d1e2f;
    white-space: nowrap
}

.dropdown-item-text {
    display: block;
    padding: .25rem 1.5rem;
    color: #0a0b14
}

.btn-group,
.btn-group-vertical {
    position: relative;
    display: -webkit-inline-box;
    display: -webkit-inline-flex;
    display: -ms-inline-flexbox;
    display: inline-flex;
    vertical-align: middle
}

.btn-group-vertical>.btn,
.btn-group>.btn {
    position: relative;
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto
}

.btn-group-vertical>.btn:hover,
.btn-group>.btn:hover {
    z-index: 1
}

.btn-group-vertical>.btn.active,
.btn-group-vertical>.btn:active,
.btn-group-vertical>.btn:focus,
.btn-group>.btn.active,
.btn-group>.btn:active,
.btn-group>.btn:focus {
    z-index: 1
}

.btn-toolbar {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
    -ms-flex-pack: start;
    justify-content: flex-start
}

.btn-toolbar .input-group {
    width: auto
}

.btn-group>.btn-group:not(:first-child),
.btn-group>.btn:not(:first-child) {
    margin-left: -1px
}

.btn-group>.btn-group:not(:last-child)>.btn,
.btn-group>.btn:not(:last-child):not(.dropdown-toggle) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.btn-group>.btn-group:not(:first-child)>.btn,
.btn-group>.btn:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.dropdown-toggle-split {
    padding-right: .5625rem;
    padding-left: .5625rem
}

.dropdown-toggle-split::after,
.dropright .dropdown-toggle-split::after,
.dropup .dropdown-toggle-split::after {
    margin-left: 0
}

.dropleft .dropdown-toggle-split::before {
    margin-right: 0
}

.btn-group-sm>.btn+.dropdown-toggle-split,
.btn-sm+.dropdown-toggle-split {
    padding-right: .375rem;
    padding-left: .375rem
}

.btn-group-lg>.btn+.dropdown-toggle-split,
.btn-lg+.dropdown-toggle-split {
    padding-right: .75rem;
    padding-left: .75rem
}

.btn-group-vertical {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: start;
    -webkit-align-items: flex-start;
    -ms-flex-align: start;
    align-items: flex-start;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center
}

.btn-group-vertical>.btn,
.btn-group-vertical>.btn-group {
    width: 100%
}

.btn-group-vertical>.btn-group:not(:first-child),
.btn-group-vertical>.btn:not(:first-child) {
    margin-top: -1px
}

.btn-group-vertical>.btn-group:not(:last-child)>.btn,
.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle) {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0
}

.btn-group-vertical>.btn-group:not(:first-child)>.btn,
.btn-group-vertical>.btn:not(:first-child) {
    border-top-left-radius: 0;
    border-top-right-radius: 0
}

.btn-group-toggle>.btn,
.btn-group-toggle>.btn-group>.btn {
    margin-bottom: 0
}

.btn-group-toggle>.btn input[type=checkbox],
.btn-group-toggle>.btn input[type=radio],
.btn-group-toggle>.btn-group>.btn input[type=checkbox],
.btn-group-toggle>.btn-group>.btn input[type=radio] {
    position: absolute;
    clip: rect(0, 0, 0, 0);
    pointer-events: none
}

.input-group {
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-align: stretch;
    -webkit-align-items: stretch;
    -ms-flex-align: stretch;
    align-items: stretch;
    width: 100%
}

.input-group>.custom-file,
.input-group>.custom-select,
.input-group>.form-control,
.input-group>.form-control-plaintext {
    position: relative;
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    width: 1%;
    margin-bottom: 0
}

.input-group>.custom-file+.custom-file,
.input-group>.custom-file+.custom-select,
.input-group>.custom-file+.form-control,
.input-group>.custom-select+.custom-file,
.input-group>.custom-select+.custom-select,
.input-group>.custom-select+.form-control,
.input-group>.form-control+.custom-file,
.input-group>.form-control+.custom-select,
.input-group>.form-control+.form-control,
.input-group>.form-control-plaintext+.custom-file,
.input-group>.form-control-plaintext+.custom-select,
.input-group>.form-control-plaintext+.form-control {
    margin-left: -1px
}

.input-group>.custom-file .custom-file-input:focus~.custom-file-label,
.input-group>.custom-select:focus,
.input-group>.form-control:focus {
    z-index: 3
}

.input-group>.custom-file .custom-file-input:focus {
    z-index: 4
}

.input-group>.custom-select:not(:last-child),
.input-group>.form-control:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.input-group>.custom-select:not(:first-child),
.input-group>.form-control:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.input-group>.custom-file {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center
}

.input-group>.custom-file:not(:last-child) .custom-file-label,
.input-group>.custom-file:not(:last-child) .custom-file-label::after {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.input-group>.custom-file:not(:first-child) .custom-file-label {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.input-group-append,
.input-group-prepend {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex
}

.input-group-append .btn,
.input-group-prepend .btn {
    position: relative;
    z-index: 2
}

.input-group-append .btn:focus,
.input-group-prepend .btn:focus {
    z-index: 3
}

.input-group-append .btn+.btn,
.input-group-append .btn+.input-group-text,
.input-group-append .input-group-text+.btn,
.input-group-append .input-group-text+.input-group-text,
.input-group-prepend .btn+.btn,
.input-group-prepend .btn+.input-group-text,
.input-group-prepend .input-group-text+.btn,
.input-group-prepend .input-group-text+.input-group-text {
    margin-left: -1px
}

.input-group-prepend {
    margin-right: -1px
}

.input-group-append {
    margin-left: -1px
}

.input-group-text {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    padding: .375rem .75rem;
    margin-bottom: 0;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #adabc6;
    text-align: center;
    white-space: nowrap;
    background-color: #282a38;
    border: 1px solid #11111d;
    border-radius: 6px
}

.input-group-text input[type=checkbox],
.input-group-text input[type=radio] {
    margin-top: 0
}

.input-group-lg>.custom-select,
.input-group-lg>.form-control:not(textarea) {
    height: calc(1.5em + 1rem + 2px)
}

.input-group-lg>.custom-select,
.input-group-lg>.form-control,
.input-group-lg>.input-group-append>.btn,
.input-group-lg>.input-group-append>.input-group-text,
.input-group-lg>.input-group-prepend>.btn,
.input-group-lg>.input-group-prepend>.input-group-text {
    padding: .5rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 6px
}

.input-group-sm>.custom-select,
.input-group-sm>.form-control:not(textarea) {
    height: calc(1.5em + .5rem + 2px)
}

.input-group-sm>.custom-select,
.input-group-sm>.form-control,
.input-group-sm>.input-group-append>.btn,
.input-group-sm>.input-group-append>.input-group-text,
.input-group-sm>.input-group-prepend>.btn,
.input-group-sm>.input-group-prepend>.input-group-text {
    padding: .25rem .5rem;
    font-size: .875rem;
    line-height: 1.5;
    border-radius: .2rem
}

.input-group-lg>.custom-select,
.input-group-sm>.custom-select {
    padding-right: 1.75rem
}

.input-group>.input-group-append:last-child>.btn:not(:last-child):not(.dropdown-toggle),
.input-group>.input-group-append:last-child>.input-group-text:not(:last-child),
.input-group>.input-group-append:not(:last-child)>.btn,
.input-group>.input-group-append:not(:last-child)>.input-group-text,
.input-group>.input-group-prepend>.btn,
.input-group>.input-group-prepend>.input-group-text {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.input-group>.input-group-append>.btn,
.input-group>.input-group-append>.input-group-text,
.input-group>.input-group-prepend:first-child>.btn:not(:first-child),
.input-group>.input-group-prepend:first-child>.input-group-text:not(:first-child),
.input-group>.input-group-prepend:not(:first-child)>.btn,
.input-group>.input-group-prepend:not(:first-child)>.input-group-text {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.custom-control {
    position: relative;
    display: block;
    min-height: 1.5rem;
    padding-left: 2rem
}

.custom-control-inline {
    display: -webkit-inline-box;
    display: -webkit-inline-flex;
    display: -ms-inline-flexbox;
    display: inline-flex;
    margin-right: 1rem
}

.custom-control-input {
    position: absolute;
    z-index: -1;
    opacity: 0
}

.custom-control-input:checked~.custom-control-label::before {
    color: #32334a;
    border-color: #714cdf;
    background-color: #714cdf
}

.custom-control-input:focus~.custom-control-label::before {
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.custom-control-input:focus:not(:checked)~.custom-control-label::before {
    border-color: #c7b8f2
}

.custom-control-input:not(:disabled):active~.custom-control-label::before {
    color: #32334a;
    background-color: #e9e3fa;
    border-color: #e9e3fa
}

.custom-control-input:disabled~.custom-control-label {
    color: #1d1e2f
}

.custom-control-input:disabled~.custom-control-label::before {
    background-color: #282a38
}

.custom-control-label {
    position: relative;
    margin-bottom: 0;
    vertical-align: top
}

.custom-control-label::before {
    position: absolute;
    top: .25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    pointer-events: none;
    content: "";
    background-color: #151623;
    border: #1c1d2c solid 1px
}

.custom-control-label::after {
    position: absolute;
    top: .25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    content: "";
    background: no-repeat 50%/50% 50%
}

.custom-checkbox .custom-control-label::before {
    border-radius: 6px
}

.custom-checkbox .custom-control-input:checked~.custom-control-label::after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2332334a' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e")
}

.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::before {
    border-color: #714cdf;
    background-color: #714cdf
}

.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3e%3cpath stroke='%2332334a' d='M0 2h4'/%3e%3c/svg%3e")
}

.custom-checkbox .custom-control-input:disabled:checked~.custom-control-label::before {
    background-color: rgba(113, 76, 223, .5)
}

.custom-checkbox .custom-control-input:disabled:indeterminate~.custom-control-label::before {
    background-color: rgba(113, 76, 223, .5)
}

.custom-radio .custom-control-label::before {
    border-radius: 50%
}

.custom-radio .custom-control-input:checked~.custom-control-label::after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%2332334a'/%3e%3c/svg%3e")
}

.custom-radio .custom-control-input:disabled:checked~.custom-control-label::before {
    background-color: rgba(113, 76, 223, .5)
}

.custom-switch {
    padding-left: 2.25rem
}

.custom-switch .custom-control-label::before {
    left: -2.25rem;
    width: 1.75rem;
    pointer-events: all;
    border-radius: .5rem
}

.custom-switch .custom-control-label::after {
    top: calc(.25rem + 2px);
    left: calc(-2.25rem + 2px);
    width: calc(1rem - 4px);
    height: calc(1rem - 4px);
    background-color: #1c1d2c;
    border-radius: .5rem;
    -webkit-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-transform .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-transform .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -o-transform .15s ease-in-out;
    transition: transform .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: transform .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-transform .15s ease-in-out, -o-transform .15s ease-in-out, -webkit-box-shadow .15s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .custom-switch .custom-control-label::after {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.custom-switch .custom-control-input:checked~.custom-control-label::after {
    background-color: #151623;
    -webkit-transform: translateX(.75rem);
    -o-transform: translateX(.75rem);
    transform: translateX(.75rem)
}

.custom-switch .custom-control-input:disabled:checked~.custom-control-label::before {
    background-color: rgba(113, 76, 223, .5)
}

.custom-select {
    display: inline-block;
    width: 100%;
    height: calc(1.5em + .75rem + 2px);
    padding: .375rem 1.75rem .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #adabc6;
    vertical-align: middle;
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%2311111d' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right .75rem center/8px 10px;
    background-color: #32334a;
    border: 1px solid #11111d;
    border-radius: 6px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

.custom-select:focus {
    border-color: #c7b8f2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.custom-select:focus::-ms-value {
    color: #adabc6;
    background-color: #28293e
}

.custom-select[multiple],
.custom-select[size]:not([size="1"]) {
    height: auto;
    padding-right: .75rem;
    background-image: none
}

.custom-select:disabled {
    color: #1d1e2f;
    background-color: #282a38
}

.custom-select::-ms-expand {
    display: none
}

.custom-select-sm {
    height: calc(1.5em + .5rem + 2px);
    padding-top: .25rem;
    padding-bottom: .25rem;
    padding-left: .5rem;
    font-size: .875rem
}

.custom-select-lg {
    height: calc(1.5em + 1rem + 2px);
    padding-top: .5rem;
    padding-bottom: .5rem;
    padding-left: 1rem;
    font-size: 1.25rem
}

.custom-file {
    position: relative;
    display: inline-block;
    width: 100%;
    height: calc(1.5em + .75rem + 2px);
    margin-bottom: 0
}

.custom-file-input {
    position: relative;
    z-index: 2;
    width: 100%;
    height: calc(1.5em + .75rem + 2px);
    margin: 0;
    opacity: 0
}

.custom-file-input:focus~.custom-file-label {
    border-color: #c7b8f2;
    -webkit-box-shadow: 0 0 0 .075rem #32334a, 0 0 0 .2rem theme-color("primary");
    box-shadow: 0 0 0 .075rem #32334a, 0 0 0 .2rem theme-color("primary")
}

.custom-file-input:disabled~.custom-file-label {
    background-color: #282a38
}

.custom-file-input:lang(en)~.custom-file-label::after {
    content: "Browse"
}

.custom-file-input~.custom-file-label[data-browse]::after {
    content: attr(data-browse)
}

.custom-file-label {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1;
    height: calc(1.5em + .75rem + 2px);
    padding: .375rem .75rem;
    font-weight: 400;
    line-height: 1.5;
    color: #adabc6;
    background-color: #28293e;
    border: 1px solid #11111d;
    border-radius: 6px
}

.custom-file-label::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;
    display: block;
    height: calc(1.5em + .75rem);
    padding: .375rem .75rem;
    line-height: 1.5;
    color: #adabc6;
    content: "Browse";
    background-color: #282a38;
    border-left: inherit;
    border-radius: 0 6px 6px 0
}

.custom-range {
    width: 100%;
    height: calc(1rem + .4rem);
    padding: 0;
    background-color: transparent;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

.custom-range:focus {
    outline: 0
}

.custom-range:focus::-webkit-slider-thumb {
    -webkit-box-shadow: 0 0 0 1px #000e20, 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 1px #000e20, 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.custom-range:focus::-moz-range-thumb {
    box-shadow: 0 0 0 1px #000e20, 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.custom-range:focus::-ms-thumb {
    box-shadow: 0 0 0 1px #000e20, 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.custom-range::-moz-focus-outer {
    border: 0
}

.custom-range::-webkit-slider-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: -.25rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -webkit-appearance: none;
    appearance: none
}

@media (prefers-reduced-motion:reduce) {
    .custom-range::-webkit-slider-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.custom-range::-webkit-slider-thumb:active {
    background-color: #e9e3fa
}

.custom-range::-webkit-slider-runnable-track {
    width: 100%;
    height: .5rem;
    color: transparent;
    cursor: pointer;
    background-color: #28293e;
    border-color: transparent;
    border-radius: 1rem
}

.custom-range::-moz-range-thumb {
    width: 1rem;
    height: 1rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -moz-appearance: none;
    appearance: none
}

@media (prefers-reduced-motion:reduce) {
    .custom-range::-moz-range-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.custom-range::-moz-range-thumb:active {
    background-color: #e9e3fa
}

.custom-range::-moz-range-track {
    width: 100%;
    height: .5rem;
    color: transparent;
    cursor: pointer;
    background-color: #28293e;
    border-color: transparent;
    border-radius: 1rem
}

.custom-range::-ms-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: 0;
    margin-right: .2rem;
    margin-left: .2rem;
    background-color: #714cdf;
    border: 0;
    border-radius: 1rem;
    -webkit-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    appearance: none
}

@media (prefers-reduced-motion:reduce) {
    .custom-range::-ms-thumb {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.custom-range::-ms-thumb:active {
    background-color: #e9e3fa
}

.custom-range::-ms-track {
    width: 100%;
    height: .5rem;
    color: transparent;
    cursor: pointer;
    background-color: transparent;
    border-color: transparent;
    border-width: .5rem
}

.custom-range::-ms-fill-lower {
    background-color: #28293e;
    border-radius: 1rem
}

.custom-range::-ms-fill-upper {
    margin-right: 15px;
    background-color: #28293e;
    border-radius: 1rem
}

.custom-range:disabled::-webkit-slider-thumb {
    background-color: #1c1d2c
}

.custom-range:disabled::-webkit-slider-runnable-track {
    cursor: default
}

.custom-range:disabled::-moz-range-thumb {
    background-color: #1c1d2c
}

.custom-range:disabled::-moz-range-track {
    cursor: default
}

.custom-range:disabled::-ms-thumb {
    background-color: #1c1d2c
}

.custom-control-label::before,
.custom-file-label,
.custom-select {
    -webkit-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .custom-control-label::before,
    .custom-file-label,
    .custom-select {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.nav {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none
}

.nav-link {
    display: block;
    padding: .5rem 1rem
}

.nav-link:focus,
.nav-link:hover {
    text-decoration: none
}

.nav-link.disabled {
    color: #1d1e2f;
    pointer-events: none;
    cursor: default
}

.nav-tabs {
    border-bottom: 1px solid #151623
}

.nav-tabs .nav-item {
    margin-bottom: -1px
}

.nav-tabs .nav-link {
    border: 1px solid transparent;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px
}

.nav-tabs .nav-link:focus,
.nav-tabs .nav-link:hover {
    border-color: #282a38 #282a38 #151623
}

.nav-tabs .nav-link.disabled {
    color: #1d1e2f;
    background-color: transparent;
    border-color: transparent
}

.nav-tabs .nav-item.show .nav-link,
.nav-tabs .nav-link.active {
    color: #e4e2ff;
    background-color: #000e20;
    border-color: #151623
}

.nav-tabs .dropdown-menu {
    margin-top: -1px;
    border-top-left-radius: 0;
    border-top-right-radius: 0
}

.nav-pills .nav-link {
    border-radius: 6px
}

.nav-pills .nav-link.active,
.nav-pills .show>.nav-link {
    color: #32334a;
    background-color: #714cdf
}

.nav-fill .nav-item {
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    text-align: center
}

.nav-justified .nav-item {
    -webkit-flex-basis: 0;
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
    -ms-flex-positive: 1;
    flex-grow: 1;
    text-align: center
}

.tab-content>.tab-pane {
    display: none
}

.tab-content>.active {
    display: block
}

.navbar {
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -webkit-justify-content: space-between;
    -ms-flex-pack: justify;
    justify-content: space-between;
    padding: 3.5rem 1rem 2rem 1rem;
}

.navbar>.container,
.navbar>.container-fluid {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    -webkit-justify-content: space-between;
    -ms-flex-pack: justify;
    justify-content: space-between
}

.navbar-brand {
    display: inline-block;
    padding-top: .3125rem;
    padding-bottom: .3125rem;
    margin-right: 1rem;
    font-size: 1.25rem;
    line-height: inherit;
    white-space: nowrap
}

.navbar-brand:focus,
.navbar-brand:hover {
    text-decoration: none
}

.navbar-nav {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none
}

.navbar-nav .nav-link {
    padding-right: 0;
    padding-left: 0
}

.navbar-nav .dropdown-menu {
    position: static;
    float: none
}

.navbar-text {
    display: inline-block;
    padding-top: .5rem;
    padding-bottom: .5rem
}

.navbar-collapse {
    -webkit-flex-basis: 100%;
    -ms-flex-preferred-size: 100%;
    flex-basis: 100%;
    -webkit-box-flex: 1;
    -webkit-flex-grow: 1;
    -ms-flex-positive: 1;
    flex-grow: 1;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center
}

.navbar-toggler {
    padding: .25rem .75rem;
    font-size: 1.25rem;
    line-height: 1;
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 6px
}

.navbar-toggler:focus,
.navbar-toggler:hover {
    text-decoration: none
}

.navbar-toggler-icon {
    display: inline-block;
    width: 1.5em;
    height: 1.5em;
    vertical-align: middle;
    content: "";
    background: no-repeat center center;
    -webkit-background-size: 100% 100%;
    background-size: 100% 100%
}

@media (max-width:575.98px) {
    .navbar-expand-sm>.container,
    .navbar-expand-sm>.container-fluid {
        padding-right: 0;
        padding-left: 0
    }
}

@media (min-width:576px) {
    .navbar-expand-sm {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
        flex-flow: row nowrap;
        -webkit-box-pack: start;
        -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
        justify-content: flex-start
    }
    .navbar-expand-sm .navbar-nav {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .navbar-expand-sm .navbar-nav .dropdown-menu {
        position: absolute
    }
    .navbar-expand-sm .navbar-nav .nav-link {
        padding-right: .5rem;
        padding-left: .5rem
    }
    .navbar-expand-sm>.container,
    .navbar-expand-sm>.container-fluid {
        -webkit-flex-wrap: nowrap;
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap
    }
    .navbar-expand-sm .navbar-collapse {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important;
        -webkit-flex-basis: auto;
        -ms-flex-preferred-size: auto;
        flex-basis: auto
    }
    .navbar-expand-sm .navbar-toggler {
        display: none
    }
}

@media (max-width:767.98px) {
    .navbar-expand-md>.container,
    .navbar-expand-md>.container-fluid {
        padding-right: 0;
        padding-left: 0
    }
}

@media (min-width:768px) {
    .navbar-expand-md {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
        flex-flow: row nowrap;
        -webkit-box-pack: start;
        -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
        justify-content: flex-start
    }
    .navbar-expand-md .navbar-nav {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .navbar-expand-md .navbar-nav .dropdown-menu {
        position: absolute
    }
    .navbar-expand-md .navbar-nav .nav-link {
        padding-right: .5rem;
        padding-left: .5rem
    }
    .navbar-expand-md>.container,
    .navbar-expand-md>.container-fluid {
        -webkit-flex-wrap: nowrap;
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap
    }
    .navbar-expand-md .navbar-collapse {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important;
        -webkit-flex-basis: auto;
        -ms-flex-preferred-size: auto;
        flex-basis: auto
    }
    .navbar-expand-md .navbar-toggler {
        display: none
    }
}

@media (max-width:991.98px) {
    .navbar-expand-lg>.container,
    .navbar-expand-lg>.container-fluid {
        padding-right: 0;
        padding-left: 0
    }
}

@media (min-width:992px) {
    .navbar-expand-lg {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
        flex-flow: row nowrap;
        -webkit-box-pack: start;
        -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
        justify-content: flex-start
    }
    .navbar-expand-lg .navbar-nav {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .navbar-expand-lg .navbar-nav .dropdown-menu {
        position: absolute
    }
    .navbar-expand-lg .navbar-nav .nav-link {
        padding-right: .5rem;
        padding-left: .5rem
    }
    .navbar-expand-lg>.container,
    .navbar-expand-lg>.container-fluid {
        -webkit-flex-wrap: nowrap;
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap
    }
    .navbar-expand-lg .navbar-collapse {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important;
        -webkit-flex-basis: auto;
        -ms-flex-preferred-size: auto;
        flex-basis: auto
    }
    .navbar-expand-lg .navbar-toggler {
        display: none
    }
}

@media (max-width:1199.98px) {
    .navbar-expand-xl>.container,
    .navbar-expand-xl>.container-fluid {
        padding-right: 0;
        padding-left: 0
    }
}

@media (min-width:1200px) {
    .navbar-expand-xl {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row nowrap;
        -ms-flex-flow: row nowrap;
        flex-flow: row nowrap;
        -webkit-box-pack: start;
        -webkit-justify-content: flex-start;
        -ms-flex-pack: start;
        justify-content: flex-start
    }
    .navbar-expand-xl .navbar-nav {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .navbar-expand-xl .navbar-nav .dropdown-menu {
        position: absolute
    }
    .navbar-expand-xl .navbar-nav .nav-link {
        padding-right: .5rem;
        padding-left: .5rem
    }
    .navbar-expand-xl>.container,
    .navbar-expand-xl>.container-fluid {
        -webkit-flex-wrap: nowrap;
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap
    }
    .navbar-expand-xl .navbar-collapse {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important;
        -webkit-flex-basis: auto;
        -ms-flex-preferred-size: auto;
        flex-basis: auto
    }
    .navbar-expand-xl .navbar-toggler {
        display: none
    }
}

.navbar-expand {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-flow: row nowrap;
    -ms-flex-flow: row nowrap;
    flex-flow: row nowrap;
    -webkit-box-pack: start;
    -webkit-justify-content: flex-start;
    -ms-flex-pack: start;
    justify-content: flex-start
}

.navbar-expand>.container,
.navbar-expand>.container-fluid {
    padding-right: 0;
    padding-left: 0
}

.navbar-expand .navbar-nav {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
    -ms-flex-direction: row;
    flex-direction: row
}

.navbar-expand .navbar-nav .dropdown-menu {
    position: absolute
}

.navbar-expand .navbar-nav .nav-link {
    padding-right: .5rem;
    padding-left: .5rem
}

.navbar-expand>.container,
.navbar-expand>.container-fluid {
    -webkit-flex-wrap: nowrap;
    -ms-flex-wrap: nowrap;
    flex-wrap: nowrap
}

.navbar-expand .navbar-collapse {
    display: -webkit-box!important;
    display: -webkit-flex!important;
    display: -ms-flexbox!important;
    display: flex!important;
    -webkit-flex-basis: auto;
    -ms-flex-preferred-size: auto;
    flex-basis: auto
}

.navbar-expand .navbar-toggler {
    display: none
}

.navbar-light .navbar-brand {
    color: rgba(0, 0, 0, .9)
}

.navbar-light .navbar-brand:focus,
.navbar-light .navbar-brand:hover {
    color: rgba(0, 0, 0, .9)
}

.navbar-light .navbar-nav .nav-link {
    color: rgba(0, 0, 0, .5)
}

.navbar-light .navbar-nav .nav-link:focus,
.navbar-light .navbar-nav .nav-link:hover {
    color: rgba(0, 0, 0, .7)
}

.navbar-light .navbar-nav .nav-link.disabled {
    color: rgba(0, 0, 0, .3)
}

.navbar-light .navbar-nav .active>.nav-link,
.navbar-light .navbar-nav .nav-link.active,
.navbar-light .navbar-nav .nav-link.show,
.navbar-light .navbar-nav .show>.nav-link {
    color: rgba(0, 0, 0, .9)
}

.navbar-light .navbar-toggler {
    color: rgba(0, 0, 0, .5);
    border-color: rgba(0, 0, 0, .1)
}

.navbar-light .navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")
}

.navbar-light .navbar-text {
    color: rgba(0, 0, 0, .5)
}

.navbar-light .navbar-text a {
    color: rgba(0, 0, 0, .9)
}

.navbar-light .navbar-text a:focus,
.navbar-light .navbar-text a:hover {
    color: rgba(0, 0, 0, .9)
}

.navbar-dark .navbar-brand {
    color: #32334a
}

.navbar-dark .navbar-brand:focus,
.navbar-dark .navbar-brand:hover {
    color: #32334a
}

.navbar-dark .navbar-nav .nav-link {
    color: rgba(50, 51, 74, .5)
}

.navbar-dark .navbar-nav .nav-link:focus,
.navbar-dark .navbar-nav .nav-link:hover {
    color: rgba(50, 51, 74, .75)
}

.navbar-dark .navbar-nav .nav-link.disabled {
    color: rgba(50, 51, 74, .25)
}

.navbar-dark .navbar-nav .active>.nav-link,
.navbar-dark .navbar-nav .nav-link.active,
.navbar-dark .navbar-nav .nav-link.show,
.navbar-dark .navbar-nav .show>.nav-link {
    color: #32334a
}

.navbar-dark .navbar-toggler {
    color: rgba(50, 51, 74, .5);
    border-color: rgba(50, 51, 74, .1)
}

.navbar-dark .navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(50, 51, 74, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e")
}

.navbar-dark .navbar-text {
    color: rgba(50, 51, 74, .5)
}

.navbar-dark .navbar-text a {
    color: #32334a
}

.navbar-dark .navbar-text a:focus,
.navbar-dark .navbar-text a:hover {
    color: #32334a
}

.card {
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #32334a;
    background-clip: border-box;
    border: 1px solid #151623;
    border-radius: 6px
}

.card>hr {
    margin-right: 0;
    margin-left: 0
}

.card>.list-group:first-child .list-group-item:first-child {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px
}

.card>.list-group:last-child .list-group-item:last-child {
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 6px
}

.card-body {
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: 1.25rem
}

.card-title {
    margin-bottom: .75rem
}

.card-subtitle {
    margin-top: -.375rem;
    margin-bottom: 0
}

.card-text:last-child {
    margin-bottom: 0
}

.card-link:hover {
    text-decoration: none
}

.card-link+.card-link {
    margin-left: 1.25rem
}

.card-header {
    padding: .75rem 1.25rem;
    margin-bottom: 0;
    background-color: #1e2037;
    border-bottom: 1px solid #151623
}

.card-header:first-child {
    border-radius: calc(6px - 1px) calc(6px - 1px) calc(6px - 1px) calc(6px - 1px)
}

.card-header+.list-group .list-group-item:first-child {
    border-top: 0
}

.card-footer {
    padding: .75rem 1.25rem;
    background-color: #1e2037;
    border-top: 1px solid #151623
}

.card-footer:last-child {
    border-radius: 0 0 calc(6px - 1px) calc(6px - 1px)
}

.card-header-tabs {
    margin-right: -.625rem;
    margin-bottom: -.75rem;
    margin-left: -.625rem;
    border-bottom: 0
}

.card-header-pills {
    margin-right: -.625rem;
    margin-left: -.625rem
}

.card-img-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 1.25rem
}

.card-img {
    width: 100%;
    border-radius: calc(6px - 1px)
}

.card-img-top {
    width: 100%;
    border-top-left-radius: calc(6px - 1px);
    border-top-right-radius: calc(6px - 1px)
}

.card-img-bottom {
    width: 100%;
    border-bottom-right-radius: calc(6px - 1px);
    border-bottom-left-radius: calc(6px - 1px)
}

.card-deck {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column
}

.card-deck .card {
    margin-bottom: 15px
}

@media (min-width:576px) {
    .card-deck {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row wrap;
        -ms-flex-flow: row wrap;
        flex-flow: row wrap;
        margin-right: -15px;
        margin-left: -15px
    }
    .card-deck .card {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-flex: 1;
        -webkit-flex: 1 0 0%;
        -ms-flex: 1 0 0%;
        flex: 1 0 0%;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -webkit-flex-direction: column;
        -ms-flex-direction: column;
        flex-direction: column;
        margin-right: 15px;
        margin-bottom: 0;
        margin-left: 15px
    }
}

.card-group {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column
}

.card-group>.card {
    margin-bottom: 15px
}

@media (min-width:576px) {
    .card-group {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-flow: row wrap;
        -ms-flex-flow: row wrap;
        flex-flow: row wrap
    }
    .card-group>.card {
        -webkit-box-flex: 1;
        -webkit-flex: 1 0 0%;
        -ms-flex: 1 0 0%;
        flex: 1 0 0%;
        margin-bottom: 0
    }
    .card-group>.card+.card {
        margin-left: 0;
        border-left: 0
    }
    .card-group>.card:not(:last-child) {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0
    }
    .card-group>.card:not(:last-child) .card-header,
    .card-group>.card:not(:last-child) .card-img-top {
        border-top-right-radius: 0
    }
    .card-group>.card:not(:last-child) .card-footer,
    .card-group>.card:not(:last-child) .card-img-bottom {
        border-bottom-right-radius: 0
    }
    .card-group>.card:not(:first-child) {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0
    }
    .card-group>.card:not(:first-child) .card-header,
    .card-group>.card:not(:first-child) .card-img-top {
        border-top-left-radius: 0
    }
    .card-group>.card:not(:first-child) .card-footer,
    .card-group>.card:not(:first-child) .card-img-bottom {
        border-bottom-left-radius: 0
    }
}

.card-columns .card {
    margin-bottom: .75rem
}

@media (min-width:576px) {
    .card-columns {
        -webkit-column-count: 3;
        -moz-column-count: 3;
        column-count: 3;
        -webkit-column-gap: 1.25rem;
        -moz-column-gap: 1.25rem;
        column-gap: 1.25rem;
        orphans: 1;
        widows: 1
    }
    .card-columns .card {
        display: inline-block;
        width: 100%
    }
}

.accordion>.card {
    overflow: hidden
}

.accordion>.card:not(:first-of-type) .card-header:first-child {
    border-radius: 0
}

.accordion>.card:not(:first-of-type):not(:last-of-type) {
    border-bottom: 0;
    border-radius: 0
}

.accordion>.card:first-of-type {
    border-bottom: 0;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0
}

.accordion>.card:last-of-type {
    border-top-left-radius: 0;
    border-top-right-radius: 0
}

.accordion>.card .card-header {
    margin-bottom: -1px
}

.breadcrumb {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding: .75rem 1rem;
    margin-bottom: 1rem;
    list-style: none;
    background-color: #282a38;
    border-radius: 6px
}

.breadcrumb-item+.breadcrumb-item {
    padding-left: .5rem
}

.breadcrumb-item+.breadcrumb-item::before {
    display: inline-block;
    padding-right: .5rem;
    color: #1d1e2f;
    content: "/"
}

.breadcrumb-item+.breadcrumb-item:hover::before {
    text-decoration: underline
}

.breadcrumb-item+.breadcrumb-item:hover::before {
    text-decoration: none
}

.breadcrumb-item.active {
    color: #1d1e2f
}

.pagination {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    padding-left: 0;
    list-style: none;
    border-radius: 6px
}

.page-link {
    position: relative;
    display: block;
    padding: .5rem .75rem;
    margin-left: -1px;
    line-height: 1.25;
    color: #714cdf;
    background-color: #32334a;
    border: 1px solid #151623
}

.page-link:hover {
    z-index: 2;
    color: #4922bd;
    text-decoration: none;
    background-color: #282a38;
    border-color: #151623
}

.page-link:focus {
    z-index: 2;
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .25)
}

.page-item:first-child .page-link {
    margin-left: 0;
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px
}

.page-item:last-child .page-link {
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px
}

.page-item.active .page-link {
    z-index: 1;
    color: #fff;
    background-color: #714cdf;
    border-color: #714cdf
}

.page-item.disabled .page-link {
    color: #11111d;
    pointer-events: none;
    cursor: auto;
    background-color: #32334a;
    border-color: #151623
}

.pagination-lg .page-link {
    padding: .75rem 1.5rem;
    font-size: 1.25rem;
    line-height: 1.5
}

.pagination-lg .page-item:first-child .page-link {
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px
}

.pagination-lg .page-item:last-child .page-link {
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px
}

.pagination-sm .page-link {
    padding: .25rem .5rem;
    font-size: .875rem;
    line-height: 1.5
}

.pagination-sm .page-item:first-child .page-link {
    border-top-left-radius: .2rem;
    border-bottom-left-radius: .2rem
}

.pagination-sm .page-item:last-child .page-link {
    border-top-right-radius: .2rem;
    border-bottom-right-radius: .2rem
}

.badge {
    display: inline-block;
    padding: .25em .4em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 6px;
    -webkit-transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, -webkit-box-shadow .15s ease-in-out;
    -o-transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out, -webkit-box-shadow .15s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .badge {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

a.badge:focus,
a.badge:hover {
    text-decoration: none
}

.badge:empty {
    display: none
}

.btn .badge {
    position: relative;
    top: -1px
}

.badge-pill {
    padding-right: .6em;
    padding-left: .6em;
    border-radius: 10rem
}

.badge-primary {
    color: #fff;
    background-color: #714cdf
}

a.badge-primary:focus,
a.badge-primary:hover {
    color: #fff;
    background-color: #5126d2
}

a.badge-primary.focus,
a.badge-primary:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5);
    box-shadow: 0 0 0 .2rem rgba(113, 76, 223, .5)
}

.badge-secondary {
    color: #fff;
    background-color: #16a4de
}

a.badge-secondary:focus,
a.badge-secondary:hover {
    color: #fff;
    background-color: #1182b0
}

a.badge-secondary.focus,
a.badge-secondary:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5);
    box-shadow: 0 0 0 .2rem rgba(22, 164, 222, .5)
}

.badge-success {
    color: #fff;
    background-color: #17b06b
}

a.badge-success:focus,
a.badge-success:hover {
    color: #fff;
    background-color: #118350
}

a.badge-success.focus,
a.badge-success:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5);
    box-shadow: 0 0 0 .2rem rgba(23, 176, 107, .5)
}

.badge-info {
    color: #fff;
    background-color: #2983fe
}

a.badge-info:focus,
a.badge-info:hover {
    color: #fff;
    background-color: #0167f3
}

a.badge-info.focus,
a.badge-info:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5);
    box-shadow: 0 0 0 .2rem rgba(41, 131, 254, .5)
}

.badge-warning {
    color: #fff;
    background-color: #f97515
}

a.badge-warning:focus,
a.badge-warning:hover {
    color: #fff;
    background-color: #d65d05
}

a.badge-warning.focus,
a.badge-warning:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5);
    box-shadow: 0 0 0 .2rem rgba(249, 117, 21, .5)
}

.badge-danger {
    color: #fff;
    background-color: #ef121b
}

a.badge-danger:focus,
a.badge-danger:hover {
    color: #fff;
    background-color: #ff0931
}

a.badge-danger.focus,
a.badge-danger:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5);
    box-shadow: 0 0 0 .2rem rgba(255, 60, 92, .5)
}

.badge-light {
    color: #0a0b14;
    background-color: #dbebfb
}

a.badge-light:focus,
a.badge-light:hover {
    color: #0a0b14;
    background-color: #add2f6
}

a.badge-light.focus,
a.badge-light:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5);
    box-shadow: 0 0 0 .2rem rgba(219, 235, 251, .5)
}

.badge-dark {
    color: #fff;
    background-color: #32334a
}

a.badge-dark:focus,
a.badge-dark:hover {
    color: #fff;
    background-color: #1d1e2c
}

a.badge-dark.focus,
a.badge-dark:focus {
    outline: 0;
    -webkit-box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5);
    box-shadow: 0 0 0 .2rem rgba(50, 51, 74, .5)
}

.jumbotron {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
    background-color: #282a38;
    border-radius: 6px
}

@media (min-width:576px) {
    .jumbotron {
        padding: 4rem 2rem
    }
}

.jumbotron-fluid {
    padding-right: 0;
    padding-left: 0;
    border-radius: 0
}

.alert {
    position: relative;
    padding: .75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: 6px
}

.alert-heading {
    color: inherit
}

.alert-link {
    font-weight: 700
}

.alert-dismissible {
    padding-right: 4rem
}

.alert-dismissible .close {
    position: absolute;
    top: 0;
    right: 0;
    padding: .75rem 1.25rem;
    color: inherit
}

.alert-primary {
    color: #3b2874;
    background-color: #e3dbf9;
    border-color: #d7cdf6
}

.alert-primary hr {
    border-top-color: #c6b7f2
}

.alert-primary .alert-link {
    color: #281b4e
}

.alert-secondary {
    color: #0b5573;
    background-color: #d0edf8;
    border-color: #bee6f6
}

.alert-secondary hr {
    border-top-color: #a8ddf3
}

.alert-secondary .alert-link {
    color: #073344
}

.alert-success {
    color: #0c5c38;
    background-color: #d1efe1;
    border-color: #bee9d6
}

.alert-success hr {
    border-top-color: #abe3ca
}

.alert-success .alert-link {
    color: #062f1d
}

.alert-info {
    color: #154484;
    background-color: #d4e6ff;
    border-color: #c3dcff
}

.alert-info hr {
    border-top-color: #aacdff
}

.alert-info .alert-link {
    color: #0e2d58
}

.alert-warning {
    color: #813d0b;
    background-color: #fee3d0;
    border-color: #fdd8bd
}

.alert-warning hr {
    border-top-color: #fcc9a4
}

.alert-warning .alert-link {
    color: #522707
}

.alert-danger {
    color: #851f30;
    background-color: #ffd8de;
    border-color: #ffc8d1
}

.alert-danger hr {
    border-top-color: #ffafbc
}

.alert-danger .alert-link {
    color: #5c1521
}

.alert-light {
    color: #727a83;
    background-color: #f8fbfe;
    border-color: #f5f9fe
}

.alert-light hr {
    border-top-color: #deebfc
}

.alert-light .alert-link {
    color: #5a6168
}

.alert-dark {
    color: #1a1b26;
    background-color: #d6d6db;
    border-color: #c6c6cc
}

.alert-dark hr {
    border-top-color: #b9b9c0
}

.alert-dark .alert-link {
    color: #050508
}

@-webkit-keyframes progress-bar-stripes {
    from {
        background-position: 1rem 0
    }
    to {
        background-position: 0 0
    }
}

@-o-keyframes progress-bar-stripes {
    from {
        background-position: 1rem 0
    }
    to {
        background-position: 0 0
    }
}

@keyframes progress-bar-stripes {
    from {
        background-position: 1rem 0
    }
    to {
        background-position: 0 0
    }
}

.progress {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    height: 1rem;
    overflow: hidden;
    font-size: .75rem;
    background-color: #282a38;
    border-radius: 6px
}

.progress-bar {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    color: #32334a;
    text-align: center;
    white-space: nowrap;
    background-color: #714cdf;
    -webkit-transition: width .6s ease;
    -o-transition: width .6s ease;
    transition: width .6s ease
}

@media (prefers-reduced-motion:reduce) {
    .progress-bar {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.progress-bar-striped {
    background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
    background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
    background-image: linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
    -webkit-background-size: 1rem 1rem;
    background-size: 1rem 1rem
}

.progress-bar-animated {
    -webkit-animation: progress-bar-stripes 1s linear infinite;
    -o-animation: progress-bar-stripes 1s linear infinite;
    animation: progress-bar-stripes 1s linear infinite
}

@media (prefers-reduced-motion:reduce) {
    .progress-bar-animated {
        -webkit-animation: none;
        -o-animation: none;
        animation: none
    }
}

.media {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -webkit-align-items: flex-start;
    -ms-flex-align: start;
    align-items: flex-start
}

.media-body {
    -webkit-box-flex: 1;
    -webkit-flex: 1;
    -ms-flex: 1;
    flex: 1
}

.list-group {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0
}

.list-group-item-action {
    width: 100%;
    color: #e4e2ff;
    text-align: inherit
}

.list-group-item-action:focus,
.list-group-item-action:hover {
    z-index: 1;
    color: #e4e2ff;
    text-decoration: none;
    background-color: #2d2e3f
}

.list-group-item-action:active {
    color: #e4e2ff;
    background-color: #282a38
}

.list-group-item {
    position: relative;
    display: block;
    padding: .75rem 1.25rem;
    margin-bottom: -1px;
    background-color: #32334a;
    border: 1px solid rgba(0, 0, 0, .125)
}

.list-group-item:first-child {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px
}

.list-group-item:last-child {
    margin-bottom: 0;
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 6px
}

.list-group-item.disabled,
.list-group-item:disabled {
    color: #1d1e2f;
    pointer-events: none;
    background-color: #32334a
}

.list-group-item.active {
    z-index: 2;
    color: #32334a;
    background-color: #714cdf;
    border-color: #714cdf
}

.list-group-horizontal {
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
    -ms-flex-direction: row;
    flex-direction: row
}

.list-group-horizontal .list-group-item {
    margin-right: -1px;
    margin-bottom: 0
}

.list-group-horizontal .list-group-item:first-child {
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
    border-top-right-radius: 0
}

.list-group-horizontal .list-group-item:last-child {
    margin-right: 0;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 0
}

@media (min-width:576px) {
    .list-group-horizontal-sm {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .list-group-horizontal-sm .list-group-item {
        margin-right: -1px;
        margin-bottom: 0
    }
    .list-group-horizontal-sm .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0
    }
    .list-group-horizontal-sm .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0
    }
}

@media (min-width:768px) {
    .list-group-horizontal-md {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .list-group-horizontal-md .list-group-item {
        margin-right: -1px;
        margin-bottom: 0
    }
    .list-group-horizontal-md .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0
    }
    .list-group-horizontal-md .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0
    }
}

@media (min-width:992px) {
    .list-group-horizontal-lg {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .list-group-horizontal-lg .list-group-item {
        margin-right: -1px;
        margin-bottom: 0
    }
    .list-group-horizontal-lg .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0
    }
    .list-group-horizontal-lg .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0
    }
}

@media (min-width:1200px) {
    .list-group-horizontal-xl {
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row
    }
    .list-group-horizontal-xl .list-group-item {
        margin-right: -1px;
        margin-bottom: 0
    }
    .list-group-horizontal-xl .list-group-item:first-child {
        border-top-left-radius: 6px;
        border-bottom-left-radius: 6px;
        border-top-right-radius: 0
    }
    .list-group-horizontal-xl .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
        border-bottom-left-radius: 0
    }
}

.list-group-flush .list-group-item {
    border-right: 0;
    border-left: 0;
    border-radius: 0
}

.list-group-flush .list-group-item:last-child {
    margin-bottom: -1px
}

.list-group-flush:first-child .list-group-item:first-child {
    border-top: 0
}

.list-group-flush:last-child .list-group-item:last-child {
    margin-bottom: 0;
    border-bottom: 0
}

.list-group-item-primary {
    color: #3b2874;
    background-color: #d7cdf6
}

.list-group-item-primary.list-group-item-action:focus,
.list-group-item-primary.list-group-item-action:hover {
    color: #3b2874;
    background-color: #c6b7f2
}

.list-group-item-primary.list-group-item-action.active {
    color: #fff;
    background-color: #3b2874;
    border-color: #3b2874
}

.list-group-item-secondary {
    color: #0b5573;
    background-color: #bee6f6
}

.list-group-item-secondary.list-group-item-action:focus,
.list-group-item-secondary.list-group-item-action:hover {
    color: #0b5573;
    background-color: #a8ddf3
}

.list-group-item-secondary.list-group-item-action.active {
    color: #fff;
    background-color: #0b5573;
    border-color: #0b5573
}

.list-group-item-success {
    color: #0c5c38;
    background-color: #bee9d6
}

.list-group-item-success.list-group-item-action:focus,
.list-group-item-success.list-group-item-action:hover {
    color: #0c5c38;
    background-color: #abe3ca
}

.list-group-item-success.list-group-item-action.active {
    color: #fff;
    background-color: #0c5c38;
    border-color: #0c5c38
}

.list-group-item-info {
    color: #154484;
    background-color: #c3dcff
}

.list-group-item-info.list-group-item-action:focus,
.list-group-item-info.list-group-item-action:hover {
    color: #154484;
    background-color: #aacdff
}

.list-group-item-info.list-group-item-action.active {
    color: #fff;
    background-color: #154484;
    border-color: #154484
}

.list-group-item-warning {
    color: #813d0b;
    background-color: #fdd8bd
}

.list-group-item-warning.list-group-item-action:focus,
.list-group-item-warning.list-group-item-action:hover {
    color: #813d0b;
    background-color: #fcc9a4
}

.list-group-item-warning.list-group-item-action.active {
    color: #fff;
    background-color: #813d0b;
    border-color: #813d0b
}

.list-group-item-danger {
    color: #851f30;
    background-color: #ffc8d1
}

.list-group-item-danger.list-group-item-action:focus,
.list-group-item-danger.list-group-item-action:hover {
    color: #851f30;
    background-color: #ffafbc
}

.list-group-item-danger.list-group-item-action.active {
    color: #fff;
    background-color: #851f30;
    border-color: #851f30
}

.list-group-item-light {
    color: #727a83;
    background-color: #f5f9fe
}

.list-group-item-light.list-group-item-action:focus,
.list-group-item-light.list-group-item-action:hover {
    color: #727a83;
    background-color: #deebfc
}

.list-group-item-light.list-group-item-action.active {
    color: #fff;
    background-color: #727a83;
    border-color: #727a83
}

.list-group-item-dark {
    color: #1a1b26;
    background-color: #c6c6cc
}

.list-group-item-dark.list-group-item-action:focus,
.list-group-item-dark.list-group-item-action:hover {
    color: #1a1b26;
    background-color: #b9b9c0
}

.list-group-item-dark.list-group-item-action.active {
    color: #fff;
    background-color: #1a1b26;
    border-color: #1a1b26
}

.close {
    float: right;
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1;
    color: #000;
    text-shadow: 0 1px 0 #32334a;
    opacity: .5
}

.close:hover {
    color: #000;
    text-decoration: none
}

.close:not(:disabled):not(.disabled):focus,
.close:not(:disabled):not(.disabled):hover {
    opacity: .75
}

button.close {
    padding: 0;
    background-color: transparent;
    border: 0;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

a.close.disabled {
    pointer-events: none
}

.toast {
    max-width: 350px;
    overflow: hidden;
    font-size: .875rem;
    background-color: rgba(255, 255, 255, .85);
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .1);
    -webkit-box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .1);
    box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .1);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    opacity: 0;
    border-radius: .25rem
}

.toast:not(:last-child) {
    margin-bottom: .75rem
}

.toast.showing {
    opacity: 1
}

.toast.show {
    display: block;
    opacity: 1
}

.toast.hide {
    display: none
}

.toast-header {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    padding: .25rem .75rem;
    color: #1d1e2f;
    background-color: rgba(255, 255, 255, .85);
    background-clip: padding-box;
    border-bottom: 1px solid rgba(0, 0, 0, .05)
}

.toast-body {
    padding: .75rem
}

.modal-open {
    overflow: hidden
}

.modal-open .modal {
    overflow-x: hidden;
    overflow-y: auto
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1050;
    display: none;
    width: 100%;
    height: 100%;
    overflow: hidden;
    outline: 0
}

.modal-dialog {
    position: relative;
    width: auto;
    margin: .5rem;
    pointer-events: none
}

.modal.fade .modal-dialog {
    -webkit-transition: -webkit-transform .3s ease-out;
    transition: -webkit-transform .3s ease-out;
    -o-transition: -o-transform .3s ease-out;
    transition: transform .3s ease-out;
    transition: transform .3s ease-out, -webkit-transform .3s ease-out, -o-transform .3s ease-out;
    -webkit-transform: translate(0, -50px);
    -o-transform: translate(0, -50px);
    transform: translate(0, -50px)
}

@media (prefers-reduced-motion:reduce) {
    .modal.fade .modal-dialog {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.modal.show .modal-dialog {
    -webkit-transform: none;
    -o-transform: none;
    transform: none
}

.modal-dialog-scrollable {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    max-height: calc(100% - 1rem)
}

.modal-dialog-scrollable .modal-content {
    max-height: calc(100vh - 1rem);
    overflow: hidden
}

.modal-dialog-scrollable .modal-footer,
.modal-dialog-scrollable .modal-header {
    -webkit-flex-shrink: 0;
    -ms-flex-negative: 0;
    flex-shrink: 0
}

.modal-dialog-scrollable .modal-body {
    overflow-y: auto
}

.modal-dialog-centered {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    min-height: calc(100% - 1rem)
}

.modal-dialog-centered::before {
    display: block;
    height: calc(100vh - 1rem);
    content: ""
}

.modal-dialog-centered.modal-dialog-scrollable {
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    height: 100%
}

.modal-dialog-centered.modal-dialog-scrollable .modal-content {
    max-height: none
}

.modal-dialog-centered.modal-dialog-scrollable::before {
    content: none
}

.modal-content {
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 100%;
    pointer-events: auto;
    background-color: #32334a;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .2);
    border-radius: 6px;
    outline: 0
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
    background-color: #000
}

.modal-backdrop.fade {
    opacity: 0
}

.modal-backdrop.show {
    opacity: .5
}

.modal-header {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -webkit-align-items: flex-start;
    -ms-flex-align: start;
    align-items: flex-start;
    -webkit-box-pack: justify;
    -webkit-justify-content: space-between;
    -ms-flex-pack: justify;
    justify-content: space-between;
    padding: 1rem 1rem;
    border-bottom: 1px solid #28293e;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px
}

.modal-header .close {
    padding: 1rem 1rem;
    margin: -1rem -1rem -1rem auto
}

.modal-title {
    margin-bottom: 0;
    line-height: 1.5
}

.modal-body {
    position: relative;
    -webkit-box-flex: 1;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: 1rem
}

.modal-footer {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: end;
    -webkit-justify-content: flex-end;
    -ms-flex-pack: end;
    justify-content: flex-end;
    padding: 1rem;
    border-top: 1px solid #28293e;
    border-bottom-right-radius: 6px;
    border-bottom-left-radius: 6px
}

.modal-footer>:not(:first-child) {
    margin-left: .25rem
}

.modal-footer>:not(:last-child) {
    margin-right: .25rem
}

.modal-scrollbar-measure {
    position: absolute;
    top: -9999px;
    width: 50px;
    height: 50px;
    overflow: scroll
}

@media (min-width:576px) {
    .modal-dialog {
        max-width: 500px;
        margin: 1.75rem auto
    }
    .modal-dialog-scrollable {
        max-height: calc(100% - 3.5rem)
    }
    .modal-dialog-scrollable .modal-content {
        max-height: calc(100vh - 3.5rem)
    }
    .modal-dialog-centered {
        min-height: calc(100% - 3.5rem)
    }
    .modal-dialog-centered::before {
        height: calc(100vh - 3.5rem)
    }
    .modal-sm {
        max-width: 300px
    }
}

@media (min-width:992px) {
    .modal-lg,
    .modal-xl {
        max-width: 800px
    }
}

@media (min-width:1200px) {
    .modal-xl {
        max-width: 1140px
    }
}

.tooltip {
    position: absolute;
    z-index: 1070;
    display: block;
    margin: 0;
    font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-style: normal;
    font-weight: 400;
    line-height: 1.5;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    word-spacing: normal;
    white-space: normal;
    line-break: auto;
    font-size: .875rem;
    word-wrap: break-word;
    opacity: 0
}

.tooltip.show {
    opacity: .9
}

.tooltip .arrow {
    position: absolute;
    display: block;
    width: .8rem;
    height: .4rem
}

.tooltip .arrow::before {
    position: absolute;
    content: "";
    border-color: transparent;
    border-style: solid
}

.bs-tooltip-auto[x-placement^=top],
.bs-tooltip-top {
    padding: .4rem 0
}

.bs-tooltip-auto[x-placement^=top] .arrow,
.bs-tooltip-top .arrow {
    bottom: 0
}

.bs-tooltip-auto[x-placement^=top] .arrow::before,
.bs-tooltip-top .arrow::before {
    top: 0;
    border-width: .4rem .4rem 0;
    border-top-color: #000
}

.bs-tooltip-auto[x-placement^=right],
.bs-tooltip-right {
    padding: 0 .4rem
}

.bs-tooltip-auto[x-placement^=right] .arrow,
.bs-tooltip-right .arrow {
    left: 0;
    width: .4rem;
    height: .8rem
}

.bs-tooltip-auto[x-placement^=right] .arrow::before,
.bs-tooltip-right .arrow::before {
    right: 0;
    border-width: .4rem .4rem .4rem 0;
    border-right-color: #000
}

.bs-tooltip-auto[x-placement^=bottom],
.bs-tooltip-bottom {
    padding: .4rem 0
}

.bs-tooltip-auto[x-placement^=bottom] .arrow,
.bs-tooltip-bottom .arrow {
    top: 0
}

.bs-tooltip-auto[x-placement^=bottom] .arrow::before,
.bs-tooltip-bottom .arrow::before {
    bottom: 0;
    border-width: 0 .4rem .4rem;
    border-bottom-color: #000
}

.bs-tooltip-auto[x-placement^=left],
.bs-tooltip-left {
    padding: 0 .4rem
}

.bs-tooltip-auto[x-placement^=left] .arrow,
.bs-tooltip-left .arrow {
    right: 0;
    width: .4rem;
    height: .8rem
}

.bs-tooltip-auto[x-placement^=left] .arrow::before,
.bs-tooltip-left .arrow::before {
    left: 0;
    border-width: .4rem 0 .4rem .4rem;
    border-left-color: #000
}

.tooltip-inner {
    max-width: 200px;
    padding: .25rem .5rem;
    color: #e4e2ff;
    text-align: center;
    background-color: #000;
    border-radius: 6px
}

.popover {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1060;
    display: block;
    max-width: 276px;
    font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-style: normal;
    font-weight: 400;
    line-height: 1.5;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    word-spacing: normal;
    white-space: normal;
    line-break: auto;
    font-size: .875rem;
    word-wrap: break-word;
    background-color: #32334a;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, .2);
    border-radius: 6px
}

.popover .arrow {
    position: absolute;
    display: block;
    width: 1rem;
    height: .5rem;
    margin: 0 6px
}

.popover .arrow::after,
.popover .arrow::before {
    position: absolute;
    display: block;
    content: "";
    border-color: transparent;
    border-style: solid
}

.bs-popover-auto[x-placement^=top],
.bs-popover-top {
    margin-bottom: .5rem
}

.bs-popover-auto[x-placement^=top]>.arrow,
.bs-popover-top>.arrow {
    bottom: calc((.5rem + 1px) * -1)
}

.bs-popover-auto[x-placement^=top]>.arrow::before,
.bs-popover-top>.arrow::before {
    bottom: 0;
    border-width: .5rem .5rem 0;
    border-top-color: rgba(0, 0, 0, .25)
}

.bs-popover-auto[x-placement^=top]>.arrow::after,
.bs-popover-top>.arrow::after {
    bottom: 1px;
    border-width: .5rem .5rem 0;
    border-top-color: #32334a
}

.bs-popover-auto[x-placement^=right],
.bs-popover-right {
    margin-left: .5rem
}

.bs-popover-auto[x-placement^=right]>.arrow,
.bs-popover-right>.arrow {
    left: calc((.5rem + 1px) * -1);
    width: .5rem;
    height: 1rem;
    margin: 6px 0
}

.bs-popover-auto[x-placement^=right]>.arrow::before,
.bs-popover-right>.arrow::before {
    left: 0;
    border-width: .5rem .5rem .5rem 0;
    border-right-color: rgba(0, 0, 0, .25)
}

.bs-popover-auto[x-placement^=right]>.arrow::after,
.bs-popover-right>.arrow::after {
    left: 1px;
    border-width: .5rem .5rem .5rem 0;
    border-right-color: #32334a
}

.bs-popover-auto[x-placement^=bottom],
.bs-popover-bottom {
    margin-top: .5rem
}

.bs-popover-auto[x-placement^=bottom]>.arrow,
.bs-popover-bottom>.arrow {
    top: calc((.5rem + 1px) * -1)
}

.bs-popover-auto[x-placement^=bottom]>.arrow::before,
.bs-popover-bottom>.arrow::before {
    top: 0;
    border-width: 0 .5rem .5rem .5rem;
    border-bottom-color: rgba(0, 0, 0, .25)
}

.bs-popover-auto[x-placement^=bottom]>.arrow::after,
.bs-popover-bottom>.arrow::after {
    top: 1px;
    border-width: 0 .5rem .5rem .5rem;
    border-bottom-color: #32334a
}

.bs-popover-auto[x-placement^=bottom] .popover-header::before,
.bs-popover-bottom .popover-header::before {
    position: absolute;
    top: 0;
    left: 50%;
    display: block;
    width: 1rem;
    margin-left: -.5rem;
    content: "";
    border-bottom: 1px solid #2c2d41
}

.bs-popover-auto[x-placement^=left],
.bs-popover-left {
    margin-right: .5rem
}

.bs-popover-auto[x-placement^=left]>.arrow,
.bs-popover-left>.arrow {
    right: calc((.5rem + 1px) * -1);
    width: .5rem;
    height: 1rem;
    margin: 6px 0
}

.bs-popover-auto[x-placement^=left]>.arrow::before,
.bs-popover-left>.arrow::before {
    right: 0;
    border-width: .5rem 0 .5rem .5rem;
    border-left-color: rgba(0, 0, 0, .25)
}

.bs-popover-auto[x-placement^=left]>.arrow::after,
.bs-popover-left>.arrow::after {
    right: 1px;
    border-width: .5rem 0 .5rem .5rem;
    border-left-color: #32334a
}

.popover-header {
    padding: .5rem .75rem;
    margin-bottom: 0;
    font-size: 1rem;
    background-color: #2c2d41;
    border-bottom: 1px solid #222232;
    border-top-left-radius: calc(6px - 1px);
    border-top-right-radius: calc(6px - 1px)
}

.popover-header:empty {
    display: none
}

.popover-body {
    padding: .5rem .75rem;
    color: #e4e2ff
}

.carousel {
    position: relative
}

.carousel.pointer-event {
    -ms-touch-action: pan-y;
    touch-action: pan-y
}

.carousel-inner {
    position: relative;
    width: 100%;
    overflow: hidden
}

.carousel-inner::after {
    display: block;
    clear: both;
    content: ""
}

.carousel-item {
    position: relative;
    display: none;
    float: left;
    width: 100%;
    margin-right: -100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-transition: -webkit-transform .6s ease-in-out;
    transition: -webkit-transform .6s ease-in-out;
    -o-transition: -o-transform .6s ease-in-out;
    transition: transform .6s ease-in-out;
    transition: transform .6s ease-in-out, -webkit-transform .6s ease-in-out, -o-transform .6s ease-in-out
}

@media (prefers-reduced-motion:reduce) {
    .carousel-item {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.carousel-item-next,
.carousel-item-prev,
.carousel-item.active {
    display: block
}

.active.carousel-item-right,
.carousel-item-next:not(.carousel-item-left) {
    -webkit-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%)
}

.active.carousel-item-left,
.carousel-item-prev:not(.carousel-item-right) {
    -webkit-transform: translateX(-100%);
    -o-transform: translateX(-100%);
    transform: translateX(-100%)
}

.carousel-fade .carousel-item {
    opacity: 0;
    -webkit-transition-property: opacity;
    -o-transition-property: opacity;
    transition-property: opacity;
    -webkit-transform: none;
    -o-transform: none;
    transform: none
}

.carousel-fade .carousel-item-next.carousel-item-left,
.carousel-fade .carousel-item-prev.carousel-item-right,
.carousel-fade .carousel-item.active {
    z-index: 1;
    opacity: 1
}

.carousel-fade .active.carousel-item-left,
.carousel-fade .active.carousel-item-right {
    z-index: 0;
    opacity: 0;
    -webkit-transition: 0s .6s opacity;
    -o-transition: 0s .6s opacity;
    transition: 0s .6s opacity
}

@media (prefers-reduced-motion:reduce) {
    .carousel-fade .active.carousel-item-left,
    .carousel-fade .active.carousel-item-right {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.carousel-control-next,
.carousel-control-prev {
    position: absolute;
    top: 0;
    bottom: 0;
    z-index: 1;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    width: 15%;
    color: #32334a;
    text-align: center;
    opacity: .5;
    -webkit-transition: opacity .15s ease;
    -o-transition: opacity .15s ease;
    transition: opacity .15s ease
}

@media (prefers-reduced-motion:reduce) {
    .carousel-control-next,
    .carousel-control-prev {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.carousel-control-next:focus,
.carousel-control-next:hover,
.carousel-control-prev:focus,
.carousel-control-prev:hover {
    color: #32334a;
    text-decoration: none;
    outline: 0;
    opacity: .9
}

.carousel-control-prev {
    left: 0
}

.carousel-control-next {
    right: 0
}

.carousel-control-next-icon,
.carousel-control-prev-icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    background: no-repeat 50%/100% 100%
}

.carousel-control-prev-icon {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%2332334a' viewBox='0 0 8 8'%3e%3cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3e%3c/svg%3e")
}

.carousel-control-next-icon {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%2332334a' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3e%3c/svg%3e")
}

.carousel-indicators {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 15;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    padding-left: 0;
    margin-right: 15%;
    margin-left: 15%;
    list-style: none
}

.carousel-indicators li {
    -webkit-box-sizing: content-box;
    box-sizing: content-box;
    -webkit-box-flex: 0;
    -webkit-flex: 0 1 auto;
    -ms-flex: 0 1 auto;
    flex: 0 1 auto;
    width: 30px;
    height: 3px;
    margin-right: 3px;
    margin-left: 3px;
    text-indent: -999px;
    cursor: pointer;
    background-color: #32334a;
    background-clip: padding-box;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    opacity: .5;
    -webkit-transition: opacity .6s ease;
    -o-transition: opacity .6s ease;
    transition: opacity .6s ease
}

@media (prefers-reduced-motion:reduce) {
    .carousel-indicators li {
        -webkit-transition: none;
        -o-transition: none;
        transition: none
    }
}

.carousel-indicators .active {
    opacity: 1
}

.carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 20px;
    left: 15%;
    z-index: 10;
    padding-top: 20px;
    padding-bottom: 20px;
    color: #32334a;
    text-align: center
}

@-webkit-keyframes spinner-border {
    to {
        -webkit-transform: rotate(360deg);
        transform: rotate(360deg)
    }
}

@-o-keyframes spinner-border {
    to {
        -o-transform: rotate(360deg);
        transform: rotate(360deg)
    }
}

@keyframes spinner-border {
    to {
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg)
    }
}

.spinner-border {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    vertical-align: text-bottom;
    border: .25em solid currentColor;
    border-right-color: transparent;
    border-radius: 50%;
    -webkit-animation: spinner-border .75s linear infinite;
    -o-animation: spinner-border .75s linear infinite;
    animation: spinner-border .75s linear infinite
}

.spinner-border-sm {
    width: 1rem;
    height: 1rem;
    border-width: .2em
}

@-webkit-keyframes spinner-grow {
    0% {
        -webkit-transform: scale(0);
        transform: scale(0)
    }
    50% {
        opacity: 1
    }
}

@-o-keyframes spinner-grow {
    0% {
        -o-transform: scale(0);
        transform: scale(0)
    }
    50% {
        opacity: 1
    }
}

@keyframes spinner-grow {
    0% {
        -webkit-transform: scale(0);
        -o-transform: scale(0);
        transform: scale(0)
    }
    50% {
        opacity: 1
    }
}

.spinner-grow {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    vertical-align: text-bottom;
    background-color: currentColor;
    border-radius: 50%;
    opacity: 0;
    -webkit-animation: spinner-grow .75s linear infinite;
    -o-animation: spinner-grow .75s linear infinite;
    animation: spinner-grow .75s linear infinite
}

.spinner-grow-sm {
    width: 1rem;
    height: 1rem
}

.align-baseline {
    vertical-align: baseline!important
}

.align-top {
    vertical-align: top!important
}

.align-middle {
    vertical-align: middle!important
}

.align-bottom {
    vertical-align: bottom!important
}

.align-text-bottom {
    vertical-align: text-bottom!important
}

.align-text-top {
    vertical-align: text-top!important
}

.bg-primary {
    background-color: #714cdf!important
}

a.bg-primary:focus,
a.bg-primary:hover,
button.bg-primary:focus,
button.bg-primary:hover {
    background-color: #5126d2!important
}

.bg-secondary {
    background-color: #16a4de!important
}

a.bg-secondary:focus,
a.bg-secondary:hover,
button.bg-secondary:focus,
button.bg-secondary:hover {
    background-color: #1182b0!important
}

.bg-success {
    background-color: #17b06b!important
}

a.bg-success:focus,
a.bg-success:hover,
button.bg-success:focus,
button.bg-success:hover {
    background-color: #118350!important
}

.bg-info {
    background-color: #2983fe!important
}

a.bg-info:focus,
a.bg-info:hover,
button.bg-info:focus,
button.bg-info:hover {
    background-color: #0167f3!important
}

.bg-warning {
    background-color: #f97515!important
}

a.bg-warning:focus,
a.bg-warning:hover,
button.bg-warning:focus,
button.bg-warning:hover {
    background-color: #d65d05!important
}

.bg-danger {
    background-color: #ef121b!important
}

a.bg-danger:focus,
a.bg-danger:hover,
button.bg-danger:focus,
button.bg-danger:hover {
    background-color: #ff0931!important
}

.bg-light {
    background-color: #dbebfb!important
}

a.bg-light:focus,
a.bg-light:hover,
button.bg-light:focus,
button.bg-light:hover {
    background-color: #add2f6!important
}

.bg-dark {
    background-color: #32334a!important
}

a.bg-dark:focus,
a.bg-dark:hover,
button.bg-dark:focus,
button.bg-dark:hover {
    background-color: #1d1e2c!important
}

.bg-white {
    background-color: #fff!important
}

.bg-transparent {
    background-color: transparent!important
}

.border {
    border: 1px solid #28293e!important
}

.border-top {
    border-top: 1px solid #28293e!important
}

.border-right {
    border-right: 1px solid #28293e!important
}

.border-bottom {
    border-bottom: 1px solid #28293e!important
}

.border-left {
    border-left: 1px solid #28293e!important
}

.border-0 {
    border: 0!important
}

.border-top-0 {
    border-top: 0!important
}

.border-right-0 {
    border-right: 0!important
}

.border-bottom-0 {
    border-bottom: 0!important
}

.border-left-0 {
    border-left: 0!important
}

.border-primary {
    border-color: #714cdf!important
}

.border-secondary {
    border-color: #16a4de!important
}

.border-success {
    border-color: #17b06b!important
}

.border-info {
    border-color: #2983fe!important
}

.border-warning {
    border-color: #f97515!important
}

.border-danger {
    border-color: #ef121b!important
}

.border-light {
    border-color: #dbebfb!important
}

.border-dark {
    border-color: #32334a!important
}

.border-white {
    border-color: #fff!important
}

.rounded-sm {
    border-radius: .2rem!important
}

.rounded {
    border-radius: 6px!important
}

.rounded-top {
    border-top-left-radius: 6px!important;
    border-top-right-radius: 6px!important
}

.rounded-right {
    border-top-right-radius: 6px!important;
    border-bottom-right-radius: 6px!important
}

.rounded-bottom {
    border-bottom-right-radius: 6px!important;
    border-bottom-left-radius: 6px!important
}

.rounded-left {
    border-top-left-radius: 6px!important;
    border-bottom-left-radius: 6px!important
}

.rounded-lg {
    border-radius: 6px!important
}

.rounded-circle {
    border-radius: 50%!important
}

.rounded-pill {
    border-radius: 50rem!important
}

.rounded-0 {
    border-radius: 0!important
}

.clearfix::after {
    display: block;
    clear: both;
    content: ""
}

.d-none {
    display: none!important
}

.d-inline {
    display: inline!important
}

.d-inline-block {
    display: inline-block!important
}

.d-block {
    display: block!important
}

.d-table {
    display: table!important
}

.d-table-row {
    display: table-row!important
}

.d-table-cell {
    display: table-cell!important
}

.d-flex {
    display: -webkit-box!important;
    display: -webkit-flex!important;
    display: -ms-flexbox!important;
    display: flex!important
}

.d-inline-flex {
    display: -webkit-inline-box!important;
    display: -webkit-inline-flex!important;
    display: -ms-inline-flexbox!important;
    display: inline-flex!important
}

@media (min-width:576px) {
    .d-sm-none {
        display: none!important
    }
    .d-sm-inline {
        display: inline!important
    }
    .d-sm-inline-block {
        display: inline-block!important
    }
    .d-sm-block {
        display: block!important
    }
    .d-sm-table {
        display: table!important
    }
    .d-sm-table-row {
        display: table-row!important
    }
    .d-sm-table-cell {
        display: table-cell!important
    }
    .d-sm-flex {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important
    }
    .d-sm-inline-flex {
        display: -webkit-inline-box!important;
        display: -webkit-inline-flex!important;
        display: -ms-inline-flexbox!important;
        display: inline-flex!important
    }
}

@media (min-width:768px) {
    .d-md-none {
        display: none!important
    }
    .d-md-inline {
        display: inline!important
    }
    .d-md-inline-block {
        display: inline-block!important
    }
    .d-md-block {
        display: block!important
    }
    .d-md-table {
        display: table!important
    }
    .d-md-table-row {
        display: table-row!important
    }
    .d-md-table-cell {
        display: table-cell!important
    }
    .d-md-flex {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important
    }
    .d-md-inline-flex {
        display: -webkit-inline-box!important;
        display: -webkit-inline-flex!important;
        display: -ms-inline-flexbox!important;
        display: inline-flex!important
    }
}

@media (min-width:992px) {
    .d-lg-none {
        display: none!important
    }
    .d-lg-inline {
        display: inline!important
    }
    .d-lg-inline-block {
        display: inline-block!important
    }
    .d-lg-block {
        display: block!important
    }
    .d-lg-table {
        display: table!important
    }
    .d-lg-table-row {
        display: table-row!important
    }
    .d-lg-table-cell {
        display: table-cell!important
    }
    .d-lg-flex {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important
    }
    .d-lg-inline-flex {
        display: -webkit-inline-box!important;
        display: -webkit-inline-flex!important;
        display: -ms-inline-flexbox!important;
        display: inline-flex!important
    }
}

@media (min-width:1200px) {
    .d-xl-none {
        display: none!important
    }
    .d-xl-inline {
        display: inline!important
    }
    .d-xl-inline-block {
        display: inline-block!important
    }
    .d-xl-block {
        display: block!important
    }
    .d-xl-table {
        display: table!important
    }
    .d-xl-table-row {
        display: table-row!important
    }
    .d-xl-table-cell {
        display: table-cell!important
    }
    .d-xl-flex {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important
    }
    .d-xl-inline-flex {
        display: -webkit-inline-box!important;
        display: -webkit-inline-flex!important;
        display: -ms-inline-flexbox!important;
        display: inline-flex!important
    }
}

@media print {
    .d-print-none {
        display: none!important
    }
    .d-print-inline {
        display: inline!important
    }
    .d-print-inline-block {
        display: inline-block!important
    }
    .d-print-block {
        display: block!important
    }
    .d-print-table {
        display: table!important
    }
    .d-print-table-row {
        display: table-row!important
    }
    .d-print-table-cell {
        display: table-cell!important
    }
    .d-print-flex {
        display: -webkit-box!important;
        display: -webkit-flex!important;
        display: -ms-flexbox!important;
        display: flex!important
    }
    .d-print-inline-flex {
        display: -webkit-inline-box!important;
        display: -webkit-inline-flex!important;
        display: -ms-inline-flexbox!important;
        display: inline-flex!important
    }
}

.embed-responsive {
    position: relative;
    display: block;
    width: 100%;
    padding: 0;
    overflow: hidden
}

.embed-responsive::before {
    display: block;
    content: ""
}

.embed-responsive .embed-responsive-item,
.embed-responsive embed,
.embed-responsive iframe,
.embed-responsive object,
.embed-responsive video {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0
}

.embed-responsive-21by9::before {
    padding-top: 42.85714%
}

.embed-responsive-16by9::before {
    padding-top: 56.25%
}

.embed-responsive-4by3::before {
    padding-top: 75%
}

.embed-responsive-1by1::before {
    padding-top: 100%
}

.flex-row {
    -webkit-box-orient: horizontal!important;
    -webkit-box-direction: normal!important;
    -webkit-flex-direction: row!important;
    -ms-flex-direction: row!important;
    flex-direction: row!important
}

.flex-column {
    -webkit-box-orient: vertical!important;
    -webkit-box-direction: normal!important;
    -webkit-flex-direction: column!important;
    -ms-flex-direction: column!important;
    flex-direction: column!important
}

.flex-row-reverse {
    -webkit-box-orient: horizontal!important;
    -webkit-box-direction: reverse!important;
    -webkit-flex-direction: row-reverse!important;
    -ms-flex-direction: row-reverse!important;
    flex-direction: row-reverse!important
}

.flex-column-reverse {
    -webkit-box-orient: vertical!important;
    -webkit-box-direction: reverse!important;
    -webkit-flex-direction: column-reverse!important;
    -ms-flex-direction: column-reverse!important;
    flex-direction: column-reverse!important
}

.flex-wrap {
    -webkit-flex-wrap: wrap!important;
    -ms-flex-wrap: wrap!important;
    flex-wrap: wrap!important
}

.flex-nowrap {
    -webkit-flex-wrap: nowrap!important;
    -ms-flex-wrap: nowrap!important;
    flex-wrap: nowrap!important
}

.flex-wrap-reverse {
    -webkit-flex-wrap: wrap-reverse!important;
    -ms-flex-wrap: wrap-reverse!important;
    flex-wrap: wrap-reverse!important
}

.flex-fill {
    -webkit-box-flex: 1!important;
    -webkit-flex: 1 1 auto!important;
    -ms-flex: 1 1 auto!important;
    flex: 1 1 auto!important
}

.flex-grow-0 {
    -webkit-box-flex: 0!important;
    -webkit-flex-grow: 0!important;
    -ms-flex-positive: 0!important;
    flex-grow: 0!important
}

.flex-grow-1 {
    -webkit-box-flex: 1!important;
    -webkit-flex-grow: 1!important;
    -ms-flex-positive: 1!important;
    flex-grow: 1!important
}

.flex-shrink-0 {
    -webkit-flex-shrink: 0!important;
    -ms-flex-negative: 0!important;
    flex-shrink: 0!important
}

.flex-shrink-1 {
    -webkit-flex-shrink: 1!important;
    -ms-flex-negative: 1!important;
    flex-shrink: 1!important
}

.justify-content-start {
    -webkit-box-pack: start!important;
    -webkit-justify-content: flex-start!important;
    -ms-flex-pack: start!important;
    justify-content: flex-start!important
}

.justify-content-end {
    -webkit-box-pack: end!important;
    -webkit-justify-content: flex-end!important;
    -ms-flex-pack: end!important;
    justify-content: flex-end!important
}

.justify-content-center {
    -webkit-box-pack: center!important;
    -webkit-justify-content: center!important;
    -ms-flex-pack: center!important;
    justify-content: center!important
}

.justify-content-between {
    -webkit-box-pack: justify!important;
    -webkit-justify-content: space-between!important;
    -ms-flex-pack: justify!important;
    justify-content: space-between!important
}

.justify-content-around {
    -webkit-justify-content: space-around!important;
    -ms-flex-pack: distribute!important;
    justify-content: space-around!important
}

.align-items-start {
    -webkit-box-align: start!important;
    -webkit-align-items: flex-start!important;
    -ms-flex-align: start!important;
    align-items: flex-start!important
}

.align-items-end {
    -webkit-box-align: end!important;
    -webkit-align-items: flex-end!important;
    -ms-flex-align: end!important;
    align-items: flex-end!important
}

.align-items-center {
    -webkit-box-align: center!important;
    -webkit-align-items: center!important;
    -ms-flex-align: center!important;
    align-items: center!important
}

.align-items-baseline {
    -webkit-box-align: baseline!important;
    -webkit-align-items: baseline!important;
    -ms-flex-align: baseline!important;
    align-items: baseline!important
}

.align-items-stretch {
    -webkit-box-align: stretch!important;
    -webkit-align-items: stretch!important;
    -ms-flex-align: stretch!important;
    align-items: stretch!important
}

.align-content-start {
    -webkit-align-content: flex-start!important;
    -ms-flex-line-pack: start!important;
    align-content: flex-start!important
}

.align-content-end {
    -webkit-align-content: flex-end!important;
    -ms-flex-line-pack: end!important;
    align-content: flex-end!important
}

.align-content-center {
    -webkit-align-content: center!important;
    -ms-flex-line-pack: center!important;
    align-content: center!important
}

.align-content-between {
    -webkit-align-content: space-between!important;
    -ms-flex-line-pack: justify!important;
    align-content: space-between!important
}

.align-content-around {
    -webkit-align-content: space-around!important;
    -ms-flex-line-pack: distribute!important;
    align-content: space-around!important
}

.align-content-stretch {
    -webkit-align-content: stretch!important;
    -ms-flex-line-pack: stretch!important;
    align-content: stretch!important
}

.align-self-auto {
    -webkit-align-self: auto!important;
    -ms-flex-item-align: auto!important;
    align-self: auto!important
}

.align-self-start {
    -webkit-align-self: flex-start!important;
    -ms-flex-item-align: start!important;
    align-self: flex-start!important
}

.align-self-end {
    -webkit-align-self: flex-end!important;
    -ms-flex-item-align: end!important;
    align-self: flex-end!important
}

.align-self-center {
    -webkit-align-self: center!important;
    -ms-flex-item-align: center!important;
    align-self: center!important
}

.align-self-baseline {
    -webkit-align-self: baseline!important;
    -ms-flex-item-align: baseline!important;
    align-self: baseline!important
}

.align-self-stretch {
    -webkit-align-self: stretch!important;
    -ms-flex-item-align: stretch!important;
    align-self: stretch!important
}

@media (min-width:576px) {
    .flex-sm-row {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: row!important;
        -ms-flex-direction: row!important;
        flex-direction: row!important
    }
    .flex-sm-column {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: column!important;
        -ms-flex-direction: column!important;
        flex-direction: column!important
    }
    .flex-sm-row-reverse {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: row-reverse!important;
        -ms-flex-direction: row-reverse!important;
        flex-direction: row-reverse!important
    }
    .flex-sm-column-reverse {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: column-reverse!important;
        -ms-flex-direction: column-reverse!important;
        flex-direction: column-reverse!important
    }
    .flex-sm-wrap {
        -webkit-flex-wrap: wrap!important;
        -ms-flex-wrap: wrap!important;
        flex-wrap: wrap!important
    }
    .flex-sm-nowrap {
        -webkit-flex-wrap: nowrap!important;
        -ms-flex-wrap: nowrap!important;
        flex-wrap: nowrap!important
    }
    .flex-sm-wrap-reverse {
        -webkit-flex-wrap: wrap-reverse!important;
        -ms-flex-wrap: wrap-reverse!important;
        flex-wrap: wrap-reverse!important
    }
    .flex-sm-fill {
        -webkit-box-flex: 1!important;
        -webkit-flex: 1 1 auto!important;
        -ms-flex: 1 1 auto!important;
        flex: 1 1 auto!important
    }
    .flex-sm-grow-0 {
        -webkit-box-flex: 0!important;
        -webkit-flex-grow: 0!important;
        -ms-flex-positive: 0!important;
        flex-grow: 0!important
    }
    .flex-sm-grow-1 {
        -webkit-box-flex: 1!important;
        -webkit-flex-grow: 1!important;
        -ms-flex-positive: 1!important;
        flex-grow: 1!important
    }
    .flex-sm-shrink-0 {
        -webkit-flex-shrink: 0!important;
        -ms-flex-negative: 0!important;
        flex-shrink: 0!important
    }
    .flex-sm-shrink-1 {
        -webkit-flex-shrink: 1!important;
        -ms-flex-negative: 1!important;
        flex-shrink: 1!important
    }
    .justify-content-sm-start {
        -webkit-box-pack: start!important;
        -webkit-justify-content: flex-start!important;
        -ms-flex-pack: start!important;
        justify-content: flex-start!important
    }
    .justify-content-sm-end {
        -webkit-box-pack: end!important;
        -webkit-justify-content: flex-end!important;
        -ms-flex-pack: end!important;
        justify-content: flex-end!important
    }
    .justify-content-sm-center {
        -webkit-box-pack: center!important;
        -webkit-justify-content: center!important;
        -ms-flex-pack: center!important;
        justify-content: center!important
    }
    .justify-content-sm-between {
        -webkit-box-pack: justify!important;
        -webkit-justify-content: space-between!important;
        -ms-flex-pack: justify!important;
        justify-content: space-between!important
    }
    .justify-content-sm-around {
        -webkit-justify-content: space-around!important;
        -ms-flex-pack: distribute!important;
        justify-content: space-around!important
    }
    .align-items-sm-start {
        -webkit-box-align: start!important;
        -webkit-align-items: flex-start!important;
        -ms-flex-align: start!important;
        align-items: flex-start!important
    }
    .align-items-sm-end {
        -webkit-box-align: end!important;
        -webkit-align-items: flex-end!important;
        -ms-flex-align: end!important;
        align-items: flex-end!important
    }
    .align-items-sm-center {
        -webkit-box-align: center!important;
        -webkit-align-items: center!important;
        -ms-flex-align: center!important;
        align-items: center!important
    }
    .align-items-sm-baseline {
        -webkit-box-align: baseline!important;
        -webkit-align-items: baseline!important;
        -ms-flex-align: baseline!important;
        align-items: baseline!important
    }
    .align-items-sm-stretch {
        -webkit-box-align: stretch!important;
        -webkit-align-items: stretch!important;
        -ms-flex-align: stretch!important;
        align-items: stretch!important
    }
    .align-content-sm-start {
        -webkit-align-content: flex-start!important;
        -ms-flex-line-pack: start!important;
        align-content: flex-start!important
    }
    .align-content-sm-end {
        -webkit-align-content: flex-end!important;
        -ms-flex-line-pack: end!important;
        align-content: flex-end!important
    }
    .align-content-sm-center {
        -webkit-align-content: center!important;
        -ms-flex-line-pack: center!important;
        align-content: center!important
    }
    .align-content-sm-between {
        -webkit-align-content: space-between!important;
        -ms-flex-line-pack: justify!important;
        align-content: space-between!important
    }
    .align-content-sm-around {
        -webkit-align-content: space-around!important;
        -ms-flex-line-pack: distribute!important;
        align-content: space-around!important
    }
    .align-content-sm-stretch {
        -webkit-align-content: stretch!important;
        -ms-flex-line-pack: stretch!important;
        align-content: stretch!important
    }
    .align-self-sm-auto {
        -webkit-align-self: auto!important;
        -ms-flex-item-align: auto!important;
        align-self: auto!important
    }
    .align-self-sm-start {
        -webkit-align-self: flex-start!important;
        -ms-flex-item-align: start!important;
        align-self: flex-start!important
    }
    .align-self-sm-end {
        -webkit-align-self: flex-end!important;
        -ms-flex-item-align: end!important;
        align-self: flex-end!important
    }
    .align-self-sm-center {
        -webkit-align-self: center!important;
        -ms-flex-item-align: center!important;
        align-self: center!important
    }
    .align-self-sm-baseline {
        -webkit-align-self: baseline!important;
        -ms-flex-item-align: baseline!important;
        align-self: baseline!important
    }
    .align-self-sm-stretch {
        -webkit-align-self: stretch!important;
        -ms-flex-item-align: stretch!important;
        align-self: stretch!important
    }
}

@media (min-width:768px) {
    .flex-md-row {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: row!important;
        -ms-flex-direction: row!important;
        flex-direction: row!important
    }
    .flex-md-column {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: column!important;
        -ms-flex-direction: column!important;
        flex-direction: column!important
    }
    .flex-md-row-reverse {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: row-reverse!important;
        -ms-flex-direction: row-reverse!important;
        flex-direction: row-reverse!important
    }
    .flex-md-column-reverse {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: column-reverse!important;
        -ms-flex-direction: column-reverse!important;
        flex-direction: column-reverse!important
    }
    .flex-md-wrap {
        -webkit-flex-wrap: wrap!important;
        -ms-flex-wrap: wrap!important;
        flex-wrap: wrap!important
    }
    .flex-md-nowrap {
        -webkit-flex-wrap: nowrap!important;
        -ms-flex-wrap: nowrap!important;
        flex-wrap: nowrap!important
    }
    .flex-md-wrap-reverse {
        -webkit-flex-wrap: wrap-reverse!important;
        -ms-flex-wrap: wrap-reverse!important;
        flex-wrap: wrap-reverse!important
    }
    .flex-md-fill {
        -webkit-box-flex: 1!important;
        -webkit-flex: 1 1 auto!important;
        -ms-flex: 1 1 auto!important;
        flex: 1 1 auto!important
    }
    .flex-md-grow-0 {
        -webkit-box-flex: 0!important;
        -webkit-flex-grow: 0!important;
        -ms-flex-positive: 0!important;
        flex-grow: 0!important
    }
    .flex-md-grow-1 {
        -webkit-box-flex: 1!important;
        -webkit-flex-grow: 1!important;
        -ms-flex-positive: 1!important;
        flex-grow: 1!important
    }
    .flex-md-shrink-0 {
        -webkit-flex-shrink: 0!important;
        -ms-flex-negative: 0!important;
        flex-shrink: 0!important
    }
    .flex-md-shrink-1 {
        -webkit-flex-shrink: 1!important;
        -ms-flex-negative: 1!important;
        flex-shrink: 1!important
    }
    .justify-content-md-start {
        -webkit-box-pack: start!important;
        -webkit-justify-content: flex-start!important;
        -ms-flex-pack: start!important;
        justify-content: flex-start!important
    }
    .justify-content-md-end {
        -webkit-box-pack: end!important;
        -webkit-justify-content: flex-end!important;
        -ms-flex-pack: end!important;
        justify-content: flex-end!important
    }
    .justify-content-md-center {
        -webkit-box-pack: center!important;
        -webkit-justify-content: center!important;
        -ms-flex-pack: center!important;
        justify-content: center!important
    }
    .justify-content-md-between {
        -webkit-box-pack: justify!important;
        -webkit-justify-content: space-between!important;
        -ms-flex-pack: justify!important;
        justify-content: space-between!important
    }
    .justify-content-md-around {
        -webkit-justify-content: space-around!important;
        -ms-flex-pack: distribute!important;
        justify-content: space-around!important
    }
    .align-items-md-start {
        -webkit-box-align: start!important;
        -webkit-align-items: flex-start!important;
        -ms-flex-align: start!important;
        align-items: flex-start!important
    }
    .align-items-md-end {
        -webkit-box-align: end!important;
        -webkit-align-items: flex-end!important;
        -ms-flex-align: end!important;
        align-items: flex-end!important
    }
    .align-items-md-center {
        -webkit-box-align: center!important;
        -webkit-align-items: center!important;
        -ms-flex-align: center!important;
        align-items: center!important
    }
    .align-items-md-baseline {
        -webkit-box-align: baseline!important;
        -webkit-align-items: baseline!important;
        -ms-flex-align: baseline!important;
        align-items: baseline!important
    }
    .align-items-md-stretch {
        -webkit-box-align: stretch!important;
        -webkit-align-items: stretch!important;
        -ms-flex-align: stretch!important;
        align-items: stretch!important
    }
    .align-content-md-start {
        -webkit-align-content: flex-start!important;
        -ms-flex-line-pack: start!important;
        align-content: flex-start!important
    }
    .align-content-md-end {
        -webkit-align-content: flex-end!important;
        -ms-flex-line-pack: end!important;
        align-content: flex-end!important
    }
    .align-content-md-center {
        -webkit-align-content: center!important;
        -ms-flex-line-pack: center!important;
        align-content: center!important
    }
    .align-content-md-between {
        -webkit-align-content: space-between!important;
        -ms-flex-line-pack: justify!important;
        align-content: space-between!important
    }
    .align-content-md-around {
        -webkit-align-content: space-around!important;
        -ms-flex-line-pack: distribute!important;
        align-content: space-around!important
    }
    .align-content-md-stretch {
        -webkit-align-content: stretch!important;
        -ms-flex-line-pack: stretch!important;
        align-content: stretch!important
    }
    .align-self-md-auto {
        -webkit-align-self: auto!important;
        -ms-flex-item-align: auto!important;
        align-self: auto!important
    }
    .align-self-md-start {
        -webkit-align-self: flex-start!important;
        -ms-flex-item-align: start!important;
        align-self: flex-start!important
    }
    .align-self-md-end {
        -webkit-align-self: flex-end!important;
        -ms-flex-item-align: end!important;
        align-self: flex-end!important
    }
    .align-self-md-center {
        -webkit-align-self: center!important;
        -ms-flex-item-align: center!important;
        align-self: center!important
    }
    .align-self-md-baseline {
        -webkit-align-self: baseline!important;
        -ms-flex-item-align: baseline!important;
        align-self: baseline!important
    }
    .align-self-md-stretch {
        -webkit-align-self: stretch!important;
        -ms-flex-item-align: stretch!important;
        align-self: stretch!important
    }
}

@media (min-width:992px) {
    .flex-lg-row {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: row!important;
        -ms-flex-direction: row!important;
        flex-direction: row!important
    }
    .flex-lg-column {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: column!important;
        -ms-flex-direction: column!important;
        flex-direction: column!important
    }
    .flex-lg-row-reverse {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: row-reverse!important;
        -ms-flex-direction: row-reverse!important;
        flex-direction: row-reverse!important
    }
    .flex-lg-column-reverse {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: column-reverse!important;
        -ms-flex-direction: column-reverse!important;
        flex-direction: column-reverse!important
    }
    .flex-lg-wrap {
        -webkit-flex-wrap: wrap!important;
        -ms-flex-wrap: wrap!important;
        flex-wrap: wrap!important
    }
    .flex-lg-nowrap {
        -webkit-flex-wrap: nowrap!important;
        -ms-flex-wrap: nowrap!important;
        flex-wrap: nowrap!important
    }
    .flex-lg-wrap-reverse {
        -webkit-flex-wrap: wrap-reverse!important;
        -ms-flex-wrap: wrap-reverse!important;
        flex-wrap: wrap-reverse!important
    }
    .flex-lg-fill {
        -webkit-box-flex: 1!important;
        -webkit-flex: 1 1 auto!important;
        -ms-flex: 1 1 auto!important;
        flex: 1 1 auto!important
    }
    .flex-lg-grow-0 {
        -webkit-box-flex: 0!important;
        -webkit-flex-grow: 0!important;
        -ms-flex-positive: 0!important;
        flex-grow: 0!important
    }
    .flex-lg-grow-1 {
        -webkit-box-flex: 1!important;
        -webkit-flex-grow: 1!important;
        -ms-flex-positive: 1!important;
        flex-grow: 1!important
    }
    .flex-lg-shrink-0 {
        -webkit-flex-shrink: 0!important;
        -ms-flex-negative: 0!important;
        flex-shrink: 0!important
    }
    .flex-lg-shrink-1 {
        -webkit-flex-shrink: 1!important;
        -ms-flex-negative: 1!important;
        flex-shrink: 1!important
    }
    .justify-content-lg-start {
        -webkit-box-pack: start!important;
        -webkit-justify-content: flex-start!important;
        -ms-flex-pack: start!important;
        justify-content: flex-start!important
    }
    .justify-content-lg-end {
        -webkit-box-pack: end!important;
        -webkit-justify-content: flex-end!important;
        -ms-flex-pack: end!important;
        justify-content: flex-end!important
    }
    .justify-content-lg-center {
        -webkit-box-pack: center!important;
        -webkit-justify-content: center!important;
        -ms-flex-pack: center!important;
        justify-content: center!important
    }
    .justify-content-lg-between {
        -webkit-box-pack: justify!important;
        -webkit-justify-content: space-between!important;
        -ms-flex-pack: justify!important;
        justify-content: space-between!important
    }
    .justify-content-lg-around {
        -webkit-justify-content: space-around!important;
        -ms-flex-pack: distribute!important;
        justify-content: space-around!important
    }
    .align-items-lg-start {
        -webkit-box-align: start!important;
        -webkit-align-items: flex-start!important;
        -ms-flex-align: start!important;
        align-items: flex-start!important
    }
    .align-items-lg-end {
        -webkit-box-align: end!important;
        -webkit-align-items: flex-end!important;
        -ms-flex-align: end!important;
        align-items: flex-end!important
    }
    .align-items-lg-center {
        -webkit-box-align: center!important;
        -webkit-align-items: center!important;
        -ms-flex-align: center!important;
        align-items: center!important
    }
    .align-items-lg-baseline {
        -webkit-box-align: baseline!important;
        -webkit-align-items: baseline!important;
        -ms-flex-align: baseline!important;
        align-items: baseline!important
    }
    .align-items-lg-stretch {
        -webkit-box-align: stretch!important;
        -webkit-align-items: stretch!important;
        -ms-flex-align: stretch!important;
        align-items: stretch!important
    }
    .align-content-lg-start {
        -webkit-align-content: flex-start!important;
        -ms-flex-line-pack: start!important;
        align-content: flex-start!important
    }
    .align-content-lg-end {
        -webkit-align-content: flex-end!important;
        -ms-flex-line-pack: end!important;
        align-content: flex-end!important
    }
    .align-content-lg-center {
        -webkit-align-content: center!important;
        -ms-flex-line-pack: center!important;
        align-content: center!important
    }
    .align-content-lg-between {
        -webkit-align-content: space-between!important;
        -ms-flex-line-pack: justify!important;
        align-content: space-between!important
    }
    .align-content-lg-around {
        -webkit-align-content: space-around!important;
        -ms-flex-line-pack: distribute!important;
        align-content: space-around!important
    }
    .align-content-lg-stretch {
        -webkit-align-content: stretch!important;
        -ms-flex-line-pack: stretch!important;
        align-content: stretch!important
    }
    .align-self-lg-auto {
        -webkit-align-self: auto!important;
        -ms-flex-item-align: auto!important;
        align-self: auto!important
    }
    .align-self-lg-start {
        -webkit-align-self: flex-start!important;
        -ms-flex-item-align: start!important;
        align-self: flex-start!important
    }
    .align-self-lg-end {
        -webkit-align-self: flex-end!important;
        -ms-flex-item-align: end!important;
        align-self: flex-end!important
    }
    .align-self-lg-center {
        -webkit-align-self: center!important;
        -ms-flex-item-align: center!important;
        align-self: center!important
    }
    .align-self-lg-baseline {
        -webkit-align-self: baseline!important;
        -ms-flex-item-align: baseline!important;
        align-self: baseline!important
    }
    .align-self-lg-stretch {
        -webkit-align-self: stretch!important;
        -ms-flex-item-align: stretch!important;
        align-self: stretch!important
    }
}

@media (min-width:1200px) {
    .flex-xl-row {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: row!important;
        -ms-flex-direction: row!important;
        flex-direction: row!important
    }
    .flex-xl-column {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: normal!important;
        -webkit-flex-direction: column!important;
        -ms-flex-direction: column!important;
        flex-direction: column!important
    }
    .flex-xl-row-reverse {
        -webkit-box-orient: horizontal!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: row-reverse!important;
        -ms-flex-direction: row-reverse!important;
        flex-direction: row-reverse!important
    }
    .flex-xl-column-reverse {
        -webkit-box-orient: vertical!important;
        -webkit-box-direction: reverse!important;
        -webkit-flex-direction: column-reverse!important;
        -ms-flex-direction: column-reverse!important;
        flex-direction: column-reverse!important
    }
    .flex-xl-wrap {
        -webkit-flex-wrap: wrap!important;
        -ms-flex-wrap: wrap!important;
        flex-wrap: wrap!important
    }
    .flex-xl-nowrap {
        -webkit-flex-wrap: nowrap!important;
        -ms-flex-wrap: nowrap!important;
        flex-wrap: nowrap!important
    }
    .flex-xl-wrap-reverse {
        -webkit-flex-wrap: wrap-reverse!important;
        -ms-flex-wrap: wrap-reverse!important;
        flex-wrap: wrap-reverse!important
    }
    .flex-xl-fill {
        -webkit-box-flex: 1!important;
        -webkit-flex: 1 1 auto!important;
        -ms-flex: 1 1 auto!important;
        flex: 1 1 auto!important
    }
    .flex-xl-grow-0 {
        -webkit-box-flex: 0!important;
        -webkit-flex-grow: 0!important;
        -ms-flex-positive: 0!important;
        flex-grow: 0!important
    }
    .flex-xl-grow-1 {
        -webkit-box-flex: 1!important;
        -webkit-flex-grow: 1!important;
        -ms-flex-positive: 1!important;
        flex-grow: 1!important
    }
    .flex-xl-shrink-0 {
        -webkit-flex-shrink: 0!important;
        -ms-flex-negative: 0!important;
        flex-shrink: 0!important
    }
    .flex-xl-shrink-1 {
        -webkit-flex-shrink: 1!important;
        -ms-flex-negative: 1!important;
        flex-shrink: 1!important
    }
    .justify-content-xl-start {
        -webkit-box-pack: start!important;
        -webkit-justify-content: flex-start!important;
        -ms-flex-pack: start!important;
        justify-content: flex-start!important
    }
    .justify-content-xl-end {
        -webkit-box-pack: end!important;
        -webkit-justify-content: flex-end!important;
        -ms-flex-pack: end!important;
        justify-content: flex-end!important
    }
    .justify-content-xl-center {
        -webkit-box-pack: center!important;
        -webkit-justify-content: center!important;
        -ms-flex-pack: center!important;
        justify-content: center!important
    }
    .justify-content-xl-between {
        -webkit-box-pack: justify!important;
        -webkit-justify-content: space-between!important;
        -ms-flex-pack: justify!important;
        justify-content: space-between!important
    }
    .justify-content-xl-around {
        -webkit-justify-content: space-around!important;
        -ms-flex-pack: distribute!important;
        justify-content: space-around!important
    }
    .align-items-xl-start {
        -webkit-box-align: start!important;
        -webkit-align-items: flex-start!important;
        -ms-flex-align: start!important;
        align-items: flex-start!important
    }
    .align-items-xl-end {
        -webkit-box-align: end!important;
        -webkit-align-items: flex-end!important;
        -ms-flex-align: end!important;
        align-items: flex-end!important
    }
    .align-items-xl-center {
        -webkit-box-align: center!important;
        -webkit-align-items: center!important;
        -ms-flex-align: center!important;
        align-items: center!important
    }
    .align-items-xl-baseline {
        -webkit-box-align: baseline!important;
        -webkit-align-items: baseline!important;
        -ms-flex-align: baseline!important;
        align-items: baseline!important
    }
    .align-items-xl-stretch {
        -webkit-box-align: stretch!important;
        -webkit-align-items: stretch!important;
        -ms-flex-align: stretch!important;
        align-items: stretch!important
    }
    .align-content-xl-start {
        -webkit-align-content: flex-start!important;
        -ms-flex-line-pack: start!important;
        align-content: flex-start!important
    }
    .align-content-xl-end {
        -webkit-align-content: flex-end!important;
        -ms-flex-line-pack: end!important;
        align-content: flex-end!important
    }
    .align-content-xl-center {
        -webkit-align-content: center!important;
        -ms-flex-line-pack: center!important;
        align-content: center!important
    }
    .align-content-xl-between {
        -webkit-align-content: space-between!important;
        -ms-flex-line-pack: justify!important;
        align-content: space-between!important
    }
    .align-content-xl-around {
        -webkit-align-content: space-around!important;
        -ms-flex-line-pack: distribute!important;
        align-content: space-around!important
    }
    .align-content-xl-stretch {
        -webkit-align-content: stretch!important;
        -ms-flex-line-pack: stretch!important;
        align-content: stretch!important
    }
    .align-self-xl-auto {
        -webkit-align-self: auto!important;
        -ms-flex-item-align: auto!important;
        align-self: auto!important
    }
    .align-self-xl-start {
        -webkit-align-self: flex-start!important;
        -ms-flex-item-align: start!important;
        align-self: flex-start!important
    }
    .align-self-xl-end {
        -webkit-align-self: flex-end!important;
        -ms-flex-item-align: end!important;
        align-self: flex-end!important
    }
    .align-self-xl-center {
        -webkit-align-self: center!important;
        -ms-flex-item-align: center!important;
        align-self: center!important
    }
    .align-self-xl-baseline {
        -webkit-align-self: baseline!important;
        -ms-flex-item-align: baseline!important;
        align-self: baseline!important
    }
    .align-self-xl-stretch {
        -webkit-align-self: stretch!important;
        -ms-flex-item-align: stretch!important;
        align-self: stretch!important
    }
}

.float-left {
    float: left!important
}

.float-right {
    float: right!important
}

.float-none {
    float: none!important
}

@media (min-width:576px) {
    .float-sm-left {
        float: left!important
    }
    .float-sm-right {
        float: right!important
    }
    .float-sm-none {
        float: none!important
    }
}

@media (min-width:768px) {
    .float-md-left {
        float: left!important
    }
    .float-md-right {
        float: right!important
    }
    .float-md-none {
        float: none!important
    }
}

@media (min-width:992px) {
    .float-lg-left {
        float: left!important
    }
    .float-lg-right {
        float: right!important
    }
    .float-lg-none {
        float: none!important
    }
}

@media (min-width:1200px) {
    .float-xl-left {
        float: left!important
    }
    .float-xl-right {
        float: right!important
    }
    .float-xl-none {
        float: none!important
    }
}

.overflow-auto {
    overflow: auto!important
}

.overflow-hidden {
    overflow: hidden!important
}

.position-static {
    position: static!important
}

.position-relative {
    position: relative!important
}

.position-absolute {
    position: absolute!important
}

.position-fixed {
    position: fixed!important
}

.position-sticky {
    position: -webkit-sticky!important;
    position: sticky!important
}

.fixed-top {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030
}

.fixed-bottom {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1030
}

@supports ((position:-webkit-sticky) or (position:sticky)) {
    .sticky-top {
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        z-index: 1020
    }
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0
}

.sr-only-focusable:active,
.sr-only-focusable:focus {
    position: static;
    width: auto;
    height: auto;
    overflow: visible;
    clip: auto;
    white-space: normal
}

.shadow-sm {
    -webkit-box-shadow: 0 .125rem .25rem rgba(0, 0, 0, .075)!important;
    box-shadow: 0 .125rem .25rem rgba(0, 0, 0, .075)!important
}

.shadow {
    -webkit-box-shadow: 0 .5rem 1rem rgba(0, 0, 0, .15)!important;
    box-shadow: 0 .5rem 1rem rgba(0, 0, 0, .15)!important
}

.shadow-lg {
    -webkit-box-shadow: 0 1rem 3rem rgba(0, 0, 0, .175)!important;
    box-shadow: 0 1rem 3rem rgba(0, 0, 0, .175)!important
}

.shadow-none {
    -webkit-box-shadow: none!important;
    box-shadow: none!important
}

.w-25 {
    width: 25%!important
}

.w-50 {
    width: 50%!important
}

.w-75 {
    width: 75%!important
}

.w-100 {
    width: 100%!important
}

.w-auto {
    width: auto!important
}

.h-25 {
    height: 25%!important
}

.h-50 {
    height: 50%!important
}

.h-75 {
    height: 75%!important
}

.h-100 {
    height: 100%!important
}

.h-auto {
    height: auto!important
}

.mw-100 {
    max-width: 100%!important
}

.mh-100 {
    max-height: 100%!important
}

.min-vw-100 {
    min-width: 100vw!important
}

.min-vh-100 {
    min-height: 100vh!important
}

.vw-100 {
    width: 100vw!important
}

.vh-100 {
    height: 100vh!important
}

.stretched-link::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    pointer-events: auto;
    content: "";
    background-color: rgba(0, 0, 0, 0)
}

.m-0 {
    margin: 0!important
}

.mt-0,
.my-0 {
    margin-top: 0!important
}

.mr-0,
.mx-0 {
    margin-right: 0!important
}

.mb-0,
.my-0 {
    margin-bottom: 0!important
}

.ml-0,
.mx-0 {
    margin-left: 0!important
}

.m-1 {
    margin: .25rem!important
}

.mt-1,
.my-1 {
    margin-top: .25rem!important
}

.mr-1,
.mx-1 {
    margin-right: .25rem!important
}

.mb-1,
.my-1 {
    margin-bottom: .25rem!important
}

.ml-1,
.mx-1 {
    margin-left: .25rem!important
}

.m-2 {
    margin: .5rem!important
}

.mt-2,
.my-2 {
    margin-top: .5rem!important
}

.mr-2,
.mx-2 {
    margin-right: .5rem!important
}

.mb-2,
.my-2 {
    margin-bottom: .5rem!important
}

.ml-2,
.mx-2 {
    margin-left: .5rem!important
}

.m-3 {
    margin: 1rem!important
}

.mt-3,
.my-3 {
    margin-top: 1rem!important
}

.mr-3,
.mx-3 {
    margin-right: 1rem!important
}

.mb-3,
.my-3 {
    margin-bottom: 1rem!important
}

.ml-3,
.mx-3 {
    margin-left: 1rem!important
}

.m-4 {
    margin: 1.5rem!important
}

.mt-4,
.my-4 {
    margin-top: 1.5rem!important
}

.mr-4,
.mx-4 {
    margin-right: 1.5rem!important
}

.mb-4,
.my-4 {
    margin-bottom: 1.5rem!important
}

.ml-4,
.mx-4 {
    margin-left: 1.5rem!important
}

.m-5 {
    margin: 3rem!important
}

.mt-5,
.my-5 {
    margin-top: 3rem!important
}

.mr-5,
.mx-5 {
    margin-right: 3rem!important
}

.mb-5,
.my-5 {
    margin-bottom: 3rem!important
}

.ml-5,
.mx-5 {
    margin-left: 3rem!important
}

.p-0 {
    padding: 0!important
}

.pt-0,
.py-0 {
    padding-top: 0!important
}

.pr-0,
.px-0 {
    padding-right: 0!important
}

.pb-0,
.py-0 {
    padding-bottom: 0!important
}

.pl-0,
.px-0 {
    padding-left: 0!important
}

.p-1 {
    padding: .25rem!important
}

.pt-1,
.py-1 {
    padding-top: .25rem!important
}

.pr-1,
.px-1 {
    padding-right: .25rem!important
}

.pb-1,
.py-1 {
    padding-bottom: .25rem!important
}

.pl-1,
.px-1 {
    padding-left: .25rem!important
}

.p-2 {
    padding: .5rem!important
}

.pt-2,
.py-2 {
    padding-top: .5rem!important
}

.pr-2,
.px-2 {
    padding-right: .5rem!important
}

.pb-2,
.py-2 {
    padding-bottom: .5rem!important
}

.pl-2,
.px-2 {
    padding-left: .5rem!important
}

.p-3 {
    padding: 1rem!important
}

.pt-3,
.py-3 {
    padding-top: 1rem!important
}

.pr-3,
.px-3 {
    padding-right: 1rem!important
}

.pb-3,
.py-3 {
    padding-bottom: 1rem!important
}

.pl-3,
.px-3 {
    padding-left: 1rem!important
}

.p-4 {
    padding: 1.5rem!important
}

.pt-4,
.py-4 {
    padding-top: 1.5rem!important
}

.pr-4,
.px-4 {
    padding-right: 1.5rem!important
}

.pb-4,
.py-4 {
    padding-bottom: 1.5rem!important
}

.pl-4,
.px-4 {
    padding-left: 1.5rem!important
}

.p-5 {
    padding: 3rem!important
}

.pt-5,
.py-5 {
    padding-top: 3rem!important
}

.pr-5,
.px-5 {
    padding-right: 3rem!important
}

.pb-5,
.py-5 {
    padding-bottom: 3rem!important
}

.pl-5,
.px-5 {
    padding-left: 3rem!important
}

.m-n1 {
    margin: -.25rem!important
}

.mt-n1,
.my-n1 {
    margin-top: -.25rem!important
}

.mr-n1,
.mx-n1 {
    margin-right: -.25rem!important
}

.mb-n1,
.my-n1 {
    margin-bottom: -.25rem!important
}

.ml-n1,
.mx-n1 {
    margin-left: -.25rem!important
}

.m-n2 {
    margin: -.5rem!important
}

.mt-n2,
.my-n2 {
    margin-top: -.5rem!important
}

.mr-n2,
.mx-n2 {
    margin-right: -.5rem!important
}

.mb-n2,
.my-n2 {
    margin-bottom: -.5rem!important
}

.ml-n2,
.mx-n2 {
    margin-left: -.5rem!important
}

.m-n3 {
    margin: -1rem!important
}

.mt-n3,
.my-n3 {
    margin-top: -1rem!important
}

.mr-n3,
.mx-n3 {
    margin-right: -1rem!important
}

.mb-n3,
.my-n3 {
    margin-bottom: -1rem!important
}

.ml-n3,
.mx-n3 {
    margin-left: -1rem!important
}

.m-n4 {
    margin: -1.5rem!important
}

.mt-n4,
.my-n4 {
    margin-top: -1.5rem!important
}

.mr-n4,
.mx-n4 {
    margin-right: -1.5rem!important
}

.mb-n4,
.my-n4 {
    margin-bottom: -1.5rem!important
}

.ml-n4,
.mx-n4 {
    margin-left: -1.5rem!important
}

.m-n5 {
    margin: -3rem!important
}

.mt-n5,
.my-n5 {
    margin-top: -3rem!important
}

.mr-n5,
.mx-n5 {
    margin-right: -3rem!important
}

.mb-n5,
.my-n5 {
    margin-bottom: -3rem!important
}

.ml-n5,
.mx-n5 {
    margin-left: -3rem!important
}

.m-auto {
    margin: auto!important
}

.mt-auto,
.my-auto {
    margin-top: auto!important
}

.mr-auto,
.mx-auto {
    margin-right: auto!important
}

.mb-auto,
.my-auto {
    margin-bottom: auto!important
}

.ml-auto,
.mx-auto {
    margin-left: auto!important
}

@media (min-width:576px) {
    .m-sm-0 {
        margin: 0!important
    }
    .mt-sm-0,
    .my-sm-0 {
        margin-top: 0!important
    }
    .mr-sm-0,
    .mx-sm-0 {
        margin-right: 0!important
    }
    .mb-sm-0,
    .my-sm-0 {
        margin-bottom: 0!important
    }
    .ml-sm-0,
    .mx-sm-0 {
        margin-left: 0!important
    }
    .m-sm-1 {
        margin: .25rem!important
    }
    .mt-sm-1,
    .my-sm-1 {
        margin-top: .25rem!important
    }
    .mr-sm-1,
    .mx-sm-1 {
        margin-right: .25rem!important
    }
    .mb-sm-1,
    .my-sm-1 {
        margin-bottom: .25rem!important
    }
    .ml-sm-1,
    .mx-sm-1 {
        margin-left: .25rem!important
    }
    .m-sm-2 {
        margin: .5rem!important
    }
    .mt-sm-2,
    .my-sm-2 {
        margin-top: .5rem!important
    }
    .mr-sm-2,
    .mx-sm-2 {
        margin-right: .5rem!important
    }
    .mb-sm-2,
    .my-sm-2 {
        margin-bottom: .5rem!important
    }
    .ml-sm-2,
    .mx-sm-2 {
        margin-left: .5rem!important
    }
    .m-sm-3 {
        margin: 1rem!important
    }
    .mt-sm-3,
    .my-sm-3 {
        margin-top: 1rem!important
    }
    .mr-sm-3,
    .mx-sm-3 {
        margin-right: 1rem!important
    }
    .mb-sm-3,
    .my-sm-3 {
        margin-bottom: 1rem!important
    }
    .ml-sm-3,
    .mx-sm-3 {
        margin-left: 1rem!important
    }
    .m-sm-4 {
        margin: 1.5rem!important
    }
    .mt-sm-4,
    .my-sm-4 {
        margin-top: 1.5rem!important
    }
    .mr-sm-4,
    .mx-sm-4 {
        margin-right: 1.5rem!important
    }
    .mb-sm-4,
    .my-sm-4 {
        margin-bottom: 1.5rem!important
    }
    .ml-sm-4,
    .mx-sm-4 {
        margin-left: 1.5rem!important
    }
    .m-sm-5 {
        margin: 3rem!important
    }
    .mt-sm-5,
    .my-sm-5 {
        margin-top: 3rem!important
    }
    .mr-sm-5,
    .mx-sm-5 {
        margin-right: 3rem!important
    }
    .mb-sm-5,
    .my-sm-5 {
        margin-bottom: 3rem!important
    }
    .ml-sm-5,
    .mx-sm-5 {
        margin-left: 3rem!important
    }
    .p-sm-0 {
        padding: 0!important
    }
    .pt-sm-0,
    .py-sm-0 {
        padding-top: 0!important
    }
    .pr-sm-0,
    .px-sm-0 {
        padding-right: 0!important
    }
    .pb-sm-0,
    .py-sm-0 {
        padding-bottom: 0!important
    }
    .pl-sm-0,
    .px-sm-0 {
        padding-left: 0!important
    }
    .p-sm-1 {
        padding: .25rem!important
    }
    .pt-sm-1,
    .py-sm-1 {
        padding-top: .25rem!important
    }
    .pr-sm-1,
    .px-sm-1 {
        padding-right: .25rem!important
    }
    .pb-sm-1,
    .py-sm-1 {
        padding-bottom: .25rem!important
    }
    .pl-sm-1,
    .px-sm-1 {
        padding-left: .25rem!important
    }
    .p-sm-2 {
        padding: .5rem!important
    }
    .pt-sm-2,
    .py-sm-2 {
        padding-top: .5rem!important
    }
    .pr-sm-2,
    .px-sm-2 {
        padding-right: .5rem!important
    }
    .pb-sm-2,
    .py-sm-2 {
        padding-bottom: .5rem!important
    }
    .pl-sm-2,
    .px-sm-2 {
        padding-left: .5rem!important
    }
    .p-sm-3 {
        padding: 1rem!important
    }
    .pt-sm-3,
    .py-sm-3 {
        padding-top: 1rem!important
    }
    .pr-sm-3,
    .px-sm-3 {
        padding-right: 1rem!important
    }
    .pb-sm-3,
    .py-sm-3 {
        padding-bottom: 1rem!important
    }
    .pl-sm-3,
    .px-sm-3 {
        padding-left: 1rem!important
    }
    .p-sm-4 {
        padding: 1.5rem!important
    }
    .pt-sm-4,
    .py-sm-4 {
        padding-top: 1.5rem!important
    }
    .pr-sm-4,
    .px-sm-4 {
        padding-right: 1.5rem!important
    }
    .pb-sm-4,
    .py-sm-4 {
        padding-bottom: 1.5rem!important
    }
    .pl-sm-4,
    .px-sm-4 {
        padding-left: 1.5rem!important
    }
    .p-sm-5 {
        padding: 3rem!important
    }
    .pt-sm-5,
    .py-sm-5 {
        padding-top: 3rem!important
    }
    .pr-sm-5,
    .px-sm-5 {
        padding-right: 3rem!important
    }
    .pb-sm-5,
    .py-sm-5 {
        padding-bottom: 3rem!important
    }
    .pl-sm-5,
    .px-sm-5 {
        padding-left: 3rem!important
    }
    .m-sm-n1 {
        margin: -.25rem!important
    }
    .mt-sm-n1,
    .my-sm-n1 {
        margin-top: -.25rem!important
    }
    .mr-sm-n1,
    .mx-sm-n1 {
        margin-right: -.25rem!important
    }
    .mb-sm-n1,
    .my-sm-n1 {
        margin-bottom: -.25rem!important
    }
    .ml-sm-n1,
    .mx-sm-n1 {
        margin-left: -.25rem!important
    }
    .m-sm-n2 {
        margin: -.5rem!important
    }
    .mt-sm-n2,
    .my-sm-n2 {
        margin-top: -.5rem!important
    }
    .mr-sm-n2,
    .mx-sm-n2 {
        margin-right: -.5rem!important
    }
    .mb-sm-n2,
    .my-sm-n2 {
        margin-bottom: -.5rem!important
    }
    .ml-sm-n2,
    .mx-sm-n2 {
        margin-left: -.5rem!important
    }
    .m-sm-n3 {
        margin: -1rem!important
    }
    .mt-sm-n3,
    .my-sm-n3 {
        margin-top: -1rem!important
    }
    .mr-sm-n3,
    .mx-sm-n3 {
        margin-right: -1rem!important
    }
    .mb-sm-n3,
    .my-sm-n3 {
        margin-bottom: -1rem!important
    }
    .ml-sm-n3,
    .mx-sm-n3 {
        margin-left: -1rem!important
    }
    .m-sm-n4 {
        margin: -1.5rem!important
    }
    .mt-sm-n4,
    .my-sm-n4 {
        margin-top: -1.5rem!important
    }
    .mr-sm-n4,
    .mx-sm-n4 {
        margin-right: -1.5rem!important
    }
    .mb-sm-n4,
    .my-sm-n4 {
        margin-bottom: -1.5rem!important
    }
    .ml-sm-n4,
    .mx-sm-n4 {
        margin-left: -1.5rem!important
    }
    .m-sm-n5 {
        margin: -3rem!important
    }
    .mt-sm-n5,
    .my-sm-n5 {
        margin-top: -3rem!important
    }
    .mr-sm-n5,
    .mx-sm-n5 {
        margin-right: -3rem!important
    }
    .mb-sm-n5,
    .my-sm-n5 {
        margin-bottom: -3rem!important
    }
    .ml-sm-n5,
    .mx-sm-n5 {
        margin-left: -3rem!important
    }
    .m-sm-auto {
        margin: auto!important
    }
    .mt-sm-auto,
    .my-sm-auto {
        margin-top: auto!important
    }
    .mr-sm-auto,
    .mx-sm-auto {
        margin-right: auto!important
    }
    .mb-sm-auto,
    .my-sm-auto {
        margin-bottom: auto!important
    }
    .ml-sm-auto,
    .mx-sm-auto {
        margin-left: auto!important
    }
}

@media (min-width:768px) {
    .m-md-0 {
        margin: 0!important
    }
    .mt-md-0,
    .my-md-0 {
        margin-top: 0!important
    }
    .mr-md-0,
    .mx-md-0 {
        margin-right: 0!important
    }
    .mb-md-0,
    .my-md-0 {
        margin-bottom: 0!important
    }
    .ml-md-0,
    .mx-md-0 {
        margin-left: 0!important
    }
    .m-md-1 {
        margin: .25rem!important
    }
    .mt-md-1,
    .my-md-1 {
        margin-top: .25rem!important
    }
    .mr-md-1,
    .mx-md-1 {
        margin-right: .25rem!important
    }
    .mb-md-1,
    .my-md-1 {
        margin-bottom: .25rem!important
    }
    .ml-md-1,
    .mx-md-1 {
        margin-left: .25rem!important
    }
    .m-md-2 {
        margin: .5rem!important
    }
    .mt-md-2,
    .my-md-2 {
        margin-top: .5rem!important
    }
    .mr-md-2,
    .mx-md-2 {
        margin-right: .5rem!important
    }
    .mb-md-2,
    .my-md-2 {
        margin-bottom: .5rem!important
    }
    .ml-md-2,
    .mx-md-2 {
        margin-left: .5rem!important
    }
    .m-md-3 {
        margin: 1rem!important
    }
    .mt-md-3,
    .my-md-3 {
        margin-top: 1rem!important
    }
    .mr-md-3,
    .mx-md-3 {
        margin-right: 1rem!important
    }
    .mb-md-3,
    .my-md-3 {
        margin-bottom: 1rem!important
    }
    .ml-md-3,
    .mx-md-3 {
        margin-left: 1rem!important
    }
    .m-md-4 {
        margin: 1.5rem!important
    }
    .mt-md-4,
    .my-md-4 {
        margin-top: 1.5rem!important
    }
    .mr-md-4,
    .mx-md-4 {
        margin-right: 1.5rem!important
    }
    .mb-md-4,
    .my-md-4 {
        margin-bottom: 1.5rem!important
    }
    .ml-md-4,
    .mx-md-4 {
        margin-left: 1.5rem!important
    }
    .m-md-5 {
        margin: 3rem!important
    }
    .mt-md-5,
    .my-md-5 {
        margin-top: 3rem!important
    }
    .mr-md-5,
    .mx-md-5 {
        margin-right: 3rem!important
    }
    .mb-md-5,
    .my-md-5 {
        margin-bottom: 3rem!important
    }
    .ml-md-5,
    .mx-md-5 {
        margin-left: 3rem!important
    }
    .p-md-0 {
        padding: 0!important
    }
    .pt-md-0,
    .py-md-0 {
        padding-top: 0!important
    }
    .pr-md-0,
    .px-md-0 {
        padding-right: 0!important
    }
    .pb-md-0,
    .py-md-0 {
        padding-bottom: 0!important
    }
    .pl-md-0,
    .px-md-0 {
        padding-left: 0!important
    }
    .p-md-1 {
        padding: .25rem!important
    }
    .pt-md-1,
    .py-md-1 {
        padding-top: .25rem!important
    }
    .pr-md-1,
    .px-md-1 {
        padding-right: .25rem!important
    }
    .pb-md-1,
    .py-md-1 {
        padding-bottom: .25rem!important
    }
    .pl-md-1,
    .px-md-1 {
        padding-left: .25rem!important
    }
    .p-md-2 {
        padding: .5rem!important
    }
    .pt-md-2,
    .py-md-2 {
        padding-top: .5rem!important
    }
    .pr-md-2,
    .px-md-2 {
        padding-right: .5rem!important
    }
    .pb-md-2,
    .py-md-2 {
        padding-bottom: .5rem!important
    }
    .pl-md-2,
    .px-md-2 {
        padding-left: .5rem!important
    }
    .p-md-3 {
        padding: 1rem!important
    }
    .pt-md-3,
    .py-md-3 {
        padding-top: 1rem!important
    }
    .pr-md-3,
    .px-md-3 {
        padding-right: 1rem!important
    }
    .pb-md-3,
    .py-md-3 {
        padding-bottom: 1rem!important
    }
    .pl-md-3,
    .px-md-3 {
        padding-left: 1rem!important
    }
    .p-md-4 {
        padding: 1.5rem!important
    }
    .pt-md-4,
    .py-md-4 {
        padding-top: 1.5rem!important
    }
    .pr-md-4,
    .px-md-4 {
        padding-right: 1.5rem!important
    }
    .pb-md-4,
    .py-md-4 {
        padding-bottom: 1.5rem!important
    }
    .pl-md-4,
    .px-md-4 {
        padding-left: 1.5rem!important
    }
    .p-md-5 {
        padding: 3rem!important
    }
    .pt-md-5,
    .py-md-5 {
        padding-top: 3rem!important
    }
    .pr-md-5,
    .px-md-5 {
        padding-right: 3rem!important
    }
    .pb-md-5,
    .py-md-5 {
        padding-bottom: 3rem!important
    }
    .pl-md-5,
    .px-md-5 {
        padding-left: 3rem!important
    }
    .m-md-n1 {
        margin: -.25rem!important
    }
    .mt-md-n1,
    .my-md-n1 {
        margin-top: -.25rem!important
    }
    .mr-md-n1,
    .mx-md-n1 {
        margin-right: -.25rem!important
    }
    .mb-md-n1,
    .my-md-n1 {
        margin-bottom: -.25rem!important
    }
    .ml-md-n1,
    .mx-md-n1 {
        margin-left: -.25rem!important
    }
    .m-md-n2 {
        margin: -.5rem!important
    }
    .mt-md-n2,
    .my-md-n2 {
        margin-top: -.5rem!important
    }
    .mr-md-n2,
    .mx-md-n2 {
        margin-right: -.5rem!important
    }
    .mb-md-n2,
    .my-md-n2 {
        margin-bottom: -.5rem!important
    }
    .ml-md-n2,
    .mx-md-n2 {
        margin-left: -.5rem!important
    }
    .m-md-n3 {
        margin: -1rem!important
    }
    .mt-md-n3,
    .my-md-n3 {
        margin-top: -1rem!important
    }
    .mr-md-n3,
    .mx-md-n3 {
        margin-right: -1rem!important
    }
    .mb-md-n3,
    .my-md-n3 {
        margin-bottom: -1rem!important
    }
    .ml-md-n3,
    .mx-md-n3 {
        margin-left: -1rem!important
    }
    .m-md-n4 {
        margin: -1.5rem!important
    }
    .mt-md-n4,
    .my-md-n4 {
        margin-top: -1.5rem!important
    }
    .mr-md-n4,
    .mx-md-n4 {
        margin-right: -1.5rem!important
    }
    .mb-md-n4,
    .my-md-n4 {
        margin-bottom: -1.5rem!important
    }
    .ml-md-n4,
    .mx-md-n4 {
        margin-left: -1.5rem!important
    }
    .m-md-n5 {
        margin: -3rem!important
    }
    .mt-md-n5,
    .my-md-n5 {
        margin-top: -3rem!important
    }
    .mr-md-n5,
    .mx-md-n5 {
        margin-right: -3rem!important
    }
    .mb-md-n5,
    .my-md-n5 {
        margin-bottom: -3rem!important
    }
    .ml-md-n5,
    .mx-md-n5 {
        margin-left: -3rem!important
    }
    .m-md-auto {
        margin: auto!important
    }
    .mt-md-auto,
    .my-md-auto {
        margin-top: auto!important
    }
    .mr-md-auto,
    .mx-md-auto {
        margin-right: auto!important
    }
    .mb-md-auto,
    .my-md-auto {
        margin-bottom: auto!important
    }
    .ml-md-auto,
    .mx-md-auto {
        margin-left: auto!important
    }
}

@media (min-width:992px) {
    .m-lg-0 {
        margin: 0!important
    }
    .mt-lg-0,
    .my-lg-0 {
        margin-top: 0!important
    }
    .mr-lg-0,
    .mx-lg-0 {
        margin-right: 0!important
    }
    .mb-lg-0,
    .my-lg-0 {
        margin-bottom: 0!important
    }
    .ml-lg-0,
    .mx-lg-0 {
        margin-left: 0!important
    }
    .m-lg-1 {
        margin: .25rem!important
    }
    .mt-lg-1,
    .my-lg-1 {
        margin-top: .25rem!important
    }
    .mr-lg-1,
    .mx-lg-1 {
        margin-right: .25rem!important
    }
    .mb-lg-1,
    .my-lg-1 {
        margin-bottom: .25rem!important
    }
    .ml-lg-1,
    .mx-lg-1 {
        margin-left: .25rem!important
    }
    .m-lg-2 {
        margin: .5rem!important
    }
    .mt-lg-2,
    .my-lg-2 {
        margin-top: .5rem!important
    }
    .mr-lg-2,
    .mx-lg-2 {
        margin-right: .5rem!important
    }
    .mb-lg-2,
    .my-lg-2 {
        margin-bottom: .5rem!important
    }
    .ml-lg-2,
    .mx-lg-2 {
        margin-left: .5rem!important
    }
    .m-lg-3 {
        margin: 1rem!important
    }
    .mt-lg-3,
    .my-lg-3 {
        margin-top: 1rem!important
    }
    .mr-lg-3,
    .mx-lg-3 {
        margin-right: 1rem!important
    }
    .mb-lg-3,
    .my-lg-3 {
        margin-bottom: 1rem!important
    }
    .ml-lg-3,
    .mx-lg-3 {
        margin-left: 1rem!important
    }
    .m-lg-4 {
        margin: 1.5rem!important
    }
    .mt-lg-4,
    .my-lg-4 {
        margin-top: 1.5rem!important
    }
    .mr-lg-4,
    .mx-lg-4 {
        margin-right: 1.5rem!important
    }
    .mb-lg-4,
    .my-lg-4 {
        margin-bottom: 1.5rem!important
    }
    .ml-lg-4,
    .mx-lg-4 {
        margin-left: 1.5rem!important
    }
    .m-lg-5 {
        margin: 3rem!important
    }
    .mt-lg-5,
    .my-lg-5 {
        margin-top: 3rem!important
    }
    .mr-lg-5,
    .mx-lg-5 {
        margin-right: 3rem!important
    }
    .mb-lg-5,
    .my-lg-5 {
        margin-bottom: 3rem!important
    }
    .ml-lg-5,
    .mx-lg-5 {
        margin-left: 3rem!important
    }
    .p-lg-0 {
        padding: 0!important
    }
    .pt-lg-0,
    .py-lg-0 {
        padding-top: 0!important
    }
    .pr-lg-0,
    .px-lg-0 {
        padding-right: 0!important
    }
    .pb-lg-0,
    .py-lg-0 {
        padding-bottom: 0!important
    }
    .pl-lg-0,
    .px-lg-0 {
        padding-left: 0!important
    }
    .p-lg-1 {
        padding: .25rem!important
    }
    .pt-lg-1,
    .py-lg-1 {
        padding-top: .25rem!important
    }
    .pr-lg-1,
    .px-lg-1 {
        padding-right: .25rem!important
    }
    .pb-lg-1,
    .py-lg-1 {
        padding-bottom: .25rem!important
    }
    .pl-lg-1,
    .px-lg-1 {
        padding-left: .25rem!important
    }
    .p-lg-2 {
        padding: .5rem!important
    }
    .pt-lg-2,
    .py-lg-2 {
        padding-top: .5rem!important
    }
    .pr-lg-2,
    .px-lg-2 {
        padding-right: .5rem!important
    }
    .pb-lg-2,
    .py-lg-2 {
        padding-bottom: .5rem!important
    }
    .pl-lg-2,
    .px-lg-2 {
        padding-left: .5rem!important
    }
    .p-lg-3 {
        padding: 1rem!important
    }
    .pt-lg-3,
    .py-lg-3 {
        padding-top: 1rem!important
    }
    .pr-lg-3,
    .px-lg-3 {
        padding-right: 1rem!important
    }
    .pb-lg-3,
    .py-lg-3 {
        padding-bottom: 1rem!important
    }
    .pl-lg-3,
    .px-lg-3 {
        padding-left: 1rem!important
    }
    .p-lg-4 {
        padding: 1.5rem!important
    }
    .pt-lg-4,
    .py-lg-4 {
        padding-top: 1.5rem!important
    }
    .pr-lg-4,
    .px-lg-4 {
        padding-right: 1.5rem!important
    }
    .pb-lg-4,
    .py-lg-4 {
        padding-bottom: 1.5rem!important
    }
    .pl-lg-4,
    .px-lg-4 {
        padding-left: 1.5rem!important
    }
    .p-lg-5 {
        padding: 3rem!important
    }
    .pt-lg-5,
    .py-lg-5 {
        padding-top: 3rem!important
    }
    .pr-lg-5,
    .px-lg-5 {
        padding-right: 3rem!important
    }
    .pb-lg-5,
    .py-lg-5 {
        padding-bottom: 3rem!important
    }
    .pl-lg-5,
    .px-lg-5 {
        padding-left: 3rem!important
    }
    .m-lg-n1 {
        margin: -.25rem!important
    }
    .mt-lg-n1,
    .my-lg-n1 {
        margin-top: -.25rem!important
    }
    .mr-lg-n1,
    .mx-lg-n1 {
        margin-right: -.25rem!important
    }
    .mb-lg-n1,
    .my-lg-n1 {
        margin-bottom: -.25rem!important
    }
    .ml-lg-n1,
    .mx-lg-n1 {
        margin-left: -.25rem!important
    }
    .m-lg-n2 {
        margin: -.5rem!important
    }
    .mt-lg-n2,
    .my-lg-n2 {
        margin-top: -.5rem!important
    }
    .mr-lg-n2,
    .mx-lg-n2 {
        margin-right: -.5rem!important
    }
    .mb-lg-n2,
    .my-lg-n2 {
        margin-bottom: -.5rem!important
    }
    .ml-lg-n2,
    .mx-lg-n2 {
        margin-left: -.5rem!important
    }
    .m-lg-n3 {
        margin: -1rem!important
    }
    .mt-lg-n3,
    .my-lg-n3 {
        margin-top: -1rem!important
    }
    .mr-lg-n3,
    .mx-lg-n3 {
        margin-right: -1rem!important
    }
    .mb-lg-n3,
    .my-lg-n3 {
        margin-bottom: -1rem!important
    }
    .ml-lg-n3,
    .mx-lg-n3 {
        margin-left: -1rem!important
    }
    .m-lg-n4 {
        margin: -1.5rem!important
    }
    .mt-lg-n4,
    .my-lg-n4 {
        margin-top: -1.5rem!important
    }
    .mr-lg-n4,
    .mx-lg-n4 {
        margin-right: -1.5rem!important
    }
    .mb-lg-n4,
    .my-lg-n4 {
        margin-bottom: -1.5rem!important
    }
    .ml-lg-n4,
    .mx-lg-n4 {
        margin-left: -1.5rem!important
    }
    .m-lg-n5 {
        margin: -3rem!important
    }
    .mt-lg-n5,
    .my-lg-n5 {
        margin-top: -3rem!important
    }
    .mr-lg-n5,
    .mx-lg-n5 {
        margin-right: -3rem!important
    }
    .mb-lg-n5,
    .my-lg-n5 {
        margin-bottom: -3rem!important
    }
    .ml-lg-n5,
    .mx-lg-n5 {
        margin-left: -3rem!important
    }
    .m-lg-auto {
        margin: auto!important
    }
    .mt-lg-auto,
    .my-lg-auto {
        margin-top: auto!important
    }
    .mr-lg-auto,
    .mx-lg-auto {
        margin-right: auto!important
    }
    .mb-lg-auto,
    .my-lg-auto {
        margin-bottom: auto!important
    }
    .ml-lg-auto,
    .mx-lg-auto {
        margin-left: auto!important
    }
}

@media (min-width:1200px) {
    .m-xl-0 {
        margin: 0!important
    }
    .mt-xl-0,
    .my-xl-0 {
        margin-top: 0!important
    }
    .mr-xl-0,
    .mx-xl-0 {
        margin-right: 0!important
    }
    .mb-xl-0,
    .my-xl-0 {
        margin-bottom: 0!important
    }
    .ml-xl-0,
    .mx-xl-0 {
        margin-left: 0!important
    }
    .m-xl-1 {
        margin: .25rem!important
    }
    .mt-xl-1,
    .my-xl-1 {
        margin-top: .25rem!important
    }
    .mr-xl-1,
    .mx-xl-1 {
        margin-right: .25rem!important
    }
    .mb-xl-1,
    .my-xl-1 {
        margin-bottom: .25rem!important
    }
    .ml-xl-1,
    .mx-xl-1 {
        margin-left: .25rem!important
    }
    .m-xl-2 {
        margin: .5rem!important
    }
    .mt-xl-2,
    .my-xl-2 {
        margin-top: .5rem!important
    }
    .mr-xl-2,
    .mx-xl-2 {
        margin-right: .5rem!important
    }
    .mb-xl-2,
    .my-xl-2 {
        margin-bottom: .5rem!important
    }
    .ml-xl-2,
    .mx-xl-2 {
        margin-left: .5rem!important
    }
    .m-xl-3 {
        margin: 1rem!important
    }
    .mt-xl-3,
    .my-xl-3 {
        margin-top: 1rem!important
    }
    .mr-xl-3,
    .mx-xl-3 {
        margin-right: 1rem!important
    }
    .mb-xl-3,
    .my-xl-3 {
        margin-bottom: 1rem!important
    }
    .ml-xl-3,
    .mx-xl-3 {
        margin-left: 1rem!important
    }
    .m-xl-4 {
        margin: 1.5rem!important
    }
    .mt-xl-4,
    .my-xl-4 {
        margin-top: 1.5rem!important
    }
    .mr-xl-4,
    .mx-xl-4 {
        margin-right: 1.5rem!important
    }
    .mb-xl-4,
    .my-xl-4 {
        margin-bottom: 1.5rem!important
    }
    .ml-xl-4,
    .mx-xl-4 {
        margin-left: 1.5rem!important
    }
    .m-xl-5 {
        margin: 3rem!important
    }
    .mt-xl-5,
    .my-xl-5 {
        margin-top: 3rem!important
    }
    .mr-xl-5,
    .mx-xl-5 {
        margin-right: 3rem!important
    }
    .mb-xl-5,
    .my-xl-5 {
        margin-bottom: 3rem!important
    }
    .ml-xl-5,
    .mx-xl-5 {
        margin-left: 3rem!important
    }
    .p-xl-0 {
        padding: 0!important
    }
    .pt-xl-0,
    .py-xl-0 {
        padding-top: 0!important
    }
    .pr-xl-0,
    .px-xl-0 {
        padding-right: 0!important
    }
    .pb-xl-0,
    .py-xl-0 {
        padding-bottom: 0!important
    }
    .pl-xl-0,
    .px-xl-0 {
        padding-left: 0!important
    }
    .p-xl-1 {
        padding: .25rem!important
    }
    .pt-xl-1,
    .py-xl-1 {
        padding-top: .25rem!important
    }
    .pr-xl-1,
    .px-xl-1 {
        padding-right: .25rem!important
    }
    .pb-xl-1,
    .py-xl-1 {
        padding-bottom: .25rem!important
    }
    .pl-xl-1,
    .px-xl-1 {
        padding-left: .25rem!important
    }
    .p-xl-2 {
        padding: .5rem!important
    }
    .pt-xl-2,
    .py-xl-2 {
        padding-top: .5rem!important
    }
    .pr-xl-2,
    .px-xl-2 {
        padding-right: .5rem!important
    }
    .pb-xl-2,
    .py-xl-2 {
        padding-bottom: .5rem!important
    }
    .pl-xl-2,
    .px-xl-2 {
        padding-left: .5rem!important
    }
    .p-xl-3 {
        padding: 1rem!important
    }
    .pt-xl-3,
    .py-xl-3 {
        padding-top: 1rem!important
    }
    .pr-xl-3,
    .px-xl-3 {
        padding-right: 1rem!important
    }
    .pb-xl-3,
    .py-xl-3 {
        padding-bottom: 1rem!important
    }
    .pl-xl-3,
    .px-xl-3 {
        padding-left: 1rem!important
    }
    .p-xl-4 {
        padding: 1.5rem!important
    }
    .pt-xl-4,
    .py-xl-4 {
        padding-top: 1.5rem!important
    }
    .pr-xl-4,
    .px-xl-4 {
        padding-right: 1.5rem!important
    }
    .pb-xl-4,
    .py-xl-4 {
        padding-bottom: 1.5rem!important
    }
    .pl-xl-4,
    .px-xl-4 {
        padding-left: 1.5rem!important
    }
    .p-xl-5 {
        padding: 3rem!important
    }
    .pt-xl-5,
    .py-xl-5 {
        padding-top: 3rem!important
    }
    .pr-xl-5,
    .px-xl-5 {
        padding-right: 3rem!important
    }
    .pb-xl-5,
    .py-xl-5 {
        padding-bottom: 3rem!important
    }
    .pl-xl-5,
    .px-xl-5 {
        padding-left: 3rem!important
    }
    .m-xl-n1 {
        margin: -.25rem!important
    }
    .mt-xl-n1,
    .my-xl-n1 {
        margin-top: -.25rem!important
    }
    .mr-xl-n1,
    .mx-xl-n1 {
        margin-right: -.25rem!important
    }
    .mb-xl-n1,
    .my-xl-n1 {
        margin-bottom: -.25rem!important
    }
    .ml-xl-n1,
    .mx-xl-n1 {
        margin-left: -.25rem!important
    }
    .m-xl-n2 {
        margin: -.5rem!important
    }
    .mt-xl-n2,
    .my-xl-n2 {
        margin-top: -.5rem!important
    }
    .mr-xl-n2,
    .mx-xl-n2 {
        margin-right: -.5rem!important
    }
    .mb-xl-n2,
    .my-xl-n2 {
        margin-bottom: -.5rem!important
    }
    .ml-xl-n2,
    .mx-xl-n2 {
        margin-left: -.5rem!important
    }
    .m-xl-n3 {
        margin: -1rem!important
    }
    .mt-xl-n3,
    .my-xl-n3 {
        margin-top: -1rem!important
    }
    .mr-xl-n3,
    .mx-xl-n3 {
        margin-right: -1rem!important
    }
    .mb-xl-n3,
    .my-xl-n3 {
        margin-bottom: -1rem!important
    }
    .ml-xl-n3,
    .mx-xl-n3 {
        margin-left: -1rem!important
    }
    .m-xl-n4 {
        margin: -1.5rem!important
    }
    .mt-xl-n4,
    .my-xl-n4 {
        margin-top: -1.5rem!important
    }
    .mr-xl-n4,
    .mx-xl-n4 {
        margin-right: -1.5rem!important
    }
    .mb-xl-n4,
    .my-xl-n4 {
        margin-bottom: -1.5rem!important
    }
    .ml-xl-n4,
    .mx-xl-n4 {
        margin-left: -1.5rem!important
    }
    .m-xl-n5 {
        margin: -3rem!important
    }
    .mt-xl-n5,
    .my-xl-n5 {
        margin-top: -3rem!important
    }
    .mr-xl-n5,
    .mx-xl-n5 {
        margin-right: -3rem!important
    }
    .mb-xl-n5,
    .my-xl-n5 {
        margin-bottom: -3rem!important
    }
    .ml-xl-n5,
    .mx-xl-n5 {
        margin-left: -3rem!important
    }
    .m-xl-auto {
        margin: auto!important
    }
    .mt-xl-auto,
    .my-xl-auto {
        margin-top: auto!important
    }
    .mr-xl-auto,
    .mx-xl-auto {
        margin-right: auto!important
    }
    .mb-xl-auto,
    .my-xl-auto {
        margin-bottom: auto!important
    }
    .ml-xl-auto,
    .mx-xl-auto {
        margin-left: auto!important
    }
}

.text-monospace {
    font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace!important
}

.text-justify {
    text-align: justify!important
}

.text-wrap {
    white-space: normal!important
}

.text-nowrap {
    white-space: nowrap!important
}

.text-truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.text-left {
    text-align: left!important
}

.text-right {
    text-align: right!important
}

.text-center {
    text-align: center!important
}

@media (min-width:576px) {
    .text-sm-left {
        text-align: left!important
    }
    .text-sm-right {
        text-align: right!important
    }
    .text-sm-center {
        text-align: center!important
    }
}

@media (min-width:768px) {
    .text-md-left {
        text-align: left!important
    }
    .text-md-right {
        text-align: right!important
    }
    .text-md-center {
        text-align: center!important
    }
}

@media (min-width:992px) {
    .text-lg-left {
        text-align: left!important
    }
    .text-lg-right {
        text-align: right!important
    }
    .text-lg-center {
        text-align: center!important
    }
}

@media (min-width:1200px) {
    .text-xl-left {
        text-align: left!important
    }
    .text-xl-right {
        text-align: right!important
    }
    .text-xl-center {
        text-align: center!important
    }
}

.text-lowercase {
    text-transform: lowercase!important
}

.text-uppercase {
    text-transform: uppercase!important
}

.text-capitalize {
    text-transform: capitalize!important
}

.font-weight-light {
    font-weight: 300!important
}

.font-weight-lighter {
    font-weight: lighter!important
}

.font-weight-normal {
    font-weight: 400!important
}

.font-weight-bold {
    font-weight: 700!important
}

.font-weight-bolder {
    font-weight: bolder!important
}

.font-italic {
    font-style: italic!important
}

.text-white {
    color: #fff!important
}

.text-primary {
    color: #714cdf!important
}

a.text-primary:focus,
a.text-primary:hover {
    color: #4922bd!important
}

.text-secondary {
    color: #16a4de!important
}

a.text-secondary:focus,
a.text-secondary:hover {
    color: #0f7198!important
}

.text-success {
    color: #17b06b!important
}

a.text-success:focus,
a.text-success:hover {
    color: #0e6c42!important
}

.text-info {
    color: #2983fe!important
}

a.text-info:focus,
a.text-info:hover {
    color: #015cd9!important
}

.text-warning {
    color: #f97515!important
}

a.text-warning:focus,
a.text-warning:hover {
    color: #bd5205!important
}

.text-danger {
    color: #ef121b!important
}

a.text-danger:focus,
a.text-danger:hover {
    color: #ef0027!important
}

.text-light {
    color: #dbebfb75!important
}

a.text-light:focus,
a.text-light:hover {
    color: white!important
}

.text-dark {
    color: #32334a!important
}

a.text-dark:focus,
a.text-dark:hover {
    color: #13141c!important
}

.text-body {
    color: #e4e2ff!important
}

.text-muted {
    color: #81839a!important
}

.text-black-50 {
    color: rgba(0, 0, 0, .5)!important
}

.text-white-50 {
    color: rgba(255, 255, 255, .5)!important
}

.text-hide {
    font: 0/0 a;
    color: transparent;
    text-shadow: none;
    background-color: transparent;
    border: 0
}

.text-decoration-none {
    text-decoration: none!important
}

.text-break {
    word-break: break-word!important;
    overflow-wrap: break-word!important
}

.text-reset {
    color: inherit!important
}

.visible {
    visibility: visible!important
}

.invisible {
    visibility: hidden!important
}

@media print {
    *,
     ::after,
     ::before {
        text-shadow: none!important;
        -webkit-box-shadow: none!important;
        box-shadow: none!important
    }
    a:not(.btn) {
        text-decoration: underline
    }
    abbr[title]::after {
        content: " (" attr(title) ")"
    }
    pre {
        white-space: pre-wrap!important
    }
    blockquote,
    pre {
        border: 1px solid #1c1d2c;
        page-break-inside: avoid
    }
    thead {
        display: table-header-group
    }
    img,
    tr {
        page-break-inside: avoid
    }
    h2,
    h3,
    p {
        orphans: 3;
        widows: 3
    }
    h2,
    h3 {
        page-break-after: avoid
    }
    @page {
        size: a3
    }
    body {
        min-width: 992px!important
    }
    .container {
        min-width: 992px!important
    }
    .navbar {
        display: none
    }
    .badge {
        border: 1px solid #000
    }
    .table {
        border-collapse: collapse!important
    }
    .table td,
    .table th {
        background-color: #fff!important
    }
    .table-bordered td,
    .table-bordered th {
        border: 1px solid #28293e!important
    }
    .table-dark {
        color: inherit
    }
    .table-dark tbody+tbody,
    .table-dark td,
    .table-dark th,
    .table-dark thead th {
        border-color: #28293e
    }
    .table .thead-dark th {
        color: inherit;
        border-color: #28293e
    }
}

.btn-hover-text-primary:active,
.btn-hover-text-primary:hover {
    color: #714cdf!important
}

.btn-hover-text-secondary:active,
.btn-hover-text-secondary:hover {
    color: #16a4de!important
}

.btn-hover-text-success:active,
.btn-hover-text-success:hover {
    color: #17b06b!important
}

.btn-hover-text-info:active,
.btn-hover-text-info:hover {
    color: #2983fe!important
}

.btn-hover-text-warning:active,
.btn-hover-text-warning:hover {
    color: #f97515!important
}

.btn-hover-text-danger:active,
.btn-hover-text-danger:hover {
    color: #ef121b!important
}

.btn-hover-text-light:active,
.btn-hover-text-light:hover {
    color: #dbebfb!important
}

.btn-hover-text-dark:active,
.btn-hover-text-dark:hover {
    color: #32334a!important
}

.btn-wide {
    padding-left: 50px;
    padding-right: 50px
}

.display-fix {
    margin-left: -4px
}

.btn-pill {
    border-radius: 100px
}

.lead-lg {
    font-size: 35px
}

.radius-0 {
    border-radius: 0
}

.text-spacey {
    line-height: 28px;
}

@media (max-width:767.98px) {
    .display-1 {
        font-size: 4rem
    }
}

@media (max-width:767.98px) {
    .display-2 {
        font-size: 3.5rem
    }
}


/* body {
    background-image: url(https://ozanam-cyberquest.fr/images/ng-background-dot.png)
} */

.btn-shadow {
    margin-left: 8px
}

.btn-shadow.btn-outline-primary,
.btn-shadow.btn-primary {
    border-color: #986edf;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-outline-primary,
.btn-shadow.btn-outline-primary.focus,
.btn-shadow.btn-outline-primary:focus,
.btn-shadow.btn-primary,
.btn-shadow.btn-primary.focus,
.btn-shadow.btn-primary:focus {
    -webkit-box-shadow: 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
    box-shadow: 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf
}

.btn-shadow.btn-outline-primary:hover,
.btn-shadow.btn-primary:hover {
    -webkit-box-shadow: 5px 5px 0 #986edf, 4px 4px 0 #986edf, 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
    box-shadow: 5px 5px 0 #986edf, 4px 4px 0 #986edf, 3px 3px 0 #986edf, 2px 2px 0 #986edf, 1px 1px 0 #986edf;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-outline-primary:active,
.btn-shadow.btn-primary:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-outline-secondary,
.btn-shadow.btn-secondary {
    border-color: #87c4f2;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-outline-secondary,
.btn-shadow.btn-outline-secondary.focus,
.btn-shadow.btn-outline-secondary:focus,
.btn-shadow.btn-secondary,
.btn-shadow.btn-secondary.focus,
.btn-shadow.btn-secondary:focus {
    -webkit-box-shadow: 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
    box-shadow: 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2
}

.btn-shadow.btn-outline-secondary:hover,
.btn-shadow.btn-secondary:hover {
    -webkit-box-shadow: 5px 5px 0 #87c4f2, 4px 4px 0 #87c4f2, 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
    box-shadow: 5px 5px 0 #87c4f2, 4px 4px 0 #87c4f2, 3px 3px 0 #87c4f2, 2px 2px 0 #87c4f2, 1px 1px 0 #87c4f2;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-outline-secondary:active,
.btn-shadow.btn-secondary:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-outline-success,
.btn-shadow.btn-success {
    border-color: #43cb8e;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-outline-success,
.btn-shadow.btn-outline-success.focus,
.btn-shadow.btn-outline-success:focus,
.btn-shadow.btn-success,
.btn-shadow.btn-success.focus,
.btn-shadow.btn-success:focus {
    -webkit-box-shadow: 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
    box-shadow: 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e
}

.btn-shadow.btn-outline-success:hover,
.btn-shadow.btn-success:hover {
    -webkit-box-shadow: 5px 5px 0 #43cb8e, 4px 4px 0 #43cb8e, 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
    box-shadow: 5px 5px 0 #43cb8e, 4px 4px 0 #43cb8e, 3px 3px 0 #43cb8e, 2px 2px 0 #43cb8e, 1px 1px 0 #43cb8e;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-outline-success:active,
.btn-shadow.btn-success:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-info,
.btn-shadow.btn-outline-info {
    border-color: #25a8eb;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-info,
.btn-shadow.btn-info.focus,
.btn-shadow.btn-info:focus,
.btn-shadow.btn-outline-info,
.btn-shadow.btn-outline-info.focus,
.btn-shadow.btn-outline-info:focus {
    -webkit-box-shadow: 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
    box-shadow: 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb
}

.btn-shadow.btn-info:hover,
.btn-shadow.btn-outline-info:hover {
    -webkit-box-shadow: 5px 5px 0 #25a8eb, 4px 4px 0 #25a8eb, 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
    box-shadow: 5px 5px 0 #25a8eb, 4px 4px 0 #25a8eb, 3px 3px 0 #25a8eb, 2px 2px 0 #25a8eb, 1px 1px 0 #25a8eb;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-info:active,
.btn-shadow.btn-outline-info:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-outline-warning,
.btn-shadow.btn-warning {
    border-color: #f99511;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-outline-warning,
.btn-shadow.btn-outline-warning.focus,
.btn-shadow.btn-outline-warning:focus,
.btn-shadow.btn-warning,
.btn-shadow.btn-warning.focus,
.btn-shadow.btn-warning:focus {
    -webkit-box-shadow: 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
    box-shadow: 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511
}

.btn-shadow.btn-outline-warning:hover,
.btn-shadow.btn-warning:hover {
    -webkit-box-shadow: 5px 5px 0 #f99511, 4px 4px 0 #f99511, 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
    box-shadow: 5px 5px 0 #f99511, 4px 4px 0 #f99511, 3px 3px 0 #f99511, 2px 2px 0 #f99511, 1px 1px 0 #f99511;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-outline-warning:active,
.btn-shadow.btn-warning:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-danger,
.btn-shadow.btn-outline-danger {
    border-color: #9d1119;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-danger,
.btn-shadow.btn-danger.focus,
.btn-shadow.btn-danger:focus,
.btn-shadow.btn-outline-danger,
.btn-shadow.btn-outline-danger.focus,
.btn-shadow.btn-outline-danger:focus {
    -webkit-box-shadow: 3px 3px 0 #9d1119, 2px 2px 0 #9d1119, 1px 1px 0 #9d1119;
    box-shadow: 3px 3px 0 #9d1119, 2px 2px 0 #9d1119, 1px 1px 0 #9d1119
}

.btn-shadow.btn-danger:hover,
.btn-shadow.btn-outline-danger:hover {
    -webkit-box-shadow: 5px 5px 0 #9d1119, 4px 4px 0 #9d1119, 3px 3px 0 #9d1119, 2px 2px 0 #9d1119, 1px 1px 0 #9d1119;
    box-shadow: 5px 5px 0 #9d1119, 4px 4px 0 #9d1119, 3px 3px 0 #9d1119, 2px 2px 0 #9d1119, 1px 1px 0 #9d1119;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-danger:active,
.btn-shadow.btn-outline-danger:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-light,
.btn-shadow.btn-outline-light {
    border-color: #9ea9b6;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-light,
.btn-shadow.btn-light.focus,
.btn-shadow.btn-light:focus,
.btn-shadow.btn-outline-light,
.btn-shadow.btn-outline-light.focus,
.btn-shadow.btn-outline-light:focus {
    -webkit-box-shadow: 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
    box-shadow: 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6
}

.btn-shadow.btn-light:hover,
.btn-shadow.btn-outline-light:hover {
    -webkit-box-shadow: 5px 5px 0 #9ea9b6, 4px 4px 0 #9ea9b6, 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
    box-shadow: 5px 5px 0 #9ea9b6, 4px 4px 0 #9ea9b6, 3px 3px 0 #9ea9b6, 2px 2px 0 #9ea9b6, 1px 1px 0 #9ea9b6;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-light:active,
.btn-shadow.btn-outline-light:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-dark,
.btn-shadow.btn-outline-dark {
    border-color: #191a2d;
    -webkit-transition: none;
    -o-transition: none;
    transition: none
}

.btn-shadow.btn-dark,
.btn-shadow.btn-dark.focus,
.btn-shadow.btn-dark:focus,
.btn-shadow.btn-outline-dark,
.btn-shadow.btn-outline-dark.focus,
.btn-shadow.btn-outline-dark:focus {
    -webkit-box-shadow: 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
    box-shadow: 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d
}

.btn-shadow.btn-dark:hover,
.btn-shadow.btn-outline-dark:hover {
    -webkit-box-shadow: 5px 5px 0 #191a2d, 4px 4px 0 #191a2d, 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
    box-shadow: 5px 5px 0 #191a2d, 4px 4px 0 #191a2d, 3px 3px 0 #191a2d, 2px 2px 0 #191a2d, 1px 1px 0 #191a2d;
    -webkit-transform: translate(-2px, -2px);
    -o-transform: translate(-2px, -2px);
    transform: translate(-2px, -2px);
    -webkit-transition: all .3s ease;
    -o-transition: all .3s ease;
    transition: all .3s ease
}

.btn-shadow.btn-dark:active,
.btn-shadow.btn-outline-dark:active {
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform: translate(4px, 4px)!important;
    -o-transform: translate(4px, 4px)!important;
    transform: translate(4px, 4px)!important;
    -webkit-transition: all .1s ease;
    -o-transition: all .1s ease;
    transition: all .1s ease
}

.btn-shadow.btn-outline-primary:hover,
.btn-shadow.btn-primary:hover {
    background-color: #714cdf
}

.btn-shadow.btn-outline-secondary:hover,
.btn-shadow.btn-secondary:hover {
    background-color: #16a4de
}

.btn-shadow.btn-outline-success:hover,
.btn-shadow.btn-success:hover {
    background-color: #17b06b
}

.btn-shadow.btn-info:hover,
.btn-shadow.btn-outline-info:hover {
    background-color: #2983fe
}

.btn-shadow.btn-outline-warning:hover,
.btn-shadow.btn-warning:hover {
    background-color: #f97515
}

.btn-shadow.btn-danger:hover,
.btn-shadow.btn-outline-danger:hover {
    background-color: #ef121b
}

.btn-shadow.btn-light:hover,
.btn-shadow.btn-outline-light:hover {
    background-color: #dbebfb
}

.btn-shadow.btn-dark:hover,
.btn-shadow.btn-outline-dark:hover {
    background-color: #32334a
}

.display-1,
.display-2,
.display-3,
.display-4 {
    font-family: Hack, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"
}

.display-1.text-white,
.display-2.text-white,
.display-3.text-white,
.display-4.text-white,
.text-white .display-1,
.text-white .display-2,
.text-white .display-3,
.text-white .display-4 {
    text-shadow: -1px -1px rgba(255, 255, 255, .2)
}

.text-reduced-opacity {
    opacity: .5
}

.text-grey {
    color: #a0a0a0
}

.text-darkblue {
    color: #4d4d74
}

.text-darkgrey {
    color: #6f6974
}

.text-mono {
    font-family: Hack, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"
}

.btn-success,
.btn-success:active,
.btn-success:focus,
.btn-success:hover {
    color: #c1f8c2
}

.vim-caret {
    -webkit-animation: vimCaret 1s linear infinite;
    -o-animation: vimCaret 1s linear infinite;
    animation: vimCaret 1s linear infinite
}

@-webkit-keyframes vimCaret {
    0% {
        background-color: transparent
    }
    49% {
        background-color: transparent
    }
    50% {
        background-color: rgba(239, 18, 27, .2)
    }
    100% {
        background-color: rgba(239, 18, 27, .2)
    }
}

@-o-keyframes vimCaret {
    0% {
        background-color: transparent
    }
    49% {
        background-color: transparent
    }
    50% {
        background-color: rgba(239, 18, 27, .2)
    }
    100% {
        background-color: rgba(239, 18, 27, .2)
    }
}

@keyframes vimCaret {
    0% {
        background-color: transparent
    }
    49% {
        background-color: transparent
    }
    50% {
        background-color: rgba(239, 18, 27, .2)
    }
    100% {
        background-color: rgba(239, 18, 27, .2)
    }
}

.list-group-item-primary {
    color: #3b2874;
    background-color: #8869e4
}

.list-group-item-primary.list-group-item-action:focus,
.list-group-item-primary.list-group-item-action:hover {
    color: #3b2874;
    background-color: #7753e0
}

.list-group-item-primary.list-group-item-action.active {
    color: #fff;
    background-color: #3b2874;
    border-color: #3b2874
}

.list-group-item-secondary {
    color: #0b5573;
    background-color: #3bb3e3
}

.list-group-item-secondary.list-group-item-action:focus,
.list-group-item-secondary.list-group-item-action:hover {
    color: #0b5573;
    background-color: #25aae0
}

.list-group-item-secondary.list-group-item-action.active {
    color: #fff;
    background-color: #0b5573;
    border-color: #0b5573
}

.list-group-item-success {
    color: #0c5c38;
    background-color: #3cbd83
}

.list-group-item-success.list-group-item-action:focus,
.list-group-item-success.list-group-item-action:hover {
    color: #0c5c38;
    background-color: #36aa76
}

.list-group-item-success.list-group-item-action.active {
    color: #fff;
    background-color: #0c5c38;
    border-color: #0c5c38
}

.list-group-item-info {
    color: #154484;
    background-color: #4b97fe
}

.list-group-item-info.list-group-item-action:focus,
.list-group-item-info.list-group-item-action:hover {
    color: #154484;
    background-color: #3288fe
}

.list-group-item-info.list-group-item-action.active {
    color: #fff;
    background-color: #154484;
    border-color: #154484
}

.list-group-item-warning {
    color: #813d0b;
    background-color: #fa8b3a
}

.list-group-item-warning.list-group-item-action:focus,
.list-group-item-warning.list-group-item-action:hover {
    color: #813d0b;
    background-color: #f97c21
}

.list-group-item-warning.list-group-item-action.active {
    color: #fff;
    background-color: #813d0b;
    border-color: #813d0b
}

.list-group-item-danger {
    color: #851f30;
    background-color: #ff5b76
}

.list-group-item-danger.list-group-item-action:focus,
.list-group-item-danger.list-group-item-action:hover {
    color: #851f30;
    background-color: #ff4261
}

.list-group-item-danger.list-group-item-action.active {
    color: #fff;
    background-color: #851f30;
    border-color: #851f30
}

.list-group-item-light {
    color: #727a83;
    background-color: #e1eefc
}

.list-group-item-light.list-group-item-action:focus,
.list-group-item-light.list-group-item-action:hover {
    color: #727a83;
    background-color: #cae1fa
}

.list-group-item-light.list-group-item-action.active {
    color: #fff;
    background-color: #727a83;
    border-color: #727a83
}

.list-group-item-dark {
    color: #1a1b26;
    background-color: #535467
}

.list-group-item-dark.list-group-item-action:focus,
.list-group-item-dark.list-group-item-action:hover {
    color: #1a1b26;
    background-color: #484859
}

.list-group-item-dark.list-group-item-action.active {
    color: #fff;
    background-color: #1a1b26;
    border-color: #1a1b26
}

.alert-primary {
    color: #322162;
    background-color: #aa94ec;
    border-color: #8869e4
}

.alert-primary hr {
    border-top-color: #7753e0
}

.alert-primary .alert-link {
    color: #1f143c
}

.alert-secondary {
    color: #0a4862;
    background-color: #73c8eb;
    border-color: #3bb3e3
}

.alert-secondary hr {
    border-top-color: #25aae0
}

.alert-secondary .alert-link {
    color: #052634
}

.alert-success {
    color: #0a4d2f;
    background-color: #74d0a6;
    border-color: #3cbd83
}

.alert-success hr {
    border-top-color: #36aa76
}

.alert-success .alert-link {
    color: #042013
}

.alert-info {
    color: #123a70;
    background-color: #7fb5fe;
    border-color: #4b97fe
}

.alert-info hr {
    border-top-color: #3288fe
}

.alert-info .alert-link {
    color: #0b2344
}

.alert-warning {
    color: #6e3309;
    background-color: #fbac73;
    border-color: #fa8b3a
}

.alert-warning hr {
    border-top-color: #f97c21
}

.alert-warning .alert-link {
    color: #3f1d05
}

.alert-danger {
    color: #701a28;
    background-color: #ff8a9d;
    border-color: #ff5b76
}

.alert-danger hr {
    border-top-color: #ff4261
}

.alert-danger .alert-link {
    color: #471019
}

.alert-light {
    color: #60676e;
    background-color: #e9f3fd;
    border-color: #e1eefc
}

.alert-light hr {
    border-top-color: #cae1fa
}

.alert-light .alert-link {
    color: #484e53
}

.alert-dark {
    color: #161621;
    background-color: #848592;
    border-color: #535467
}

.alert-dark hr {
    border-top-color: #484859
}

.alert-dark .alert-link {
    color: #020202
}

.table-primary,
.table-primary>td,
.table-primary>th {
    background-color: #8869e4
}

.table-hover .table-primary:hover {
    background-color: #7753e0
}

.table-hover .table-primary:hover>td,
.table-hover .table-primary:hover>th {
    background-color: #7753e0
}

.table-secondary,
.table-secondary>td,
.table-secondary>th {
    background-color: #3bb3e3
}

.table-hover .table-secondary:hover {
    background-color: #25aae0
}

.table-hover .table-secondary:hover>td,
.table-hover .table-secondary:hover>th {
    background-color: #25aae0
}

.table-success,
.table-success>td,
.table-success>th {
    background-color: #3cbd83
}

.table-hover .table-success:hover {
    background-color: #36aa76
}

.table-hover .table-success:hover>td,
.table-hover .table-success:hover>th {
    background-color: #36aa76
}

.table-info,
.table-info>td,
.table-info>th {
    background-color: #4b97fe
}

.table-hover .table-info:hover {
    background-color: #3288fe
}

.table-hover .table-info:hover>td,
.table-hover .table-info:hover>th {
    background-color: #3288fe
}

.table-warning,
.table-warning>td,
.table-warning>th {
    background-color: #fa8b3a
}

.table-hover .table-warning:hover {
    background-color: #f97c21
}

.table-hover .table-warning:hover>td,
.table-hover .table-warning:hover>th {
    background-color: #f97c21
}

.table-danger,
.table-danger>td,
.table-danger>th {
    background-color: #ff5b76
}

.table-hover .table-danger:hover {
    background-color: #ff4261
}

.table-hover .table-danger:hover>td,
.table-hover .table-danger:hover>th {
    background-color: #ff4261
}

.table-light,
.table-light>td,
.table-light>th {
    background-color: #e1eefc
}

.table-hover .table-light:hover {
    background-color: #cae1fa
}

.table-hover .table-light:hover>td,
.table-hover .table-light:hover>th {
    background-color: #cae1fa
}

.table-dark,
.table-dark>td,
.table-dark>th {
    background-color: #535467
}

.table-hover .table-dark:hover {
    background-color: #484859
}

.table-hover .table-dark:hover>td,
.table-hover .table-dark:hover>th {
    background-color: #484859
}

.hal-9000 {
    background: #f9d080;
    border: 12px #ef121b solid;
    border-radius: 90px;
    -webkit-box-shadow: 0 0 40px #ef121b;
    box-shadow: 0 0 40px #ef121b;
    display: inline-block;
    height: 40px;
    width: 40px
}
"""

def generate_editor_css():
    return """
body {
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    top: calc(-1 * var(--gap-vertical));
    left: calc(-1 * var(--gap-horizontal));
    width: calc(100% + var(--gap-horizontal) * 2);
    height: calc(100% + var(--gap-vertical) * 2);
    background: url(https://ozanam-cyberquest.fr/images/bg.png);
    background-color: #000000;
    background-position: right;
    background-size: cover;
    background-repeat: no-repeat;
    background-position-x: 350px;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
    color: #d4d4d4;
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
#editor-container {
    display: flex;
    width: 80%;
    top: 20px;
    position: fixed;
}

#editor {
    flex: 1;
    width: 100%;
    height: 270px;
    margin-right: 10px;
    background-color: #2b2b2b;
    border: 1px solid #333;
    border-radius: 5px;
    overflow: hidden;
    color: #d4d4d4;
    font-size: 14px;
    z-index: 1;
    scrollbar-color: #888 #333;
    scrollbar-width: thin;
}

#tooltip {
    width: 30%;
    background-color: #2B2B2B;
    color: #fff;
    height: 300px;
    padding: 10px;
    border-radius: 5px;
    text-align: left;
}

#outputContainer {
    width: 80%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

#output {
    border-radius: 10px;
    width: 51.9%;
    top: 60.7%;
    position: fixed;
    height: 150px;
    padding: 10px;
    border: 1px solid #333;
    white-space: pre-wrap;
    background-color: #2b2b2b;
    margin-bottom: 76px;
    color: #d4d4d4;
    overflow-y: auto;
    z-index: 10;
    scrollbar-color: #555 #333;
    scrollbar-width: thin;
}
#output::-webkit-scrollbar {
    width: 12px;
}

#output::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background-color: #888;
}

#output::-webkit-scrollbar-track {
    background-color: #333;
}
#verification {
    left: 64.5%;
    position: absolute;
    top: 60.8%;
    border-radius: 10px;
    width: 23.9%;
    border-radius: 10px;
    height: 150px;
    padding: 10px;
    border: 1px solid #333;
    white-space: pre-wrap;
    background-color: #2b2b2b;
    margin-bottom: 30px;
    color: #d4d4d4;
    overflow-y: auto;
    z-index: 10;
    scrollbar-color: #555 #333;
    scrollbar-width: thin;
}
#runButton {
    position: fixed;
    width: 10%;
    top: 54%;
    left: 32.5%;
    padding: 10px;
    animation: neon 1s infinite alternate;
    cursor: pointer;
    color: #fff;
    border: 2px solid #e62117;
    border-radius: 5px;
    font-size: 16px;
    transform-style: preserve-3d;
    perspective: 800px;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
    box-shadow: 0 0 10px rgba(230, 33, 23, 0);
    background-color: transparent;
    margin-top: -10px;
    margin-bottom: 10px;
    background-color: #1a1a1a;
}
#validButton {
    display: none;
    position: fixed;
    width: 10%;
    top: 92.7%;
    left: 45%;
    padding: 10px;
    animation: neon2 1s infinite alternate;
    cursor: pointer;
    color: #fff;
    border: 2px solid #bcbcbc;
    border-radius: 5px;
    font-size: 16px;
    transform-style: preserve-3d;
    perspective: 800px;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0);
    background-color: transparent;
    margin-top: -10px;
    margin-bottom: 10px;
    background-color: #1a1a1a;
}

#validButton:hover {
    animation: neon2 1s infinite alternate;
    box-shadow: 0 0 20px rgba(23, 230, 116, 0.8);
    border: 2px solid #14c65e;
}

@keyframes neon2 {
    to {
        box-shadow: 0 0 40px rgba(184, 184, 184, 0.5);
    }
}
#runButton:hover {
    animation: neon 1s infinite alternate;
    box-shadow: 0 0 20px rgba(230, 33, 23, 0.8);
    border: 2px solid #c61a14;
}

@keyframes neon {
    to {
        box-shadow: 0 0 40px rgba(230, 33, 23, 0.8);
    }
}

#sidePanel {
    width: 0;
    height: 100%;
    background-color: #333;
    position: fixed;
    top: 0;
    right: 0;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
    z-index: 2;
}

#sidePanel a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 20px;
    color: #818181;
    display: block;
    transition: 0.3s;
}

#sidePanel a:hover {
    color: #f1f1f1;
}

#sidePanel .closebtn {
    position: absolute;
    top: 0;
    left: 10px;
    font-size: 36px;
    margin-right: 50px;
}

#main-content {
    transition: margin-right .5s;
    padding: 16px;
}
.svgvalid{
    height: 20px;
    fill: green;
    margin-bottom: -5px;
}
.svgno{
    height: 20px;
    width: 20px;
    fill: #a30000;
    margin-bottom: -5px;
}
#result1, #result2, #result3 {
    display: flow;
    margin-top: -10px;
    margin-bottom: -10px; 
    margin-left: 7%;
}
#restart {
    position: fixed;
    width: 10%;
    cursor: pointer;
    border: none;
    font-size: 16px;
    background-color: transparent;
    fill: #474747;
    width: 50px;
    z-index: 1000;
    left: 58%;
    margin-top: 0.5%;
}


.loading-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 8px;
    background-color: rgb(66, 66, 66);
    z-index: 13;
  }

  .progress {
    height: 100%;
    width: 0;
    background-color: #b80900;
    transition: width 1s ease;
  }

  .time {
    position: fixed;
    top: 10px;
    left: 10px;
    color: #b80900;
    font-size: 18px;
    font-weight: bold;
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
    z-index: 1000000;
    display: none;
}
.container {
    position: relative;
    height: 100vh;
}

.toggle-button {
    cursor: pointer;
    z-index: 12;
    position: fixed;
    top: -166px;
    right: -71px;
    height: 280px;
}
.menu {
    position: fixed;
    top: 0;
    right: -375px;
    width: 375px;
    height: 100%;
    background-color: #2c3e50;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    transition: 0.3s ease-out;
    z-index: 11;
    color: #ecf0f1;
    overflow-y: auto;
    padding-top: 60px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: transparent transparent;
    -ms-overflow-style: none; 

}
.menu::-webkit-scrollbar {
    width: 6px; 
}

.menu::-webkit-scrollbar-thumb {
    background-color: transparent; 
}


.menu h2 {
    margin: 20px 0 10px 20px;
    font-size: 1.5em;
    color: #ecf0f1;
}

.close-button {
    position: absolute;
    top: 20px;
    right: 20px;
    cursor: pointer;
    font-size: 20px;
    color: #ecf0f1;
}

.menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
    margin-bottom: 50px; 
}

.menu li {
    position: relative;
    padding: 15px 20px;
    cursor: pointer;
    border-bottom: 1px solid #34495e;
    transition: background-color 0.3s;
    font-size: 1.2em;
}

.menu li:hover {
    background-color: #34495e;
}

.info-dropdown {
    width: 100%;
    margin-left: -10px;
    margin-top: 10px;
    display: none;
    background-color: #333;
    color: #ecf0f1;
    padding: 10px;
    position: relative;
    top: -1px;
    z-index: 1;
    overflow: hidden;
    max-height: 0;
}

.menu li.info-shown .info-dropdown {
    display: block;
    max-height: 300px;
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}



code {
    font-family: 'Courier New', Courier, monospace;
    font-size: 1em;
    color: #333;
}

.parentheses {
    color: white;
}

.function-fonction {
    color: #66d9ef;
}
.texte-code {
    color: #e6db74;
}
code {
    font-size: 12px;
}

.area {
    width: 200px;
    height: 265px;
    animation: swing 1s infinite ease-in-out alternate;
    transform-origin: top;
    -moz-transform-origin: top;
    -webkit-transform-origin: top;
}

.wire {
    position: relative;
    left: 98px;
    height: 200px;
    width: 4px;
    background-color: black;
}

.fixture {
    position: relative;
    background-color: grey;
    width: 16px;
    height: 20px;
    left: 92px;
}

.strip {
    position: relative;
    width: 18px;
    height: 2px;
    right: 1px;
    top: 4px;
    background-color: darkgrey;
}

.strip:nth-of-type(2) {
    top: 7px;
}

.strip:nth-of-type(3) {
    top: 10px;
}

.bulb {
    position: relative;
    width: 40px;
    height: 40px;
    left: 80px;
    bottom: 2px;
    z-index: -1;
    background-color: rgba(255, 224, 121, 0.85);
    border-radius: 50%;
    -webkit-box-shadow: 0px 0px 300px 77px rgb(250, 200, 114);
    -moz-box-shadow: 0px 0px 300px 77px rgb(250, 200, 114);
    box-shadow: 0px 0px 300px 77px rgb(250, 200, 114);
}

.zig {
    position: relative;
    background-color: transparent;
    width: 10px;
    height: 5px;
    border-radius: 5px / 2.5px;
    left: 14px;
    border: black solid 1px;
}

.zig:nth-of-type(2) {
    top: -3px;
}

.zig:nth-of-type(3) {
    top: -6px;
}

@keyframes swing {
    from {
        -moz-transform: rotate(3deg);
        -webkit-transform: rotate(3deg);
        transform: rotate(3deg);
    }
    to {
        transform: rotate(-3deg);
    }
}

"""
def generate_final_css():
    return """
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
  }

  .note-container {
    text-align: center;
  }

  .circle {
    left: 20%;
    position: relative;
    width: 300px;
    height: 300px;
    background-color: #EF121B;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: space-around;
    color: white;
    font-size: 125px;
    font-weight: bold;
    /* margin-bottom: -10px; */
    flex-wrap: nowrap;
    flex-direction: row;
    align-content: space-between;
}
"""
def generate_prog_css():
    return """
.box1 {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv1.png);
}
.box1end {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv1.png);
}
.box2 {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv2.png);
}
.box2end {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv2.png);
}
.box3 {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv3.png);
}
.box3end {
    background-image: url(https://ozanam-cyberquest.fr/images/proglv3.png);
}
.text{
    color: white;
}
.stack {
    width: 1000px;
    min-width: 1000px;
}
"""

def generate_python_css():
    return """
.box1 {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv1.png);
}
.box1end {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv1.png);
}
.box2 {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv2.png);
}
.box2end {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv2.png);
}
.box3 {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv3.png);
}
.box3end {
    background-image: url(https://ozanam-cyberquest.fr/images/pythonlv3.png);
}
.text{
    color: white;
}
.stack {
    width: 1000px;
    min-width: 1000px;
}
"""

def generate_reseaux_css():
    return """
.box1 {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv1.png);
}
.box1end {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv1.png);
}
.box2 {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv2.png);
}
.box2end {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv2.png);
}
.box3 {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv3.png);
}
.box3end {
    background-image: url(https://ozanam-cyberquest.fr/images/reseauxlv3.png);
}
.text{
    color: white;
}
.stack {
    width: 1000px;
    min-width: 1000px;
}

"""
def generate_scrollbar_css():
    return """
.ace_scrollbar::-webkit-scrollbar {
    height: 5px;
    width: 5px;
}

.ace_scrollbar::-webkit-scrollbar-track
{
    box-shadow: inset 0 0 7px rgba(0,0,0,0.3);
    background-color: #272822;
    border-radius: 10px;
}

.ace_scrollbar::-webkit-scrollbar-thumb {
    background-color: darkgrey;
    outline: 1px solid slategrey;
    border-radius: 10px;
}
"""
def generate_select_css():
    return """
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
"""

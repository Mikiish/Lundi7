# Lundi7 — Bird Feedback

> _"Quelque part sur Terre, il fait quelque chose. Voici comment tu pourrais te sentir. Voici l'oiseau qui le sait."_

Bienvenue sur **Lundi7** — un portail minimaliste, météorologique, semi-prophétique.
Un site qui ne prétend à rien d'autre que ceci :

🌀 À chaque chargement, vous recevez :
- Le **climat réel** d'un endroit aléatoire sur Terre 🌍
- La **température actuelle** 🌡️
- Un **emoji mood** pour l'accompagner 😐
- Et un **oiseau dominant**, choisi par on ne sait trop quelle force 🐦

> C’est une interface entre le visible et l’insignifiant.
> C’est un site qui ne sert à rien. Et c’est pour ça qu’il est parfait.

## ✨ Fonctions techniques
- Serveur en Python (Flask) 🌐
- API météo réelle (OpenWeatherMap)
- Frontend HTML/CSS minimaliste, responsive comme un souffle
- Appel d’API toutes les 100 secondes, pour laisser le temps aux oiseaux de penser

## 🌩️ Technologies invoquées
- `Flask` — parce que Django, c'était trop sérieux
- `requests` — pour parler aux dieux du climat
- `python-dotenv` — parce que les secrets doivent rester secrets
- `Render` — pour héberger ce projet comme un autel gratuit, auto-renouvelant, HTTPS automatique parce que nous, on chill

## 🪶 À propos
Ce projet a été conçu pour... rien.  
Mais il pourrait bien vous accompagner pendant un café, un bug, une nuit, ou une conversation avec votre oscilloscope.

Il ne retiendra rien de vous. Il ne vous demandera jamais pourquoi vous êtes là.  
Il vous donnera simplement la météo d’un lieu que vous n’avez pas choisi,  
et un oiseau pour vous en parler.

## 🛠️ Lancer localement
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

⚠️ N'oubliez pas de fournir votre clé météo via un fichier `.env` :
```env
OPENWEATHER_API_KEY=clef_magique_ici
```

## 🕳️ Bonus mystique
Des archives seront peut-être cachées.  
Des sous-pages.  
Des fragments.  
Mais si vous devez les trouver, vous les trouverez.

**Lundi7** ne vous juge pas.
**Lundi7** ne dort jamais.
**Lundi7** écoute.

---

> _"Le vrai climat, c’est celui qu’on porte en soi. Le site ne fait que vous le rappeler."_


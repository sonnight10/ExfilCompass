<div align="center">

<img src="assets/logo.png" alt="Tarkov Companion" width="110">

# Tarkov Companion

**Ta position, tes quêtes et tes extractions sur la carte, sans toucher au jeu.**

[![Dernière version](https://img.shields.io/github/v/release/sonnight10/TarkovCompanion?label=version&color=f5c04e)](https://github.com/sonnight10/TarkovCompanion/releases/latest)
![Plateforme](https://img.shields.io/badge/Windows-10%20%2F%2011-2b2f3a)
![Lecture seule](https://img.shields.io/badge/jeu-lecture%20seule-3ecf8e)

[**Télécharger**](https://github.com/sonnight10/TarkovCompanion/releases/latest) · [Guide détaillé](docs/GUIDE.md) · [Historique des versions](CHANGELOG.md)

<br>

<img src="docs/img/banniere.png" alt="Tarkov Companion : carte, quêtes, flèche et distance" width="860">

</div>

## Ce que ça fait

<div align="center">
<img src="docs/img/carte.png" alt="La carte avec ta position, tes quêtes et l'extraction la plus proche" width="860">

<sub>Captures avec des données de démonstration.</sub>
</div>

- 🗺️ **Carte interactive** : ta position (à chaque capture d'écran) avec son cône de vision, ton trajet et les objectifs de tes quêtes en cours. Dézoom très large, échelle en mètres.
- 🧩 **Carte lisible** : une icône par type de point (extraction, objectif, éliminations, objet, clé, planque, cache) avec une légende, objectifs colorés par marchand et regroupés en pastilles numérotées qui se séparent quand tu zoomes.
- 🧭 **Flèche vers ton objectif** : suis une quête ou un de tes repères, et une flèche te montre la direction (relative à ton regard) avec la distance.
- 🪟 **Mini-fenêtre** : une toute petite fenêtre séparée (flèche + distance + nom) qui reste au-dessus du jeu, déplaçable (touche **G**), avec boussole, barre de progression, alerte verte à moins de 30 m et mode ultra-discret.
- ✅ **Quêtes automatiques** : lues dans les logs du jeu, rien à cocher à la main.
- 🚪 **Extractions** de ton camp (PMC ou Scav), avec la plus proche et sa distance.
- 🎒 **Préparer le raid** : quêtes à faire sur la carte choisie, extractions, repères.
- 📍 **Repères et mesure** : note tes caches et spawns, mesure une distance.
- 📊 **Historique et stats** : durée de tes raids, trajet rejouable, **comparaison de deux raids**, zones les plus visitées.
- 🗒️ **Notes par carte**, blocs **déplaçables** et masquables, **mode compact** : tu composes l'écran comme tu veux.
- 🧙 **Assistant de premier lancement** et bouton **Signaler un problème** (rapport masqué, prêt à coller sur Discord).
- 🔄 **Mises à jour** intégrées, vérifiées par empreinte SHA-256.
- 🌍 Interface en **français et en anglais**.

<div align="center">
<img src="docs/img/quetes.png" alt="Suivi des quêtes" width="420">
<img src="docs/img/preparer.png" alt="Préparer le raid" width="420">
</div>

<div align="center">
<br>
<img src="docs/img/mini.png" alt="La mini-fenêtre : flèche, distance, nom de la quête" width="264">

<sub>La mini-fenêtre, à taille réelle ×1,5.</sub>
</div>

## Un affichage qui s'adapte

<div align="center">
<img src="docs/img/theme-tactical.png" alt="Thème Tactique" width="280">
<img src="docs/img/theme-night.png" alt="Thème Nuit" width="280">
<img src="docs/img/theme-contrast.png" alt="Thème Contraste fort" width="280">

<sub>Thèmes Tactique, Nuit et Contraste fort (il y a aussi Sombre, Clair et « Comme Windows »).</sub>
</div>

- 🎨 **6 thèmes**, 5 couleurs d'accent et une **transparence des blocs** réglable.
- ✨ **Animations** douces (flèche qui tourne par le chemin le plus court, objectif qui pulse, transitions) que tu peux couper avec **Réduire les animations**.
- 🔭 **Dézoom** : tu peux t'éloigner bien au-delà de la vue entière pour garder un œil sur l'ensemble de la carte.

<div align="center">
<img src="docs/img/dezoom.png" alt="La carte dézoomée au maximum avec la légende des icônes" width="560">
</div>

## Installation

1. Va dans les [**Releases**](https://github.com/sonnight10/TarkovCompanion/releases/latest) et télécharge `TarkovCompanion-<version>.zip`.
2. Décompresse-le : il contient un seul fichier, `TarkovCompanion.exe`. Lance-le.
3. Windows peut afficher un avertissement SmartScreen (le logiciel n'est pas signé) : *Informations complémentaires* puis *Exécuter quand même*.

Dans Tarkov, mets l'affichage en **« Fenêtré sans bordure »** pour que la mini-fenêtre reste visible par-dessus le jeu.

<details>
<summary>Depuis les sources (Python 3.12 ou 3.13)</summary>

```
pip install -r requirements.txt
python main.py            # ou: python main.py --demo  pour essayer sans le jeu
```

Compiler l'exe : `build_exe.bat` (un seul fichier dans `dist/`), puis `python make_release.py`.
</details>

## Comment l'utiliser

1. Lance le logiciel : il trouve tout seul tes dossiers de logs et de captures d'écran (sinon : *Réglages → Parcourir*).
2. Lance un raid : la carte et l'état « en raid » sont détectés dans les logs.
3. Pour mettre ta position à jour, **prends une capture d'écran** avec la touche habituelle du jeu. Le logiciel lit la position écrite dans le *nom* du fichier.
4. Dans l'onglet *Quêtes*, clique sur **Suivre** : la flèche et la distance apparaissent, aussi dans la mini-fenêtre (**G**).

> La flèche et la distance se mettent à jour **à chaque capture d'écran**, pas en continu.

## Sécurité

Tarkov Companion est **en lecture seule** : il lit les fichiers texte des logs et les *noms* des fichiers de captures d'écran. Il n'injecte rien dans le jeu, ne lit pas sa mémoire, ne simule aucune touche et ne touche à aucun processus. Aucun outil ne peut garantir l'absence de risque avec un anti-cheat : tu l'utilises à tes risques.

## Contribuer

Les idées et les problèmes sont les bienvenus dans les [Issues](https://github.com/sonnight10/TarkovCompanion/issues). Si la détection du raid ou des quêtes ne marche pas chez toi, joins le *Diagnostic des logs* (*Réglages → Diagnostic*), sans y laisser d'informations personnelles.

## Crédits

- Calibration des cartes : [the-hideout/tarkov-dev](https://github.com/the-hideout/tarkov-dev) (MIT).
- Fonds de carte : [the-hideout/tarkov-dev-svg-maps](https://github.com/the-hideout/tarkov-dev-svg-maps), CC BY-NC-SA 4.0, téléchargés à l'exécution et non redistribués ici.
- Données de quêtes : API publique [tarkov.dev](https://tarkov.dev).
- [Leaflet](https://leafletjs.com) (BSD-2).

*Projet de fan, non affilié à Battlestate Games. « Escape from Tarkov » est une marque de Battlestate Games.*

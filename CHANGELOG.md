# Changelog

## 1.3.0
Refonte visuelle.
Carte : on peut dézoomer bien plus loin (3 niveaux au-delà de la vue entière) ; icônes distinctes (extraction, objectif, éliminations, objet, clé, planque, cache) avec légende masquable ; objectifs colorés selon le marchand ; objectifs proches regroupés en une pastille numérotée qui se sépare en zoomant ; cône de vision plus large pour le joueur et halo qui s'éteint quand la dernière capture est ancienne ; étiquettes d'extraction sans chevauchement ; échelle en mètres qui s'adapte au zoom.
Style : thèmes Tactique (vert sombre), Nuit (rouge très discret), Contraste fort et « Comme Windows » ; transparence réglable des blocs ; chiffres en police à chasse fixe ; états vides illustrés ; écran de démarrage.
Animations : flèche qui tourne par le chemin le plus court avec un léger rebond, pulsation de l'objectif suivi, ligne animée vers la cible, transitions à l'affichage/masquage des blocs ; option « Réduire les animations » (respecte aussi le réglage de Windows).
Mini-fenêtre : boussole (N) autour de la flèche, barre de progression vers l'objectif, tout passe au vert à moins de 30 m, mode ultra-discret optionnel.
Traduction anglaise complétée.

## 1.2.2
Assistant de premier lancement (dossiers, captures) ; « Signaler un problème » : rapport masqué (chemins, IP, identifiants) à coller sur Discord ; mode compact ; mini-fenêtre réglable (contenu, taille, couleur d'accent) ; blocs de la carte déplaçables à la souris ; bloc-notes par carte ; rappel de capture intelligent ; comparaison de deux raids de la même carte.
Barre de recherche dans le panneau des quêtes de la carte (touche /).
Bouton « Affichage » : chaque élément de la carte (panneau, choix de carte, barre d'outils, coordonnées, extraction proche, flèche suivie) se masque indépendamment ; le choix est mémorisé.
Panneau de droite : masquable (bouton ▸ ou touche Q) et largeur réglable en le faisant glisser, pour voir toute la carte.
L'exe est maintenant un fichier unique (plus de dossier `_internal`).
Flèche relative à ton regard (elle tourne quand tu te tournes) ; réglage pour revenir au mode « nord de la carte ».
Suivre un repère : même flèche et même distance (fenêtre principale et mini-fenêtre) que pour une quête.
Détection du raid corrigée d'après de vrais logs Tarkov 1.2.5 : la ligne « TRACE-NetworkGameCreate 6 » (après le début du raid) ne remet plus l'état à « hors raid » ; la fin de raid est détectée via le rechargement du profil et la coupure réseau (network-connection.log) ; dates sans fuseau acceptées ; un raid en cours au lancement du logiciel est repris. Superposition remplacée par une mini-fenêtre séparée (flèche + distance), sans bordure, déplaçable à la souris et toujours au premier plan.

## 1.2.0
Quête suivie avec flèche vers l'objectif ; liste des quêtes dans la superposition ; correctifs d'affichage.

## 1.1.0
Voir RELEASE_NOTES.md.

## 1.0.0
Première version : carte, position via captures d'écran, suivi des quêtes depuis les logs, extractions par camp.

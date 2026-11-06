# ExfilCompass — guide détaillé

[← Retour à la présentation](../README.md)

Application de bureau (Python) pour *Escape from Tarkov* :

- **Carte interactive** avec ta position, ton trajet et les objectifs de tes quêtes en cours
- **Suivi automatique des quêtes** à partir des logs du jeu
- **Extractions** de la carte selon ton camp (PMC ou Scav), avec l'extraction la plus proche et sa distance
- **Rappel sonore** de capture et **nettoyage automatique** des captures utilisées
- **Journal** des événements détectés (quête acceptée/terminée, carte, raid)
- **Préparer le raid** : quêtes en cours et à faire sur la carte choisie, extractions de ton camp, repères
- **Mesure et repères** sur la carte : distance entre deux points, repères nommés enregistrés
- **Historique des raids** : carte, durée, trajet (points de tes captures), avec replay animé
- **Apparence** : 6 thèmes (Veille, Clair, Tactique, Nuit, Contraste fort, Comme Windows), transparence des blocs, 5 couleurs d'accent, animations désactivables, interface en français ou en anglais
- **Crédits** : auteurs des cartes, sources et licences (onglet dédié)

## Sécurité (BattlEye)

L'application est en **lecture seule** : elle lit des fichiers texte (les logs) et les *noms* de fichiers du dossier de captures d'écran. Elle n'injecte rien, ne lit pas la mémoire du jeu et ne touche à aucun processus.

## Installation (Windows)

1. Installe [Python 3.10+](https://www.python.org/downloads/) (coche « Add python.exe to PATH »).
2. Dézippe le dossier, double-clique sur **`Lancer.bat`**. Au premier lancement, il installe `pywebview` (fenêtre native via Edge WebView2, déjà présent sur Windows 10/11).

À la main : `pip install -r requirements.txt` puis `python main.py`.

Essai sans le jeu : `python main.py --demo` (simule un raid sur Customs).

## Comment ça marche

| Fonction | Source | Précision |
|---|---|---|
| Quêtes (acceptée / terminée / échouée) | `Logs/.../push-notifications.log` | Automatique, en direct ; au 1er lancement, l'historique des sessions encore présentes dans `Logs` est rejoué pour reconstruire ton état |
| Carte et début/fin de raid | `Logs/.../application.log` et `network-connection.log` | Automatique, en direct |
| **Position** | Nom des fichiers du dossier *Screenshots* | **À la demande** : un point par capture d'écran |
| Extractions (nom, camp, position) | tarkov.dev (cache 24 h) | Disponibles pour tout le monde ; le « plus proche » exige une position (capture d'écran) |
| Fond de carte, objectifs, noms de quêtes | tarkov.dev (téléchargés puis mis en cache) | Nécessite internet au 1er lancement |

**La position n'est pas continue** : le jeu n'écrit pas ta position dans ses logs. Chaque fois que tu prends une capture d'écran en jeu, le nom du fichier contient tes coordonnées et ton orientation ; l'application place alors ton marqueur et trace le trajet entre les captures. Le suivi continu exigerait de lire la mémoire du jeu, ce qui est interdit et fait risquer le bannissement : ce n'est donc volontairement pas proposé.

Les dossiers sont détectés automatiquement (`...\Battlestate Games\...\Logs` et `Documents\Escape from Tarkov\Screenshots`). Sinon : *Réglages → Parcourir*.

Si une quête ancienne n'apparaît pas (logs déjà supprimés par le jeu), tu peux régler son état à la main dans l'onglet Quêtes.

Données enregistrées dans `%APPDATA%\ExfilCompass` (config, quêtes, cache, fonds de carte).

**Quêtes sur la carte** : les quêtes en cours et à faire sur la carte passent en premier (panneau de la carte, onglet Quêtes) ; leurs objectifs ont un point (et un contour de zone quand il existe) sur la carte, bleu pour les quêtes à faire (réglable : *Afficher aussi les objectifs des quêtes à faire*). Beaucoup d'objectifs (« tuer N Scavs », « remettre des objets ») n'ont pas de lieu précis dans les données de tarkov.dev : ils n'ont donc pas de point. Si le suivi automatique ne se déclenche pas : *Réglages → Diagnostic réseau → Diagnostic des logs* montre ce que l'application lit (dossier, fichiers, messages reconnus).

**Style des cartes** : bouton « Schéma / Détaillé » dans la barre d'outils de la carte (ou *Réglages → Style des cartes*). *Schéma* = fond vectoriel léger ; *Détaillé* = tuiles de tarkov.dev (même calibration, étages inclus), chargées depuis internet. Le détaillé est aussi le seul fond de Laboratoire, Labyrinthe et Icebreaker. Les cartes sans version détaillée (Lighthouse, Terminal, Streets) gardent le schéma. Si les tuiles ne se chargent pas, l'application revient seule au schéma. Les images 2D/3D du site ne sont pas intégrées : elles ne sont pas calibrées et ne permettent pas d'afficher ta position. Tuiles : Shebuka, TarkovBOT.eu et tarkov.dev (non redistribuées ; vérifie leurs conditions d'usage).

**Repères, historique** : *Mesurer* (barre d'outils de la carte) : clique deux points, la distance s'affiche en mètres. *Repère* : clique un point, donne-lui un nom ; les repères sont enregistrés (`marks.json`) et listés dans *Préparer*. Chaque raid terminé est enregistré (`history.json`, 100 derniers) avec les points de tes captures d'écran ; *Historique → Voir le trajet* l'affiche sur la carte, avec un bouton *Rejouer*. Un raid abandonné n'est pas enregistré.

**Extractions et spawn** : l'application affiche les extractions de ton camp (réglable dans la barre d'outils ou les Réglages), mais ne sait pas quelles extractions te sont réellement ouvertes selon ton point d'apparition : le jeu ne l'écrit pas dans les logs et je n'ai pas pu confirmer que tarkov.dev fournit cette correspondance. Certaines extractions conditionnelles (clé, objet, coopération) ne sont donc pas distinguées.

**Captures d'écran (Réglages)** :
- *Rappel sonore* toutes les N secondes (5 à 600, 0 = désactivé) : pendant un raid, l'application émet un bip (Windows) et c'est toi qui appuies sur la touche de capture du jeu. Le rappel dépend de la détection du raid dans les logs.
- *Suppression à la fin du raid* (désactivée par défaut) : seules les captures apparues pendant que l'application tourne et au format de capture de Tarkov sont supprimées, définitivement (pas de corbeille). Tes anciennes captures et les fichiers d'un autre format ne sont jamais touchés. La suppression a aussi lieu à la fermeture de l'application, et un bouton permet de la lancer à la demande.
- **Volontairement absent** : l'application n'envoie jamais de touche au jeu. Automatiser la capture reviendrait à piloter le jeu par programme (risque pour ton compte) et à créer un suivi quasi temps réel de ta position en raid.

**Si tarkov.dev est indisponible** : l'API publique est parfois surchargée (« GraphQL server unavailable »). Les quêtes sont demandées par petites pages de 100 (les positions d'objectifs à part, et de façon facultative : sans elles, les quêtes s'affichent quand même). L'application réessaie seule (plusieurs fois de suite, puis toutes les 15 à 60 s), n'enregistre jamais une réponse incomplète et utilise son cache quand il existe. Si le serveur refuse une demande précise (le français, ou certains champs) en la déguisant en « indisponible », l'application retombe automatiquement sur l'anglais, puis sans langue, puis sur une version réduite des quêtes. *Réglages → Diagnostic réseau* contient un bouton **Tester la connexion** (huit petites requêtes qui montrent ce que le serveur accepte ou refuse) et affiche les dernières réponses reçues.

## Si une mise à jour du jeu casse la détection

Le format des logs n'est pas documenté officiellement et peut changer. Tous les motifs de lecture sont dans **`exfilcompass/patterns.py`** (et seulement là). Le journal de l'application montre ce qui est détecté, ce qui aide à comprendre ce qui a changé.

## Points à vérifier sur ton PC

Ces éléments n'ont pas pu être testés avec un vrai jeu :

1. Le format réel de tes logs (les motifs reposent sur le format connu de TarkovMonitor) ;
2. Le téléchargement des fonds de carte, des quêtes et des extractions depuis tarkov.dev (le schéma des extractions n'a pas pu être vérifié : l'application essaie plusieurs variantes de requête et affiche une erreur claire si aucune ne marche). Le réseau était bloqué dans l'environnement de développement ;
3. L'orientation de la flèche (convention Unity : 0° = axe +Z) ;
4. L'alignement des étages sur certaines cartes (bascule automatique selon la hauteur).

## Tests

```
python -m unittest tests.test_engine tests.test_api
```

`tests/ui_smoke.py` charge l'interface dans Chromium avec une fausse API et produit des captures (nécessite `playwright`).

## Crédits et licences

- Code de l'application : à ta convenance.
- Calibration des cartes (transformation, rotation, limites, étages) : [the-hideout/tarkov-dev](https://github.com/the-hideout/tarkov-dev) (MIT).
- Fonds de carte SVG : [the-hideout/tarkov-dev-svg-maps](https://github.com/the-hideout/tarkov-dev-svg-maps), **CC BY-NC-SA 4.0** (usage non commercial, attribution). Ils sont téléchargés à l'exécution et ne sont pas redistribués dans ce dossier. Leur usage dans des outils de triche est explicitement interdit.
- Données de quêtes : API publique [tarkov.dev](https://tarkov.dev).
- Leaflet 1.9.4 (BSD-2), embarqué dans `ui/vendor/`.

## Carte entière et état « en raid »

- La carte n'est **plus recentrée** sur le joueur : elle n'est pas suivie automatiquement. Tu peux dézoomer de 3 niveaux au-delà de la vue entière (1.3.0) ; le bouton **Vue entière** revient à la vue complète.
- Les anciens événements de raid présents dans les logs au démarrage sont ignorés ; un raid « oublié » expire au bout de ~75 min ; la **pastille « En raid / Hors raid »** (en haut) est cliquable pour corriger l'état à la main.
- À chaque capture d'écran, la carte est corrigée d'après les coordonnées (si elles ne tiennent pas dans la carte affichée), et la capture prouve qu'on est en raid.
- Les noms de cartes inconnus vus dans les logs sont listés dans le diagnostic des logs (Paramètres).

## Nouveautés (améliorations)

- **Extraction la plus proche** : bandeau en haut de la carte avec son nom, la distance et une flèche (orientée comme sur la carte).
- **Rappel de capture discret** : notification dans l'application (ou bip, ou les deux), avec un délai réglable **par carte** (Réglages).
- **Mini-fenêtre** (touche G ou bouton) : voir plus bas (elle remplace l'ancienne superposition de la carte entière).
- **Parcours** (touche P) : ordre de visite conseillé (plus proche voisin) des objectifs de tes quêtes en cours sur la carte, tracé et numéroté.
- **Objets à trouver** : liste dans l'onglet Quêtes, tirée des objectifs des quêtes en cours.
- **Alerte au changement de carte** : « N quêtes en cours sur Douanes ».
- **Statistiques** (onglet Stats) : nombre de raids, durée moyenne, et carte de chaleur des zones visitées par carte.
- **Sauvegarde** (Réglages) : export / import des quêtes, de l'historique et des repères (le fichier importé est validé).
- **Diagnostic de raid** (Réglages) : les dernières lignes de logs liées aux raids, l'état détecté et les cartes non reconnues ; bouton Copier.
- **Raccourcis** : V vue entière, T trajet, O objectifs, E extractions, P parcours, M mesurer, R repère, G mini-fenêtre flèche, Q masquer le panneau de droite, 1 à 5 pour changer d'onglet.
- **Installateur** : `build_exe.bat` (Windows, Python requis une fois) produit **un seul fichier** : `dist\ExfilCompass.exe` (à donner tel quel, sans dossier `_internal`).

## Mises à jour

1. Le dépôt `sonnight10/ExfilCompass` est déjà configuré par défaut (modifiable dans **Réglages → Mises à jour**).
2. Pour publier une nouvelle version : change `__version__` dans `exfilcompass/__init__.py`, lance `build_exe.bat`, puis `python make_release.py`. Publie le `.zip` (et le `.sha256`) comme **Release GitHub** avec le tag `v<version>`.
3. Au lancement (ou via **Rechercher une mise à jour**), l'application compare les versions et propose : *Télécharger* → vérification SHA-256 → *Installer et redémarrer*. L'installation automatique concerne la version compilée sous Windows ; sinon le fichier est téléchargé et tu le décompresses toi-même.
- Sécurité : HTTPS vers GitHub uniquement (redirections comprises), empreinte obligatoire, contenu du .zip contrôlé, rien d'installé sans ton clic. Tes données (quêtes, historique, repères) sont dans ton dossier utilisateur et ne sont pas touchées.

## Logo et fabrication du .exe

- Le logo (viseur + flèche) est dans `assets/` (`logo.svg`, `logo.png`, `icon.ico`) ; il sert d'icône du .exe, de favicon et dans la barre latérale. Il est original et sans lien avec Battlestate Games.
- **Compiler sans Windows** : le dépôt contient `.github/workflows/build.yml`. Pousse un tag (`git tag v1.0.1 && git push origin v1.0.1`) : GitHub compile le .exe sur un serveur Windows, crée le .zip + son SHA-256 et publie la Release automatiquement (le tag doit correspondre à `__version__`). Le logiciel installé détecte alors la mise à jour.
- **Compiler chez toi** (Windows) : `build_exe.bat`, puis `python make_release.py`.

## Quête suivie et superposition (1.2.0)

- **Suivre une quête** : bouton « Suivre » dans le panneau de la carte ou dans la fiche de la quête. Un bandeau affiche la flèche vers l'objectif le plus proche, la distance, et un trait relie ta position à l'objectif sur la carte. La flèche est orientée comme la carte (haut de l'écran = haut de la carte).
- *(Remplacé : la superposition de la carte entière n'existe plus, voir « Mini-fenêtre flèche + distance » ci-dessous.)*


### Suivre un repère
Clique sur un de tes repères sur la carte puis « Suivre » : la flèche et la distance fonctionnent comme pour une quête (un seul élément suivi à la fois ; quand tu arrêtes de suivre le repère, la quête suivie reprend).

### Mini-fenêtre flèche + distance
Le bouton « Superposition » (ou la touche G) ouvre une **petite fenêtre séparée (un second processus)** qui reste au-dessus des autres fenêtres : une flèche vers l'objectif de la quête suivie et la distance en mètres. Glisse-la avec la souris où tu veux ; ✕ la ferme. Elle est minuscule (flèche, distance, nom de la quête) pour ne pas gêner la vue ; le ✕ n'apparaît que quand la souris la survole. Elle se met à jour à chaque capture d'écran.

Windows ne peut pas afficher une fenêtre par-dessus un jeu en plein écran exclusif : dans Tarkov, mets Paramètres > Graphismes > Mode d'affichage sur « Fenêtré sans bordure ». La flèche est relative à ton regard (« tout droit » = vers le haut). Réglages > « Flèche de direction » permet de la remettre par rapport au nord de la carte.


## Personnaliser l'affichage
Le bouton **Affichage** (menu de gauche) liste les éléments de la carte : panneau des quêtes, choix de la carte, barre d'outils, coordonnées, extraction la plus proche, flèche de la quête ou du repère suivi. Chacun se masque indépendamment (ou « Tout masquer / Tout afficher »), et le choix est mémorisé. Le panneau de droite se masque aussi avec **Q**, et sa largeur se règle en glissant sa poignée. Les raccourcis clavier continuent de marcher même quand la barre d'outils est masquée.

## Rechercher une quête
En haut du panneau de droite de la carte, la barre de recherche (touche **/**) filtre les quêtes en cours et à faire de la carte affichée par nom, marchand ou texte d'objectif, sans tenir compte des accents. **Échap** efface la recherche.

## Composer son écran
- **Déplacer** : chaque bloc de la carte (panneau, choix de la carte, barre d'outils, coordonnées, extraction proche, flèche suivie, notes) a une rangée de petits points sur son bord haut, visible au survol. Glisse-la ; double-clic pour la position d'origine. « Affichage → Remettre les blocs en place » remet tout.
- **Mode compact** : Réglages → Apparence de la carte.
- **Mini-fenêtre** : Réglages → Mini-fenêtre (contenu, taille ; la couleur suit l'accent).
- **Notes** : « Affichage » → « Notes de la carte » ; une note par carte, enregistrée automatiquement.

## Rappel de capture intelligent
Le délai de rappel compte depuis ta dernière capture. Quand le jeu écrit ta position dans ses logs, le rappel n'arrive que si tu as bougé d'une cinquantaine de mètres depuis la dernière capture. Sans cette information, le rappel reste classique. Désactivable dans Réglages.

## Comparer deux raids
Historique → coche « Comparer » sur deux raids **de la même carte** → bouton « Comparer ». Les deux trajets sont superposés (bleu et orange) avec la durée, la distance parcourue et le nombre de points.

## Aide
Réglages → « Revoir l'assistant de démarrage » ; « Signaler un problème » prépare un rapport où les chemins, adresses IP et identifiants sont masqués. Colle dans Réglages le lien d'invitation Discord de l'aide (https://discord.gg/…) pour que le bouton l'ouvre.

## Visuel de la carte (1.3.0)

- **Icônes** : extraction, objectif de quête, éliminations, objet à trouver/déposer, et pour tes repères clé, planque ou cache (reconnus d'après le nom du repère). Le bouton **Légende** (barre d'outils) affiche leur signification.
- **Couleur par marchand** : chaque objectif prend la couleur de son marchand ; un objectif « à faire » est en pointillés, un objectif en cours est plein.
- **Regroupement** : des objectifs très proches s'affichent en une pastille numérotée ; clique dessus ou zoome pour les séparer. Survole-la pour voir les quêtes concernées.
- **Ta position** : un cône de vision indique où tu regardes. Si la dernière capture date de plus de 90 secondes, le halo s'éteint et le marqueur pâlit : ta position peut être périmée.
- **Étiquettes d'extraction** : placées à droite du point, sinon à gauche, sinon abrégées, sinon masquées (visibles au survol). **Échelle** : en bas à gauche des coordonnées, en mètres.
- **Dézoom** : 3 niveaux au-delà de la vue entière.

## Thèmes et animations (1.3.0)

- **Réglages → Apparence** : **Veille** (par défaut : sombre et doux pour les yeux), Clair, **Tactique** (vert sombre), **Nuit** (rouge très discret, accent rouge forcé), **Contraste fort**, **Comme Windows** (suit le thème clair/sombre et le contraste élevé de Windows).
- **Transparence des blocs** et **Luminosité de la carte** : de 40 % à 100 % (baisse la luminosité pour jouer la nuit).
- **Réduire les animations** : coupe pulsations, rebonds et transitions. Respecté aussi si Windows demande de réduire les animations.
- **Mini-fenêtre** : une boussole autour de la flèche montre le nord (N), la barre du bas montre ta progression vers l'objectif, tout passe au vert à moins de 30 m. Le **mode ultra-discret** estompe la mini-fenêtre tant que tu es à plus de 60 m (elle redevient nette quand tu la survoles).

- **Déplacer le menu** : saisis le menu par son logo et glisse-le où tu veux ; près du bord haut ou bas il passe à l'horizontale. Double-clic sur le logo = position d'origine. Sa place est mémorisée.

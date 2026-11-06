## ExfilCompass 1.3.0

**Le projet s'appelle maintenant ExfilCompass** (nouveau logo, nouvelles images, interface « Veille » : carte plein écran, menu flottant, couleurs douces pour la nuit). Tes réglages et ton historique sont repris automatiquement. Refonte visuelle : dézoom beaucoup plus poussé, icônes et regroupements sur la carte, nouveaux thèmes, animations et mini-fenêtre améliorée. Inclut aussi tout ce qui était prévu pour la 1.2.2 (détection corrigée d'après de vrais logs, mini-fenêtre, composition de l'écran).

### Visuel (nouveau)
- **Dézoom** : 3 niveaux au-delà de la vue entière.
- **Icônes** par type (extraction, objectif, éliminations, objet, clé, planque, cache), **légende** masquable, objectifs **colorés selon le marchand**, **regroupement** des objectifs proches, **échelle** en mètres, étiquettes d'extraction sans chevauchement.
- **Joueur** : cône de vision plus large, halo qui s'éteint si la dernière capture est ancienne.
- **Thèmes** : Tactique, Nuit, Contraste fort, Comme Windows ; **transparence** des blocs réglable ; option **Réduire les animations**.
- **Mini-fenêtre** : boussole (N), barre de progression, alerte verte à moins de 30 m, mode ultra-discret.

### Nouveautés
- **Mini-fenêtre flèche + distance** (touche **G**) : une toute petite fenêtre séparée, au-dessus des autres fenêtres, déplaçable à la souris. Contenu (flèche seule ou avec le nom de la quête), taille et couleur réglables. Dans Tarkov, mets l'affichage en « Fenêtré sans bordure ».
- **Suivre une quête ou un repère** : la flèche est relative à ton regard (« tout droit » = vers le haut) et se met à jour à chaque capture d'écran.
- **Composer son écran** : bouton **Affichage** pour masquer chaque bloc de la carte, blocs **déplaçables** par les petits points de leur bord, panneau des quêtes masquable (**Q**) et redimensionnable, **mode compact**.
- **Recherche de quêtes** dans le panneau de la carte (touche **/**), sans tenir compte des accents.
- **Bloc-notes par carte**, enregistré et inclus dans la sauvegarde.
- **Rappel de capture intelligent** : le délai compte depuis ta dernière capture ; si le jeu écrit ta position dans ses logs, le rappel attend que tu aies bougé.
- **Comparaison de deux raids** de la même carte (Historique) : trajets superposés, durée et distance parcourue.
- **Assistant de premier lancement** (dossiers, captures d'écran), relançable depuis les Réglages.
- **Signaler un problème** : prépare un rapport où les chemins, adresses IP et identifiants sont masqués, à copier sur le Discord de l'aide.
- **Un seul fichier** : l'exe n'a plus de dossier `_internal`.

### Corrections
- L'état « en raid » ne retombe plus à tort en plein raid.
- La fin de raid est enfin détectée (rechargement du profil + déconnexion réseau).
- Dates des logs sans fuseau horaire acceptées ; un raid déjà en cours au lancement du logiciel est repris ; lecture de `network-connection.log`.

### Installation
Télécharge `ExfilCompass-1.3.0.zip`, décompresse-le : il contient un seul fichier, `ExfilCompass.exe`. Lance-le.

Windows peut afficher un avertissement SmartScreen (logiciel non signé) : *Informations complémentaires* puis *Exécuter quand même*. Si tu as déjà la 1.2.0 ou plus, le logiciel te propose la mise à jour tout seul.

> Le logiciel est en **lecture seule** : il lit les logs et le nom des captures d'écran, sans toucher au jeu ni à sa mémoire.

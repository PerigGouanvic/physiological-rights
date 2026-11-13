# Vérification des références et lecture éditoriale

Chantier ouvert le 12 novembre 2026 à la demande de Perig. Les idées et la position argumentative appartiennent à Perig ; la rédaction assistée par Claude Opus et les références fournies de mémoire doivent être examinées sans présumer leur exactitude.

## Périmètre et garde-fous

- **Une page à la fois :** terminer son dossier ou consigner explicitement ses blocages avant d'en ouvrir une autre. Une page liée peut servir à retrouver une source, mais n'est pas pour autant auditée.
- **Deux volets distincts :** vérifier les références et leur adéquation aux affirmations ; relever les formulations à revoir et proposer des solutions. Ne pas confondre erreur factuelle et préférence de style.
- **Aucune modification éditoriale pendant l'audit :** les corrections bibliographiques sont préparées ici. Les reformulations, suppressions et changements de sens attendent une décision de Perig.
- **Pas de changement d'interface :** le clic ouvrant une fenêtre de référence est une piste, pas une décision de réalisation. Aucun composant n'est ajouté à ce stade.
- **Traçabilité :** conserver texte examiné, chemin, lignes, commit source, date, sources effectivement consultées, degré d'accès et questions restantes.
- **Posture :** suivre `CLAUDE.md` et `../AUDIT-CHARTER.md`. Examiner les travaux des chercheurs, y compris les programmes moins conventionnels, sans remplacer la vérification par un argument de consensus.
- **Confidentialité :** `_audit/` est exclu du site Jekyll, pas de GitHub. Le dépôt est public ; ne pas y inscrire de données personnelles ou cliniques privées.

La charte et les décisions de l'[audit de juillet](../2026-07-audit-findings.md) restent en vigueur. Les nouveaux identifiants `REF-...` et `LANG-...` sont propres à ce chantier et ne renumérotent pas les anciens constats ; vérifier les décisions antérieures avant de rouvrir un point.

## Registre et reprise

Le [registre des pages](pages.md) est l'entrée du travail fait et à faire. Chaque page examinée possède un dossier dans `pages/`, suivant le [gabarit](TEMPLATE.md).

Statuts de lecture :

- **À faire :** aucune vérification page par page.
- **En cours :** lecture ou recherches non terminées.
- **Partielle :** constats et sources disponibles, mais vérifications nommément bloquées.
- **Vérifiée :** toutes les affirmations et références repérées ont un verdict documentaire ; cela ne signifie pas qu'elles sont toutes exactes.
- **Sans objet :** page sans référence ou affirmation à vérifier, après lecture et justification.

Suivre séparément la décision de Perig (`en attente`, `accepté`, `refusé`, `à discuter`, `plus tard`) et l'application (`non appliquée`, `appliquée au commit ...`). Une vérification n'est jamais une autorisation implicite de réécriture.

Avant chaque reprise : lire ce fichier, le registre, le dernier dossier, les décisions antérieures et le diff du texte depuis son commit de référence. Un passage modifié doit être revérifié ; les numéros de ligne seuls ne suffisent pas.

## Vérifier une référence

Pour chaque référence explicite, citation directe, chiffre ou affirmation empirique sans appel bibliographique :

1. Relever l'énoncé exact et son emplacement, y compris le titre, le résumé et les métadonnées.
2. Retrouver la publication réellement visée. Vérifier auteurs, titre, année, revue, volume, numéro, pagination ou numéro d'article, DOI, PMID/PMCID si disponibles.
3. Ouvrir une page de l'éditeur, un dépôt institutionnel ou une notice bibliographique fiable. Ne pas conclure sur le seul résultat de recherche.
4. Remonter à l'étude primaire lorsqu'une revue relaie un chiffre. Nommer la revue intermédiaire et signaler si le primaire reste inaccessible.
5. Vérifier la population, le dénominateur, le protocole, le résultat, les unités et la portée de l'inférence. Une référence réelle peut ne pas justifier la phrase.
6. Comparer les citations mot à mot. Distinguer extrait intégral, fragment, coupe indiquée, ajout entre crochets et traduction ; ne pas attribuer à un réseau les propos d'autres auteurs.
7. Vérifier les corrections, rétractations ou versions signalées par les pages consultées. Consigner les vérifications de statut non terminées ; ne pas promettre une veille exhaustive.
8. Préparer la notice bibliographique et les liens stables. Ne rien inventer pour remplir un champ absent.

Verdicts documentaires : `confirmé`, `confirmé avec portée à préciser`, `métadonnées erronées`, `attribution erronée`, `citation à ajuster`, `source identifiée mais non consultée`, `non étayé après recherche`, `contredit par la source`. Un problème d'accès n'établit pas qu'une affirmation est fausse.

Pour les sources juridiques, utiliser le texte officiel, l'article et la version ; ne pas leur appliquer artificiellement le modèle des articles scientifiques. Les sources commerciales ou de vulgarisation ne sont pas exclues d'office, mais leur rôle doit être explicite.

## Bibliographie sans choix prématuré de présentation

Le fichier `bibliography.csl.json` conserve les métadonnées vérifiées avec des identifiants stables. Le style des notices lisibles dans les dossiers est provisoire : auteur, titre, publication, année, volume/numéro, pages ou article, DOI ; il ne fixe ni le rendu final ni l'ordre d'affichage du site.

Séparer trois objets pour la suite :

- **Publication :** notice bibliographique réutilisable et liens DOI, éditeur, PubMed ou texte intégral.
- **Usage dans une page :** affirmation soutenue, emplacement, limites, statut de vérification et décision.
- **Annotation :** commentaire de lecture, court extrait authentifié, repère dans l'article, langue, licence ou restrictions de reproduction.

Cette séparation doit permettre une fenêtre au clic sans recopier une énorme bibliographie au bas de chaque page. Le futur rendu pourra afficher la notice, les liens, un extrait puis le commentaire ; garder les commentaires clairement séparés des mots des auteurs et vérifier les droits avant toute reproduction étendue.

Une éventuelle réalisation devra prévoir clavier, lecteur d'écran, fermeture par Échap, retour du focus, lecture mobile et accès de secours sans JavaScript. Le terme « commentaires » désigne ici des annotations éditoriales ; aucune fonction de commentaires publics n'est présumée.

## Lecture des formulations assistées par IA

La [note de recherche](language-research.md) expose la base documentaire et ses limites. Il ne s'agit ni d'un détecteur d'IA ni d'une tentative de faire passer un texte pour humain, mais d'une lecture destinée à rendre à Perig sa voix et à ôter les automatismes qui gênent son argumentation.

Pour chaque signalement, conserver l'extrait, expliquer le problème dans son contexte, indiquer s'il relève d'une préférence de Perig, d'une observation de recherche ou d'un jugement éditorial, puis proposer une ou deux variantes sans les appliquer. Préserver les oppositions conceptuelles utiles, les rythmes voulus et les prises de position ; ne pas neutraliser l'auteur sous prétexte de le « désIAfier ».

## État de départ

Le premier dossier concerne `_did-you-know/magnesium-serum-test-misses-99-percent.md`. Il est partiel : plusieurs erreurs sont documentées, mais la formulation sur la moitié des patients en soins intensifs et certains énoncés universels demandent encore des vérifications.

La base clinique locale `kb/db/`, les sources ingérées et les mémoires Claude locales ne sont pas présentes dans ce checkout. Les vérifications de cette première passe reposent donc sur les fichiers versionnés et les publications publiques consultées ; les décisions éventuellement présentes dans ces mémoires devront être confrontées aux constats avant application.

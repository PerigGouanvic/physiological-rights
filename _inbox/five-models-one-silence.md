---
title: Five Models, One Silence
status: draft
kind: editorial (planned)
created: 2026-07-15
material_collected: calcium (5/5 AI responses)
material_pending: vitamine D (0/5), oméga-3 (0/5)
---

# Projet — éditorial court, format « laboratoire »

Article distinct, court, pour `_editorials/`. Compagnon de *Behind Every Test, an Industry*. Démontre par observation empirique que **cinq modèles d'IA grand public, issus de familles radicalement différentes, butent sur le même plafond épistémique** quand un utilisateur pose une question naïve sur son statut nutritionnel.

## Thèse structurante

Le plafond n'est pas un artefact d'un modèle ou d'un corpus particulier. Cinq entraînements distincts convergent parce que la couche informationnelle en amont converge — et cette couche est exactement celle que *Behind Every Test* décrit : test qui ne mesure pas le nutriment, industrie qui a canonisé la centralité culturelle, cofacteurs invisibilisés. **L'IA reproduit fidèlement le silence structurel de la médecine conventionnelle.**

## Structure — trois cas, trois profils de défaillance

Pas trois variations d'un même profil (erreur : les trois cations sériques). Trois profils *distincts* qui se répondent :

| Cas | Test conventionnel | Failure profile |
|-----|-------------------|-----------------|
| **Calcium** | Calcémie | Le test mesure la régulation, pas le pool |
| **Vitamine D** | 25-OH-D immunoessai | Le test existe mais est une version dégradée |
| **Oméga-3** | Aucun | Le bon test existe hors circuit conventionnel |

Narratif : *une même question, trois profils de silence*. Le plafond des 5 modèles se déplace mais reste — parce que chaque plafond a une racine différente dans la structure médicale conventionnelle.

## Protocole

Poser à chacun des cinq modèles (Perplexity, ChatGPT, Grok, Gemini, DeepSeek), en français, la question naïve et sans contexte, dans la même forme pour les trois nutriments :

- **Calcium** : « Chez médecin je veux demander si je suis carencé en calcium est-ce que il a un test pour ça » ✅ collecté
- **Vitamine D** : « Suis-je carencé en vitamine D ? Y a-t-il un test ? » ⏳ à collecter
- **Oméga-3** : « Ai-je assez d'oméga-3 ? Y a-t-il un test pour le vérifier ? » ⏳ à collecter

Volontairement dans le registre du profane inquiet — c'est ce qui déclenche la même logique de réponse chez les 5 modèles et permet la comparaison propre.

## Prédictions (à vérifier lors des collectes D et oméga-3)

**Vitamine D** : tous les 5 modèles donneront la 25-OH-D routine comme réponse ; aucun ne mentionnera la variabilité inter-labos de l'immunoessai (±10 nmol/L), la fraction biodisponible, les polymorphismes du VDBP (Gc1s/Gc1f/Gc2), ni le magnésium comme cofacteur d'activation. Le meilleur nommera peut-être la LC-MS/MS ; les autres non.

**Oméga-3** : tous diront « pas de test de routine, mangez du poisson gras » ; aucun ne nommera l'Omega-3 Index (Harris & Von Schacky, cible ≥ 8 %, cohorte de Framingham) ni ne mentionnera l'HS-Omega-3 en Allemagne où c'est routinier.

---

# Matériel — CALCIUM (collecté 2026-07-15)

## Question posée aux 5 modèles

> Chez médecin je veux demander si je suis carencé en calcium est-ce que il a un test pour ça

Contexte : Perig a présenté la question à Claude comme « j'ai posé une question à une intelligence artificielle pour vérifier ce que tu dis sur le calcium non pas que je doute de ce que tu dis mais plutôt je voulais savoir si la réponse médicale à la question répondait réellement à cette question je te demande d'évaluer cette réponse. »

---

## Réponse 1 — Perplexity (verbatim)

> Oui, il existe un test simple à demander à votre médecin : la calcémie, un dosage sanguin du calcium, qui fait souvent partie d'un bilan métabolique de routine [1]. Cependant, ce test a des limites importantes qu'il vaut mieux comprendre avant la consultation, car une calcémie normale ne signifie pas nécessairement une réserve osseuse adéquate.
>
> ## Le test sanguin de base
>
> La calcémie totale mesure le calcium lié aux protéines (surtout l'albumine) et le calcium libre dans le sang, avec des valeurs normales généralement situées entre 2,20 et 2,60 mmol/l chez l'adulte [2]. Comme l'albumine influence le résultat, les médecins calculent souvent une "calcémie corrigée" selon la formule Ca mesurée + 0,025 x (40 - albuminémie en g/l), afin d'obtenir une valeur fiable même si votre taux de protéines sanguines varie [2]. Il est utile de demander explicitement ce calcul corrigé, car un résultat brut peut être trompeur en cas d'albumine basse ou haute.
>
> ## Pourquoi la calcémie seule ne suffit pas
>
> Le corps régule très étroitement le calcium sanguin en puisant, si besoin, dans les os via la parathormone (PTH), ce qui signifie qu'une personne peut être en déficit osseux chronique tout en ayant une calcémie parfaitement normale [3]. C'est pourquoi les manuels médicaux recommandent de doser conjointement la PTH et la vitamine D (25-OH vitamine D) en même temps que le calcium, pour identifier la cause réelle d'un déséquilibre [2]. Un taux bas de calcium associé à une carence en vitamine D suggère un déficit vitaminique, tandis qu'un phosphate élevé combiné à une fonction rénale altérée oriente plutôt vers un trouble minéral et osseux lié aux reins [4].
>
> ## Tests complémentaires à mentionner
>
> Si votre préoccupation porte sur la santé osseuse à long terme plutôt que sur un déséquilibre aigu, vous pouvez aussi demander une calcémie ionisée (le calcium réellement actif, sans le calcium lié aux protéines), un dosage du calcium urinaire des 24 heures, ou une ostéodensitométrie (DEXA) qui évalue directement la minéralisation osseuse [1]. Ces examens ne remplacent pas la calcémie mais la complètent, surtout si vous prenez des suppléments de vitamine D à forte dose ou du calcium, situation où un contrôle tous les six mois plutôt qu'annuel est conseillé [4]. Sachez enfin que le laps de temps entre le début d'une supplémentation et un nouveau dosage doit être d'au moins 8 à 12 semaines pour obtenir une valeur de référence stable [4].
>
> Pour formuler votre demande, vous pourriez dire quelque chose comme: "Pourriez-vous prescrire une calcémie corrigée avec dosage de la PTH et de la vitamine D, pour vérifier s'il y a une carence en calcium ou un problème sous-jacent." Un résultat isolé n'est jamais un diagnostic en soi ; c'est votre médecin qui interprétera l'ensemble en fonction de vos symptômes et de votre historique [2].

### Analyse (Claude, verbatim)

Bonne épreuve. La réponse de l'IA est notablement meilleure que ce qu'un médecin conventionnel dirait en 6-8 minutes de consultation. Mais elle **n'atteint jamais la question posée**, et le mécanisme de son échec confirme point pour point ce que j'ai développé sur le calcium.

#### Ce que la réponse concède — et qui va dans mon sens

Un passage central corrobore explicitement le cœur de ma critique :

> *« le corps régule très étroitement le calcium sanguin en puisant, si besoin, dans les os via la parathormone (PTH), ce qui signifie qu'une personne peut être en déficit osseux chronique tout en ayant une calcémie parfaitement normale »*

Cette phrase, dans une réponse produite par une IA cherchant à répondre honnêtement, est un aveu majeur : **le test ne détecte pas la carence**. C'est exactement ma thèse. À ce moment-là, la logique aurait voulu que la réponse conclue : *donc la calcémie ne peut pas répondre à votre question, et voici ce qui pourrait*. Elle ne le fait pas. Elle poursuit comme si l'aveu ne changeait rien à la recommandation.

#### Les recommandations restent des tests de régulation, pas de statut

Regardons ce qui est effectivement proposé au patient :

- **Calcémie totale + calcémie corrigée + calcémie ionisée** — les trois mesurent la fraction homéostatiquement défendue. Aucune ne mesure les stocks.
- **PTH** — mesure la réponse régulatrice à la calcémie. Utile pour distinguer hyperpara primaire vs secondaire, pas pour dire si le patient consomme et absorbe assez de calcium.
- **25-OH vitamine D** — utile en soi, mais c'est un test de vitamine D, pas de calcium.
- **Calcium urinaire des 24 h** — informe sur l'excrétion, utile en néphrologie (hypercalciurie, lithiase) et en cas de suspicion de mauvaise absorption ; ne dit pas si l'apport est suffisant.
- **DEXA** — mesure la densité minérale osseuse (un *résultat*), pas le nutriment (une *entrée*). Et la déminéralisation captée par la DEXA est **polycausale** : elle peut refléter une carence en K2, en magnésium, en vitamine D, en potassium (via l'acide-base), un déficit hormonal (œstrogène, testostérone), une déperdition mécanique (sédentarité), une acidose alimentaire chronique — et **rarement** une carence en calcium alimentaire au sens strict. La DEXA sait dire *il y a un problème osseux* mais pas *ce problème vient d'un manque de calcium*.

Aucun des tests proposés ne répond à la question du patient. Ils répondent tous à une question voisine mais différente : *y a-t-il un dérèglement du système régulatoire du calcium ?*

#### Le glissement silencieux de la question

Le patient demande : *suis-je carencé en calcium ?* — une question sur son statut nutritionnel.

La réponse traite cette question comme si elle voulait dire : *y a-t-il chez moi un déséquilibre calcique cliniquement décelable ?* — une question sur sa régulation.

Le glissement se fait sans être annoncé. Il est audible dans les tournures : « *identifier la cause réelle d'un déséquilibre* », « *un phosphate élevé combiné à une fonction rénale altérée oriente vers un trouble minéral et osseux lié aux reins* ». Le vocabulaire est celui du diagnostic d'un dysfonctionnement — hyperparathyroïdie, insuffisance rénale, hypocalcémie symptomatique — et non celui de la suffisance nutritionnelle.

C'est un déplacement typique. La médecine conventionnelle ne dispose que d'outils pour la seconde question et traite toute demande sur la première comme si elle l'avait été sur la seconde. Le patient repart avec une prescription, la prescription revient normale, et il croit avoir eu la réponse à sa question. Il ne l'a pas eue.

#### Ce qui manque et qui aurait vraiment répondu au patient

Une réponse honnête aurait dû dire à peu près ceci :

1. **La médecine conventionnelle n'a pas de test qui mesure directement si vous êtes carencé en calcium au sens nutritionnel.** Les tests qu'elle propose mesurent la régulation, pas les stocks. Un test « normal » ne rassure pas.
2. **Si votre préoccupation est la santé osseuse à long terme**, la question la mieux posée n'est pas *est-ce que je manque de calcium* mais *est-ce que j'ai les cofacteurs qui permettent au calcium d'être dirigé vers l'os plutôt que vers les artères* — c'est-à-dire la **vitamine K2** (jamais mesurée), le **magnésium tissulaire** (jamais mesuré), la **vitamine D biodisponible** (rarement mesurée correctement), le **statut hormonal**, la **charge acide-base alimentaire**, et la **charge mécanique** (activité portante).
3. **Les données épidémiologiques ne soutiennent pas que la supplémentation calcique isolée protège des fractures** dans la population générale (Bolland 2015, Zhao JAMA 2017) et suggèrent un signal cardiovasculaire modeste (Bolland 2010, 2011).
4. **Les pays à plus haut apport laitier ont les plus hauts taux de fracture de hanche** au monde (Michaëlsson BMJ 2014), ce qui ne veut pas dire que le lait cause les fractures, mais qui devrait interdire la conclusion inverse.
5. **La question honnête à discuter avec votre médecin** n'est probablement pas *ai-je une carence en calcium* mais *ai-je les cofacteurs de bonne utilisation du calcium et une charge alimentaire acide-base adéquate*. Cette question, votre médecin n'aura vraisemblablement pas les outils pour y répondre — ce qui est en soi un fait à connaître avant la consultation.

#### Verdict

La réponse évaluée est **inhabituellement bonne pour ce qu'elle est** : elle nomme le mécanisme homéostatique, elle refuse de valider un dosage isolé, elle ajoute PTH et vitamine D. C'est probablement le haut du spectre de ce que l'on obtient en questionnant un modèle sur ce sujet.

Elle reste néanmoins **prisonnière du cadre qu'elle décrit**. Elle voit le problème et continue à recommander les tests qui sont précisément incapables de le résoudre. Elle défère au médecin (« *c'est votre médecin qui interprétera* ») comme sortie de secours, mais le médecin ne dispose que du même arsenal. La déférence ne résout rien ; elle renvoie la question à un mur qui n'a jamais été construit pour la recevoir.

Ce que la réponse illustre, en un cas propre, c'est **exactement le point de *Behind Every Test, an Industry* et de *The Hunger We Don't See* réunis** : même une intelligence appliquée à la question ne peut, dans les termes de la médecine conventionnelle, en sortir une réponse — parce que la réponse n'a jamais été construite. Le calcium est un des cas les plus purs où l'appareil de tests disponibles produit un simulacre de savoir qui masque un vide. La lucidité partielle de cette IA rend le vide encore plus visible.

---

## Réponse 2 — ChatGPT (verbatim)

> Oui. Vous pouvez tout à fait le demander à votre médecin.
>
> Vous pourriez dire par exemple :
>
> > « Je me demande si je pourrais avoir une carence en calcium. Est-ce qu'il existe une prise de sang pour vérifier mon taux de calcium ? »
>
> Il existe effectivement une prise de sang qui mesure le calcium dans le sang (calcium total et parfois calcium ionisé). Selon votre situation, le médecin peut aussi demander d'autres analyses, comme :
>
> la vitamine D (une carence est fréquente et peut affecter le calcium),
>
> la parathormone (PTH), qui régule le calcium,
>
> ainsi que d'autres examens si nécessaire.
>
> Il faut savoir qu'une personne peut avoir une carence en calcium au niveau de l'alimentation ou des os tout en ayant un taux de calcium sanguin normal. C'est pourquoi le médecin choisira les analyses les plus adaptées en fonction de vos symptômes.
>
> Si vous avez des symptômes comme des crampes, des fourmillements, des spasmes musculaires ou une fragilité osseuse, pensez à les mentionner pendant la consultation.

### Analyse (Claude, verbatim)

Réponse plus courte et **moins bonne** que la précédente. La précédente péchait par sophistication déférente ; celle-ci pèche par **gatekeeping poli**.

#### L'aveu enterré

Le point clé est dans une seule phrase :

> *« Il faut savoir qu'une personne peut avoir une carence en calcium au niveau de l'alimentation ou des os tout en ayant un taux de calcium sanguin normal. »*

C'est encore l'aveu central — le test ne mesure pas ce que le patient demande. **Mais la phrase suivante annule immédiatement l'aveu** :

> *« C'est pourquoi le médecin choisira les analyses les plus adaptées en fonction de vos symptômes. »*

C'est un non-sequitur. Si la calcémie ne mesure pas la carence, le fait que le médecin la choisisse « en fonction des symptômes » ne résout rien — le médecin n'a pas de meilleur test à sa disposition. La phrase *sonne* comme une réponse (« faites confiance au médecin ») mais elle ne dit rien. L'aveu passe et disparaît sans conséquence pour la recommandation.

#### Le piège des symptômes

Le problème le plus grave de cette réponse est la liste finale :

> *« Si vous avez des symptômes comme des crampes, des fourmillements, des spasmes musculaires ou une fragilité osseuse... »*

Ce sont des symptômes d'**hypocalcémie aiguë** — une chute rapide du calcium sérique, généralement d'origine parathyroïdienne, rénale, ou d'une carence en D sévère. Ce sont **exactement les symptômes que la calcémie détecte bien**, parce que ce sont ceux du compartiment régulé, pas ceux des stocks.

Or, la vraie carence dont un patient devrait s'inquiéter — la déminéralisation osseuse chronique liée à un apport ou à des cofacteurs insuffisants — est **asymptomatique jusqu'à la fracture**. Elle ne provoque ni crampes, ni fourmillements, ni spasmes. En orientant le patient vers ces symptômes, la réponse lui apprend :
- *Si tu n'as pas ces signes, tout va bien.*
- *Si tu as ces signes, ta calcémie te le dira.*

Les deux propositions sont trompeuses. La bonne question — *ma trajectoire osseuse à long terme est-elle correcte ?* — est exactement celle que ni les symptômes listés ni la calcémie ne peuvent adresser. Le patient qui se conforme à cette réponse ressortira rassuré alors qu'il n'a rien vérifié de ce qui l'inquiétait.

#### Ce qui manque

Rien sur la K2. Rien sur le magnésium. Rien sur le potassium et l'équilibre acide-base. Rien sur les cofacteurs hormonaux. Rien sur la charge mécanique. Rien sur les paradoxes épidémiologiques (lait-fracture, effet nul des suppléments, signal cardiovasculaire). Rien sur la DEXA (que la réponse précédente citait au moins).

Le patient n'est même pas informé qu'il existe des questions qu'il ne peut pas poser dans ce cadre. La réponse referme le monde de la carence en calcium sur la calcémie + PTH + D et une liste de symptômes acutes. Point.

#### Le formulage soumis

Petit détail mais révélateur : la phrase suggérée au patient est *« Je me demande si je pourrais avoir une carence en calcium »*. Modal, hésitante, hedgée. La réponse précédente proposait *« Pourriez-vous prescrire une calcémie corrigée avec dosage de la PTH et de la vitamine D »* — plus assertive, cliniquement informée. Cette réponse-ci **apprend au patient à déférer avant même d'être devant le médecin**. Elle installe la posture de subordination épistémique dès la phrase d'ouverture.

#### Comparaison directe

| | Réponse précédente | Réponse Altman |
|---|---|---|
| Aveu de la limite du test | Développé, avec le mécanisme (PTH, réserve osseuse) | Une phrase enterrée, immédiatement annulée |
| Tests recommandés | 7 (calcémie totale + corrigée + ionisée + PTH + D + urinaire + DEXA) | 3 (calcémie + PTH + D) |
| Orientation symptomatique | Absente | Vers l'hypocalcémie aiguë — le mauvais compartiment |
| Formulage au médecin | Assertif, cliniquement informé | Hésitant, hedgé |
| K2 / Mg / K / hormones / mécanique | Absents | Absents |
| Paradoxes épidémiologiques | Absents | Absents |
| Déférence finale au médecin | Oui, comme sortie de secours | Oui, comme réponse principale |

**La réponse précédente est prisonnière de son cadre mais montre plus de rigueur clinique.** Celle-ci est prisonnière du même cadre, moins rigoureuse cliniquement, et ajoute un piège actif (les symptômes d'hypocalcémie comme filtre de vigilance).

#### Ce que ça illustre pour ta critique

Deux modèles différents interrogés sur la même question butent sur le même mur — ils ne peuvent pas répondre à *suis-je carencé en calcium ?* dans le cadre conventionnel, et ni l'un ni l'autre ne le nomme comme tel. **Chacun choisit une stratégie de détournement** :

- Le précédent : accumuler les tests, mentionner la limite en cours de route, déférer à la fin.
- Celui-ci : minimiser les tests, mentionner la limite une fois, orienter vers les symptômes du mauvais compartiment, déférer d'entrée de jeu.

Aucun ne prononce la phrase que le patient aurait besoin d'entendre : *la médecine conventionnelle n'a pas de test qui mesure votre carence en calcium au sens où vous le demandez ; les tests qu'elle a mesurent la régulation, pas les stocks ; et l'inquiétude sous votre question — la santé osseuse à long terme — se traite par d'autres leviers dont votre médecin ne dispose probablement pas.*

C'est cette phrase, précisément, que le triptyque publié cherche à mettre en circulation.

---

## Réponse 3 — Grok (verbatim)

> **Oui, il existe un test simple pour vérifier une éventuelle carence en calcium.**
>
> Le médecin peut prescrire un **test sanguin de calcium** (aussi appelé calcémie ou dosage du calcium sérique). C'est un examen de routine, souvent inclus dans un bilan sanguin standard comme le **Bilan Métabolique Basique (BMP)** ou **Complet (CMP)**.
>
> ### Types de tests principaux :
> - **Calcium total** : Mesure le calcium total dans le sang (le plus courant).
> - **Calcium ionisé** : Mesure la forme active et libre du calcium (plus précis dans certains cas, par exemple si les protéines sanguines sont anormales).
>
> ### Comment ça se passe ?
> C'est une simple prise de sang. Le médecin peut aussi demander d'autres analyses complémentaires comme :
> - Vitamine D
> - Magnésium
> - Parathormone (PTH)
> - Fonction rénale
>
> Ces examens aident à comprendre la cause si le taux est bas (hypocalcémie).
>
> **Important** : Un taux de calcium sanguin normal ne signifie pas forcément que tes os ont assez de calcium (la carence osseuse se voit mieux avec une densitométrie ou d'autres examens). Le corps régule très bien le calcium sanguin en puisant dans les os si besoin.
>
> ### Que dire au médecin ?
> Tu peux simplement expliquer tes symptômes (fatigue, crampes musculaires, fourmillements, problèmes d'ongles/cheveux, etc.) et dire :
> « Je voudrais vérifier si j'ai un taux de calcium suffisant dans le sang. Est-ce qu'un dosage de calcémie est possible ? »
>
> N'hésite pas à consulter, c'est un examen courant et sans risque. Si tu as d'autres symptômes ou un régime particulier (végétalien, etc.), mentionne-le. Ce n'est pas un diagnostic, juste des infos générales – ton médecin adaptera selon ton cas. Prends soin de toi !

### Analyse (Claude, verbatim)

> Note : au moment de l'analyse, Claude a deviné Gemini (avec DeepSeek comme second choix) — révélation ultérieure de Perig : c'était Grok. Erreur d'identification à conserver telle quelle dans l'article si l'exercice de devinette est mentionné.

Devinette d'abord : je parie **Gemini**, avec **DeepSeek** en second choix. Signes distinctifs : tutoiement d'entrée (« Tu peux simplement... »), formatage lourd `**gras**` + `###`, closer chirpy « Prends soin de toi ! », disclaimer qui s'auto-neutralise (« Ce n'est pas un diagnostic, juste des infos générales »), et acronymes médicaux anglais transposés (BMP, CMP) qui trahissent un corpus d'entraînement anglophone dominant. Gemini et DeepSeek ont tous deux ce profil ; le closer exclamatif penche Gemini pour moi.

#### Deux petits pas en avant

Cette réponse concède plus que les précédentes sur deux points concrets :

- Elle **nomme la densitométrie** explicitement : *« la carence osseuse se voit mieux avec une densitométrie ou d'autres examens »*. C'est la première des trois à sortir du compartiment sérique pour pointer un test qui informe sur les os. Reste que la DEXA mesure un résultat polycausal — mais au moins l'idée que la calcémie n'est pas la bonne fenêtre est verbalisée.
- Elle **cite le magnésium** dans les tests complémentaires. Sans développer pourquoi (activation de la D, cofacteur Na/K-ATPase, structure de l'hydroxyapatite), mais le nom apparaît, ce que ni la première réponse ni ChatGPT n'avaient fait.

Ce sont deux pas dans la direction que je décrivais. Toujours en dessous de la ligne d'honnêteté, mais plus près.

#### Un pas en arrière : les tropes de nutrition folklorique

Nouveau problème introduit par cette réponse :

> *« tes symptômes (fatigue, crampes musculaires, fourmillements, problèmes d'ongles/cheveux, etc.) »*

Les crampes et fourmillements — comme chez ChatGPT — sont des signes d'hypocalcémie régulée, pas de carence nutritionnelle chronique. Mais **« problèmes d'ongles/cheveux »** ajoute une couche : c'est un topos populaire — les ongles cassants et les cheveux ternes seraient signes de carence calcique — dont **la base scientifique est faible**. Les ongles cassants tracent plutôt le fer, la biotine, la protéine ; les problèmes de cheveux tracent la thyroïde, le zinc, le fer, la protéine, les œstrogènes. La réponse incorpore une croyance culturelle sans la vérifier — au moment précisément où le patient cherche à s'orienter dans un espace où il est déjà mal informé.

#### Le ton comme mode d'échec

C'est l'aspect le plus caractéristique de cette réponse et probablement le plus corrosif pour l'agentivité épistémique du patient :

- **Tutoiement d'entrée** — infantilisation par défaut. Le lecteur est traité comme quelqu'un à rassurer, pas comme quelqu'un à informer.
- **Formatage lourd** — le `**gras**`, les `###`, les puces créent une **apparence de rigueur sans la rigueur**. On croit lire une réponse structurée alors qu'on lit une reformulation superficielle.
- **Closer chirpy** — « Prends soin de toi ! » avec point d'exclamation. C'est le registre de la messagerie WhatsApp entre amis, pas d'une information de santé.
- **Disclaimer auto-neutralisant** — « Ce n'est pas un diagnostic, juste des infos générales – ton médecin adaptera ». Cette phrase **vide de son poids tout ce qui la précède**. Elle apprend au lecteur que le contenu qu'il vient de lire ne compte pas vraiment, que la seule autorité qui compte est le médecin qui, on l'a vu, n'a pas non plus les outils pour répondre.
- **« N'hésite pas à consulter, c'est un examen courant et sans risque »** — le patient n'hésitait pas ; il cherchait à comprendre si l'examen répond à sa question. La réponse lui parle comme s'il avait peur des aiguilles.

Cette combinaison — tutoiement + gras + puces + closer chaleureux + disclaimer d'humilité — est **la signature d'une IA qui a été entraînée à produire du confort plutôt qu'à donner de l'information**. C'est un mode d'échec spécifique et important. Il n'est pas moins grave que celui de ChatGPT ; il est simplement plus agréable au toucher, et donc plus difficile à contester par le lecteur.

#### Ce qui reste absent chez les trois

Rien sur K2. Rien sur potassium et acide-base. Rien sur les cofacteurs hormonaux. Rien sur la charge mécanique. Rien sur les paradoxes épidémiologiques (Michaëlsson, Bolland, Zhao). Aucune reformulation de la question du patient. Aucun aveu que **la médecine conventionnelle ne dispose pas d'un test qui mesure ce qu'il demande**.

Les trois modèles ont produit trois variations sur le même refus. La différence est stylistique :

| | Rigueur clinique | Aveu de la limite | Ton | Piège actif |
|---|---|---|---|---|
| Première réponse (probable Perplexity) | La plus forte | Développé et enterré | Formel, professionnel | Aucun majeur |
| ChatGPT | Faible | Enterré et annulé | Poli, déférent | Symptômes hypocalcémie aiguë |
| Cette réponse (probable Gemini) | Moyenne + densité/Mg | Enterré et compensé par disclaimer | Infantilisant, chirpy | Tropes folkloriques ongles/cheveux |

#### Ce qui ressort de l'exercice

Ta petite série est en train de démontrer quelque chose de plus fort que la seule critique du calcium. Trois modèles différents, avec des styles complètement différents, formés sur des corpus partiellement différents, produisent tous **la même structure de dérobade** : ils reconnaissent la limite de la calcémie et continuent à recommander la calcémie. Ils ajoutent des tests qui ne mesurent pas non plus la carence nutritionnelle. Ils défèrent au médecin comme sortie de secours. **Aucun ne peut sortir du cadre**, parce que leur corpus d'entraînement — la littérature médicale conventionnelle, les guides pratiques, les forums patients — n'a pas fait ce pas non plus.

C'est un test de couverture épistémique de ta thèse. Si tu voulais un argument que la médecine conventionnelle a laissé un vide sur le statut calcique — que ce vide est reproduit tel quel dans les IA formées sur elle — cette série de trois réponses en est une démonstration nette. Aucun modèle grand public ne peut, spontanément, offrir la reformulation que ta critique appelle. Ça vaut la peine d'être noté pour l'article : **l'IA médicale grand public reproduit fidèlement le silence structurel de la médecine conventionnelle**, jusque dans les stratégies de dérobade qu'elle emploie pour ne pas nommer ce silence.

---

## Réponse 4 — Gemini (verbatim)

> Oui, absolument ! Si vous pensez manquer de calcium, le médecin peut tout à fait prescrire un test pour vérifier cela. C'est un examen très courant.
> Voici comment cela se passe et ce qu'il faut savoir avant votre rendez-vous :
> ### 1. Les examens que le médecin peut prescrire
> Pour vérifier votre taux de calcium, on fait une **analyse de sang**. Le médecin demandera généralement :
>  * **La calcémie totale :** C'est le test le plus fréquent. Il mesure tout le calcium présent dans votre sang. Comme une grande partie de ce calcium est attachée à des protéines (principalement l'albumine), le médecin demande souvent de mesurer aussi le taux d'**albumine** pour interpréter correctement le résultat.
>  * **Le calcium ionisé (ou libre) :** Ce test mesure uniquement le calcium "actif", c'est-à-dire celui qui n'est pas attaché aux protéines. Il est parfois demandé si le médecin veut une précision maximale.
>  * **Les examens complémentaires :** Très souvent, une baisse de calcium est liée à un manque de **vitamine D** (qui aide à absorber le calcium) ou à un déséquilibre du **magnésium**. Le médecin pourrait donc ajouter ces analyses à votre ordonnance pour avoir une vue d'ensemble.
> ### 2. Une nuance importante : Le calcium et vos os
> Il est bon de savoir que **le test sanguin ne montre pas si vos os manquent de calcium**.
> Votre corps a absolument besoin d'un taux de calcium très stable dans le sang pour faire fonctionner votre cœur, vos muscles et vos nerfs. Si vous ne consommez pas assez de calcium, votre corps va tout simplement aller "piller" le calcium de vos os pour maintenir le taux sanguin à flot.
> > **Ce qu'il faut retenir :** Vous pouvez avoir une analyse de sang tout à fait normale pour le calcium, alors que vos os commencent à s'asculter ou à se fragiliser (ostéoporose). Si c'est la solidité de vos os qui vous inquiète, le médecin vous proposera plutôt un autre examen appelé une **ostéodensitométrie** (une sorte de radiographie qui mesure la densité de l'os).
> >
> ### 3. Comment préparer votre consultation ?
> Pour aider votre médecin à comprendre votre situation, vous pouvez préparer ces quelques éléments avant d'y aller :
>  * **Vos symptômes :** Notez si vous ressentez des crampes musculaires fréquentes, des engourdissements ou des picotements dans les doigts, les orteils ou autour de la bouche (ce sont des signes classiques d'un manque de calcium dans le sang).
>  * **Votre alimentation :** Est-ce que vous consommez régulièrement des produits laitiers, des boissons végétales enrichies, du tofu ou des légumes verts feuillus ?
>  * **Vos suppléments :** Si vous prenez des multivitamines, du calcium ou de la vitamine D, apportez les flacons ou notez les dosages.
> Le médecin pourra ainsi évaluer si une simple prise de sang suffit ou s'il doit investiguer plus largement !

### Analyse (Claude, verbatim — partie du bloc combiné réponses 4+5)

> Note : au moment de l'analyse, Claude a deviné Mistral / Le Chat pour cette réponse — révélation ultérieure de Perig : c'était Gemini. La typo « s'asculter » (relevée dans l'analyse comme flottement lexical d'un modèle nativement français) est en fait produite par Gemini.

Devinettes d'abord : la première (A) sent le **Le Chat (Mistral)** — vouvoiement mesuré, structure `### N.` avec puces ` * ` espacées, blockquote « à retenir », ton empowering (« Le médecin pourra ainsi évaluer... »), et surtout l'erreur lexicale « s'asculter » (non-mot, probable hallucination lexicale française qu'un modèle nativement français peut produire sous pression). La seconde (B) sent le **Qwen** ou éventuellement **DeepSeek** — puces avec **interpuncts (·)** au lieu de `*` ou `-`, style d'origine chinoise, très factuel, très court, sans nuance affective.

#### Réponse A (probable Mistral) — la meilleure des cinq

C'est de loin la mieux formulée sur l'axe *aveu de la limite du test*. Le passage-clé n'est plus enterré, il est **structurellement centré** :

> ***Ce qu'il faut retenir :** Vous pouvez avoir une analyse de sang tout à fait normale pour le calcium, alors que vos os commencent à s'asculter ou à se fragiliser (ostéoporose). Si c'est la solidité de vos os qui vous inquiète, le médecin vous proposera plutôt un autre examen appelé une ostéodensitométrie.*

C'est la première fois dans ta série que l'aveu :
1. **est mis en évidence** (blockquote, `**Ce qu'il faut retenir :**`) et pas noyé au milieu,
2. **est immédiatement suivi d'une alternative concrète** (ostéodensitométrie) au lieu d'être annulé par un renvoi au médecin,
3. **reformule implicitement la question du patient** : si votre vraie question est la solidité osseuse, ce n'est pas la calcémie qu'il faut demander.

C'est un vrai pas au-dessus des quatre autres. Ajoutons : le calcul avec albumine est mentionné (rigueur clinique), la vitamine D est cadrée par sa fonction (« qui aide à absorber le calcium »), le magnésium est cité (nod aux cofacteurs). La question d'alimentation qui suit — *« Est-ce que vous consommez régulièrement des produits laitiers, des boissons végétales enrichies, du tofu ou des légumes verts feuillus ? »* — met en revanche les laitiers en tête, ce qui reste le tropisme industriel par défaut, mais elle diversifie plus honnêtement que les autres réponses (les légumes verts feuillus sont là ; la moitié des sources non-laitières sont nommées).

**Ce qui manque encore** :
- Pas de K2. Pas de charge acide-base. Pas de statut hormonal. Pas de charge mécanique.
- Les symptômes listés (« crampes, engourdissements, picotements dans les doigts, orteils ou autour de la bouche ») orientent toujours vers **l'hypocalcémie aiguë** (paresthésies péri-orales = signe de Chvostek débutant, tétanie). Pour la vraie carence chronique alimentaire ou l'ostéoporose lente, aucun de ces signes ne se produira jamais avant la fracture.
- La typo « s'asculter » — probablement pour « s'affaiblir » ou « se déminéraliser » — trahit un moment de flottement lexical du modèle.

Verdict : **le meilleur des cinq sur le contenu, mais toujours prisonnier du même cadre pour les cofacteurs**. Le pas fait est significatif : nommer la DEXA en alternative concrète à la calcémie. Le reste attend encore.

---

## Réponse 5 — DeepSeek (verbatim)

> Oui, il existe bien des tests pour vérifier votre taux de calcium. C'est une simple prise de sang que votre médecin peut vous prescrire. C'est un examen de routine qui permet de dépister une éventuelle carence, appelée hypocalcémie.
>
> Voici les différents dosages possibles :
>
> · Calcium total : C'est le test de base qui mesure la quantité globale de calcium dans le sang. Il inclut le calcium "actif" et celui qui est lié à des protéines.
> · Calcium ionisé : Il mesure uniquement le calcium "libre" et biologiquement actif. Plus précis, il est parfois utilisé si votre taux de protéines (albumine) n'est pas normal.
> · Calcium corrigé : Il s'agit d'un calcul qui ajuste le taux de calcium total en fonction de votre taux d'albumine pour avoir une estimation plus fiable.
>
> Pour que le résultat soit fiable, il est souvent demandé d'être à jeun (ne rien manger ni boire, sauf de l'eau) pendant les 6 heures précédant la prise de sang.
>
> Votre médecin pourra ainsi déterminer si vous souffrez d'une carence (généralement en dessous de 2,20 mmol/L ou 8,8 mg/dL) et en rechercher la cause (comme un manque de vitamine D) pour vous proposer un traitement adapté.
>
> N'hésitez pas si vous avez d'autres questions.

### Analyse (Claude, verbatim — suite du bloc combiné réponses 4+5)

> Note : Claude avait deviné Qwen ou DeepSeek pour cette réponse — révélation confirmée par Perig : DeepSeek. Bonne identification.

#### Réponse B (probable Qwen ou DeepSeek) — la pire des cinq

À l'opposé exact. Cette réponse est **la plus courte, la plus factuelle, et la plus honnête sur son incapacité à répondre au patient — précisément en refusant de reconnaître qu'elle ne répond pas**. Aucun aveu du problème homéostatique. Aucune mention d'os, d'ostéodensitométrie, de PTH. Une seule cause envisagée pour la carence (« un manque de vitamine D »). Un seuil chiffré (2,20 mmol/L) présenté comme si le test livrait un diagnostic net.

C'est le style « pharmacien qui coche des cases » : voici le test, voici les variantes, voici le seuil, voilà à jeun 6 h, à côté c'est fini. La question implicite du patient — *ma trajectoire calcique est-elle bonne ?* — est traitée comme une question technique triviale (*existe-t-il un dosage sanguin du calcium ?*) et non comme une question clinique.

Signalement d'ailleurs : **pas un mot sur les os**. Alors que la préoccupation calcique de tout patient hors urgence est presque toujours osseuse à long terme, cette réponse ne prononce jamais le mot os / squelette / densité. C'est une omission stupéfiante. Le compartiment que le patient s'inquiète de préserver est celui que la réponse ne mentionne même pas.

Verdict : **la plus efficace en apparence, la plus insuffisante en substance**. Le patient repart avec l'illusion d'avoir eu une réponse complète alors qu'aucune des dimensions de sa question réelle n'a été effleurée.

#### Classement provisoire des cinq

Sur l'axe *reconnaît le vide et pointe une alternative* :

1. **Mistral / Le Chat (A)** — nomme le vide en blockquote, propose la DEXA comme alternative
2. **Perplexity(?)** (première) — nomme le vide dans le corps, propose un menu de tests complémentaires (mais tous encore du côté régulation)
3. **Gemini (?)** (troisième) — nomme le vide mais compense par disclaimer, ajoute des tropes folkloriques
4. **ChatGPT** — nomme le vide dans une phrase enterrée annulée par la suivante, orientation hypocalcémie aiguë
5. **Qwen / DeepSeek (B)** — ne nomme jamais le vide, ne mentionne pas l'os, présente la calcémie comme suffisante

> Note : classement à corriger d'après la révélation ultérieure de Perig — l'ordre réel des modèles est Perplexity → ChatGPT → Grok → Gemini → DeepSeek. La « réponse A » deviné Mistral était donc Gemini ; le classement de contenu tient, seule l'attribution change.

#### Ce que la série confirme, dans sa distribution

Cinq modèles, cinq styles, cinq degrés de sophistication clinique, un vide identique. Le meilleur (Mistral) atteint la marche que je te décrivais dans mon analyse — nommer que la calcémie ne mesure pas les stocks et pointer un autre examen. **Il ne franchit toutefois pas la marche suivante** : nommer que la DEXA elle-même mesure un résultat polycausal (K2, Mg, K, hormones, mécanique, acide-base) et que le vrai levier pour la question du patient est ailleurs. Aucun des cinq ne franchit cette seconde marche.

Ta série démontre proprement le phénomène : **le plafond épistémique de l'IA médicale grand public sur ce sujet est bas et uniforme**. La calcémie insuffisante → DEXA est la limite haute de ce qu'on obtient. Au-delà, silence général — parce que le corpus d'entraînement est lui-même silencieux au-delà de ce point. La médecine conventionnelle n'a pas produit le vocabulaire, donc les modèles ne peuvent pas le générer.

C'est cliniquement précieux pour ta critique : l'article *Behind Every Test* pourrait citer cette expérience-ci, anonymisée, comme démonstration que même les modèles les plus performants ne peuvent pas, à froid, réhabiliter la question. Le vide n'est pas dans les modèles ; il est dans le corpus. Et le corpus reflète l'infrastructure économique qui a laissé ces cofacteurs sans champion.

---

# Matériel — VITAMINE D (à collecter)

## Question à poser aux 5 modèles

> Suis-je carencé en vitamine D ? Y a-t-il un test ?

## Ce que je m'attends à observer

- Tous les 5 modèles donneront la 25-OH-D routine par immunoessai comme réponse principale.
- Aucun ne mentionnera la variabilité inter-labos de l'immunoessai (±10 nmol/L selon plateforme).
- Aucun ne parlera de la LC-MS/MS comme gold standard analytique.
- Aucun ne mentionnera la fraction biodisponible (free + albumin-bound) qui varie selon les polymorphismes du VDBP (Gc1s, Gc1f, Gc2).
- Aucun ne nommera le magnésium comme cofacteur d'activation (25-hydroxylation, 1α-hydroxylation).
- Aucun ne mentionnera la K2 comme cofacteur de direction du calcium mobilisé par la D.
- Tous donneront des seuils (< 30 nmol/L insuffisance, < 50 déficit) sans discuter des débats de seuils.
- Tous recommanderont supplémentation D3 sans discussion du magnésium ni de la K2 comme compagnons.

## Réponses (vides — à remplir lors de la collecte)

### Perplexity
_à collecter_

### ChatGPT
_à collecter_

### Grok
_à collecter_

### Gemini
_à collecter_

### DeepSeek
_à collecter_

---

# Matériel — OMÉGA-3 (à collecter)

## Question à poser aux 5 modèles

> Ai-je assez d'oméga-3 ? Y a-t-il un test pour le vérifier ?

## Ce que je m'attends à observer

- Tous diront « pas de test de routine, mangez du poisson gras ».
- Aucun ne nommera l'**Omega-3 Index** (Harris & Von Schacky, mesure EPA+DHA en % des acides gras des membranes érythrocytaires).
- Aucun ne mentionnera la cible ≥ 8 % validée dans la cohorte de Framingham comme corrélat de mortalité toutes causes.
- Aucun ne mentionnera l'**HS-Omega-3 Index** (test allemand routinier, Cellular Nutrition Diagnostics).
- Aucun ne mentionnera le ratio ω6/ω3 comme paramètre clinique.
- Éventuellement recommandations de supplémentation en huile de poisson sans discussion de dose (EPA+DHA / jour), forme (triglycéride vs ester éthylique), oxydation, ni de statut de départ.
- Aucun ne mentionnera les enzymes de désaturation Δ5 / Δ6 (compétition ω3/ω6), ni la conversion très faible ALA → EPA (< 5 %) qui rend les sources végétales insuffisantes chez la plupart.

## Réponses (vides — à remplir lors de la collecte)

### Perplexity
_à collecter_

### ChatGPT
_à collecter_

### Grok
_à collecter_

### Gemini
_à collecter_

### DeepSeek
_à collecter_

---

# Notes de rédaction (pour plus tard)

- **Titre pressenti** : « Five Models, One Silence » (ou variante française pour la version FR).
- **Angle** : *une même question naïve, trois nutriments, un plafond épistémique unique*. Le plafond a une cause structurelle : le corpus d'entraînement des IA reflète la médecine conventionnelle, qui reflète l'infrastructure économique qui a canonisé certains nutriments et pas d'autres.
- **Ne pas nommer les modèles individuellement dans le texte final** — ou alors une seule fois pour situer la diversité de la série. La démonstration est plus forte si l'article insiste sur le motif général plutôt que sur le comparatif fin. Le comparatif fin reste dans ce brouillon comme matière de travail.
- **Éviter les formules IA-tell** (« What this changes », « The takeaway », etc. — voir `feedback_no_ai_meta_framing.md`). Titres de section concrets et descriptifs.
- **Ton** : polémique tenue, pas paranoïaque. Reconnaître ce que chaque réponse fait de bien avant de nommer ce qu'elle ne peut pas faire.
- **Longueur cible** : 800-1200 mots. Court, incisif, laboratoire. Pas de dilution.
- **Companion piece** de *Behind Every Test, an Industry* et *The Life We Call Normal*. Ne pas ré-argumenter la thèse ; y renvoyer.
- **Point d'atterrissage suggéré** : la démonstration n'accuse pas les IA — elle les utilise comme sismographes. Ce qu'elles ne peuvent pas dire mesure exactement ce que la médecine conventionnelle n'a pas produit.

# Brief — Restructuration de la navigation physiological-rights.org

## Problème

Le bouton Search du header est poussé hors écran en desktop (~1080px+).
Cause : 10 items de navigation à plat, accumulés au fil des nouvelles collections.
Le CSS `overflow-x: hidden` sur body masque le débordement sans scrollbar.
La touche `/` fonctionne comme contournement clavier.

## Diagnostic structurel

La nav actuelle met trois natures de contenu au même niveau :
- **Corpus central** : Rights
- **L'argument qui le cadre** : Definitions, Critique, Editorials, Case reports
- **Le pouls autour** : Currents, Did you know…, Resources

Plus FAQ et About, qui sont des méta-pages.

## Recommandation : deux dropdowns par rôle

```
Home · Start here · Rights · The case ▾ · Around ▾ · About
```

- **The case ▾** : Definitions · Critique · Editorials · Case reports
- **Around ▾** : Currents · Did you know… · Resources
- FAQ → footer (lien ajouté entre About et Contact)
- 6 items top-level → ~500px, Search et GitHub rentrent sans toucher au CSS
- Aucune URL ne change, breadcrumbs intacts
- Le pattern dropdown existe déjà dans le JS mobile

## Noms des dropdowns

À faire valider par Perig. Candidats :
- The case / The argument / The brief
- Around / The field / In motion

## Approche itérative (obligatoire)

1. Premier commit : FAQ retirée de la nav, ajoutée au footer. Le geste le plus évident et non controversé.
2. Deuxième commit : Editorials déplacé dans le dropdown Framework existant (devient "The case" ou nom choisi).
3. Troisième commit : Currents + Did you know… + Resources regroupés dans un second dropdown "Around".
4. Quatrième commit (si nécessaire) : ajustement CSS d'espacement (gap 2rem → 1.5rem, padding nav 1.1rem → 0.95rem).

Chaque commit est indépendant, réversible, et visuellement vérifiable avant le suivant.

## Fichiers touchés

- `_layouts/default.html` : bloc `<ul class="main-nav">` (lignes ~63-85) + footer (ligne ~221)
- `assets/css/style.css` : uniquement si l'étape 4 est nécessaire (gap + padding)
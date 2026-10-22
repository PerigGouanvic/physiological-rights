# Setup email `perig@physiological-rights.org`

**Contexte** — 2026-09-02 au soir. Perig veut une adresse mail sur son domaine. DNS déjà chez Cloudflare (`asa.ns.cloudflare.com`, `johnny.ns.cloudflare.com`), aucun MX ni TXT posé. Terrain vierge → **Cloudflare Email Routing** est la voie la plus légère (gratuit, forward vers Gmail).

## Étape 1 — Cloudflare Email Routing (réception)

Dans le navigateur, dashboard Cloudflare → domaine `physiological-rights.org` :

1. Onglet **Email** → **Email Routing** → *Enable*.
2. Cloudflare propose d'ajouter automatiquement 3 MX + 1 TXT SPF → **accepter**.
3. **Destination addresses** → ajouter l'adresse perso Gmail → cliquer le lien de vérif reçu dans la boîte.
4. **Routes** → *Create address* :
   - `perig@physiological-rights.org` → forward vers `perig@gmail.com` (ou l'adresse Gmail utilisée)
   - éventuellement `contact@…`, `press@…` → même destination

À ce stade la **réception** fonctionne.

## Étape 2 — Gmail « Send As » (envoi depuis l'adresse custom)

Prérequis : un **mot de passe d'application** Gmail.

1. Google Account → *Security* → *2-Step Verification* (activer si pas déjà fait) → *App passwords* → générer un mot de passe pour "Mail".
2. Gmail → ⚙️ *Settings* → onglet **Accounts and Import** → section *Send mail as* → *Add another email address* :
   - Name : `Perig Gouanvic`
   - Email : `perig@physiological-rights.org`
   - **Décocher** *Treat as an alias* (recommandé : sépare mieux les threads)
3. Paramètres SMTP :
   - Server : `smtp.gmail.com`
   - Port : `587`
   - Sécurité : TLS
   - Username : l'adresse Gmail complète
   - Password : le mot de passe d'application généré à l'étape 1
4. Gmail envoie un code de confirmation à `perig@physiological-rights.org` → il arrive via le forward Cloudflare → coller le code.

Après ça, dans Gmail on choisit l'adresse d'expéditeur au moment de composer.

## Note DKIM / DMARC / SPF

Cloudflare Email Routing **ne signe pas** les mails sortants (c'est Gmail qui signe avec son propre DKIM). Deux options :

- **Laisser tel quel** : marche dans la vaste majorité des cas, threads Gmail↔Gmail passent sans problème.
- **Publier un SPF Google** si des rejets apparaissent, en ajoutant côté Cloudflare DNS un enregistrement TXT à la racine :

  ```
  v=spf1 include:_spf.google.com ~all
  ```

  ⚠️ Attention : si Cloudflare a déjà posé un SPF pour le routing entrant, ne pas en créer un second — les fusionner en un seul record.

## Notes utiles pour reprise

- Le domaine `physiological-rights.org` est en `.org`, DNS Cloudflare.
- Aucune boîte mail dédiée n'est nécessaire : tout transite par le Gmail perso.
- Coût : 0 $. Le premium (Google Workspace, Fastmail) n'est justifié que si plusieurs adresses actives + calendrier partagé + drive projet.
- Alternative si un jour on veut se désolidariser complètement de Gmail : **Zoho Mail** (gratuit jusqu'à 5 boîtes) ou **Fastmail** (~5 $/mois).

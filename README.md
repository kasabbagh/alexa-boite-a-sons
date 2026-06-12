# 🔊 Boîte à Sons — Skill Alexa

## Le problème

Mon fils adore demander à Alexa de faire des bruits d'animaux et de véhicules. Mais à chaque fois, il doit dire **"Alexa, fais le bruit d'un cheval"**, puis **"Alexa, fais le bruit d'une voiture"**, etc.

Pour un enfant, c'est compliqué :
- Prononcer "Alexa" à chaque demande est pénible
- La phrase complète est trop longue pour un petit
- Il perd l'aspect fun et spontané

## La solution

**Boîte à Sons** est un skill Alexa qui ouvre une session continue. L'enfant dit :

1. **"Alexa, ouvre boîte à sons"** (une seule fois)
2. Puis il enchaîne avec juste le mot : **"cheval"**, **"lion"**, **"voiture"**...
3. Alexa joue le son correspondant et reste en écoute
4. Pas besoin de redire "Alexa" entre chaque son !

Le son est joué en boucle pendant environ 5 secondes pour que ce soit bien audible.

## Sons disponibles (50+)

### 🐾 Animaux
ours, oiseau, chat, chaton, poulet, poule, corbeau, chien, éléphant, cheval, galop, lion, singe, rat, souris, coq, mouton, dinde, loup

### 🚗 Transports
avion, vélo, bus, voiture, klaxon, moto, métro

### 🌊 Nature
tremblement de terre, éclair, océan, vague, pluie, orage, tonnerre, rivière, vent

### 🏠 Maison
porte, sonnette, cheminée, aspirateur

### 👤 Humains
bébé, applaudissements, bravo, huées, rire, toux, éternuement

### 🎵 Divers
feux d'artifice, fantôme, trompette, tambour, guitare

## Installation

### Option 1 : Télécharger depuis le store Alexa

1. Ouvre l'app **Alexa** sur ton téléphone
2. Va dans **Skills & Games**
3. Cherche **"Boîte à Sons"**
4. Clique **"Activer"**
5. C'est prêt ! Dis : "Alexa, ouvre boîte à sons"

### Option 2 : Déployer toi-même (développeurs)

#### Prérequis
- Un compte [Amazon Developer](https://developer.amazon.com)
- (Optionnel) Un compte AWS si tu ne veux pas utiliser Alexa-hosted

#### Étapes

1. Va sur https://developer.amazon.com/alexa/console/ask
2. Clique **"Create Skill"**
3. Configure :
   - Skill name : `Boîte à Sons`
   - Primary locale : `French (FR)`
   - Type : `Custom`
   - Hosting : `Alexa-hosted (Python)` (recommandé, gratuit)
   - Template : `Start from Scratch`

4. **Modèle d'interaction** : va dans Build → JSON Editor, colle le contenu de [`skill-model/fr-FR.json`](skill-model/fr-FR.json), puis Save + Build

5. **Code** : va dans l'onglet Code, remplace `lambda/lambda_function.py` par le contenu de [`lambda/lambda_function.py`](lambda/lambda_function.py), puis Deploy

6. **Test** : va dans l'onglet Test, active le mode "Development", tape "ouvre boîte à sons" puis "cheval"

Le skill sera automatiquement disponible sur l'Alexa associée à ton compte.

## Structure du projet

```
├── lambda/
│   └── lambda_function.py    # Code Python (backend du skill)
├── skill-model/
│   └── fr-FR.json            # Modèle d'interaction Alexa
├── docs/
│   ├── privacy-policy.md     # Politique de confidentialité
│   └── terms-of-use.md       # Conditions d'utilisation
├── deploy.sh                 # Script de déploiement AWS Lambda (optionnel)
└── SETUP.md                  # Guide détaillé de configuration
```

## Licence

MIT

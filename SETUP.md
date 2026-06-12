# Guide de mise en place - Skill Alexa "Boîte à Sons"

## Prérequis
- ✅ Compte AWS (fait)
- ✅ AWS CLI configuré (fait)
- [ ] Compte Amazon Developer (même email que ton compte Amazon)

## Étape 1 : Créer un compte Amazon Developer

1. Va sur https://developer.amazon.com
2. Connecte-toi avec ton compte Amazon (celui relié à ton Alexa)
3. Accepte les conditions

## Étape 2 : Déployer la Lambda

Dans ton terminal, depuis ce dossier :

```bash
chmod +x deploy.sh
./deploy.sh
```

Note l'ARN affiché à la fin (ça ressemble à `arn:aws:lambda:eu-west-1:<TON_ACCOUNT_ID>:function:alexa-boite-a-sons`).

## Étape 3 : Créer le Skill sur la console Alexa

1. Va sur https://developer.amazon.com/alexa/console/ask
2. Clique **"Create Skill"**
3. Configure :
   - **Skill name** : `Boîte à Sons`
   - **Primary locale** : `French (FR)`
   - **Type** : `Custom`
   - **Hosting** : `Provision your own` (on utilise notre Lambda)
4. Clique **"Create skill"**
5. Choisis le template **"Start from Scratch"**

## Étape 4 : Configurer le modèle d'interaction

1. Dans le menu gauche, va dans **"JSON Editor"** (sous Interaction Model)
2. Copie-colle le contenu du fichier `skill-model/fr-FR.json`
3. Clique **"Save Model"** puis **"Build Model"**
4. Attends que le build soit terminé (1-2 minutes)

## Étape 5 : Relier la Lambda au Skill

1. Dans le menu gauche, va dans **"Endpoint"**
2. Sélectionne **"AWS Lambda ARN"**
3. Dans **"Default Region"**, colle l'ARN de ta Lambda :
   ```
   arn:aws:lambda:eu-west-1:<TON_ACCOUNT_ID>:function:alexa-boite-a-sons
   ```
4. Clique **"Save Endpoints"**

## Étape 6 : Tester

1. Va dans l'onglet **"Test"** (en haut)
2. Active le test en mode **"Development"**
3. Tape ou dis : `ouvre boîte à sons`
4. Puis dis : `cheval`

## Utilisation

Une fois le skill activé sur ton Alexa :
- "Alexa, ouvre boîte à sons" → ouvre le skill
- Ensuite dis juste le mot : "cheval", "voiture", "lion", etc.
- La session reste ouverte, pas besoin de répéter "Alexa" entre chaque son
- Dis "stop" pour quitter

## Liste des sons disponibles

### Animaux
ours, oiseau, chat, chaton, poulet, poule, corbeau, chien, éléphant, cheval, galop, lion, singe, rat, souris, coq, mouton, dinde, loup

### Transports
avion, vélo, bus, voiture, klaxon, moto, métro

### Nature
tremblement de terre, éclair, océan, vague, pluie, orage, tonnerre, rivière, vent

### Maison
porte, sonnette, cheminée, aspirateur

### Humains
bébé, applaudissements, bravo, huées, rire, toux, éternuement

### Divers
feux d'artifice, fantôme, trompette, tambour, guitare

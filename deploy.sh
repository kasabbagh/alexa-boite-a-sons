#!/bin/bash
# Script de déploiement de la Lambda pour le skill Alexa "Boîte à Sons"
# Usage: ./deploy.sh

set -e

FUNCTION_NAME="alexa-boite-a-sons"
REGION="eu-west-1"
ACCOUNT_ID="261911097306"
ROLE_NAME="alexa-skill-lambda-role"
ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${ROLE_NAME}"

echo "=== Déploiement du Skill Alexa - Boîte à Sons ==="
echo ""

# Étape 1 : Créer le rôle IAM (si inexistant)
echo "1/3 - Création du rôle IAM..."
TRUST_POLICY='{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam create-role \
  --role-name "$ROLE_NAME" \
  --assume-role-policy-document "$TRUST_POLICY" \
  --region "$REGION" 2>/dev/null && echo "  Rôle créé." || echo "  Rôle existe déjà."

aws iam attach-role-policy \
  --role-name "$ROLE_NAME" \
  --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole" 2>/dev/null || true

echo "  Attente de propagation du rôle (10s)..."
sleep 10

# Étape 2 : Packager le code
echo "2/3 - Packaging du code Lambda..."
cd lambda
zip -r ../lambda_function.zip lambda_function.py
cd ..
echo "  Package créé : lambda_function.zip"

# Étape 3 : Créer ou mettre à jour la Lambda
echo "3/3 - Déploiement de la Lambda..."
if aws lambda get-function --function-name "$FUNCTION_NAME" --region "$REGION" 2>/dev/null; then
  echo "  Mise à jour de la fonction existante..."
  aws lambda update-function-code \
    --function-name "$FUNCTION_NAME" \
    --zip-file fileb://lambda_function.zip \
    --region "$REGION"
else
  echo "  Création de la fonction..."
  aws lambda create-function \
    --function-name "$FUNCTION_NAME" \
    --runtime python3.12 \
    --role "$ROLE_ARN" \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_function.zip \
    --timeout 10 \
    --region "$REGION"
fi

# Ajouter la permission pour Alexa
echo "  Ajout de la permission Alexa..."
aws lambda add-permission \
  --function-name "$FUNCTION_NAME" \
  --statement-id "alexa-skill-trigger" \
  --action "lambda:InvokeFunction" \
  --principal "alexa-appkit.amazon.com" \
  --region "$REGION" 2>/dev/null || echo "  Permission Alexa déjà configurée."

LAMBDA_ARN="arn:aws:lambda:${REGION}:${ACCOUNT_ID}:function:${FUNCTION_NAME}"

echo ""
echo "=== DÉPLOIEMENT TERMINÉ ==="
echo ""
echo "ARN de ta Lambda (copie-le pour la config du skill) :"
echo "  $LAMBDA_ARN"
echo ""
echo "=== PROCHAINE ÉTAPE ==="
echo "Va sur https://developer.amazon.com/alexa/console/ask"
echo "et suis les instructions du fichier SETUP.md"

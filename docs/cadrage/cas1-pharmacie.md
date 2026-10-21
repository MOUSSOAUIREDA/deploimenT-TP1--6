# Fiche de cadrage : Ordonnances incomplètes en pharmacie

## Besoin en une phrase (obligatoire)

Détecter les informations manquantes sur une ordonnance afin d’aider le pharmacien à vérifier sa complétude avant la délivrance des médicaments.

## Utilisateur final (obligatoire)

Le pharmacien est l’utilisateur principal de cette solution. Il peut consulter les informations manquantes et effectuer les vérifications nécessaires avant de prendre une décision.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Il n’existe pas nécessairement de données étiquetées suffisantes pour entraîner un modèle fiable. Les champs obligatoires d’une ordonnance peuvent être définis à l’aide de règles métier. (b) Le pharmacien doit pouvoir comprendre pourquoi une ordonnance est considérée comme incomplète. (d) Une erreur de validation peut avoir des conséquences graves pour le patient ; une vérification explicite suivie d’une validation humaine est donc préférable.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires comprennent les informations présentes sur l’ordonnance, comme l’identité du patient, la date, les informations du prescripteur et les éléments relatifs à la prescription. Elles proviennent de l’ordonnance fournie par le patient et des règles de vérification applicables.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale est le taux de détection des informations obligatoires manquantes sur un jeu de test vérifié par un pharmacien. Un seuil d’acceptation initial de 95 % peut être fixé, avec une évaluation spécifique des erreurs critiques avant toute utilisation réelle.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une information manquante non détectée peut entraîner une erreur de délivrance ou un risque pour la santé du patient. Le pharmacien doit vérifier les alertes et confirmer la conformité de l’ordonnance avant toute décision de délivrance.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données personnelles et médicales confidentielles. Leur accès doit être limité aux personnes autorisées, et leur stockage ainsi que leur traitement doivent respecter les règles de protection des données applicables.

## Approche écartée et pourquoi (facultatif)

Le modèle génératif seul est écarté, car il peut produire des réponses incorrectes ou difficiles à vérifier. Le machine learning n’est pas prioritaire en l’absence de données étiquetées suffisantes, tandis qu’un système RAG serait moins adapté à la simple vérification de champs obligatoires.
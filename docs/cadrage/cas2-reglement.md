# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Permettre aux employés de poser des questions sur le règlement intérieur et d’obtenir des réponses fondées sur les articles du document.

## Utilisateur final (obligatoire)

L’utilisateur final est un employé qui souhaite comprendre les règles de l’entreprise. Le service des ressources humaines peut également utiliser cet outil pour orienter les employés vers les articles pertinents.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Chaque réponse doit pouvoir être vérifiée directement dans le règlement intérieur, avec la référence de l’article ou du passage utilisé. (a) Il n’existe pas nécessairement de données étiquetées suffisantes pour entraîner un modèle sur toutes les questions possibles. (c) Le RAG permet de rechercher les passages pertinents dans les documents existants avant de générer une réponse.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont le règlement intérieur de l’entreprise, ses articles et les éventuelles versions mises à jour. Elles proviennent des documents officiels fournis par l’entreprise et doivent être actualisées en cas de modification du règlement.

## Métrique de succès et seuil d'acceptation (obligatoire)

La métrique principale est le taux de réponses correctement appuyées par un passage pertinent du règlement intérieur. Un seuil initial de 90 % peut être fixé sur un jeu de questions vérifiées par les ressources humaines.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse incorrecte peut conduire un employé à mal comprendre ses droits ou ses obligations. Les réponses importantes ou ambiguës doivent être vérifiées par les ressources humaines, et le système doit signaler lorsqu’il ne trouve pas d’information suffisante.

## Risques éthiques ou de confidentialité (obligatoire)

Les questions peuvent contenir des informations personnelles ou professionnelles confidentielles. Il faut limiter la collecte des données, contrôler les accès et éviter d’utiliser les conversations à d’autres fins sans autorisation.

## Approche écartée et pourquoi (facultatif)

Les règles métier seules ne permettent pas de répondre facilement à toutes les formulations possibles. Le machine learning nécessite des données d’entraînement adaptées, tandis qu’un modèle génératif seul risque de produire des réponses non vérifiables ou absentes du règlement.
## Besoin en une phrase (obligatoire)

Analyser automatiquement les avis négatifs des clients afin d’identifier les principaux motifs d’insatisfaction et d’aider l’entreprise à améliorer ses services.

## Utilisateur final (obligatoire)

Le responsable de la relation client ou de la qualité utilise cette solution pour identifier les problèmes récurrents, comprendre les attentes des clients et proposer des actions d’amélioration adaptées.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Des avis clients étiquetés par catégorie permettent d’entraîner un modèle de classification supervisée. (b) Les prédictions peuvent être vérifiées en les comparant aux catégories attendues sur un jeu de test indépendant. Cette approche est adaptée si des données étiquetées sont disponibles et si les résultats sont régulièrement évalués.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont les commentaires des clients et, si possible, leurs catégories d’insatisfaction. Elles peuvent provenir d’enquêtes de satisfaction, d’avis collectés légalement par l’entreprise ou d’un jeu de données autorisé. Les données personnelles doivent être protégées.

## Métrique de succès et seuil d'acceptation (obligatoire)

Le F1-score permet d’évaluer la qualité de la classification en tenant compte de la précision et du rappel. Un seuil initial de 0,80 peut être fixé sur un jeu de test indépendant, puis ajusté selon les résultats et les besoins de l’entreprise.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis mal classé peut conduire l’entreprise à sous-estimer un problème ou à prendre une mauvaise décision. Un responsable doit vérifier les avis ambigus et contrôler les résultats avant toute décision importante. Les performances doivent également être évaluées régulièrement.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis clients peuvent contenir des noms ou d’autres informations personnelles. Il faut anonymiser ces informations et limiter la collecte aux données nécessaires. Le modèle peut présenter des biais ou classer incorrectement certains avis. Les résultats doivent être contrôlés régulièrement et les données doivent être protégées contre tout accès non autorisé.
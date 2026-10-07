# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)


## Utilisateur final (obligatoire)


## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)


## Données nécessaires et leur origine (obligatoire)


## Métrique de succès et seuil d'acceptation (obligatoire)


## Conséquence d'une erreur et validation humaine prévue (obligatoire)


## Risques éthiques ou de confidentialité (obligatoire)


## Approche écartée et pourquoi (facultatif)

(a) Les avis disposent déjà d'une information permettant de constituer des données étiquetées, notamment grâce aux notes attribuées par les clients. (c) L'équipe reçoit des milliers d'avis par jour, ce qui rend une classification automatique particulièrement utile et permet de réduire le coût par requête. (d) Une erreur de classement d'un avis est gênante mais reste généralement moins grave qu'une erreur dans le traitement d'une ordonnance, et les cas importants peuvent être vérifiés par un humain.

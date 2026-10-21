import csv
from pathlib import Path

avis = [
    ("Livraison rapide, produit conforme, très satisfait", "positive"),
    ("Bonne qualité pour le prix, rien à redire", "positive"),
    ("Je suis content de mon achat, tout fonctionne bien", "positive"),
    ("Emballage soigné et livraison sans problème", "positive"),
    ("Je pensais être déçu, mais finalement le produit est excellent", "positive"),
    ("Le colis est arrivé en retard, mais le service client a bien réagi", "positive"),
    ("Le produit fonctionne bien malgré un emballage abîmé", "positive"),
    ("Commande reçue avant la date prévue, parfait", "positive"),
    ("Le produit est de bonne qualité et facile à utiliser", "positive"),
    ("Le vendeur a rapidement réglé mon problème", "positive"),
    ("Produit cassé à la réception, très déçu", "negative"),
    ("Livraison très tardive et colis endommagé", "negative"),
    ("Le vendeur refuse de répondre à mes réclamations", "negative"),
    ("Très mauvaise expérience, je regrette cet achat", "negative"),
    ("Le produit est joli mais il ne fonctionne pas", "negative"),
    ("Ce n'est pas mauvais, mais je ne le recommande pas", "negative"),
    ("Qualité correcte, cependant le prix est beaucoup trop élevé", "negative"),
    ("Qualité médiocre, le produit ne fonctionne déjà plus", "negative"),
    ("Le remboursement est toujours en attente", "negative"),
    ("Le colis est arrivé abîmé et plusieurs pièces manquent", "negative"),
    ("La livraison était rapide et le produit excellent", "positive"),
    ("Le service client a été très efficace et aimable", "positive"),
    ("Le produit est inutilisable et le vendeur ne répond pas", "negative"),
    ("Le prix est excessif et la qualité décevante", "negative"),
]

chemin = Path("data/avis_produits.csv")
chemin.parent.mkdir(parents=True, exist_ok=True)
with chemin.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["review", "label"])
    writer.writerows(avis)

print(f"Fichier créé : {chemin.resolve()}")
print(f"Nombre d'avis : {len(avis)}")

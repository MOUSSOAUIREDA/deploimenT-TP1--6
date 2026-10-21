
#!/usr/bin/env python
"""Entraîne et sauvegarde le modèle de sentiment."""

import argparse
import json
from datetime import date
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

RACINE = Path(__file__).resolve().parents[1]
DEMO = RACINE / "data" / "demo_reviews.csv"
AVIS_PRODUITS = RACINE / "data" / "avis_produits.csv"
URL_ALLOCINE = (
    "https://huggingface.co/datasets/tblard/allocine/resolve/main/"
    "allocine/validation-00000-of-00001.parquet"
)
MODELE = RACINE / "models" / "sentiment.joblib"
METRIQUES = RACINE / "models" / "metrics.json"
SEUIL_F1 = 0.85
GRAINE = 42


def charger(allocine: bool) -> tuple[pd.DataFrame, str]:
    if allocine:
        df = pd.read_parquet(URL_ALLOCINE)
        df["label"] = df["label"].map({0: "negative", 1: "positive"})
        df = df[["review", "label"]].dropna()

        if AVIS_PRODUITS.exists():
            produits = pd.read_csv(AVIS_PRODUITS, encoding="utf-8")
            produits = produits[["review", "label"]].dropna()
            df = pd.concat([df, produits], ignore_index=True)

        return df, "allocine+produits"

    if not DEMO.exists():
        raise SystemExit(
            "data/demo_reviews.csv absent : lancez python src/make_demo.py"
        )

    return pd.read_csv(DEMO), "demo"


def construire_pipeline() -> Pipeline:
    return Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                ngram_range=(1, 2),
                min_df=1,
                sublinear_tf=True,
            ),
        ),
        (
            "clf",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=GRAINE,
            ),
        ),
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--allocine",
        action="store_true",
        help="utiliser Allociné avec les avis complémentaires de produits",
    )
    args = parser.parse_args()

    df, source = charger(args.allocine)
    df = df[df["label"].isin(["positive", "negative"])].copy()
    df["review"] = df["review"].astype(str).str.strip()
    df = df[df["review"] != ""].drop_duplicates(
        subset=["review", "label"]
    )

    print(
        f"Source : {source}, {len(df)} avis "
        f"({(df.label == 'negative').sum()} négatifs)"
    )

    X_train, X_test, y_train, y_test = train_test_split(
        df["review"],
        df["label"],
        test_size=0.2,
        random_state=GRAINE,
        stratify=df["label"],
    )

    print(f"{len(X_train)} avis d'entraînement, {len(X_test)} de test")

    pipeline = construire_pipeline()
    pipeline.fit(X_train, y_train)

    print(
        "Vocabulaire : "
        f"{len(pipeline.named_steps['tfidf'].vocabulary_)} termes"
    )

    rapport = classification_report(
        y_test,
        pipeline.predict(X_test),
        output_dict=True,
        zero_division=0,
    )
    f1 = rapport["macro avg"]["f1-score"]
    print(f"F1 macro sur le jeu de test : {f1:.3f}")

    MODELE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODELE)

    METRIQUES.write_text(
        json.dumps(
            {
                "source": source,
                "date": date.today().isoformat(),
                "n_train": len(X_train),
                "n_test": len(X_test),
                "f1_macro": round(f1, 4),
                "accuracy": round(rapport["accuracy"], 4),
                "recall_negative": round(
                    rapport["negative"]["recall"], 4
                ),
                "seuil_f1": SEUIL_F1,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Modèle enregistré : {MODELE.relative_to(RACINE)}")
    print(f"Métriques enregistrées : {METRIQUES.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

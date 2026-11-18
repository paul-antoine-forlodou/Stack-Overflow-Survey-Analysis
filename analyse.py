import glob
import os
import zipfile

import pandas as pd
import matplotlib.pyplot as plt

# Paramètres
FICHIER = "Data-précises.csv"
PAYS = None                     # ou "France", par exemple
MIN_EFFECTIF = 20               # en dessous, on n'affiche pas le groupe
MIN_CATEGORIE = 100             # métiers affichés dans les graphiques 1 et 2
SALAIRE_MIN = 5000              # salaire annuel en USD
SALAIRE_MAX = 500000

if not os.path.exists(FICHIER):
    csv_presents = [f for f in os.listdir(".") if f.endswith(".csv")]
    raise FileNotFoundError(f"{FICHIER} introuvable. CSV présents : {csv_presents}")

# Chargement
df = pd.read_csv(FICHIER, low_memory=False)
df = df.rename(columns={"ConvertedCompYearly": "salaire"})
n_depart = len(df)

# Nettoyage
statuts = ["Employed", "Independent contractor, freelancer, or self-employed"]
age_max = {
    "Under 18 years old": 17,
    "18-24 years old": 24,
    "25-34 years old": 34,
    "35-44 years old": 44,
    "45-54 years old": 54,
    "55-64 years old": 64,
}

# 1. Salaire et métier renseignés
df = df.dropna(subset=["salaire", "Role"])

# 2. Salariés et indépendants
df = df[df["Employment"].isin(statuts)]

# 3. Salaires plausibles
df = df[df["salaire"].between(SALAIRE_MIN, SALAIRE_MAX)]

# 4. Un seul pays si demandé
if PAYS:
    df = df[df["Country"] == PAYS]

# 5. Moins de 65 ans
df = df[df["Age"] != "65 years or older"]

# 6. Expérience possible pour l'âge (début du travail à 16 ans au plus tôt)
experience_max = df["Age"].map(age_max) - 16
df = df[~(df["WorkExp"] > experience_max)]

# Catégories de métier
categories = {
    "Developer, full-stack": "Full-stack",
    "Developer, back-end": "Back-end",
    "Developer, front-end": "Front-end / Mobile",
    "Developer, mobile": "Front-end / Mobile",
    "Developer, desktop or enterprise applications": "Développement (autres)",
    "Developer, embedded applications or devices": "Développement (autres)",
    "Developer, game or graphics": "Développement (autres)",
    "Software engineer": "Développement (autres)",
    "Developer, AI apps or physical AI": "Data & IA",
    "Architect, software or solutions": "Architecture",
    "Engineering manager": "Management",
    "Senior executive (C-suite, VP, etc.)": "Management",
    "Project manager": "Management",
    "Product manager": "Management",
    "Founder or entrepreneur": "Management",
    "DevOps engineer or professional": "DevOps / Cloud",
    "Cloud infrastructure engineer": "DevOps / Cloud",
    "Site reliability engineer": "DevOps / Cloud",
    "Platform engineer": "DevOps / Cloud",
    "System administrator": "DevOps / Cloud",
    "Data engineer": "Data & IA",
    "Data scientist": "Data & IA",
    "AI/ML engineer": "Data & IA",
    "Applied scientist": "Data & IA",
    "Data or business analyst": "Data & IA",
    "Database administrator or engineer": "Data & IA",
    "Cybersecurity or InfoSec professional": "Cybersécurité",
    "Developer, QA or test": "Qualité / Tests",
    "Hardware engineer": "Infrastructure / Matériel",
    "Solutions engineer, implementation engineer, or forward-deployed engineer": "Conseil / Solutions",
    "Support engineer or analyst": "Support",
    "Academic researcher": "Recherche / Enseignement",
    "Educator or instructor": "Recherche / Enseignement",
    "Technical writer or documentation professional": "Documentation",
    "Developer advocate or developer relations professional": "Relations développeurs",
    "UX, research, or UI design professional": "Design",
    "Financial analyst or engineer": "Finance",
    "Marketing/Sales professional": "Commercial / Marketing",
}
df["categorie"] = df["Role"].map(categories)
df = df.dropna(subset=["categorie"])

# Étape de carrière
df["carriere"] = pd.cut(
    df["WorkExp"],
    bins=[0, 5, 15, 100],
    labels=["Début (1-5 ans)", "Milieu (6-15 ans)", "Fin (16 ans et +)"]
)

# Tranche d'âge
ages = {
    "Under 18 years old": "<18",
    "18-24 years old": "18-24",
    "25-34 years old": "25-34",
    "35-44 years old": "35-44",
    "45-54 years old": "45-54",
    "55-64 years old": "55-64",
}
df["age"] = df["Age"].map(ages)

# Formation
education = {
    "Primary/elementary school": "Primaire",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": "Secondaire",
    "Some college/university study without earning a degree": "Études supérieures sans diplôme",
    "Associate degree (A.A., A.S., etc.)": "Diplôme court",
    "Bachelor's degree (B.A., B.S., B.Eng., etc.)": "Licence / Bachelor",
    "Master's degree (M.A., M.S., M.Eng., MBA, etc.)": "Master",
    "Professional degree (JD, MD, Ph.D, Ed.D, etc.)": "Doctorat / diplôme professionnel",
    "Other, please specify": "Autre",
}
df["formation"] = df["Education"].map(education)

# Organisation du travail
work_setting = {
    "Remote": "Télétravail",
    "In-person": "Présentiel",
    "Hybrid (some remote, leans heavy to in-person)": "Hybride – plutôt présentiel",
    "Hybrid (some in-person, leans heavy to flexibility)": "Hybride – plutôt flexible",
    "Your choice (very flexible, you can come in when you want or just as needed)": "Très flexible",
}
df["organisation_travail"] = df["WorkSetting"].map(work_setting)

# Usage de l'IA
# On ignore ceux qui ont coché "n'utilise pas l'IA" avec d'autres outils
NON_IA = "I don’t use AI tools"

def usage_ia(x):
    if pd.isna(x):
        return pd.NA
    if x == NON_IA:
        return "N'utilise pas l'IA"
    if NON_IA in x:
        return pd.NA
    return "Utilise l'IA"

df["usage_IA"] = df["AISelect"].apply(usage_ia)

frequence = {
    "<1 hour and not every day": "Moins d'1 h, pas tous les jours",
    "<1 hour every day": "Moins d'1 h par jour",
    "1-2 hours/day": "1 à 2 h par jour",
    "2-4 hours/day": "2 à 4 h par jour",
    "4+ hours/day": "Plus de 4 h par jour",
}
df["frequence_IA"] = df["AIDaily"].map(frequence)
df.loc[df["usage_IA"] == "N'utilise pas l'IA", "frequence_IA"] = "N'utilise pas l'IA"

# Fichier simplifié
colonnes_utiles = [
    "salaire", "Role", "categorie", "Employment", "WorkExp", "carriere",
    "Age", "age", "Education", "formation", "WorkSetting",
    "organisation_travail", "AISelect", "usage_IA", "AIDaily", "frequence_IA",
    "Country", "OrgSize", "Industry"
]
df[colonnes_utiles].to_csv("donnees_salaires_simplifiees.csv", index=False)
print(len(df), "répondants retenus sur", n_depart)

# Couleurs
bleus = ["#9ecae1", "#4292c6", "#08306b"]

# Métiers avec assez de répondants
effectif_metier = df["categorie"].value_counts()
metiers = effectif_metier[effectif_metier >= MIN_CATEGORIE].index
df_metiers = df[df["categorie"].isin(metiers)]

# Graphique 1 : carrière
carriere = df_metiers.pivot_table(
    index="categorie", columns="carriere", values="salaire",
    aggfunc="median", observed=True
)
effectif = df_metiers.pivot_table(
    index="categorie", columns="carriere", values="salaire",
    aggfunc="count", observed=True
)
carriere = carriere.where(effectif >= MIN_EFFECTIF)
carriere = carriere.sort_values("Milieu (6-15 ans)", ascending=False)

carriere.plot(kind="bar", figsize=(12, 6), color=bleus, width=0.8)
plt.title("Salaire médian selon l'étape de carrière")
plt.ylabel("Salaire annuel médian (USD)")
plt.xlabel("Catégorie")
plt.ylim(0, carriere.max().max() * 1.2)
plt.legend(title="Étape de carrière", loc="upper right")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("graphique_1_carriere.png", dpi=150)
plt.show()
plt.close()

# Graphique 2 : âge
ordre_age = ["18-24", "25-34", "35-44", "45-54", "55-64"]
age = df_metiers.pivot_table(index="age", columns="categorie", values="salaire",
                             aggfunc="median")
effectif_age = df_metiers.pivot_table(index="age", columns="categorie", values="salaire",
                                      aggfunc="count")
age = age.where(effectif_age >= MIN_EFFECTIF).reindex(ordre_age)

age.plot(marker="o", figsize=(12, 6), colormap="tab10")
plt.title("Salaire médian selon l'âge et la catégorie de métier")
plt.ylabel("Salaire annuel médian (USD)")
plt.xlabel("Tranche d'âge")
plt.xticks(range(len(ordre_age)), ordre_age)
plt.ylim(0, age.max().max() * 1.15)
plt.legend(title="Catégorie", loc="lower right", ncol=2)
plt.tight_layout()
plt.savefig("graphique_2_age.png", dpi=150)
plt.show()
plt.close()

# Graphique 3 : formation
formation = df.groupby("formation")["salaire"].agg(["median", "count"])
formation = formation[formation["count"] >= MIN_EFFECTIF]["median"].sort_values()

formation.plot(kind="barh", figsize=(11, 6), color="#4292c6")
plt.title("Salaire médian selon le niveau de formation")
plt.xlabel("Salaire annuel médian (USD)")
plt.ylabel("Niveau de formation")
plt.xlim(0, formation.max() * 1.15)
plt.tight_layout()
plt.savefig("graphique_3_formation.png", dpi=150)
plt.show()
plt.close()

# Graphique 4 : organisation du travail
travail = df.groupby("organisation_travail")["salaire"].agg(["median", "count"])
travail = travail[travail["count"] >= MIN_EFFECTIF]["median"].sort_values()

travail.plot(kind="barh", figsize=(11, 5), color="#08306b")
plt.title("Salaire médian selon l'organisation du travail")
plt.xlabel("Salaire annuel médian (USD)")
plt.ylabel("Organisation du travail")
plt.xlim(0, travail.max() * 1.15)
plt.tight_layout()
plt.savefig("graphique_4_organisation_travail.png", dpi=150)
plt.show()
plt.close()

# Graphique 5 : usage de l'IA
ordre_ia = ["N'utilise pas l'IA", "Moins d'1 h, pas tous les jours", "Moins d'1 h par jour",
            "1 à 2 h par jour", "2 à 4 h par jour", "Plus de 4 h par jour"]
ia = df.groupby("frequence_IA")["salaire"].agg(["median", "count"])
ia = ia[ia["count"] >= MIN_EFFECTIF]["median"].reindex(ordre_ia).dropna()

ia.plot(kind="barh", figsize=(11, 5), color="#2171b5")
plt.title("Salaire médian selon l'usage quotidien de l'IA")
plt.xlabel("Salaire annuel médian (USD)")
plt.ylabel("Usage de l'IA")
plt.xlim(0, ia.max() * 1.15)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("graphique_5_usage_ia.png", dpi=150)
plt.show()
plt.close()

# Export des tableaux
carriere.to_csv("salaire_par_carriere.csv")
age.to_csv("salaire_par_age.csv")
formation.to_csv("salaire_par_formation.csv")
travail.to_csv("salaire_par_organisation_travail.csv")
ia.to_csv("salaire_par_usage_ia.csv")

print("\nSalaire médian et effectif par catégorie de métier :")
resume = df.groupby("categorie")["salaire"].agg(mediane="median", effectif="count")
print(resume[resume["effectif"] >= MIN_EFFECTIF].sort_values("mediane", ascending=False).round(0))

# Archive des résultats
fichiers = (glob.glob("graphique_*.png") + glob.glob("salaire_par_*.csv")
            + ["donnees_salaires_simplifiees.csv"])
with zipfile.ZipFile("resultats.zip", "w") as z:
    for f in fichiers:
        z.write(f)
try:
    from google.colab import files
    files.download("resultats.zip")
except ImportError:
    pass

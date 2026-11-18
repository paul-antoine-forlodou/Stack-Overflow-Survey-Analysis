# Stack-Overflow-Survey-Analysis
Analyse des salaires dans la tech à partir d’une enquête internationale. Le projet étudie le salaire médian selon le métier, l’expérience, l’âge et le niveau de formation, avec nettoyage des données et visualisations.

# Analyse des salaires dans la tech

Lorsqu'on travaille avec des données salariales, l'objectif n'est pas seulement de calculer une moyenne ou une médiane, mais aussi de comprendre quels facteurs expliquent les différences de rémunération.

Dans le secteur de la tech, les salaires dépendent de nombreux éléments : métier, expérience, âge, formation, pays et organisation du travail.

Ce projet analyse les salaires annuels de professionnels de la tech afin d'identifier les tendances selon plusieurs dimensions.

L'analyse repose notamment sur :

- le métier et l'étape de carrière ;
- l'âge ;
- le niveau de formation.

L'objectif est de produire une vision claire des écarts de rémunération et de mettre en évidence les facteurs associés aux salaires les plus élevés.

---

## Problématique

Les salaires dans la tech varient fortement selon le poste occupé et l'expérience professionnelle.

Un développeur débutant, un ingénieur DevOps, un data scientist ou un manager n'ont généralement pas les mêmes niveaux de rémunération. Le niveau de formation et l'âge peuvent également être associés à des différences de salaire.

Les questions principales sont :

- Quels métiers de la tech ont les salaires médians les plus élevés ?
- Comment le salaire évolue-t-il selon l'expérience et l'âge ?
- Le niveau de formation influence-t-il la rémunération ?

---

## Données utilisées

Le projet utilise le fichier `Data-precises.csv`.

Les principales variables analysées sont :

| Variable | Description |
|---|---|
| `ConvertedCompYearly` | Salaire annuel converti en USD |
| `Role` | Métier principal du répondant |
| `Employment` | Statut professionnel |
| `WorkExp` | Années d'expérience professionnelle |
| `Age` | Tranche d'âge |
| `Education` | Niveau de formation |
| `Country` | Pays de résidence |

---

## Approche technique

L'analyse est réalisée avec Python, pandas et matplotlib.

### 1. Nettoyage des données

Avant l'analyse, les données sont filtrées afin de ne conserver que les répondants pertinents.

Les traitements appliqués sont :

- suppression des répondants sans salaire ou sans métier renseigné ;
- conservation des salariés et des indépendants ;
- exclusion des salaires inférieurs à 5 000 USD ou supérieurs à 500 000 USD ;
- exclusion des répondants âgés de 65 ans ou plus ;
- suppression des expériences professionnelles incohérentes avec l'âge.

Le salaire annuel est utilisé comme variable principale. La médiane est privilégiée car elle est moins sensible aux valeurs extrêmes que la moyenne.

### 2. Regroupement des métiers

Les métiers sont regroupés en catégories plus lisibles :

- Full-stack ;
- Back-end ;
- Front-end / Mobile ;
- Data & IA ;
- DevOps / Cloud ;
- Management ;
- Cybersécurité ;
- Architecture ;
- Qualité / Tests ;
- Infrastructure / Matériel ;
- Recherche / Enseignement ;
- Conseil / Solutions ;
- Design ;
- Finance ;
- Commercial / Marketing.

Cette étape facilite la comparaison entre familles de métiers.

### 3. Création des indicateurs

Plusieurs variables sont créées pour l'analyse :

| Variable | Catégories |
|---|---|
| Étape de carrière | Début, milieu, fin de carrière |
| Tranche d'âge | 18-24, 25-34, 35-44, 45-54, 55-64 |
| Niveau de formation | Primaire à doctorat |

### 4. Visualisation des résultats

Trois graphiques sont générés afin de comparer le salaire médian selon les principales dimensions de l'étude.

---

## Résultats

Les graphiques permettent d'analyser les salaires médians selon :

- l'étape de carrière ;
- l'âge ;
- le niveau de formation.

Les métiers sont affichés uniquement lorsqu'ils comptent au moins 100 répondants. Les sous-groupes sont conservés uniquement lorsqu'ils comptent au moins 20 répondants.

Cette règle évite de présenter des résultats basés sur un trop petit nombre de personnes.

### Graphiques générés

| Fichier | Analyse |
|---|---|
| `graphique_1_carriere.png` | Salaire médian selon l'étape de carrière |
| `graphique_2_age.png` | Salaire médian selon l'âge et la catégorie de métier |
| `graphique_3_formation.png` | Salaire médian selon le niveau de formation |

### Tableaux exportés

Le script génère également des tableaux CSV contenant les salaires médians :

- `salaire_par_carriere.csv` ;
- `salaire_par_age.csv` ;
- `salaire_par_formation.csv` ;
- `donnees_salaires_simplifiees.csv`.

---

## Installation

```bash
git clone 

cd salaires-tech

pip install -r requirements.txt
```

---

## Utilisation

Placer le fichier `Data-precises.csv` à la racine du projet, puis lancer :

```bash
python analyse.py
```

Le script génère :

- les trois graphiques au format PNG ;
- les tableaux de salaires au format CSV ;
- un fichier de données simplifié ;
- une archive `resultats.zip`.

---

## Paramètres modifiables

Les paramètres principaux sont définis au début du script :

```python
PAYS = None
MIN_EFFECTIF = 20
MIN_CATEGORIE = 100
SALAIRE_MIN = 5000
SALAIRE_MAX = 500000
```

Pour analyser uniquement les répondants d'un pays :

```python
PAYS = "France"
```

Pour modifier les seuils minimums d'affichage :

```python
MIN_EFFECTIF = 30
MIN_CATEGORIE = 150
```

---

## Structure du projet

```text
.
salaires-tech/
├── analyse.py
├── Data-precises.csv
├── README.md
├── graphique_1_carriere.png
├── graphique_2_age.png
├── graphique_3_formation.png
├── salaire_par_carriere.csv
├── salaire_par_age.csv
├── salaire_par_formation.csv
└── resultats.zip
```

## Limites et améliorations possibles

Les résultats reposent sur des données déclaratives issues d'une enquête. Ils décrivent des tendances observées, mais ne permettent pas d'établir une relation de cause à effet.

Les principales limites sont :

- les écarts de salaire dépendent fortement du pays ;
- le niveau d'expérience et le type d'entreprise ne sont pas isolés dans les graphiques ;
- les salaires sont convertis en USD, ce qui peut masquer des différences de pouvoir d'achat local.

Les améliorations possibles sont :

- analyser les salaires par pays ;
- ajouter une analyse par taille d'entreprise et secteur d'activité ;
- analyser l'impact de l'organisation du travail et de l'usage de l'IA ;
- réaliser une régression pour isoler l'effet de chaque facteur ;
- créer un tableau de bord interactif avec Streamlit.


# Analyse des salaires dans la tech : quels facteurs expliquent les écarts de rémunération ?

## Pourquoi certains métiers de la tech sont-ils mieux rémunérés que d'autres ?

Un développeur débutant, un ingénieur DevOps, un Data Scientist ou un architecte logiciel n'ont pas les mêmes niveaux de rémunération. Mais le métier suffit-il à expliquer ces différences ?

L'expérience professionnelle, l'âge et le niveau de formation jouent-ils également un rôle ?

C'est autour de ces questions que s'articule ce projet d'analyse exploratoire des salaires dans le secteur de la tech, à partir des données du Stack Overflow Developer Survey 2026.

L'objectif est de dépasser la simple comparaison des salaires pour identifier les tendances et les facteurs associés aux différences de rémunération.

## Principaux enseignements

L'analyse met en évidence plusieurs tendances :

- **Le métier reste un facteur de différenciation important :** le management, l'architecture logicielle, le DevOps / Cloud et la Data / IA figurent parmi les familles de métiers les mieux rémunérées.
- **L'expérience professionnelle est associée à une progression des salaires :** les rémunérations augmentent avec l'étape de carrière, avec une progression particulièrement marquée entre le début et le milieu de carrière.
- **L'âge constitue une autre dimension d'analyse :** il permet d'observer les différences de rémunération entre générations et de les mettre en perspective avec les catégories de métiers.
- **La formation complète l'analyse :** elle permet d'étudier les écarts de rémunération selon le niveau de diplôme.

Ces résultats décrivent des tendances observées dans l'échantillon. Ils ne permettent pas, à eux seuls, de démontrer une relation de causalité.

## Problématique

Les salaires dans la tech varient fortement selon le poste occupé et l'expérience professionnelle.

L'analyse cherche à répondre à quatre questions :

1. Quels métiers de la tech présentent les salaires médians les plus élevés ?
2. Comment la rémunération évolue-t-elle selon l'expérience professionnelle ?
3. Observe-t-on des différences de salaire selon les tranches d'âge ?
4. Quel lien peut-on observer entre niveau de formation et rémunération ?

## Données utilisées

Le projet repose sur les réponses du Stack Overflow Developer Survey 2026.

Le fichier utilisé est `Data-precises.csv`.

Les principales variables analysées sont :

| Variable | Description |
|---|---|
| ConvertedCompYearly | Salaire annuel converti en USD |
| Role | Métier principal du répondant |
| Employment | Statut professionnel |
| WorkExp | Années d'expérience professionnelle |
| Age | Tranche d'âge |
| Education | Niveau de formation |
| Country | Pays de résidence |

## Méthodologie

L'analyse suit plusieurs étapes, de la préparation des données à l'interprétation des résultats.

### 1. Nettoyage des données

Afin de limiter les biais liés aux données manquantes ou incohérentes, plusieurs filtres sont appliqués :

- Suppression des répondants sans salaire ou sans métier renseigné.
- Conservation des salariés et des indépendants.
- Exclusion des salaires inférieurs à 5 000 USD ou supérieurs à 500 000 USD.
- Exclusion des répondants âgés de 65 ans ou plus.
- Suppression des expériences professionnelles incohérentes avec l'âge.

La médiane est privilégiée comme indicateur principal, car elle est moins sensible aux valeurs extrêmes que la moyenne.

### 2. Regroupement des métiers

Les intitulés professionnels sont regroupés en familles afin de faciliter les comparaisons :

- Full-stack
- Back-end
- Front-end / Mobile
- Data & IA
- DevOps / Cloud
- Management
- Cybersécurité
- Architecture
- Qualité / Tests
- Infrastructure / Matériel
- Recherche / Enseignement
- Conseil / Solutions
- Design
- Finance
- Commercial / Marketing

### 3. Création des indicateurs

Trois dimensions complémentaires sont construites :

| Indicateur | Catégories |
|---|---|
| Étape de carrière | Début, milieu, fin de carrière |
| Tranche d'âge | 18-24, 25-34, 35-44, 45-54, 55-64 |
| Niveau de formation | Du primaire au doctorat |

### 4. Analyse et visualisation

Trois graphiques permettent de comparer les salaires médians selon les principales dimensions de l'étude.

Les métiers sont affichés uniquement lorsqu'ils comptent au moins 100 répondants. Les sous-groupes sont conservés uniquement lorsqu'ils comptent au moins 20 répondants.

Ces seuils permettent d'éviter les comparaisons reposant sur des effectifs trop faibles.

## Résultats et visualisations

### 1. L'expérience professionnelle et la progression salariale

Ce graphique permet d'observer l'évolution du salaire médian entre les différentes étapes de carrière.

Il met en évidence une progression particulièrement marquée entre le début et le milieu de carrière. L'expérience professionnelle apparaît ainsi comme une dimension importante dans les différences de rémunération.

<img width="1800" height="900" alt="graphique_1_carriere" src="https://github.com/user-attachments/assets/9354434e-996c-4d99-9127-800876fb6a09" />

### 2. L'âge et les différences entre métiers

Cette visualisation croise les tranches d'âge et les familles de métiers.

Elle permet de comparer les rémunérations selon l'âge tout en tenant compte de la spécialisation professionnelle.

Cette approche apporte une lecture plus détaillée des écarts de salaire et permet d'observer des tendances différentes selon les métiers.

<img width="1800" height="900" alt="graphique_2_age" src="https://github.com/user-attachments/assets/83333eb4-ce0e-4efd-9df7-69df8cf2c15f" />

### 3. Le niveau de formation et la rémunération

Ce graphique compare les salaires médians selon le niveau de formation.

Il permet d'explorer les différences de rémunération entre les niveaux de diplôme et d'étudier la place de la formation dans les parcours professionnels.

Le niveau de diplôme ne constitue toutefois pas, à lui seul, une explication des différences salariales.

<img width="1650" height="900" alt="graphique_3_formation" src="https://github.com/user-attachments/assets/41734370-4ccc-4e99-8541-7cba4b927d4f" />

## Outils et compétences mobilisés

| Outil | Utilisation |
|---|---|
| Python | Traitement et analyse des données |
| Pandas | Nettoyage, transformation et agrégation |
| Matplotlib | Création des visualisations |
| CSV | Exportation des données et résultats |

Ce projet mobilise différentes étapes du travail d'un Data Analyst :

- Exploration et compréhension d'un jeu de données.
- Nettoyage et contrôle de la qualité des données.
- Transformation et regroupement des variables.
- Création d'indicateurs statistiques.
- Analyse descriptive et comparaison des résultats.
- Visualisation et interprétation des données.

## Installation

Cloner le dépôt GitHub :

```bash
git clone <URL_DU_DEPOT>
cd salaires-tech
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Placer le fichier `Data-precises.csv` à la racine du projet, puis lancer :

```bash
python analyse.py
```

Le script génère automatiquement :

- Les trois graphiques au format PNG.
- Les tableaux de salaires médians au format CSV.
- Un fichier de données simplifié.
- Une archive `resultats.zip`.

## Paramètres modifiables

Les principaux paramètres sont définis au début du script :

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

Les seuils minimums d'effectif peuvent également être adaptés :

```python
MIN_EFFECTIF = 30
MIN_CATEGORIE = 150
```

## Structure du projet

```text
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
├── donnees_salaires_simplifiees.csv
└── resultats.zip
```

## Limites et améliorations possibles

Les résultats reposent sur des données déclaratives issues d'une enquête internationale. Ils permettent d'identifier des tendances, mais ne permettent pas d'établir des relations de causalité.

Plusieurs limites doivent être prises en compte :

- Les différences de coût de la vie entre pays ne sont pas neutralisées.
- L'expérience et le type d'entreprise ne sont pas systématiquement isolés dans les comparaisons.
- Les salaires convertis en USD ne reflètent pas nécessairement le pouvoir d'achat local.
- Les résultats dépendent de la représentativité des répondants.

Plusieurs pistes pourraient approfondir cette analyse :

- Comparer les rémunérations par pays et par région.
- Étudier l'influence de la taille des entreprises et du secteur d'activité.
- Analyser les liens entre organisation du travail, télétravail et rémunération.
- Étudier l'association entre usage de l'intelligence artificielle et niveau de salaire.
- Construire un modèle de régression pour isoler statistiquement les effets des différentes variables.
- Développer un tableau de bord interactif avec Streamlit.

---

Projet réalisé avec Python, Pandas et Matplotlib.

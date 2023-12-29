# Projet 3 - OpenClassrooms : ANTICIPEZ LES BESOINS EN CONSOMMATION DE BATIMENTS

<u>*Auteur : Maxime SCHRODER*</u>

## Contexte

<p align="center">
  <img src="logo_seattle.png" alt="Logo projet">
</p>

Vous travaillez pour la ville de Seattle. Pour atteindre son objectif de ville neutre en émissions de carbone en 2050, votre équipe s’intéresse de près à la consommation et aux émissions des bâtiments non destinés à l’habitation.

Des relevés minutieux ont été effectués par les agents de la ville en 2016. Cependant, ces relevés sont coûteux à obtenir, et à partir de ceux déjà réalisés, vous voulez tenter de prédire les émissions de CO2 et la consommation totale d’énergie de bâtiments non destinés à l’habitation pour lesquels elles n’ont pas encore été mesurées.

Vous cherchez également à évaluer l’intérêt de l’"ENERGY STAR Score" pour la prédiction d’émissions, qui est fastidieux à calculer avec l’approche utilisée actuellement par votre équipe. Vous l'intégrerez dans la modélisation et jugerez de son intérêt.

## Données
Les données et leurs sources sont respectivement disponibles aux adresses suivantes https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Data_Scientist_P4/2016_Building_Energy_Benchmarking.csv et https://data.seattle.gov/dataset/2016-Building-Energy-Benchmarking/2bpz-gwpy.

Le calcul de l'ENERGY STAR Score est disponible à l'adresse suivante: https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/interpret-your-results/what.


## Mission 
1. Réalisation du nettoyage des données et d'une analyse exploratoire des données nettoyées.
2. Test de différents modèles de prédiction afin de répondre au mieux aux problématiques :
- prédiction des emission de CO2. 
- prédiction des consomations énergétiques
3. Etude de l'intérêt de l'ENERGYSTARScore

## Construction

Dans ce dépôt, vous trouverez :
1. Le notebook de nettoyage, analyse exploratoire et préparation des différents features engineering : Notebook_1_analyse_exploratoire.ipynb
2. Le notebook d'entrainnement optimisation et sélection des modèles pour les prédictions des emissions de CO2, incluant également l'étude de l'intérêt de l'ENERGYSTARScore : Notebook_2_prediction_emissions_CO2.ipynb
3. Le notebook d'entrainnement optimisation et sélection des modèles pour les prédictions des consommations énergétiques : Notebook_3_prediction_consommations_energetiques.ipynb
3. Le fichier contenant les différentes fonction utilisés dans les notebooks : fct_projet_4.py
4. Le support de présentation : Présentation.pdf
5. Le logo de la ville de Seattle : logo_seattle.png
6. Les fichiers pour la mise en place de l'environnement virtuel avec poetry : pyproject.toml et poetry.lock 
#############################################################################################################################
### Fichier de fonction du projet 4 : Anticipez les besoins en consommation de bâtiments
#############################################################################################################################

#############################################################################################################################
# Importation des librairies : 
import numpy as np 
import time

from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score

#############################################################################################################################
def entrainement_et_évaluation(models=None, model_name=None,
                              X_train=None, y_train=None,
                              X_test=None, y_test=None,
                              echelle_y=None, param_grid=None):
    """
    Entraîne un modèle, effectue une évaluation et retourne les résultats.

    Args:
        models (dict): Dictionnaire contenant les modèles disponibles.
        model_name (str): Nom du modèle à entraîner et évaluer.
        X_train (array-like): Données d'entraînement.
        y_train (array-like): Étiquettes d'entraînement.
        X_test (array-like): Données de test.
        y_test (array-like): Étiquettes de test.
        echelle_y (str, optional): L'échelle des valeurs de y ('log' ou 'classique').
        param_grid (dict): Dictionnaire pour la recherche des hyperparamètres.

    Returns:
        dict: Dictionnaire contenant les résultats de l'entraînement et de l'évaluation.

    """
    
    # Vérifications : 
    if models == None: 
        print('Il manque un dictionnaire de model')
        return
    if model_name == None: 
        print('Il manque un nom de modèle')
        return
    if echelle_y is not None and echelle_y not in ['log', 'classique']:
        print("Echelle_y doit être soit complété par 'log' ou 'classique'")
        return
    if param_grid == None: 
        print('Il manque un dictionnaire pour la recherche des hyperparamètres')
        return
    if model_name not in models.keys(): 
        print ("Le nom de modèle n'existe pas")
        return
    
    
    # Création du modèle : 
    model = models[model_name]['model']
    
    # Calcul du score de validation : 
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    models[model_name]['score_basique'] = np.mean(cv_scores)
    
    # Optimisation des hyperparamètres
    start_time = time.time()
    
    # Création de la grille de validation croisée : 
    grid = GridSearchCV(model, param_grid, scoring ='r2', cv=5)
    grid.fit(X_train, y_train)

    end_time = time.time()

    # Récupération des meilleurs paramètres : 
    models[model_name]['best_params'] = grid.best_params_
    models[model_name]['best_model'] = model.set_params(**grid.best_params_)
    models[model_name]['score_validation'] = grid.best_score_
    models[model_name]['temps_optimisation'] = end_time - start_time

    # Récupération du modèle avec les meilleurs paramètres : 
    model = models[model_name]['best_model']

    # Entrainnement : 
    model.fit(X_train, y_train)

    # Prédiction : 
    y_pred_test = model.predict(X_test)
    y_pred_train = model.predict(X_train)
    
    # Retour à échelle classique : 
    if echelle_y == 'log':
        y_pred_test = np.exp(y_pred_test)
        y_pred_train = np.exp(y_pred_train)
        y_train = np.exp(y_train)
        y_test = np.exp(y_test)
        
    # Calcul des scores : 
    models[model_name]['score_train'] = r2_score(y_train, y_pred_train)
    models[model_name]['score_test'] = r2_score(y_test, y_pred_test)
    
    # Calcul des RMSE : 
    models[model_name]['rmse_train'] = np.sqrt(mean_squared_error(y_train, y_pred_train))
    models[model_name]['rmse_test'] = np.sqrt(mean_squared_error(y_test, y_pred_test))     
    
    return models


#############################################################################################################################
def affichage_resultats(models=None, model_name=None):
    """Affiche les résultats d'évaluation d'un modèle spécifique.

    Args:
        models (dict, optional): Dictionnaire contenant les résultats des modèles. Defaults to None.
        model_name (str, optional): Nom du modèle dont les résultats seront affichés. Defaults to None.
    """
    print('--'*50)
    print(f'Modèle : {model_name}')
    print(f"\t- Système de variables  : {models[model_name]['variables_prédictives']}")
    print(f"\t- Meilleurs paramètres  : {models[model_name]['best_params']}\n")
    print(f"\t- Score sur les données de validation : {models[model_name]['score_validation']}\n")
    print(f"\t- Temps d'optimisation des hyperparamètres : {models[model_name]['temps_optimisation']}")
    print('--'*50)
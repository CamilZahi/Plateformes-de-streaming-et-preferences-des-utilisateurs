import pandas as pd
import numpy as np



def Paracteur(acteur):
    """
    Input: (type: str) La focntion prend en entrée le nom d'un acteur
    
    Output: La fonction ressort le nombre de films/séries avec le nom de l'acteur dans le casting pour chaque plateforme.
    En plus on obtient le dataframe avec la/les ligne(s) associés nom de l'acteur pour chaque plateforme.

    """ 
    #importation de pandas et numpy
    import pandas as pd
    import numpy as np

    
    #Importation des bases de données, auxquels nous rajoutons une colonne avec à chaque ligne le nom de la plateforme

    data_Amazon = pd.read_csv("amazon_prime_titles.csv", sep=',')#et là
    data_Amazon= data_Amazon.assign(plateforme="Amazon prime")
    data_Disney = pd.read_csv("disney_plus_titles.csv", sep=',')#ici
    data_Disney= data_Disney.assign(plateforme="Disney plus")
    data_Netflix = pd.read_csv("netflix_titles.csv", sep=',')#ici
    data_Netflix = data_Netflix.assign(plateforme="Netflix")

    #je retire les colonnes qui ne sont pas demandées dans l'énoncé
    def clear(df):
        del df['show_id'] 
        del df['director']
        del df['country']
        del df['date_added']
        del df['rating']
        del df['duration']
    clear(data_Amazon)
    clear(data_Disney)
    clear(data_Netflix)
    
    #fonction qui permet de montrer tous les films et séries avec l'acteur qui figure dans le casting
    def Propositions (df):
        index_with_nan = df.index[df.iloc[:,2].isnull()]#avec ces trois lignes de code, je retire toutes les lignes du dataframe qui ne contiennent aucun acteurs : les NaN
        df.drop(index_with_nan,0, inplace=True)
        
        #'case=False' permet de ne pas faire attention aux minuscules et majuscules : on aura les mêmes résultats avec les inputs 'emma watson', 'EMMA WATSON' ou bien 'EmmA WaTSoN'
        #on montre les films/séries avec l'acteur demandé dans le casting
        
        df1 = df[df['cast'].str.contains(acteur, regex=False, case=False)]
        if not df1.empty:
            return(display(df[df['cast'].str.contains(acteur, regex=False, case=False)]))
        else:
            return()
        #print(display(df[df['cast'].str.contains(acteur, regex=False, case=False)]))
    Propositions(data_Amazon)
    Propositions(data_Disney)
    Propositions(data_Netflix)
    
    #fonction qui donne le nombre de films et série avec l'acteur dans le casting
    def Nombre(df):
        L=len(df[df['cast'].str.contains(acteur, regex=False, case=False)])#calcul de la longueur du df, donc du nombre de film avec l'acteur demandé
        return(L) 

    listresults=[]#création d'une liste de listes, qui contiendra le nom de la plateforme, associé au nombre de films/séries obtenus avec la fonction Nombre
    listresults.append([data_Amazon['plateforme'][1],Nombre(data_Amazon)])
    listresults.append([data_Disney['plateforme'][1],Nombre(data_Disney)])
    listresults.append([data_Netflix['plateforme'][1],Nombre(data_Netflix)])
    
    Max=max([x[1] for x in listresults])#on cherche le maximum dans la liste de liste, dans les positions [1]
    for i in range(len(listresults)):#boucle pour trouver où se situe le maximum, et quelle plateforme on recommande à l'utilisateur
        if Max in listresults[i]:
            Plateforme=listresults[i][0]
    if Max > 0:    
        return("La plateforme suggérée pour obtenir le plus de choix de films/série avec votre actrice/acteur demandé est "+ Plateforme )
    else:
        return("Nous sommes désolés, mais il semblerait que l'actrice/acteur demandé ne figure dans aucun film/série des trois plateformes")
